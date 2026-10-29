import itertools
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Patch, Rectangle
from openpyxl import load_workbook

OUT = "images/"
wb = load_workbook("Lab3b_Risk_Quantification.xlsx", data_only=True)
rk, ct, pj = wb["Risk"], wb["Controls"], wb["Projection"]
names = ["API Authentication\nBypass", "Database\nInjection", "Session\nHijacking"]
short = ["F1 API Auth Bypass", "F2 DB Injection", "F3 Session Hijacking"]
ale = [rk[f"D{r}"].value for r in (5, 6, 7)]
sle = [rk[f"B{r}"].value for r in (5, 6, 7)]
aro = [rk[f"C{r}"].value for r in (5, 6, 7)]
prio = [rk[f"F{r}"].value for r in (5, 6, 7)]
cn = ["API Security Gateway", "Web Application Firewall", "MFA Enhancement"]
init = [ct[f"B{r}"].value for r in (5, 6, 7)]
maint = [ct[f"C{r}"].value for r in (5, 6, 7)]
eff = [ct[f"F{r}"].value for r in (5, 6, 7)]
red = [ct[f"G{r}"].value for r in (5, 6, 7)]
resid = [ct[f"H{r}"].value for r in (5, 6, 7)]
roi1 = [ct[f"J{r}"].value for r in (5, 6, 7)]
pay_d = [ct[f"O{r}"].value for r in (5, 6, 7)]
y1 = [ct[f"I{r}"].value for r in (5, 6, 7)]
H = wb["Inputs"]["B19"].value

PC = {"Critical": "#C0392B", "High": "#E67E22", "Medium": "#F1C40F", "Low": "#27AE60"}
NAVY, TEAL, GREY = "#1F3864", "#2E86AB", "#7F8C8D"
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False,
                     "axes.titleweight": "bold", "axes.titlesize": 13, "figure.dpi": 150})

def money(x, _=None):
    a = abs(x)
    if a >= 1e6: return f"${x/1e6:,.1f}M" if a % 1e6 else f"${x/1e6:,.0f}M"
    if a >= 1e3: return f"${x/1e3:,.0f}K"
    return f"${x:,.0f}"
MF = FuncFormatter(money)

# 1 ALE bar
fig, ax = plt.subplots(figsize=(9, 5.5))
b = ax.bar(names, ale, color=[PC[p] for p in prio], edgecolor="black", linewidth=.6)
for r, v in zip(b, ale): ax.text(r.get_x()+r.get_width()/2, v, f"${v:,.0f}", ha="center", va="bottom", fontweight="bold", fontsize=10)
ax.set_title("Annualized Loss Expectancy (ALE) by Vulnerability"); ax.set_ylabel("ALE (USD per year)")
ax.set_xlabel("Vulnerability"); ax.yaxis.set_major_formatter(MF); ax.set_ylim(0, max(ale)*1.12)
ax.legend(handles=[Patch(color=PC[k], label=k) for k in ("Critical", "High", "Medium")], title="Risk priority")
fig.tight_layout(); fig.savefig(OUT+"01_ale_bar.png"); plt.close()

# 2 pie
fig, ax = plt.subplots(figsize=(7.5, 6))
w, t, a = ax.pie(ale, labels=short, colors=[PC[p] for p in prio], autopct="%1.1f%%", startangle=90, pctdistance=.75,
                 wedgeprops=dict(edgecolor="white", linewidth=2), textprops={"fontsize": 10})
for x in a: x.set_fontweight("bold")
ax.set_title("Share of Total ALE ($35.0M)"); ax.legend(w, [f"{s}: ${v:,.0f}" for s, v in zip(short, ale)], loc="lower center", bbox_to_anchor=(.5, -.12), fontsize=9)
fig.tight_layout(); fig.savefig(OUT+"02_risk_distribution_pie.png"); plt.close()

# 3 heat map
import numpy as np
inp = wb["Inputs"]
levels = ["Low", "Medium", "High"]
mat = {imp: [inp[f"{c}{r}"].value for c in "BCD"] for imp, r in zip(["High", "Medium", "Low"], (31, 32, 33))}
HC = {"Low": "#27AE60", "Medium": "#F1C40F", "High": "#E74C3C"}
fig, ax = plt.subplots(figsize=(8.5, 6))
for i, imp in enumerate(["High", "Medium", "Low"]):
    for j, p in enumerate(levels):
        ax.add_patch(Rectangle((j, 2-i), 1, 1, facecolor=HC[mat[imp][j]], edgecolor="white", linewidth=3, alpha=.85))
        ax.text(j+.5, 2-i+.08, mat[imp][j], ha="center", va="bottom", fontsize=9, color="#333", alpha=.7)
pb = [rk[f"G{r}"].value for r in (5, 6, 7)]; ib = [rk[f"H{r}"].value for r in (5, 6, 7)]
cnt = {}
for k in range(3):
    j, i = levels.index(pb[k]), ["High", "Medium", "Low"].index(ib[k]); n = cnt.get((j, i), 0); cnt[(j, i)] = n+1
    ax.text(j+.5, 2-i+.62-n*.25, f"F{k+1}: {short[k][3:]}\n({aro[k]:.0%}, ${sle[k]/1e6:,.1f}M SLE)", ha="center", va="center", fontsize=9, fontweight="bold",
            bbox=dict(boxstyle="round", fc="white", ec="black"))
ax.set_xlim(0, 3); ax.set_ylim(0, 3)
ax.set_xticks([.5, 1.5, 2.5]); ax.set_xticklabels(["Low\n(<20%)", "Medium\n(20-<35%)", "High\n(>=35%)"])
ax.set_yticks([.5, 1.5, 2.5]); ax.set_yticklabels(["Low\n(<$1M)", "Medium\n(\\$1M to <\\$10M)", "High\n(>=$10M)"])
ax.set_xlabel("Probability of exploit (annual)"); ax.set_ylabel("Impact (single loss event)")
ax.set_title("Risk Heat Map - Probability vs Impact"); ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.legend(handles=[Patch(color=HC[k], label=k) for k in ("High", "Medium", "Low")], title="Rating", loc="upper left", bbox_to_anchor=(1.01, 1))
fig.tight_layout(); fig.savefig(OUT+"03_risk_heatmap.png"); plt.close()

# 4 scatter cost vs effectiveness
fig, ax = plt.subplots(figsize=(9, 6))
cols = [PC[p] for p in prio]
ax.scatter(init, [e*100 for e in eff], s=[r/ max(red)*2500+200 for r in red], c=cols, alpha=.75, edgecolor="black")
for x, y, n, r in zip(init, eff, cn, red):
    ax.annotate(f"{n}\nrisk reduction {money(r)}/yr", (x, y*100), xytext=(12, -34 if y < .9 else 14), textcoords="offset points", fontsize=9, fontweight="bold")
ax.set_xlabel("Initial investment (USD)"); ax.set_ylabel("Effectiveness (% reduction of targeted vulnerability)")
ax.set_title("Control Cost vs Effectiveness\n(bubble size = annual $ risk reduction)")
ax.xaxis.set_major_formatter(MF); ax.set_xlim(100000, 420000); ax.set_ylim(65, 102); ax.grid(alpha=.3)
ax.legend(handles=[Patch(color=PC[p], label=f"Mitigates {p}-priority risk") for p in ("Critical", "High", "Medium")], loc="lower right", fontsize=8)
fig.tight_layout(); fig.savefig(OUT+"04_cost_vs_effectiveness_scatter.png"); plt.close()

# 5 ROI horizontal (log)
order = sorted(range(3), key=lambda i: roi1[i])
fig, ax = plt.subplots(figsize=(9.5, 4.8))
vals = [roi1[i]*100 for i in order]
bars = ax.barh([cn[i] for i in order], vals, color=[PC[prio[i]] for i in order], edgecolor="black", linewidth=.6)
ax.set_xscale("log"); ax.set_xlim(10, 80000)
for bar, v, i in zip(bars, vals, order):
    ax.text(v*1.12, bar.get_y()+bar.get_height()/2, f"{v:,.0f}%  (payback {pay_d[i]:,.0f} days)", va="center", fontsize=9, fontweight="bold")
ax.set_xlabel("Year-1 ROI (%) - logarithmic scale"); ax.set_ylabel("Control")
ax.set_title("Return on Investment by Control (Year 1)"); ax.grid(axis="x", alpha=.3)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}%"))
ax.legend(handles=[Patch(color=PC[p], label=f"Mitigates {p} risk") for p in ("Critical", "High", "Medium")], loc="lower right", fontsize=8)
fig.tight_layout(); fig.savefig(OUT+"05_roi_horizontal_bar.png"); plt.close()

# 6 line: residual exposure phased
months = [pj[f"A{r}"].value for r in range(19, 32)]
expo = [pj[f"B{r}"].value for r in range(19, 32)]
fig, ax = plt.subplots(figsize=(9.5, 5.5))
ax.step(months, expo, where="post", color=NAVY, linewidth=2.5, marker="o")
ev = [(1, "WAF live (day ~30)"), (3, "MFA live (day ~90)"), (6, "API Gateway live (~month 6)")]
for m, t in ev:
    ax.annotate(f"{t}\n{money(expo[m])}/yr", (m, expo[m]), xytext=(m+.4, expo[m]+4e6), fontsize=9, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GREY))
ax.axhline(expo[-1], ls="--", color=GREY); ax.text(12, expo[-1]+.8e6, "Residual risk", ha="right", fontsize=9, color=GREY)
ax.set_xlabel("Months from project start"); ax.set_ylabel("Annualized exposure (USD per year)")
ax.set_title("Risk Reduction Over Time - Phased Control Roll-out"); ax.yaxis.set_major_formatter(MF)
ax.set_xticks(range(13)); ax.set_ylim(0, 40e6); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(OUT+"06_risk_reduction_timeline.png"); plt.close()

# 6b cumulative net benefit
yrs = list(range(6))
fig, ax = plt.subplots(figsize=(9.5, 5.5))
for r, n, p in zip((6, 7, 8), cn, prio):
    ax.plot(yrs, [pj[f"{c}{r}"].value for c in "BCDEFG"], marker="o", linewidth=2.2, label=n, color=PC[p] if p != "Medium" else "#D4AC0D")
ax.plot(yrs, [pj[f"{c}9"].value for c in "BCDEFG"], marker="s", linewidth=3, ls="--", color=NAVY, label="Portfolio")
ax.axhline(0, color="black", linewidth=.8)
ax.set_xlabel("Years after deployment"); ax.set_ylabel("Cumulative net benefit (USD)"); ax.yaxis.set_major_formatter(MF)
ax.set_title("Cumulative Net Benefit of Controls (benefit - cost)"); ax.legend(); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(OUT+"06b_cumulative_net_benefit.png"); plt.close()

# 7 before / after
import numpy as np
x = np.arange(3); w = .38
fig, ax = plt.subplots(figsize=(9.5, 5.5))
b1 = ax.bar(x-w/2, ale, w, label="Before controls (ALE)", color="#C0392B", edgecolor="black", linewidth=.6)
b2 = ax.bar(x+w/2, resid, w, label="After controls (residual ALE)", color="#27AE60", edgecolor="black", linewidth=.6)
for bs in (b1, b2):
    for r in bs: ax.text(r.get_x()+r.get_width()/2, r.get_height(), money(r.get_height()), ha="center", va="bottom", fontsize=9, fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(names); ax.set_ylabel("ALE (USD per year)"); ax.set_xlabel("Vulnerability")
ax.set_title("Risk Exposure Before vs After Controls"); ax.yaxis.set_major_formatter(MF); ax.legend(); ax.set_ylim(0, max(ale)*1.12)
fig.tight_layout(); fig.savefig(OUT+"07_before_after_double_bar.png"); plt.close()

# 8 stacked investment (3-year TCO)
fig, ax = plt.subplots(figsize=(9, 5.5))
m3 = [m*H for m in maint]
ax.bar(cn, init, label="Initial investment", color=NAVY, edgecolor="black", linewidth=.6)
ax.bar(cn, m3, bottom=init, label=f"Maintenance ({H} years)", color=TEAL, edgecolor="black", linewidth=.6)
for i in range(3):
    ax.text(i, init[i]/2, money(init[i]), ha="center", color="white", fontweight="bold")
    ax.text(i, init[i]+m3[i]/2, money(m3[i]), ha="center", color="white", fontweight="bold")
    ax.text(i, init[i]+m3[i]+8000, f"Total {money(init[i]+m3[i])}", ha="center", fontweight="bold")
ax.set_ylabel("Cost (USD)"); ax.set_xlabel("Control"); ax.yaxis.set_major_formatter(MF)
ax.set_title(f"Control Investment Breakdown ({H}-Year Total Cost of Ownership)"); ax.legend(); ax.set_ylim(0, 560000)
fig.tight_layout(); fig.savefig(OUT+"08_investment_stacked_bar.png"); plt.close()

# 9 Gantt
tasks = [("IMMEDIATE (0-30 days)", None, None, None),
 ("Emergency triage + virtual patches for F1-F3", 0, 14, "#C0392B"),
 ("Deploy Web Application Firewall (WAF)", 0, 30, "#C0392B"),
 ("Enable API / DB / session anomaly monitoring", 7, 30, "#C0392B"),
 ("IR runbook + breach-notification readiness", 0, 30, "#C0392B"),
 ("SHORT-TERM (30-90 days)", None, None, None),
 ("Roll out MFA enhancement", 30, 90, "#E67E22"),
 ("Fix root cause: parameterized queries / code fixes", 15, 90, "#E67E22"),
 ("Re-test (pen test validation of F2, F3)", 75, 90, "#E67E22"),
 ("LONG-TERM (90-365 days)", None, None, None),
 ("Deploy Advanced API Security Gateway", 90, 180, "#2E86AB"),
 ("Encrypt / tokenize PII at rest (reduce F2 residual)", 120, 270, "#2E86AB"),
 ("Quarterly risk re-quantification + CISO/CFO review", 90, 365, "#2E86AB"),
 ("Annual full pen test + program review", 335, 365, "#2E86AB")]
fig, ax = plt.subplots(figsize=(12, 6.5))
for i, (n, s, e, c) in enumerate(tasks):
    y = len(tasks)-i
    if s is None: ax.text(-3, y, n, fontweight="bold", fontsize=10, color=NAVY, ha="right", va="center"); continue
    ax.barh(y, e-s, left=s, color=c, edgecolor="black", height=.55)
    ax.text(-3, y, n, ha="right", va="center", fontsize=9)
    ax.text(e+3, y, f"d{s}-{e}", va="center", fontsize=8, color=GREY)
for d, lab in [(30, "30 days"), (90, "90 days"), (365, "1 year")]:
    ax.axvline(d, ls="--", color=GREY, alpha=.7); ax.text(d, len(tasks)+1, lab, ha="center", fontsize=9, fontweight="bold")
ax.set_xlim(0, 390); ax.set_ylim(0, len(tasks)+1.6); ax.set_yticks([])
ax.set_xlabel("Days from project start"); ax.set_title("Risk Treatment Timeline (Gantt)", pad=20)
ax.spines["left"].set_visible(False)
ax.legend(handles=[Patch(color="#C0392B", label="Immediate"), Patch(color="#E67E22", label="Short-term"), Patch(color="#2E86AB", label="Long-term")], loc="upper right", bbox_to_anchor=(1, .85))
fig.subplots_adjust(left=.38, right=.97); fig.savefig(OUT+"09_gantt_risk_treatment.png"); plt.close()

# 10 Bonus: budget frontier
combos = [("None", ()), ("API", (0,)), ("WAF", (1,)), ("MFA", (2,)), ("API+WAF", (0, 1)), ("API+MFA", (0, 2)), ("WAF+MFA", (1, 2)), ("All 3", (0, 1, 2))]
pts = [(n, sum(y1[i] for i in s), sum(red[i] for i in s)) for n, s in combos]
front = []; best = -1
for n, c, b in sorted(pts, key=lambda p: p[1]):
    if b > best: front.append((n, c, b)); best = b
fig, ax = plt.subplots(figsize=(9.5, 5.8))
ax.scatter([p[1] for p in pts], [p[2] for p in pts], s=90, color=GREY, zorder=3)
ax.plot([p[1] for p in front], [p[2] for p in front], color=NAVY, linewidth=2.5, marker="o", zorder=4, label="Efficient frontier")
for n, c, b in pts: ax.annotate(n, (c, b), xytext=(6, -14), textcoords="offset points", fontsize=9)
for bud, lab in [(250000, "$250K"), (450000, "$450K"), (850000, "$850K")]:
    ax.axvline(bud, ls=":", color="#C0392B"); ax.text(bud, 1.5e6, f"budget {lab}", rotation=90, ha="right", va="bottom", fontsize=8, color="#C0392B")
ax.set_xlabel("Year-1 outlay (initial + maintenance, USD)"); ax.set_ylabel("Annual risk reduction (USD)")
ax.set_title("Bonus: Cost vs Risk-Reduction Benefit for Every Control Combination")
ax.xaxis.set_major_formatter(MF); ax.yaxis.set_major_formatter(MF); ax.grid(alpha=.3); ax.legend(loc="center right")
fig.tight_layout(); fig.savefig(OUT+"10_bonus_budget_frontier.png"); plt.close()

# 11 Executive dashboard
fig = plt.figure(figsize=(16, 10)); gs = fig.add_gridspec(3, 3, height_ratios=[.55, 1.6, 1.5], hspace=.55, wspace=.32, left=.06, right=.97, top=.89, bottom=.07)
fig.suptitle("SecureMobile Banking Platform - Cyber Risk Executive Dashboard", fontsize=20, fontweight="bold", color=NAVY, y=.975)
fig.text(.5, .925, "Prepared for CISO / CFO  |  Quantitative risk analysis (ALE = SLE x ARO)", ha="center", fontsize=11, color=GREY)
tot_ale, tot_red = sum(ale), sum(red)
tiles = [("Total annual exposure", money(tot_ale), "#C0392B"), ("Annual risk reduction", money(tot_red), "#27AE60"),
         ("Year-1 investment", money(sum(y1)), NAVY)]
for k, (l, v, c) in enumerate(tiles):
    a = fig.add_subplot(gs[0, k]); a.axis("off")
    a.add_patch(Rectangle((0, 0), 1, 1, transform=a.transAxes, facecolor=c, alpha=.92))
    a.text(.5, .62, v, transform=a.transAxes, ha="center", va="center", fontsize=26, fontweight="bold", color="white")
    a.text(.5, .18, l, transform=a.transAxes, ha="center", va="center", fontsize=12, color="white")
# top 3 risks table
a = fig.add_subplot(gs[1, 0]); a.axis("off"); a.set_title("Top 3 Risks (ranked by ALE)", loc="left")
rank = sorted(range(3), key=lambda i: -ale[i])
cells = [[f"{k+1}. {short[i][3:]}", f"${sle[i]/1e6:,.2f}M", f"{aro[i]:.0%}", f"${ale[i]/1e6:,.2f}M", prio[i]] for k, i in enumerate(rank)]
tb = a.table(cellText=cells, colLabels=["Risk", "SLE", "ARO", "ALE", "Priority"], loc="upper center", cellLoc="center", colWidths=[.34, .2, .1, .2, .16])
tb.auto_set_font_size(False); tb.set_fontsize(9); tb.scale(1, 2.6)
for (r, c), cell in tb.get_celld().items():
    if r == 0: cell.set_facecolor(NAVY); cell.get_text().set_color("white"); cell.get_text().set_fontweight("bold")
    elif c == 4: cell.set_facecolor(PC[cells[r-1][4]]); cell.get_text().set_fontweight("bold")
# before/after
a = fig.add_subplot(gs[1, 1]); w = .38
a.bar(x-w/2, ale, w, color="#C0392B", label="Before"); a.bar(x+w/2, resid, w, color="#27AE60", label="After")
a.set_xticks(x); a.set_xticklabels(["F1 API", "F2 DB inj.", "F3 Session"], fontsize=9); a.yaxis.set_major_formatter(MF)
a.set_title("Risk Exposure Before vs After"); a.set_ylabel("ALE (USD/yr)"); a.legend(fontsize=8)
# ROI
a = fig.add_subplot(gs[1, 2]); a.barh([cn[i] for i in order], vals, color=[PC[prio[i]] for i in order], edgecolor="black", linewidth=.5)
a.set_xscale("log"); a.set_xlim(10, 1e6); a.set_title("Year-1 ROI by Control"); a.set_xlabel("ROI % (log scale)")
for bar, v in zip(a.patches, vals): a.text(v*1.2, bar.get_y()+bar.get_height()/2, f"{v:,.0f}%", va="center", fontsize=9, fontweight="bold")
a.tick_params(axis="y", labelsize=8)
# recommended controls table
a = fig.add_subplot(gs[2, 0:2]); a.axis("off"); a.set_title("Recommended Controls (implement in ROI order)", loc="left")
rows = [[cn[i], f"${init[i]:,.0f}", f"${maint[i]:,.0f}", f"${red[i]:,.0f}", f"{roi1[i]*100:,.0f}%", f"{pay_d[i]:,.0f} days"] for i in reversed(order)]
rows.append(["Portfolio", f"${sum(init):,.0f}", f"${sum(maint):,.0f}", f"${tot_red:,.0f}", f"{ct['J8'].value*100:,.0f}%", f"{ct['O8'].value:,.0f} days"])
tb = a.table(cellText=rows, colLabels=["Control", "Initial", "Annual maint.", "Annual risk reduction", "Yr-1 ROI", "Payback"], loc="upper center", cellLoc="center", colWidths=[.32, .12, .14, .2, .12, .1])
tb.auto_set_font_size(False); tb.set_fontsize(9); tb.scale(1, 2.2)
for (r, c), cell in tb.get_celld().items():
    if r == 0: cell.set_facecolor(NAVY); cell.get_text().set_color("white"); cell.get_text().set_fontweight("bold")
    if r == len(rows): cell.set_facecolor("#D9E1F2"); cell.get_text().set_fontweight("bold")
# stacked
a = fig.add_subplot(gs[2, 2]); a.bar(["API GW", "WAF", "MFA"], init, color=NAVY, label="Initial"); a.bar(["API GW", "WAF", "MFA"], m3, bottom=init, color=TEAL, label=f"Maint. ({H}y)")
a.yaxis.set_major_formatter(MF); a.set_title("Investment Breakdown"); a.set_ylabel("USD"); a.legend(fontsize=8)
fig.text(.06, .015, f"Residual exposure after all controls: {money(sum(resid))}/yr ({sum(resid)/tot_ale:.0%} of baseline). Largest remaining item: F2 DB injection {money(resid[1])}/yr -> add parameterized queries + PII encryption (see Gantt).", fontsize=9.5, style="italic", color="#333", parse_math=False)
fig.savefig(OUT+"11_executive_dashboard.png"); plt.close()
print("done")
