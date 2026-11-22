# CX SharePoint Refresh — employee feedback triage and improvement backlog

**Prepared:** 23 November 2026  
**Source:** Microsoft Forms export supplied by project team, `Help us improve our CX pages.xlsx` (six responses; identifiers 1–6).  
**Authority:** Microsoft Forms / approved restricted organisational storage holds raw submissions; Jira holds assigned work and authoritative workflow states. This public GitHub staging document contains only de-identified, minimised issue summaries and **proposed** actions. No raw names, addresses, attachments, free text or internal system URLs are reproduced here.  
**Current state:** Triage proposal only. Issues have not been reproduced, Jira tickets created/transited, or owners assigned.

## Summary

- **6 survey responses** received in the export, giving **7 actionable backlog items** because response 3 raises both findability/content and a distinct potentially over-broad permissions concern.
- Themes: 3 feedback submissions concerning missing information/resources, 2 suggestions for improvement, 1 outdated/incorrect information. These are **form response categories**, not counts of actions (which are seven).
- Proposed P1 checks: outdated executive correspondence destination, CXVoices access permissions, and outdated Qualtrics "Coming soon" label. The P1 priority indicates prompt triage rather than confirmed incident severity.
- Proposed P2 improvements: direct CXVoices pathway, Customer Commitments discoverability, Knowledge Articles in service-improvement journey, and HCD thinking/mindsets Learning Hub entry.
- **Overlap:** CXVoices and Qualtrics requests may have shared content ownership but are distinct acceptance tests. Avoid two competing maintained CXVoices pages without validating the authoritative source.

## Feedback-backed backlog

| ID | Source form response | Affected experience | Feedback and proposed change | Proposed priority | Status | Verification and acceptance criteria | Owner / dependency |
|---|---|---|---|---|---|---|---|
| CXFB-01 | 2 | Get help delivering customer service → Executive Correspondence | Current destination reportedly contains outdated guidance. Confirm the current Managed Case / Executive Correspondence source; replace or redirect tile if approved. | P1 | Needs reproduction | Existing tile destination checked; approved current source linked; ordinary-employee permissions and link tested; no duplicate guidance created | CX content editor + executive correspondence owner |
| CXFB-02 | 3 | CXVoices knowledge/source access | Survey respondent reports existing CXVoices content is organisation-editable. Verify effective permissions and change only with content-owner approval. | P1 | Security/configuration check pending | Actual site/page/library ACLs inspected by authorised admin; intended readers/editors agreed; least-privilege configuration applied if needed; access re-tested and change logged | CXVoices owner + SharePoint admin |
| CXFB-03 | 5 | Get training and grow your skills → Qualtrics | Tile reportedly still displays "Coming soon" although Qualtrics is live. Update tile copy and link to approved application/training route. | P1 | Needs reproduction | No obsolete status label; authorised Qualtrics and Learning Hub links function; access and wording validated by service owner | CX content owner + CXVoices/Qualtrics owner |
| CXFB-04 | 3 | Act on customer data and feedback → CXVoices | Add discoverable entry to CXVoices introduction, training and approved Qualtrics access. First determine whether an authoritative current page exists or a new page is genuinely required. | P2 | Design/source decision pending | Employee can find CXVoices from relevant data/feedback CX journey; clear purpose, training and approved system link; owner and review date defined; no unnecessary duplicate page | CXVoices content owner + CX publishing |
| CXFB-05 | 4 | Get training and grow your skills → Customer Commitments | Customer Commitments information/links reportedly cannot be found. Add a direct, clearly labelled route to current authoritative resource. | P2 | Needs source verification | Current approved Commitments identified, linked and distinguishable from Customer Charter; findability test passes | Customer Commitments content owner + CX content editor |
| CXFB-06 | 1 | Customer Experience landing page → Improve your service for customers | Knowledge Articles are linked under customer service help, but also relevant to improving service. Consider second contextual navigation entry without duplicating content. | P2 | Design review pending | Appropriate Knowledge Articles link discoverable from improvement pathway; label explains why; same authoritative source; no duplicate content | CX content owner + knowledge management |
| CXFB-07 | 6 | Get training and grow your skills → HCD capability | Add Learning Hub tile/pathway for HCD thinking and mindsets resources, subject to approved catalogue links. | P2 | Content availability check pending | Approved HCD learning items found and linked; title/description make the employee need clear; working access tested | CX learning lead + Learning Hub owner |

**Priority caveat:** P1/P2 are working triage assessments; confirm severity, ownership and effort in Jira after reproducing issues. A finding of organisation-wide edit access may warrant immediate escalation under internal security and publishing controls; do not infer a breach from the survey alone.

## Recommended sprint slicing

**First small correction batch:** CXFB-01 (outdated link), CXFB-03 (Qualtrics status) and verify CXFB-02 (permissions). These can be triaged rapidly, but changes still require appropriate publisher/owner approval.

**Content and navigation batch:** CXFB-04/05/06/07. Validate one authoritative destination per topic, add concise employee-intent entry points, and test from the relevant CX page and CoMpanion.

**Separate from the feedback backlog:** existing go-live PVT for all seven pages and 26 documents, and legacy-page retirement. Do not treat six survey submissions as evidence that all other pages are defect-free.

## Triage process

1. Check each proposed item against live page and destination; capture reproducibility and evidence in restricted project systems.
2. Confirm authoritative source and content owner, especially Customer Commitments versus Customer Charter, CXVoices and Knowledge Articles.
3. Record exact Jira issue key, sprint, assignee, estimate, state and acceptance criteria in Jira; optionally add only Jira issue IDs and summarised state here after reconciliation.
4. Deliver smallest safe corrections first; get required approval for content/permission changes.
5. Test as a non-editor employee; check CoMpanion source behaviour where navigation is affected.
6. Review resolved versus open feedback at closure; aggregate themes and track fixes, not identifiable respondents.

## Monitoring measures

- Six form submissions (not unique respondents).
- Seven triage actions (one response splits into two risk domains).
- By response-category: missing information/resources = 3; suggestion for improvement = 2; incorrect/outdated = 1.
- When Jira reconciled: accepted/rejected/deferred count, median resolution time, high-priority unresolved count, link verification, and repeated issue themes.
- Do **not** treat the six responses as representative satisfaction, post-launch conversion, or permission-breach confirmation.

## Related evidence

- `docs/deployment/2026-11-18-employee-feedback-survey.md` — form design and privacy/triage rules.
- `docs/deployment/2026-11-18-go-live-page-export-pvt.md` — seven-page go-live evidence, T0 analytics, CoMpanion and PVT caveats.
- `docs/deployment/project_closure_plan_2026-11-19.md` — four-week verification, retrospective, recommendations and handover plan.

**Source-control note:** This file is a public GitHub staging observation only, not proof of Bitbucket or Confluence sync. Confirm latest approved organisational source before publication or task-state updates.
