# CX SharePoint Refresh — effort by deliverable and ways of working

**Prepared:** 23 November 2026  
**Status:** Pre-populated retrospective working review; team estimates and evidence validation outstanding.  
**Purpose:** Understand where delivery effort went, what was produced, what working practices helped, and where rework or coordination costs arose. **This is not individual productivity scoring or a timesheet reconstruction.**

## How to use this review

1. Start from the recorded output/evidence inventory below.
2. In a short cross-functional estimation session, assign **team person-days** to each deliverable across four mutually exclusive categories: **direct research/design/build**, **coordination/review**, **QA/testing**, and **rework**. A person-day means one person's day of effort, not a calendar day. Allocate rework only to the rework category, excluding it from the other three categories; distinguish avoidable rework from purposeful iteration.
3. Use 0.5-day increments and a confidence tag (high/medium/low); include approximate involvement and work outside meetings. If evidence is insufficient, mark **unknown**, not zero.
4. Attribute shared meetings to the deliverables they actually supported; do not duplicate the same meeting across every stream. Treat project-wide ceremonies separately under coordination.
5. Discuss 2–3 efficiency hypotheses with the team using observed examples; don't present them as proven savings without measured time.
6. Compare output **quality and maintainability** alongside effort; avoid simplistic hours-per-page comparisons across different complexity.

## Pre-populated delivery and practice matrix

| ID | Deliverable / outcome | Repo-backed evidence of what we produced | How we worked (observed/documented) | Effort to estimate | Confidence / verification gap |
|---|---|---|---|---|---|
| E01 | Discovery and problem framing | 12 CX employee interviews; current-state assessment of purple/green/black content; internal benchmark; five employee insights; scoping playback | Interviews, synthesis, current-state audit, Digital alignment and leadership playback | Interview preparation/conduct/synthesis; audit; meeting/review | Evidence strong for interview count; full content inventory and broader employee validation not proven |
| E02 | Experience strategy and information architecture | Employee-need journey; CoMWeb as pathway not repository; one-authoritative-source / link-not-duplicate; L1 + six L2 page approach; working content-home decisions and design artefacts | Collaborative workshops, Miro/Figma, iterations on language/content, feasibility and stakeholder feedback | Design synthesis, wireframes, page/IA reviews and iterations | Seven final page exports confirm structure; approvals and prototype hours need validating |
| E03 | Published CX employee pages | Seven final exported pages; user-reported release 18 Nov 10:30 AEDT; 52 configured editorial cards and internal cross-navigation in page-export audit | Content writing/editing, SharePoint page build, link configuration, cross-team review, publishing checkpoint with authorised publisher | Per-page content and page configuration; links, review, QA and release | Static export available; employee-access functional PVT pending |
| E04 | CX resource library and document access | Reported batch of 26 files; document-set metadata work; CX Segments/Modes and customer-insight collection decisions | File preparation, resource classification, metadata, grouping, folder-vs-view feasibility, direct-PDF links, end-of-sprint design reversal | File preparation + metadata + file grouping/moving + repair/re-test; identify time spent revisiting architecture | Original-file manifest and completed 26/26 test not independently established |
| E05 | CoMpanion knowledge-navigation capability | Draft CX guide, intent-to-page mapping, precedence for official public site, verified-at-the-time phone/customer-service details, staff/mailroom source separation, natural-language retrieval test approach and five-question team script | Knowledge mapping, prompt/answer review, source-citation testing, versioned guide refinement | Guide drafting, iterative testing, source conflict resolution, administrator coordination | Guide deployment and production PVT outstanding; separate employee guide from project-agent guidance |
| E06 | Publishing governance and maintenance model | Working CX publishing SOP, site-page fields, ownership/approval flow, metadata/retirement principles, deferred naming-standard recommendation | Process mapping against current CoMWeb workflows; publisher/owner consultation; decisions grounded in live publishing issues | SOP creation, governance consultations, revisions, handover | Draft is not approved branch policy; ownership and cadence require sign-off |
| E07 | Release quality and measurement | Deployment handover, 7-page export audit, 26-item library PVT plan, website UAT/PVT scenarios, analytics T0 from eight screenshots, employee feedback survey and seven de-identified backlog items from six responses | Checklists, testing, QA, analytics capture, survey design, triage and prioritisation | Pre-release QA + PVT + monitoring + feedback analysis; distinguish planned from completed | Site analytics T0 includes pre-launch activity; functional PVT/clean T1 unverified |
| E08 | Delivery coordination and decisions | Project phase plan, Confluence/Jira operating model, meeting evidence, scoping playback, decision log, 17 Nov cutover decisions, four-week closure plan | Sprint/milestone communication; Teams/workshops; Miro/Figma as daily delivery; Jira evidence-led outcome reporting; Confluence as rationale source | Planning, playback, alignment, approvals, re-plan, cross-tool reconciliation, retrospection | Jira/Confluence live activity and actual team time not verified in GitHub |

**Important:** Delivered outputs and work methods are distinct from hours spent. No number in the table is a claim of person-days or cost.

## Proposed effort capture (blank for team validation)

Fill in estimates only after team discussion. **Total = direct + coordination + QA + rework; the four categories are mutually exclusive; exclude rework from direct, coordination and QA.** Shared effort must be allocated once.

| Deliverable | Direct research/design/build (days) | Coordination/reviews (days) | QA/testing (days) | Rework (days) | Total (days) | Confidence |
|---|---:|---:|---:|---:|---:|---|
| E01 Discovery | — | — | — | — | — | — |
| E02 Experience design | — | — | — | — | — | — |
| E03 Seven pages | — | — | — | — | — | — |
| E04 Resource library | — | — | — | — | — | — |
| E05 CoMpanion | — | — | — | — | — | — |
| E06 Governance | — | — | — | — | — | — |
| E07 Quality/measurement | — | — | — | — | — | — |
| E08 Coordination | — | — | — | — | — | — |

If a meeting contributes substantively to one deliverable, allocate its time there; keep E08 for genuinely project-wide coordination so it does not become a double-count bucket. When estimating one total team meeting, multiply duration by participant count only if all attendance/engagement is relevant and verified.

## How we worked — retrospective comparison

| Working practice | Repository evidence | Possible efficiency mechanism (hypothesis) | Possible counter-cost to test |
|---|---|---|---|
| Lightweight Jira, active collaboration elsewhere | 12 Oct operating adjustment in `docs/ways_of_working.md`: workshops, Miro, Figma and Teams for work; Jira as evidence-led milestones | Reduced duplicative administrative updates | End-of-sprint status reconciliation; unclear ownership or missed blockers |
| Employee-need-first, link-don't-duplicate | Discovery and experience design records; seven-page content model | Fewer new duplicated sources; simpler ongoing updates | Source-selection, link/permission checks and dependencies |
| Minimum viable page release | Seven refreshed pages rather than unbounded migration | Focused scope and early publication | Deferred links and content requests in post-launch backlog |
| Folder-based document grouping at cutover | D-019/020 and 17 Nov links-meeting note: flat/filter-view not proven, restore original names | Reduced launch implementation risk; supported direct resource links | Rework from moves, renaming reversals and retesting |
| CoMpanion as another entry path | CoMpanion guidance and two initial live document retrieval observations | May make resources easier to find via natural language | Knowledge guide maintenance, source conflicts, slow responses, PVT effort |
| Governance designed during delivery | Working SOP and publishing process discussions | Practical handover aligned to actual publishing work | Repeated consultation and unresolved ownership approvals |
| Employee feedback after go-live | Six Forms responses and seven proposed issues in 23 Nov triage | Targeted follow-up rather than speculation | Corrective effort and unplanned support load |

**Do not claim efficiency savings or a reduction in elapsed delivery time from these hypotheses alone.** The retrospective should distinguish avoidable rework from purposeful iteration and risk-reduction.

## Proposed executive visual

A single horizontal stacked bar chart with the eight deliverables on the y-axis and person-days on the x-axis, segmented into **direct work**, **coordination/reviews**, **QA/testing** and **rework**. Display next to an output register and three findings:
- **Reuse / efficiency:** What working practice demonstrably avoided duplicated effort?
- **Friction:** Which approvals, changes or system limitations consumed avoidable effort?
- **Forward recommendation:** Which change will be trialled in the next CX project?

Only render the chart when time estimates have been validated; blank or unknown values are not zero.

## Short team calibration exercise (25 minutes)

- **5 min:** Confirm eight deliverables and what actually shipped; merge categories only where effort cannot be distinguished.
- **10 min:** Individually estimate person-days by output and activity; reconcile gaps, not every decimal.
- **5 min:** Name high-confidence evidence and uncertainty; isolate largest rework/coordination events.
- **5 min:** Select three lessons and a proposed change to working practice for the executive summary.

## Supporting repository sources

- `docs/project_overview.md`, `docs/discovery_and_content_audit.md`, `docs/scoping_playback.md` — discovery, 12 interviews, proposed direction.
- `docs/experience_and_content_design.md`, `docs/scope_and_delivery_plan.md` — employee-need design and deliverable architecture.
- `docs/ways_of_working.md` — 12 October Jira/Confluence/Miro/Figma/Teams adjustment.
- `docs/content_governance_and_publishing_sop.md`, `docs/decision_log.md` — governance and cutover changes.
- `evidence/2026-11-17-sharepoint-refresh-links-meeting.md`, `docs/deployment/document_metadata_validation.md` — folder, filenames and library test caveats.
- `docs/deployment/2026-11-18-go-live-page-export-pvt.md` — seven-page export, T0 analytics, verification gaps.
- `docs/deployment/2026-11-23-feedback-triage-backlog.md`, `docs/deployment/project_closure_plan_2026-11-19.md` — feedback/closure.

**Authority caveat:** GitHub is an interim staging reference; actual effort, Jira issue timing, approvals and publication history must be validated against organisational sources. This note is not a Bitbucket or Confluence update.

**Closure use (24 November):** Calibrate during W2 (26 Nov–2 Dec proposed), consolidate validated totals and lessons in the W3 executive summary, and retain unknowns rather than assuming zero. See [closure plan](project_closure_plan_2026-11-19.md).
