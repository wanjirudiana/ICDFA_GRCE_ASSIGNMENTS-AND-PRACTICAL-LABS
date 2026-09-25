# TechGlobal Security Governance Transformation - Week 3 Practical Lab

**Consultant Report - Lead Security Governance Consultant**
Module: Security Governance - Week 3 Practical Laboratory


## Repository Contents

| File | Description |
|---|---|
| `TechGlobal_Security_Governance_Consultant_Report.docx` | The full consultant report (Word) - primary deliverable. |
| `README.md` | This file - full content of the report, formatted for GitHub. |
| `charts/fig1_governance_structure.png` | Five-tier governance operating model diagram. |
| `charts/fig2_escalation_workflow.png` | Five-stage major cyber-risk escalation workflow diagram. |

---

## Scenario

### Practical Context

TechGlobal is a rapidly growing technology organisation with approximately 2,500 employees
across five global offices. Although revenue and product adoption are increasing, its
information security governance structure has not matured at the same pace.

Security decisions are currently concentrated with the IT Director, there are no formal security
governance committees, business units make inconsistent security decisions, and executive
leadership and the Board have limited visibility into cyber risk.

The author has been appointed Lead Security Governance Consultant and tasked with transforming
TechGlobal's informal, IT-centric security model into a structured, business-aligned governance
framework. The responsibility is to establish clear roles, accountability, decision authority,
cross-functional governance, risk escalation and Board-level oversight.

### Objectives

What this report must demonstrate: analyse weaknesses created by informal and IT-centric security
governance; design a scalable governance structure connecting Board oversight, executive
leadership, security management and business units; define responsibilities and decision
authority for the Board, CEO, CISO, CRO/Risk, Legal, Finance, HR and IT; establish effective
cross-functional governance committees; apply a RACI model to critical security-governance
activities; design a major cyber-risk escalation workflow; and identify segregation-of-duties
conflicts with appropriate corrective controls.

### Instructor Briefing - Laboratory Guidance

Assume the role of Lead Security Governance Consultant for TechGlobal. The organisation has grown
rapidly, but cybersecurity decision-making remains heavily concentrated within IT, resulting in
unclear accountability, inconsistent business-unit practices and inadequate executive and Board
oversight.

During this laboratory, you will redesign TechGlobal's security governance operating model. You
will analyse governance weaknesses, create a stakeholder map and organisation structure, define
cross-functional responsibilities for the Board, CEO, CISO, CRO/Risk, Legal, Finance, HR and IT,
design the organisation's security governance committee ecosystem, and develop a detailed RACI
matrix covering at least 15 governance activities.

You will also design a major cyber-risk escalation workflow, establish escalation thresholds and
analyse at least five segregation-of-duties or accountability weaknesses in the existing
governance model. Submit one professionally structured consultant report together with the
required supporting governance artefacts.

---

## Table of Contents

1. Executive Summary
2. Current-State Analysis: Weaknesses of Informal, IT-Centric Governance
3. Target Governance Operating Model
4. Roles, Responsibilities and Decision Authority
5. Security Governance Committee Ecosystem
6. RACI Matrix - Critical Security-Governance Activities
7. Major Cyber-Risk Escalation Workflow and Thresholds
8. Segregation-of-Duties and Accountability Weaknesses
9. Implementation Roadmap
10. Conclusion
11. Appendix A - RACI Legend and Notes


---

## Executive Summary

TechGlobal has grown to approximately 2,500 employees across five global offices, but its
security governance has not kept pace with that growth. Today, security decision-making is
concentrated in a single role - the IT Director - with no formal governance committees, no
consistent policy baseline across business units, and no structured mechanism for executive or
Board visibility into cyber risk. This concentration of authority is not a personal failing of
the IT Director; it is the predictable result of a security function that scaled technically
without a matching governance structure.

This report sets out a practical transformation plan. Section 1 analyses the specific weaknesses
the current model creates. Section 2 proposes a five-tier governance operating model connecting
the Board, an Executive Security Steering Committee, three specialist committees, the CISO
function, and business-unit security liaisons in each of the five offices. Section 3 defines
decision authority and accountability for the Board, CEO, CISO, CRO/Risk, Legal, Finance, HR and
IT. Section 4 designs the committee ecosystem itself - purpose, membership, chair and decision
rights for each body. Section 5 provides a RACI matrix across sixteen governance activities.
Section 6 designs a five-stage major cyber-risk escalation workflow with numeric thresholds.
Section 7 identifies six segregation-of-duties and accountability weaknesses in the current
model, each with a proportionate corrective control. Section 8 sequences the transformation into
a 12-month roadmap so the Board can fund and govern the change itself as a managed programme
rather than a one-off reorganisation.

---

## 1. Current-State Analysis: Weaknesses of Informal, IT-Centric Governance

An IT-centric, informal governance model tends to work while an organisation is small enough for
one capable person to hold the full picture in their head. At TechGlobal's current scale - 2,500
employees, five offices, and continued growth - that model has already been outgrown. The
weaknesses below are not hypothetical; each maps to a specific governance failure mode that has
caused material incidents at comparably-sized organisations.

| Weakness | Description | Business / Governance Impact |
|---|---|---|
| Single point of accountability | The IT Director sets strategy, approves budget, designs controls, operates them, and accepts risk - with no independent party checking any of these decisions. | No segregation of duties; a blind spot, error or conflict of interest anywhere in this chain has no independent check before it becomes an incident. |
| No formal governance committees | Security decisions are made ad hoc, in one-to-one conversations or informal emails, with no minuted record. | No audit trail for the Board, regulators or auditors; decisions cannot be shown to have followed a consistent, defensible process. |
| Inconsistent business-unit practice across five offices | Each office applies its own interpretation of security requirements, with no shared baseline. | Uneven risk exposure across the group; multiplies the number of ways a control gap can be introduced, and complicates compliance across the jurisdictions the five offices sit in. |
| Limited executive and Board visibility | There is no standing reporting cadence bringing cyber risk to executive leadership or the Board. | The Board cannot discharge its oversight duty, cannot demonstrate governance to regulators or insurers, and has no early warning of building risk before it becomes a material incident. |
| No independent risk (CRO) function | Risk-acceptance decisions are made as technical judgement calls by IT, not weighed against a Board-approved enterprise risk appetite. | Risk acceptance is inconsistent and undocumented; the organisation cannot state its aggregate cyber-risk exposure at any point in time. |
| Legal/Privacy not embedded in security decisions | Legal is not a standing part of the security decision process. | Regulatory and breach-notification risk is unmanaged, which is a material exposure given the five offices likely sit under multiple data-protection regimes. |
| No vendor/third-party risk governance | As a fast-growing technology company, TechGlobal likely has significant, uncontrolled cloud and SaaS vendor sprawl. | Third-party risk (consistently one of the costliest incident categories in practice) is effectively ungoverned. |
| No risk-based budget governance | Security spend is prioritised by IT's own judgement rather than against a jointly-owned risk register. | Finance and the business have no visibility into whether security investment matches actual risk, weakening the case for future budget asks. |
| Model does not scale with growth | TechGlobal's headcount and office count are still growing; an informal, one-person model has a hard ceiling. | Without structural change, the probability of a governance failure increases faster than the organisation's ability to detect and correct it. |

---

## 2. Target Governance Operating Model

The target model replaces a single point of authority with five connected tiers, each with a
distinct role: the Board sets appetite and provides oversight; an Executive Security Steering
Committee translates that appetite into strategy, budget and policy; three specialist committees
handle architecture, incident response and regional alignment; the CISO function owns day-to-day
policy and operations; and each of the five offices has a named business-unit security liaison
feeding local context upward and receiving standards downward. This is deliberately a flat,
five-tier structure rather than a deep hierarchy - appropriate for a 2,500-person organisation,
where an over-engineered model would simply be ignored in practice.

![Figure 1. TechGlobal target security governance operating model](charts/fig1_governance_structure.png)

*Figure 1. TechGlobal target security governance operating model - Board to business-unit liaisons.*

Three design principles run through this structure. First, no single role both sets policy and
approves its own compliance with that policy - the recurring weakness identified in Section 1.
Second, every business unit (each of the five offices) has a named channel into governance,
rather than being left to interpret policy independently. Third, the model is scalable: a sixth
office, or a doubling of headcount, adds another liaison seat into the same structure rather than
requiring redesign.

---

## 3. Roles, Responsibilities and Decision Authority

Each role below is defined by what it can decide unilaterally, what it is ultimately accountable
for, who it must consult before acting, and its reporting line - the same structure that prevents
the single-point-of-failure weakness identified in Section 1 from re-emerging in the new model.

| Role | Decision Authority | Accountability | Consultation Duty | Reporting / Relationship |
|---|---|---|---|---|
| **Board (Risk & Audit Committee)** | Approves enterprise risk appetite and security strategy; accepts residual risk above the CEO's delegated authority. | Ultimate fiduciary accountability for TechGlobal's cyber-risk posture to shareholders and stakeholders. | Consults CEO, CISO and (once appointed) CRO before ratifying material decisions; commissions independent assurance as needed. | Receives quarterly reporting from the Executive Security Steering Committee, plus ad hoc briefing for material incidents. |
| **Chief Executive Officer (CEO)** | Approves security strategy and budget within Board-set appetite; chairs the Executive Security Steering Committee. | Accountable to the Board for TechGlobal's overall risk posture and for the effectiveness of the governance transformation itself. | Consults CISO, Legal, Finance and business-unit leads on material risk, spend and disclosure decisions. | Reports to the Board; CISO, CRO, Legal, Finance and HR report up through or to the CEO. |
| **Chief Information Security Officer (CISO)** | Approves security policy, control standards, architecture decisions and incident-response execution. | Accountable for the security programme's design and operating effectiveness, and for timely escalation per Section 6. | Consults IT on feasibility, Legal on regulatory exposure, business-unit liaisons on local operating constraints. | Reports administratively to the CEO (not to IT), with a standing functional line to the Board Risk & Audit Committee, preserving independence from IT operations. |
| **Chief Risk Officer (CRO) / Risk function** | Approves enterprise risk-acceptance decisions within a defined threshold (Section 6); owns the risk register. | Accountable for aggregating cyber risk with other enterprise risks and maintaining consistent risk-acceptance discipline. | Consults CISO for technical risk detail, Legal for regulatory interpretation, Finance for financial-impact modelling. | Reports to the Board/CEO; independent of IT and the CISO's operational chain - TechGlobal should appoint or designate this function as a first step of the transformation. |
| **Legal / Privacy / Compliance** | Approves regulatory breach-notification content and timing across all five jurisdictions; approves external counsel engagement. | Accountable for regulatory compliance, contractual exposure and accuracy of external disclosures. | Consults CISO on facts and timeline, CRO on risk classification, Communications on public messaging. | Reports to CEO/General Counsel; advises the Board directly on material legal exposure. |
| **Finance** | Approves incident-related and control-investment spend within delegated authority; owns cyber-insurance placement. | Accountable for financial-impact quantification, budget integrity and insurance recovery. | Consults CISO on cost estimates, Legal on insurance/contract terms, CRO on risk-financing strategy. | Reports to CEO/CFO; briefs the Board on the financial dimension of cyber risk and incidents. |
| **Human Resources** | Approves disciplinary action for security-policy violations; owns the group-wide security-awareness programme across all five offices. | Accountable for personnel-related risk (insider-threat indicators, joiner-mover-leaver access hygiene) and fair process. | Consults CISO/Legal before disciplinary action tied to a security incident; consults IT on access-timing at each office. | Reports to CEO/Head of HR; coordinates with CISO on awareness metrics and with IT on the access lifecycle. |
| **Information Technology (IT Director / IT function)** | Approves technical implementation of approved controls; executes access provisioning and system changes across all offices. | Accountable for control implementation, system availability and technical remediation timelines - no longer for policy approval or risk acceptance. | Consults CISO before deploying changes with security impact; consults CRO/Finance on infrastructure investment trade-offs. | Reports to CIO/COO; is now a control operator within the new model, not the final approver of security policy or risk acceptance (see Section 7). |

---

## 4. Security Governance Committee Ecosystem

Five bodies replace today's single informal decision point. Each has a distinct purpose, a named
chair, defined membership, a meeting cadence, and explicit decision rights - so that, unlike the
current model, every security decision of consequence is made by a defined group against a
defined mandate, not by one person's judgement on a given day.

| Committee | Purpose | Chair / Core Membership | Frequency | Decision Authority |
|---|---|---|---|---|
| **Board Risk & Audit Committee** | Ultimate oversight of enterprise and cyber risk appetite; independent assurance. | Independent Director (Chair); CEO and CISO attend by invitation. | Quarterly, plus ad hoc for material incidents. | Approves risk appetite; final risk-acceptance authority above the CEO's delegated limit; commissions independent audit. |
| **Executive Security Steering Committee** | Cross-functional forum translating Board risk appetite into strategy, policy and budget. | CEO (Chair); CRO, CISO, Legal, Finance, HR, and a rotating business-unit lead. | Monthly. | Approves security strategy, policy (on CISO's recommendation), and budget prioritisation; owns Executive-level incident escalation. |
| **Security Governance & Architecture Review Board** | Technical governance: architecture, technology adoption, and control-standard decisions. | CISO (Chair); IT leadership, Enterprise Architecture, DevOps, Privacy. | Bi-weekly. | Approves security architecture, control standards, and any new technology adoption with security impact. |
| **Cyber Incident Response Steering Committee** | Coordinates major incident response across functions, avoiding an IT-only response to a cross-functional problem. | CISO / named Incident Commander; Legal, Communications, HR, Finance, IT, and the affected office's liaison. | Activated on demand for Severity >= Medium incidents (Section 6). | Approves incident response strategy, interim emergency spend, and the public communication position. |
| **Regional Security Liaison Forum** | Aligns practice across the five offices; surfaces local regulatory context and business-unit exceptions. | Head of GRC (Chair); one named security liaison per office, plus regional HR/Legal representation. | Monthly. | Raises business-unit exceptions and local risks for approval upward; has no independent approval authority of its own, preventing a repeat of today's inconsistent business-unit decisions. |

---

## 5. RACI Matrix - Critical Security-Governance Activities

The matrix below covers **sixteen** governance activities, exceeding the minimum of fifteen
required. Each activity has exactly one Accountable party, consistent with the principle that
ownership of an outcome should not be shared even where the underlying work is.

**R** = Responsible - **A** = Accountable - **C** = Consulted - **I** = Informed

| Governance Activity | Board | CEO | CISO | CRO/Risk | Legal | Finance | HR | IT |
|---|---|---|---|---|---|---|---|---|
| 1. Security strategy & governance framework approval | A | R | R | C | C | C | I | C |
| 2. Enterprise cyber-risk appetite & acceptance | A | R | C | R | C | C | I | I |
| 3. Information security policy approval | I | A | R | C | C | I | C | C |
| 4. Security architecture / major technology adoption | I | I | A | C | C | C | I | R |
| 5. Cloud & vendor onboarding security review | I | I | A | C | C | C | I | R |
| 6. Privileged access approval | I | I | A | I | I | I | I | R |
| 7. Regional business-unit security exception approval | I | I | A | C | C | I | I | C |
| 8. Major incident response governance | I | A | R | C | C | I | I | R |
| 9. Regulatory / breach notification decision | I | I | C | C | A | I | I | C |
| 10. Third-party / vendor cyber-risk acceptance | I | I | C | A | C | C | I | C |
| 11. Cybersecurity budget prioritisation | C | A | R | C | I | R | I | C |
| 12. Security awareness & disciplinary action | I | I | C | I | C | I | A | I |
| 13. Data classification standard approval | I | I | A | C | C | I | I | R |
| 14. Cyber-insurance placement & renewal | C | A | C | C | C | R | I | I |
| 15. New-office / market-entry security due diligence | I | A | R | R | C | C | I | C |
| 16. Board cyber-risk reporting | C | A | R | R | I | I | I | I |

---

## 6. Major Cyber-Risk Escalation Workflow and Thresholds

Today, an incident's escalation depends entirely on the IT Director's individual judgement about
who else needs to know, and when. The workflow below removes that dependency by defining, in
advance, the numeric and categorical triggers that move an incident from operational detection
through to Board escalation - so the same category of incident is handled consistently regardless
of which office it originates in or who first detects it.

![Figure 2. TechGlobal major cyber-risk escalation workflow](charts/fig2_escalation_workflow.png)

*Figure 2. TechGlobal major cyber-risk escalation workflow, Detection through Board escalation.*

| Stage | Trigger Criteria / Threshold | Responsible Role | Required Evidence | Timing Target |
|---|---|---|---|---|
| **1. Detection** | Any alert matching a defined detection rule, from any of the five offices or the SOC. | SOC / Business-Unit Security Liaison | Alert log, initial indicators, affected asset/office. | Triage within 1 hour of detection. |
| **2. Triage** | Confirmed incident (not a false positive); severity classified Low-Critical using a pre-agreed matrix. | Security Management (CISO's team) | Triage summary, scope estimate, affected systems/data. | Classification complete within 1 hour of detection. |
| **3. Management review** | Severity = Medium, OR incident spans more than one office, OR any regulated-data exposure suspected. | CISO / relevant Department Head | Containment status, impact estimate, office(s) affected. | CISO/Department Head notified within 4 hours of triage. |
| **4. Executive escalation** | Severity = High, OR estimated financial impact exceeds $250,000, OR more than 1,000 records/individuals affected, OR incident spans more than one office. | Executive Security Steering Committee (CEO, CRO, Legal, CISO) | Impact assessment, cost estimate, regulatory-exposure category, remediation plan. | Executive brief within 24 hours of confirmation. |
| **5. Board escalation** | Severity = Critical, OR material regulatory notification required in any jurisdiction, OR cost/reputational impact exceeds the Board-set risk appetite, OR resolution has not progressed within 72 hours. | CEO and CISO, with CRO and Legal | Full incident report, root cause (where known), regulatory notification status per jurisdiction, financial exposure. | Board notified within 72 hours of confirmation, aligned to common regulatory notification clocks. |

Final risk-acceptance authority above the CEO's delegated limit rests with the Board Risk & Audit
Committee. All stage-to-stage timings are aligned to the Board-approved escalation SLA.

---

## 7. Segregation-of-Duties and Accountability Weaknesses

The current model concentrates conflicting duties in a small number of hands - most often the IT
Director. The six weaknesses below (exceeding the minimum of five) are drawn directly from the
current-state description, each with a control that is proportionate to a 2,500-person
organisation rather than an enterprise-scale bureaucracy.

### Weakness 1 - The IT Director both administers and approves privileged access

**Risk:** The same individual who can create administrator accounts can also approve their own
access requests, so undetected privilege escalation, fraud or a cover-up of an earlier error is
possible with no independent check.

**Corrective control:** Route all privileged-access requests through the CISO function
(Architecture Review Board) for independent approval; keep IT as implementer only, and run a
quarterly access recertification performed by someone outside the IT chain (e.g., the Regional
Security Liaison Forum's GRC chair).

### Weakness 2 - The IT Director is the sole approver of risk-acceptance decisions

**Risk:** Without a CRO or a defined risk-acceptance threshold, every risk decision is a
unilateral technical judgement call rather than a decision weighed against a Board-approved risk
appetite.

**Corrective control:** Appoint or designate a CRO/Risk function (Section 3) and adopt the
risk-acceptance thresholds in Section 6: acceptance above a defined financial or severity
threshold requires Executive Security Steering Committee or Board sign-off, never the IT Director
alone.

### Weakness 3 - The same person authors and approves security policy

**Risk:** Policy that is both written and approved by one person has no independent quality
check and can be shaped to justify existing practice rather than to set an appropriate standard.

**Corrective control:** Require all security policy to be drafted by the CISO but formally
ratified by the Executive Security Steering Committee (RACI Activity 3), with Legal and HR
consulted before ratification.

### Weakness 4 - Business units in each office independently procure cloud/SaaS tools ("shadow IT")

**Risk:** Without a central security gate, each of the five offices can introduce new vendors and
data flows that the CISO function never reviews, creating unmanaged data-protection and
vendor-risk exposure.

**Corrective control:** Add a mandatory security review step to the procurement workflow, gated
by Finance's purchase-order approval, with output routed to the Security Governance & Architecture
Review Board (RACI Activity 5) before any new cloud/SaaS tool goes live.

### Weakness 5 - Regional IT staff develop, test and deploy their own changes without independent review

**Risk:** In each office, the same staff who write a change can also test and deploy it to
production, so a misconfiguration - accidental or deliberate - can reach production with no
second set of eyes.

**Corrective control:** Enforce mandatory independent peer review and Change Advisory Board
sign-off (via the Architecture Review Board) for any change with security impact, in every office,
with requester, reviewer and deployer recorded as distinct identities.

### Weakness 6 - No independent internal audit or assurance function tests the IT Director's own controls

**Risk:** Without independent assurance, the organisation is relying on the control operator to
self-report on the effectiveness of their own controls - precisely the conflict of interest the
new governance model is designed to remove.

**Corrective control:** Commission an annual independent control assessment (internal audit
function or outsourced assurance provider) reporting directly to the Board Risk & Audit Committee,
entirely outside the IT/CISO reporting chain.

---

## 8. Implementation Roadmap

Governance transformation is itself a risk if it is attempted all at once - committees created
without members who understand their mandate simply become another informal process. The roadmap
below sequences the model in Sections 2-7 over twelve months, so the Board can govern the
transformation as a funded, tracked programme.

| Phase | Timeframe | Key Actions | Success Milestone |
|---|---|---|---|
| **Phase 1 - Foundation** | Months 0-3 | Appoint/designate CRO function; charter and hold first Executive Security Steering Committee; ratify escalation thresholds (Section 6); begin privileged-access remediation (Weakness 1). | Executive Security Steering Committee meeting minuted monthly; privileged-access approval moved out of IT. |
| **Phase 2 - Structural build-out** | Months 3-6 | Stand up Architecture Review Board and Regional Security Liaison Forum with named liaisons in all five offices; ratify security policy through the Committee (Weakness 3); gate cloud/SaaS procurement (Weakness 4). | All five offices have a named, active security liaison; policy ratification record exists for all current policies. |
| **Phase 3 - Assurance & Board integration** | Months 6-12 | Stand up Cyber Incident Response Steering Committee and run a first cross-functional tabletop exercise; commission first independent control assessment (Weakness 6); deliver first quarterly Board cyber-risk report. | Board receives its first structured quarterly cyber-risk report; independent assurance report delivered to the Audit Committee. |

---

## 9. Conclusion

TechGlobal's security risk has not been created by any individual's failure - it is the
structural result of governance that did not grow alongside the business. The model in this
report does not remove the IT function's central operational role; it surrounds that role with
the accountability, cross-functional input and Board visibility a 2,500-person, five-office
organisation now requires. Implemented in the sequence set out in Section 8, it gives the Board a
defensible, auditable governance structure within twelve months, without requiring TechGlobal to
over-build governance beyond what its current scale warrants.

---

## Appendix A - RACI Legend and Notes

- **R (Responsible):** performs the work required to complete the activity.
- **A (Accountable):** owns the outcome and is answerable for it; exactly one A per activity in
  this report.
- **C (Consulted):** provides input before the decision or action is finalised (two-way
  communication).
- **I (Informed):** notified after the decision or action, for awareness (one-way communication).

## License
 
Coursework artefact prepared for educational purposes as part of a security governance module.
No proprietary or real-organisation data is included.
 
