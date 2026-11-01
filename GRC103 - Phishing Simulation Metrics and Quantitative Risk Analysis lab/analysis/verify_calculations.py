"""Independent re-computation of the Lab 3 workbook (cross-check; no spreadsheet needed).
Run:  python analysis/verify_calculations.py
"""
import csv, math
from pathlib import Path

Z = 1.96
SLE, P_BREACH, STAFF, EXECS = 4_350_000, 0.25, 2000, 80
K = 1  # campaign-equivalent phishing events per year (ANALYST ASSUMPTION)

rows = list(csv.DictReader(open(Path(__file__).parent.parent / "data" / "campaign_results.csv")))
for r in rows:
    for c in ("sent", "opened", "clicked", "credentials_submitted", "data_entry"):
        r[c] = int(r[c])

def wald(x, n):
    p = x / n; m = Z * math.sqrt(p * (1 - p) / n); return p, max(0, p - m), min(1, p + m)
def wilson(x, n):
    p = x / n; d = 1 + Z**2 / n
    c = (p + Z**2 / (2 * n)) / d; h = Z * math.sqrt(p * (1 - p) / n + Z**2 / (4 * n**2)) / d
    return c - h, c + h

print("== Phase 1: rates (denominator = emails sent) and conversions ==")
for r in rows:
    s = r["sent"]
    print(f"{r['campaign']}: open {r['opened']/s:.1%} click {r['clicked']/s:.1%} cred {r['credentials_submitted']/s:.1%} "
          f"data {r['data_entry']/s:.1%} | open->click {r['clicked']/r['opened']:.1%} "
          f"click->cred {r['credentials_submitted']/r['clicked']:.1%}")
tot = {c: sum(r[c] for r in rows) for c in ("sent", "credentials_submitted")}
pooled = tot["credentials_submitted"] / tot["sent"]
print(f"Pooled credential rate: {tot['credentials_submitted']}/{tot['sent']} = {pooled:.1%} (brief said 22.1%)")

print("\n== Brief method re-done (NOT defensible) ==")
for r in rows:
    rate = r["credentials_submitted"] / r["sent"]
    print(f"{r['campaign']}: {rate*STAFF:.0f} accounts x 25% = {rate*STAFF*P_BREACH:.0f} 'breaches' -> ${rate*STAFF*P_BREACH*SLE:,.0f}")
print(f"P(>=1 breach) if 600 accounts independent: {1-(1-P_BREACH)**600:.4%}")

print("\n== Defensible ALE (SLE x ARO, ARO = k x P per event) ==")
for k in (1, 2, 4):
    aro = k * P_BREACH
    print(f"k={k}: ARO={aro:.2f}  ALE=${aro*SLE:,.0f}  P(>=1 breach/yr)={1-(1-P_BREACH)**k:.1%}")
ale0 = K * P_BREACH * SLE

print("\n== Controls (scenario effectiveness; costs treated as annual) ==")
ctrl = {"MFA": (45 * STAFF, 0.999), "Training": (50 * STAFF, 0.60), "Email filtering": (50_000, 0.20)}
resid = 1
for n, (cost, e) in ctrl.items():
    red = ale0 * e; resid *= 1 - e
    print(f"{n}: cost ${cost:,.0f} reduction ${red:,.0f} ROI {(red-cost)/cost:.0%} break-even effectiveness {cost/ale0:.1%}")
cost_all = sum(c for c, _ in ctrl.values())
print(f"Combined: effectiveness {1-resid:.4%}, reduction ${ale0*(1-resid):,.0f}, cost ${cost_all:,.0f}")

print("\n== Confidence intervals (credential submission) ==")
for r in rows:
    p, lo, hi = wald(r["credentials_submitted"], r["sent"]); wl, wh = wilson(r["credentials_submitted"], r["sent"])
    print(f"{r['campaign']}: p={p:.1%} Wald {lo:.1%}-{hi:.1%} Wilson {wl:.1%}-{wh:.1%}")

print(f"\nBreak-even: $490,000 / ${SLE:,} = {490_000/SLE:.4f} breaches")
