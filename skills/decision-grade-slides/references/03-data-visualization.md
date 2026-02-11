# Data Visualization And Evidence Standards

## Table of Contents
- Claim-to-evidence matrix
- Required metadata on quantitative slides
- Chart selection by analytical question
- Integrity and audit checks
- Uncertainty and confidence encoding

## Claim-to-evidence matrix

Match claim type to evidence type.

1. Trend claim
- Claim pattern: metric changed over time.
- Minimum evidence: multi-period time series, baseline and latest, delta (% and absolute).

2. Comparison claim
- Claim pattern: one segment outperforms another.
- Minimum evidence: same period, same denominator, ranked comparison with gap magnitude.

3. Driver claim
- Claim pattern: factors explain change.
- Minimum evidence: decomposition (waterfall, bridge, contribution table) summing to total delta.

4. Causal claim
- Claim pattern: action X caused outcome Y.
- Minimum evidence: controlled comparison, experiment, quasi-experiment, or robust before/after with confound checks.
- If not available, downgrade wording to association.

5. Forecast claim
- Claim pattern: future outcome estimate.
- Minimum evidence: model assumptions, range/scenario bounds, sensitivity drivers.

## Required metadata on quantitative slides

Every quantitative slide must contain:
- Metric definition.
- Unit and currency.
- Time window.
- Segment or population boundary.
- Source and extraction date.
- Any transformation rule (indexing, smoothing, exclusions).

## Chart selection by analytical question

Pick chart by decision question:
- What changed over time -> line chart.
- Where are biggest gaps -> sorted horizontal bars.
- What explains variance -> waterfall/bridge.
- Which options dominate on two dimensions -> scatter/2x2 matrix.
- How much uncertainty exists -> range bars, fan chart, scenario bands.

## Integrity and audit checks

Before finalizing:
- Reconcile chart totals to source table.
- Validate that percentage denominators are identical across comparisons.
- Confirm signs (+/-) and color coding are consistent.
- Ensure rounded values still reconcile (or footnote rounding effect).
- Check chart title claim matches numerically to displayed data.

## Uncertainty and confidence encoding

Do not hide uncertainty.

Label status explicitly:
- Final: validated data, stable definition.
- Preliminary: analysis still evolving.
- Indicative: directional estimate, not exact.
- Illustrative: hypothetical values to explain relationship.

Treat uncertainty labels as mandatory for non-final numbers.
