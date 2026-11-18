# CX SharePoint Refresh — employee feedback survey

**Captured:** 18 November 2026 from supplied Microsoft Forms screenshots.  
**Form title:** Help us improve our CX pages  
**Purpose:** Gather employee-reported broken links, outdated information, confusing navigation and improvement suggestions following the refreshed CX pages launch.  
**Status:** Invitation and form configuration visible in screenshots; response totals, live form URL, owner and storage settings not independently verified. Do not store individual responses in this public repository.

## Launch invitation

The screenshot invitation, dated 18 November 2026, announces the launch of the Customer Experience pages on CoMWeb and invites reports of broken links, outdated information and unclear content. Its action is **Start now**; the target URL is not visible and must not be invented.

## Survey fields (as displayed)

| ID | Field | Type | Required | Options / instructions |
|---|---|---|---|---|
| Q1 | Which page is this about? | Single-select; Other free text | Yes | Customer Experience (main page); Understand who our customers are; Find customer data and feedback; Improve your service for customers; Get training and grow your skills; Support customers with confidence; Not sure where to start?; Other |
| Q2 | What type of issue or feedback is it? | Single-select; Other free text | Yes | Broken link or button; Incorrect or outdated information; Something is unclear or confusing; Missing information or resources; Layout or display issue; Suggestion for improvement; Other |
| Q3 | Tell us a little more | Long text | Yes | What is not working, incorrect, missing or could be improved? |
| Q4 | Where exactly did you notice this? | Long text | Yes | Page link, section name or heading, if known |
| Q5 | Do you have a suggestion for how we could improve it? | Long text | Yes | Suggested action or wording |
| Q6 | Have a screenshot or file to share? | File upload | Not marked required | Up to three files; 10 MB each; Word, Excel, PowerPoint, PDF, image, video or audio; remove personal or sensitive customer information |

**Privacy notice observed:** The form states that the owner can see the respondent's name and email address. Treat responses as **identified**, not anonymous; Q6 explicitly says non-anonymous.

## Survey page-label reconciliation

Preserve the raw response label alongside the approved final page title:

| Survey label | Proposed final CX page | Confidence |
|---|---|---|
| Customer Experience (main page) | Customer Experience | Exact / obvious |
| Understand who our customers are | Understand who our customers are | Exact |
| Find customer data and feedback | Act on customer data and feedback | Likely; verify |
| Improve your service for customers | Improve your service for customers | Exact |
| Get training and grow your skills | Get training and grow your skills | Exact |
| Support customers with confidence | Get help delivering customer service | Likely; verify |
| Not sure where to start? | Navigation issue; canonical page unresolved | No one-to-one mapping |
| Other | Human triage from text and URL | Unresolved |
| **Absent explicit option** | **Connect with the CX team** | Survey coverage gap |

Confirm the two label mismatches and missing direct CX-team choice with the form owner. Do not silently rewrite historic responses if the form options change.

## Proposed feedback register (restricted organisational system)

One record per submission: `response_id`, `submitted_at`, `page_raw`, `canonical_page`, `issue_category_raw`, `issue_description`, `location_or_url`, `suggested_change`, `attachment_reference`, `triage_status`, `severity`, `owner`, `ticket_reference`, `resolution_date`, `verification_result`.

Use an **approved CoM location** for response exports, identity, attachments, free-text and triage data. Suggested status values: New, Reviewing, Action agreed, Resolved, Closed without change. Severity: Blocking, Significant, Minor, Enhancement. These are proposed working values, not claims about configured fields.

## Evaluation and operational loop

1. Monitor received responses in Microsoft Forms; protect respondent identity and attachments.
2. Triage by page, issue category and severity; verify issue reproduction; de-duplicate reports.
3. Assign corrective action in Jira or authorised work tracker and record the issue/URL.
4. Verify the fix as an ordinary employee, not solely as a SharePoint editor.
5. Review aggregated counts, issue themes, open/resolved items and median resolution time when timestamps permit.
6. Compare themes with T0 page analytics; **feedback volume is not a satisfaction or task-success measure** and does not replace functional PVT or CoMpanion retrieval tests.

## Scope of feedback routing

For operational navigation failures, including contact-centre operating hours, after-hours assistance, available self-service channels, urgent/emergency contacts and mailroom services, classify feedback under **Get help delivering customer service** unless the report clearly concerns another final page. Capture exact employee question, link/page section and whether the information was missing, inaccurate or difficult to find. Operational contact/hours details must be verified against the authorised service owner before publishing a correction.

## Validation actions

- Obtain the actual Forms URL, collection owner, retention arrangements and response-access permissions in the organisational handover (not public GitHub).
- Confirm form labels against all seven launched pages and consider whether Q5 needs to be compulsory for defect reports.
- Verify internal operating-hours, after-hours, self-service, emergency-escalation and mailroom service content with its accountable owner.
- Distinguish reported release, form availability, response collection and resolution from approved release sign-off.

**Source authority:** Microsoft Forms is the response source; SharePoint is authoritative for published content; Jira/approved tracker is authoritative for remediation. This GitHub file records the survey design only; Bitbucket/Confluence sync not established.
