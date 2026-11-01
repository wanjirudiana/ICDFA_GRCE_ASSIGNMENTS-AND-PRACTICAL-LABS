import math, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).parent.parent / "figures"
camps = ["A: HR Bonus", "B: IT Reset", "C: CEO Doc"]
sent = [100, 250, 80]; data = {"Open": [82, 200, 72], "Click": [47, 150, 60], "Credential": [18, 75, 12], "Data entry": [5, 25, 8]}
fig, ax = plt.subplots(figsize=(8, 4.5)); w = 0.2
for i, (k, v) in enumerate(data.items()):
    ax.bar([x + i * w for x in range(3)], [a / s * 100 for a, s in zip(v, sent)], w, label=k)
ax.set_xticks([x + 1.5 * w for x in range(3)]); ax.set_xticklabels(camps); ax.set_ylabel("% of emails sent"); ax.set_title("Campaign funnel rates"); ax.legend(); fig.tight_layout(); fig.savefig(out / "funnel_rates.png", dpi=150)
fig, ax = plt.subplots(figsize=(8, 3.5)); Z = 1.96
for i, (x, n, l) in enumerate([(18, 100, "A"), (75, 250, "B"), (12, 80, "C")]):
    p = x / n; d = 1 + Z**2 / n; c = (p + Z**2 / (2 * n)) / d; h = Z * math.sqrt(p * (1 - p) / n + Z**2 / (4 * n**2)) / d
    ax.errorbar(p * 100, i, xerr=[[p * 100 - (c - h) * 100], [(c + h) * 100 - p * 100]], fmt="o", capsize=5); 
ax.set_yticks(range(3)); ax.set_yticklabels(["A (n=100)", "B (n=250)", "C (n=80, census)"]); ax.set_xlabel("Credential submission rate (%), 95% Wilson CI"); ax.set_title("Credential submission rate with 95% CI"); fig.tight_layout(); fig.savefig(out / "credential_ci.png", dpi=150)
fig, ax = plt.subplots(figsize=(8, 4)); ale = 1_087_500
names = ["MFA", "Training", "Email filtering"]; cost = [90_000, 100_000, 50_000]; eff = [.999, .6, .2]
ax.bar(names, [(ale * e - c) / c * 100 for e, c in zip(eff, cost)]); ax.set_ylabel("ROI % (direct cost, base case)"); ax.set_title("Control ROI - defensible model (scenario assumptions)"); fig.tight_layout(); fig.savefig(out / "control_roi.png", dpi=150)
