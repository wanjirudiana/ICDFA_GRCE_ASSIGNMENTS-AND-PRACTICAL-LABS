# Lab 3 – GRC Phishing Simulation & Quantitative Risk Analysis

Lead-GRC-analyst exercise for **GlobalTech Inc.**: analyse three phishing simulations, quantify exposure, compare controls and brief management. Everything here is a data-analysis exercise on supplied results – no phishing emails were sent and no credentials were collected.

## Scenario

I am acting as the lead GRC analyst at **GlobalTech Inc.** The CISO has provided results from three phishing simulation campaigns run last quarter. The task is to analyse the data, evaluate organisational exposure, compare security control investments and prepare an evidence-based briefing for management that will inform next year's security budget and strategy.

This is a data-analysis exercise on supplied simulation results. No phishing emails were sent and no credentials were collected.

### Data supplied

| Campaign | Lure | Target group | Sent | Opened | Clicked | Credentials submitted | Data entry |
|---|---|---|---|---|---|---|---|
| A | HR Bonus Notification | 100 employees | 100 | 82 | 47 | 18 | 5 |
| B | IT System Password Reset | 250 employees | 250 | 200 | 150 | 75 | 25 |
| C | CEO Urgent Document Review | 80 executives and assistants | 80 | 72 | 60 | 12 | 8 |

**Organisational context (from the brief):**

- Total employees: 2,000
- Average salary: $85,000 per year
- Estimated cost of a data breach: $4.35 million
- Probability of a major breach if credentials are stolen: 25%

The breach cost and the control-effectiveness percentages are treated as **scenario assumptions**, not verified industry benchmarks.

## Objectives

1. Calculate campaign open, click-through, credential submission and data entry rates.
2. Calculate conversion rates using the correct denominators.
3. Evaluate financial exposure using clearly documented assumptions.
4. Compare control costs, estimated risk reductions and return on investment.
5. Calculate and interpret confidence intervals.
6. Identify errors and limitations in quantitative risk models and communicate defensible conclusions.

## Deliverables

- Completed calculation worksheets for Phases 1 and 2
- Risk assessment matrix
- Statistical analysis with confidence intervals
- Executive briefing with financial calculations
- Control recommendation table with ROI calculations
- Bonus: break-even analysis for the $490,000 investment

## Brief's guidance on errors

Some worked examples in the brief contain calculation errors or unsupported assumptions, so every figure was independently verified. In particular:

- Click-through rate is distinguished from credential submission rate.
- Compromised accounts are not treated as independent breaches without justification.
- Annualised loss estimates use an explicit annual occurrence assumption.

## Repository layout

| Path | Purpose |
|---|---|
| `analysis/Lab3_Phishing_Risk_Analysis.xlsx` | Calculation workbook (live formulas, 9 sheets) |
| `analysis/verify_calculations.py` | Independent Python re-computation used to cross-check the workbook |
| `analysis/make_figures.py` | Generates the charts in `figures/` |
| `data/campaign_results.csv` | Supplied simulation results |
| `report/` | Written executive report |
| `figures/` | Funnel, confidence-interval and ROI charts |

## Headline results

| Campaign | Open | Click | Credential | Data entry | Credential 95 % CI (Wilson) |
|---|---|---|---|---|---|
| A – HR Bonus (n=100) | 82.0 % | 47.0 % | 18.0 % | 5.0 % | 11.7 – 26.7 % |
| B – IT Reset (n=250) | 80.0 % | 60.0 % | 30.0 % | 10.0 % | 24.7 – 35.9 % |
| C – CEO Doc (n=80) | 90.0 % | 75.0 % | 15.0 % | 10.0 % | 8.8 – 24.4 % |
| Pooled (n=430) | 82.3 % | 59.8 % | 24.4 % | 8.8 % | 20.6 – 28.7 % |

* Click-through (stage 2) and credential submission (stage 3) are different metrics. Campaign B: 60 % clicked, 30 % submitted credentials (50 % of clickers).
* B vs A is significant (p ≈ 0.02); A vs C is not (p ≈ 0.59).
* **Defensible baseline ALE ≈ $1.09 M/yr** (SLE $4.35 M × ARO 0.25 at k = 1 event/yr) versus the brief's $652.5 M.
* ROI (direct cost, base case): MFA ≈ 1,107 %, training ≈ 552 %, email filtering ≈ 335 % – all conditional on scenario effectiveness assumptions. Once MFA is in place, the marginal ROI of the other two (on this risk alone) is negative.
* Break-even: $490,000 ÷ $4,350,000 ≈ **0.113 of a breach** per year.

## Method and key corrections to the brief

1. **Denominators** – headline rates use emails *sent*; conversion rates use the *previous* funnel stage.
2. **Accounts ≠ breaches** – the brief treats 600 compromised accounts as 150 independent breaches (implying a ~100 % chance of a breach, and $652.5 M of loss). A breach is an organisation-level event; the 25 % is applied once per credential-theft event.
3. **ALE needs an explicit annual rate** – ARO = k × 25 %, with k (events per year) stated as an assumption and sensitivity-tested (k = 1, 2, 4).
4. **Arithmetic errors fixed** – matrix exposure for A ($391.5 M, not $156.6 M) and C ($326.25 M, not $104.4 M) by the brief's own method; pooled rate 24.4 % not 22.1 %; email-filter ROI 260,900 % not 260,800 %; controls' "reductions" summing to more than the baseline; post-control table totals.
5. **Scenario assumptions flagged** – $4.35 M breach cost, 25 % escalation, MFA 99.9 %, training 60 %, filtering 20 %. "Industry average" figures with no source were excluded.

The full list (23 items) is on the workbook's `Error_Log` sheet.

## How to reproduce

```bash
python analysis/verify_calculations.py   # prints every headline number
python analysis/make_figures.py          # regenerates figures/
```
Open the workbook, change the yellow cells on `Inputs`, and every sheet recalculates.

## Limitations
* Simulation groups were not random samples and saw different lures; confidence intervals capture sampling error only.
* Sampling error is small compared with uncertainty in the scenario assumptions (breach cost, escalation probability, control effectiveness, event frequency).
* Costs are treated as annual; benefits outside credential theft (malware, BEC, compliance, insurance) are not modelled.
