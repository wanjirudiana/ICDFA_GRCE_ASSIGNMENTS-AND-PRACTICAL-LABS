# GRC103 Module 3 | Lab 2: Ransomware Risk Treatment Case Lab

**Scenario:** Advise Northbridge Community Health (a fictional three-clinic provider) on how to spend a $100,000 first-year budget to reduce ransomware risk.
**Inspiration:** The 2021 ransomware attack on Ireland's Health Service Executive (HSE).
**Source:** Health Service Executive, *Cyber-attack and HSE response*; last reviewed 1 December 2025; accessed 18 October 2026. https://www2.hse.ie/services/cyber-attack/what-happened/

> Northbridge, its budget, treatment prices, insurance terms and the later change in circumstances are fictional classroom assumptions. They are not facts about HSE.

---

## What is in this package

| File | Purpose |
|---|---|
| `Northbridge_Lab2_Report.pdf` | The report to submit (the limit is 4). |
| `Northbridge_Lab2_Workbook.xlsx` | The editable spreadsheet to submit: risk register, budget and insurance calculations. |
| `README.md` | This file. |


## How the lab is organised

| Task | What it asks | Where to find it |
|---|---|---|
| 1. Assess and prioritise risks | Four risks, a register, two HSE facts kept separate from assumptions, scores with explanations | Report Task 1; workbook `Evidence` and `Risk Register` |
| 2. Treatment portfolio | Options within $100,000, avoidance, mitigation, transfer, one time-limited acceptance | Report Task 2; workbook `Budget` |
| 3. Retained financial exposure | Insurance payout and retained loss for $180,000 and $400,000 losses | Report Task 3; workbook `Insurance` |
| 4. Respond to a change | Failed restore test, 4-hour paper limit, option B rises to $35,000 | Report Task 4; workbook `Decision Record` |
| 5. Plan and communicate | 30-day plan, residual risk re-scoring, board memo (max 300 words) | Report Task 5; workbook `30-Day Plan` |

## Workbook guide

| Sheet | Contents |
|---|---|
| `Cover` | Your details, source link, colour legend |
| `Evidence` | HSE facts (H1, H2) separated from Northbridge assumptions (N1 to N5) |
| `Risk Register` | Four risks with asset, threat, weakness, impact, owner, initial and residual scores (formulas) |
| `Budget` | Options A to G, initial and revised selections, totals, remaining budget, within-budget check |
| `Insurance` | Policy inputs and payout, retained loss and total outlay for covered and excluded claims |
| `Decision Record` | Initial decision versus revised decision after the change |
| `30-Day Plan` | Actions with owner, cost, target date and effectiveness test; cost check against the budget |

**Colour code:** blue text = editable input, black = formula, green = link to another sheet.
Scores, ratings, totals and insurance results are **formulas**. Change an input (for example a likelihood, or a 1/0 selection on the `Budget` sheet) and everything recalculates.

## Key results at a glance

**Initial risk scores** (likelihood x impact; Low 1-4, Medium 5-9, High 10-16, Critical 17-25):

| Risk | Score | Rating |
|---|---|---|
| R1 Service disruption | 4 x 5 = 20 | Critical (cannot be accepted) |
| R2 Sensitive-data loss | 3 x 5 = 15 | High (board escalation) |
| R3 Unnecessary supplier exposure | 4 x 3 = 12 | High (board escalation) |
| R4 Delayed detection | 4 x 4 = 16 | High (board escalation) |

**Decisions:**

| | Options | Committed | Remaining |
|---|---|---|---|
| Decision 1 (initial) | A, C, D, E, G | $100,000 | $0 |
| Decision 2 (after the change) | A, C, D, E | $80,000 | $20,000 ring-fenced continuity reserve |

**Insurance (option G):** insurer payment = min(max(loss - $25,000, 0), $250,000)

| Loss | Insurer pays | Retained | Total outlay (with $20,000 premium) |
|---|---|---|---|
| $180,000 covered | $155,000 | $25,000 | $45,000 |
| $400,000 covered | $250,000 | $150,000 | $170,000 |
| Claim excluded | $0 | Entire loss | Loss + $20,000 |

**Residual risk after the revised plan:** R1 15 High, R2 12 High, R3 6 Medium, R4 9 Medium. Untested controls are not treated as proven effective.

**Time-limited acceptance:** residual R2 gap from deferring MFA and segmentation. Owner: Data Protection Officer. Expiry: 30 June 2027. Simulated approver: Board Risk Committee Chair.

## Assumptions and notes

- Owners such as COO, Data Protection Officer, Head of IT and IT Security Lead are roles assumed for the fictional organisation.
- The **24-hour manual booking target** is a proposal for the board to confirm. It is not part of the lab brief.
- Dates in the 30-day plan run from 12 November to 11 December 2026.
- Insurance and managed services do not remove organisational accountability.
- Other reasonable portfolios exist (for example, keeping insurance after the change). Marking rewards consistent, evidence-based reasoning, not one fixed answer.

## Marking guide (100 marks)

Evidence and risk register 20 | Treatment selection and budget 25 | Financial calculations 15 | Response to the change and residual risk 20 | Treatment plan and board memo 20
