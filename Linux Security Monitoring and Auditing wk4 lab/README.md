# Linux Security Monitoring and Auditing Lab

**From technical evidence to governance assurance**

Course: GRC102 - Information Security Governance (Week 4 Practical Laboratory)
Institution: International Cybersecurity and Digital Forensics Academy
Author: [Your Name]
Date: 05 October 2026

---

## Scenario

An organisation relies on Linux systems for business-critical services. Management has approved security controls for authentication monitoring, privileged access, system auditing, and vulnerability and configuration assessment. However, internal assurance reviews show that the evidence for these controls is collected inconsistently.

I acted as a **Security Control Assurance Analyst**. The task was to inspect an assigned Linux system, generate and analyse security evidence, identify issues that need governance attention, and produce a control-monitoring record and audit report for management.

The goal was not just to run commands. Each piece of evidence had to be explained, linked to a control objective and an owner, and turned into a remediation and retest action.

## Environment

| Item | Detail |
|---|---|
| System | Kali Linux VM (isolated training environment) |
| Hostname | dee |
| Kernel | 6.18.12+kali-amd64 |
| auditd | 4.1.2 |
| Lynis | 3.1.6 (up-to-date) |
| Time zone | EAT (UTC+3); the lab brief uses WAT, which is EAT minus one hour |

All activity was done only inside the assigned VM. No external systems were targeted, no changes were saved to `/etc/passwd` or `/etc/shadow`, and no logging was disabled.

## What the lab covered

1. **auditd:** verify the service, create custom audit rules, generate benign events, and query them with `ausearch` and `aureport`.
2. **Log analysis:** review the journal with `journalctl` for authentication, privilege use, errors and warnings.
3. **Lynis assessment:** run a system audit and interpret the hardening index and component results.
4. **SIEM and automation (conceptual):** map host evidence to enterprise monitoring and decide what is an operational alert and what is a governance issue.
5. **Governance task:** build a control-monitoring table with owners, thresholds, remediation and retest plans.

## Key results

| Area | Result |
|---|---|
| auditd | Active and enabled; 5 rules loaded successfully |
| Audit events | 16,728 events in the window; 0 account changes; 0 logins recorded |
| Privileged use | sudo activity attributable to one user (cybergirlie to root) |
| Failed passwords | None found in the journal |
| Lynis hardening index | 63 out of 100 (273 tests) |
| Lynis components | Firewall found; intrusion software and malware scanner not found |

## Findings

| ID | Finding | Priority |
|---|---|---|
| F01 | Disk reports 3 pending sectors on the host that stores the audit and log evidence | High |
| F02 | auditd is not forwarding events off-host ("No plugins found, not dispatching events") | Moderate |
| F03 | No `/var/log/auth.log`; the auth.log audit rule watches a file that does not exist | Moderate |
| F04 | No intrusion detection or prevention software (Lynis) | Moderate |
| F05 | No malware scanner (Lynis) | Moderate |
| F06 | Hardening index of 63 out of 100 | Moderate |
| F07 | Repeated local authentication failures (login screen and screensaver) | Low |

**Highest priority:** F01. The assurance process depends on the audit and journal evidence stored on that disk, and there is no second copy off-host.

## Evidence

### auditd service and rules

![auditd status](screenshots/01_auditd_status.png)

![Loaded audit rules](screenshots/02_audit_rules.png)

### Audit events

The `passwd_changes` key recorded two read-only accesses to `/etc/passwd` by `sudo` for user `cybergirlie` (auid 1000) at 20:14:31 EAT.

![ausearch passwd_changes](screenshots/03_ausearch_passwd.png)

![ausearch program_execution](screenshots/04_ausearch_execve.png)

The `auth_failures` key returned only the rule-load record, because the watched file does not exist.

![ausearch auth_failures](screenshots/05_ausearch_auth.png)

### Audit summary reports

![aureport summary](screenshots/06_aureport_summary.png)

![aureport failed](screenshots/07_aureport_failed.png)

![aureport login](screenshots/08_aureport_login.png)

### Log analysis

![journalctl follow](screenshots/09_journalctl_follow.png)

![sudo events in the journal](screenshots/10_sudo_events.png)

![Authentication search](screenshots/11_auth_search.png)

![Current boot journal](screenshots/12_journal_boot.png)

![Journal errors](screenshots/13_journal_errors.png)

![Journal warnings](screenshots/14_journal_warnings.png)

### Lynis assessment

![Lynis version](screenshots/15_lynis_version.png)

![Lynis summary](screenshots/16_lynis_summary.png)

## Governance mapping

Each finding was mapped to a control, an owner and a retest.

| Control | Status | Owner |
|---|---|---|
| System auditing (auditd) | Operating | Linux sysadmin / Security Operations |
| Off-host audit forwarding | Gap | Security Operations |
| Authentication monitoring | Partially effective | Linux sysadmin / Security Operations |
| Privileged-access monitoring | Operating | Linux sysadmin / IAM lead |
| Account-file integrity | Operating | System owner |
| Log retention and time integrity | Operating, verification pending | Linux sysadmin |
| Hardening baseline | Needs improvement | Infrastructure |
| Host protection (IDS and malware scanning) | Gap | Security Operations |
| Evidence storage reliability | Needs action | Infrastructure |

## SIEM and continuous monitoring (concept)

```
Linux host (auditd, journald, Lynis, smartd)
  -> agent or forwarder (audit dispatcher, rsyslog, Filebeat or Wazuh-type agent)
  -> SIEM (normalise, correlate, alert)
  -> SOC alerts (operational) and dashboards/reports (governance)
  -> ticketing and workflow tracking through retest
```

- **Operational alerts:** repeated failed logins on one account, a write to `/etc/shadow`, a single disk warning.
- **Governance issues:** audit forwarding failing for a long period, persistent logging gaps, hardening index below target for repeated cycles, missing protective tooling.

## Escalation thresholds (proposed)

These are my suggested thresholds for management approval, not existing policy.

- **CISO:** any unauthorised write to `/etc/passwd` or `/etc/shadow`; auditd stopped or rules cleared; audit forwarding down for more than 24 hours; rising disk pending sectors.
- **Risk function:** hardening index below target for two cycles; Moderate findings open for more than 30 days.
- **Management committee:** a control that fails retest twice, or evidence of compromise or evidence loss.

## Limitations

- The specific Lynis warnings and suggestions (with test IDs) were not captured, so Lynis findings are based on the summary screen only.
- The optional Lynis hardening and retest was not performed.
- The 1 audit anomaly event and the 192 to 227 failed syscalls were not investigated further.

## Repository structure

```
.
|-- README.md
|-- docs/
|   `-- GRC102_W4_Lab_Report.docx   (full audit report)
`-- screenshots/                    (evidence images used above)
```

## Skills demonstrated

Linux auditing (auditd, ausearch, aureport), log analysis (journalctl, PAM, sudo), security assessment (Lynis), control monitoring, risk prioritisation, and SIEM concepts.

## AI-assistance declaration

The lab activities, commands and screenshots are my own work on the assigned VM. An AI assistant was used for explanation, report structuring and language drafting, and I reviewed the technical claims against the captured evidence.
