#!/usr/bin/env python3
import argparse
import gzip
import re
import sys
import urllib.request
from html import unescape


SOURCE_URL = "https://infernobar.pl/"

DAY_NAMES = "Poniedziałek|Wtorek|Środa|Czwartek|Piątek|Sobota|Niedziela"
DAY_RE = re.compile(rf"^({DAY_NAMES})\s*\(\d{{1,2}}\.\d{{1,2}}\)$", re.IGNORECASE)
STOP_RE = re.compile(r"^(ZUPA DNIA|DANIE DNIA|ZESTAW ZUPA)", re.IGNORECASE)
LABEL_RE = re.compile(r"^(ZUPA|DANIE I|DANIE II|PIZZA DNIA):\s*(.*)$", re.IGNORECASE)
LABEL_PREFIX_RE = re.compile(
    r"^(ZUPA|DANIE I|DANIE II|PIZZA DNIA)\s*:\s*",
    re.IGNORECASE,
)
BR_RE = re.compile(r"<\s*br\s*/?\s*>", re.IGNORECASE)
TAG_RE = re.compile(r"<[^>]+>")


def fetch_home_html(*, timeout_seconds: int) -> str:
    req = urllib.request.Request(
        SOURCE_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip",
        },
        method="GET",
    )

    with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
        raw = resp.read()
        if resp.headers.get("Content-Encoding", "").lower() == "gzip":
            raw = gzip.decompress(raw)
        html = raw.decode("utf-8", errors="replace")
    return html


def _extract_lunch_section(html: str) -> str:
    anchor = html.find('id="lunchmenu"')
    if anchor == -1:
        raise ValueError("Could not find lunch menu section (id=lunchmenu)")
    end = html.find("ZOBACZ MENU", anchor)
    if end == -1:
        end = min(len(html), anchor + 200_000)
    return html[anchor:end]


def _html_to_text(s: str) -> str:
    s = BR_RE.sub("\n", s)
    s = s.replace("</p>", "\n").replace("</div>", "\n")
    s = TAG_RE.sub("", s)
    s = unescape(s)
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"[ \t\f\v]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def extract_lunch_text(html: str) -> str:
    text = _html_to_text(_extract_lunch_section(html))

    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    out: list[str] = []
    in_block = False
    first_day = True
    pending_label: str | None = None

    for i, ln in enumerate(lines):
        if DAY_RE.fullmatch(ln):
            j = i + 1
            while j < len(lines) and not lines[j]:
                j += 1
            if j < len(lines) and DAY_RE.fullmatch(lines[j]):
                continue  # skip tab list
            if not first_day:
                out.append("")
            out.append(ln)
            in_block = True
            first_day = False
            continue

        if not in_block:
            continue
        if STOP_RE.match(ln):
            break

        if pending_label:
            if ln and ln == ln.upper():
                ln = ln.lower()
                ln = ln[0].upper() + ln[1:]
            out.append(f"{pending_label}: {ln}".rstrip())
            pending_label = None
            continue

        ln = LABEL_PREFIX_RE.sub(r"\1: ", ln)
        label_match = LABEL_RE.match(ln)
        if label_match:
            label, rest = label_match.groups()
            if not rest:
                pending_label = label.upper()
                continue
            if rest and rest == rest.upper():
                rest = rest.lower()
                rest = rest[0].upper() + rest[1:]
            ln = f"{label.upper()}: {rest}".rstrip()
        elif ln and ln == ln.upper():
            ln = ln.lower()
            ln = ln[0].upper() + ln[1:]
        out.append(ln)

    return "\n".join(out).strip()


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Inferno Bar lunch menu extractor")
    ap.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="HTTP timeout in seconds (default: 20)",
    )
    args = ap.parse_args(argv)

    try:
        html = fetch_home_html(
            timeout_seconds=args.timeout,
        )
        text = extract_lunch_text(html)
    except Exception as e:
        sys.stderr.write(f"ERROR: {e}\n")
        return 1

    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
