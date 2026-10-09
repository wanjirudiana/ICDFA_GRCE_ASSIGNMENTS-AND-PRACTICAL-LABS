# GRC102 Practical Lab 8 — Security Governance Simulation

**Author:** Diana Wanjiru
**Student ID:** C11/26/CGRCE/17188
**Course:** GRC102 Information Security Governance
**Assessment:** Practical Lab 8 — Monitoring, Auditing Controls and Executive Reporting

This repository contains an isolated Docker-based security governance simulation modelled on the governance failures associated with the 2017 Equifax data breach, built for the GRC102 Week 8 practical lab. It includes an intentionally vulnerable environment, a vulnerability scanner, an attack simulation, a governance tracker, control-implementation scripts, and automated metrics/reporting tooling.

Official lab instructions: https://github.com/icdfa/grc-engineering-labs/blob/master/phase1/grc102/week8/LAB_INSTRUCTIONS.md

The full evidence report (`report/GRC102_Lab8_Evidence_Report_Diana_Wanjiru.docx` / submitted PDF) explains every finding in detail, including two issues disclosed openly in this README and the report: a required image substitution, and a discrepancy between the automated board/dashboard reports and the verified technical state of the environment.

---

## ⚠️ Important disclosures (read before running)

1. **Image substitution.** The official lab's `docker-compose.yml` references `vulhub/struts2:s2-045`, which is not a resolvable tag on Docker Hub. This repository uses `piesecurity/apache-struts2-cve-2017-5638` instead — a prebuilt image running Apache Struts 2.3.12 on Tomcat 7, within the version range affected by the same CVE (CVE-2017-5638 / S2-045).
2. **Simulated vs. real controls.** `implement_governance_controls.py` updates the governance tracker (adding control and metric records) but does **not** modify the running containers. Verified scans taken after running `--all` and `--verify` confirm Struts remained unpatched and the database remained accessible with default credentials throughout this exercise. This is documented honestly in the evidence report as the central governance finding of the lab, rather than hidden.
3. **Dashboard/board report discrepancy.** `governance_metrics.py` generates an executive dashboard and board report showing 100% compliance and "Good" posture, while the same-day verification scan shows otherwise. The evidence report treats this gap — not any single technical vulnerability — as the most important governance lesson surfaced by the exercise.

---

## Environment

| Component | Detail |
|---|---|
| Host OS | Kali GNU/Linux Rolling 2026.1 (kernel 6.18.12, Debian-based) — substituted for the brief's reference Ubuntu host; Docker behaves identically |
| Container runtime | Docker 28.5.2, Docker Compose |
| Web service | `piesecurity/apache-struts2-cve-2017-5638` (Struts 2.3.12 / Tomcat 7), bound to `127.0.0.1:8080` only |
| Database | `mysql:5.7`, seeded with synthetic customer data |
| Monitoring | `ubuntu:20.04`, with a monitoring script mounted (not actively scheduled — see disclosures) |
| Network | Isolated Docker bridge network `secgov_network`; web service never exposed beyond localhost |

---

## Repository structure

```
.
├── README.md
├── docker-compose.yml                     # Final, corrected compose file
├── database_init/
│   └── init.sql                           # Synthetic customer_data schema + seed rows
├── monitoring/
│   ├── security_monitor.sh                # Monitoring/alerting script
│   └── security_cron                      # Intended cron schedule (not installed — see disclosures)
│
├── initialize_governance.py               # Seeds the governance tracker
├── governance_tracker.py                  # Governance tracker / dashboard CLI
├── vulnerability_scanner.py                # Struts / MySQL / segmentation checks
├── simulate_attack.py                     # CVE-2017-5638 exploitation attempt
├── analyze_governance_failures.py         # Maps scan/attack evidence to governance failures
├── implement_governance_controls.py       # Applies patch/segmentation/DB/monitoring/oversight controls
├── patch_management.py                    # Patch simulation + patch_status.json writer
├── governance_metrics.py                  # Generates dashboard, board report, charts, framework docs
│
├── governance_data.json                   # Governance tracker state (policies/controls/risks/metrics)
├── patch_status.json                      # Real recorded patch state (see disclosures)
├── vulnerability_report_20261008_140248.json   # Baseline scan (pre hostname-fix)
├── vulnerability_report_20261008_220618.json   # Baseline scan (post hostname-fix)
├── vulnerability_report_20261008_223747.json   # Post --all control run
├── vulnerability_report_20261008_224201.json   # Post --verify run (final)
├── governance_failure_report_20261008_222959.json
│
├── equifax_comparison.md                  # Governance-failure comparison with the Equifax breach
├── governance_controls_report.md          # Auto-generated controls summary (see disclosures)
├── governance_oversight.md                # Oversight roles, reporting lines, accountability
├── board_report.md                        # Auto-generated board report (see disclosures)
├── governance_metrics_framework.md        # Metrics categories, schema, lifecycle
├── dashboard_user_guide.md                # How to read the executive dashboard
├── executive_dashboard.html               # Auto-generated executive dashboard (see disclosures)
│
├── metrics_visualizations/
│   ├── patch_compliance.png
│   ├── vuln_remediation.png
│   ├── security_incidents.png
│   ├── monitoring_coverage.png
│   └── policy_compliance.png
│
├── evidence/                              # Labelled screenshots referenced in the PDF report (Fig1.1–Fig4.7e)
└── report/
    └── GRC102_Lab8_Evidence_Report_Diana_Wanjiru.pdf
```

---

## How to run

```bash
# 1. Create the isolated network
docker network create secgov_network

# 2. Start the environment
docker-compose up -d
docker ps   # confirm all three containers are Up

# 3. Initialise the governance tracker (run once; delete governance_data.json first to redo)
./initialize_governance.py

# 4. Baseline evidence
./vulnerability_scanner.py
./governance_tracker.py --dashboard

# 5. Attack simulation and failure analysis
./simulate_attack.py
./analyze_governance_failures.py

# 6. Implement and verify controls
./implement_governance_controls.py --all
./implement_governance_controls.py --verify
./vulnerability_scanner.py          # re-scan to check real post-control state

# 7. Metrics and reporting
./governance_metrics.py
```

**Note:** `vulnerability_scanner.py` and `simulate_attack.py` target `http://localhost:8080` — run them from the Kali host (not inside a container), since the web port is bound to loopback only.

---

## How to verify the findings yourself

```bash
cat patch_status.json                       # real recorded patch state
cat vulnerability_report_20261008_224201.json   # final scan — compare to board_report.md
```

If `patch_status.json` does not contain `"struts_patched": true` or `"network_segmented": true`, those controls were not actually applied to the running containers, regardless of what `governance_controls_report.md` or the dashboard state.

---

## Marking criteria cross-reference

| Brief requirement | Where to find it |
|---|---|
| Part 1 evidence | `docker-compose.yml`, `database_init/`, `evidence/Fig1_*`, baseline scan/dashboard JSON |
| Part 2 evidence | `simulate_attack.py` output, `governance_failure_report_*.json`, `equifax_comparison.md`, `evidence/Fig2_*` |
| Part 3 evidence | `implement_governance_controls.py`, `patch_status.json`, post-control scans, `evidence/Fig3_*` |
| Part 4 evidence | `governance_metrics.py` outputs, `metrics_visualizations/`, `evidence/Fig4_*` |
| Associated PDF report | `report/GRC102_Lab8_Evidence_Report_Diana_Wanjiru.pdf` |

---

## References

- NIST NVD. [CVE-2017-5638](https://nvd.nist.gov/vuln/detail/CVE-2017-5638)
- U.S. GAO (2018). *GAO-18-559: Actions Taken by Equifax and Federal Agencies in Response to the 2017 Breach.*
- U.S. House Committee on Oversight and Government Reform (2018). *The Equifax Data Breach*, Majority Staff Report.
- CIS Controls — [Network Segmentation](https://www.cisecurity.org/controls/implement-network-segmentation)
- ICDFA GRC Engineering Labs — [GRC102 Week 8 Lab Instructions](https://github.com/icdfa/grc-engineering-labs/blob/master/phase1/grc102/week8/LAB_INSTRUCTIONS.md)

---

**Repository URL:** `[INSERT REPOSITORY URL HERE]`
**Commit/branch assessed:** `[INSERT COMMIT HASH HERE]`
