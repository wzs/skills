---
name: decision-grade-slides
description: Create decision-grade slide decks by designing content with rigorous concept structure, information architecture, evidence selection, language precision, and high-clarity visual layout. Use when Codex must create, rewrite, or critique decks in PowerPoint, Google Slides, Keynote, or markdown slides, especially for executive or strategic communication where each slide must state a clear claim and prove it with the right data.
---

# Decision-Grade Slides

## Overview

Build slides as decision artifacts, not documentation dumps. For every slide, define one claim, prove it with evidence, and state the implication in plain language.

Default pattern: `claim -> evidence -> implication`.

## Core Workflow

1. Frame the decision
- Write the single decision this deck supports.
- Define audience and what they must approve, fund, or change.
- Define scope boundary: what stays in main flow vs backup.

2. Build concept architecture before visuals
- Create top-down argument tree: answer -> 2-5 arguments -> evidence.
- Enforce MECE for sibling arguments.
- Reject branches that fail "so what" (no decision consequence).

3. Author the title stream first
- Draft slide action titles before chart design.
- Read titles in order; they must form a coherent narrative.
- Ensure each title is specific, directional, and decision-relevant.

4. Specify evidence for each claim
- For each slide, define required proof type before building exhibit.
- Include baseline, comparator, delta, timeframe, and source.
- Label uncertainty explicitly when evidence is indicative or illustrative.

5. Compose high-clarity slides
- One core message per slide.
- One dominant visual per slide, plus minimal supporting annotation.
- Use layout hierarchy so primary message wins in 3-second scan.

6. Tighten language and logic
- Rewrite for plain, concrete, active language.
- Remove hedge words and topic labels.
- Ensure every sentence either advances claim or clarifies implication.

7. Run quality gates
- Structure gate: argument tree is complete and non-overlapping.
- Evidence gate: data is sufficient for stated claim type.
- Visual gate: chart type and emphasis match intended comparison.
- Language gate: title and callouts are concise, concrete, and unambiguous.

## Non-Negotiables

- Never use topic titles like "Market Overview".
- Never place two independent conclusions on one slide.
- Never show data without explicit implication.
- Never state causality without causal evidence design.
- Never use decorative visuals that reduce comprehension.

## Output Contract

When building or rewriting a deck, output in this order unless user overrides:

1. Decision statement and audience objective
2. Argument tree (answer, arguments, evidence needs)
3. Slide title stream (ordered action titles)
4. Slide specs table (title, claim, evidence type, exhibit type, implication)
5. Visual system spec (grid, type scale, color semantics, annotation rules)
6. Quality log (structural gaps, evidence risks, language issues)

## Reference Guide

Load only the files needed for the task:

- Concept hierarchy, storyline logic, and chapter architecture: `references/01-information-architecture.md`
- Visual composition, typography, spacing, and hierarchy: `references/02-slide-design-layout.md`
- Data requirements, chart choice, and quantitative integrity: `references/03-data-visualization.md`
- Language precision, title formulas, and copy standards: `references/04-language-and-messaging.md`
- Reusable blueprints and prompts: `references/05-templates.md`

## Failure Modes

- Deck narrates activity instead of decision logic.
- Slides describe topics instead of claims.
- Evidence is present but does not actually prove the title.
- Visual emphasis highlights the wrong datapoint.
- Language is abstract, hedged, or jargon-heavy.
