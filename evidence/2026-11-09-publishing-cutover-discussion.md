# CX SharePoint refresh: publishing and cutover discussion

**Source:** Teams transcript supplied as `SharePoint refresh -  about publishing and cutover.vtt` (8-minute discussion with Jasmine De Boni, Brooke Crawford and José Andrade).  
**Capture date:** 9 November 2026; actual meeting date not independently established from transcript.  
**Status:** Meeting evidence and proposed actions, not approved change authority. Check with the current Bitbucket/Confluence/Jira records before operational use.

## Summary
The team is targeting **18 November 2026** for CX SharePoint go-live. Jasmine explained that the purple-site publishing process uses a SharePoint back-end workflow with email notifications. Given the number of changes, she advised coordinating the grouped cutover directly with Jenny rather than processing each request through normal shared-inbox handling. Pages should be finished in draft in advance. Publishing should be quick once Jenny actioned approvals, but precise timing and sequencing remain to be arranged.

Jasmine indicated that Jenny also needs to support archive operations on old purple-site pages so they no longer appear in CoMpanion. **Purple and green sites are separate instances:** the purple-site publishing team does not control green-site unpublishing. Legacy page links are a principal cutover risk because **redirects are not available**; links may survive in other intranet pages, Learning Hub modules and training resources.

Brooke reported that Mindy has built the new pages with content in place; language simplification, refinements and correct file destinations remain. The proposed root-only document library was raised, but Jasmine could not confirm whether it is compatible with the existing library's folder-inherited metadata.

## What the session established
1. **Publishing workflow:** SharePoint back-end workflow generates automated email notifications. Jasmine suggested a coordinated Jenny-led process for this batch of pages. This is a recommended approach, not yet a confirmed cutover booking.
2. **Draft readiness:** New pages should be ready in draft before the launch day; publishing was described as almost instantaneous after actioning, not a tested service-level commitment.
3. **Legacy-page archiving:** Jenny has additional steps for purple-site page archival, including avoidance of old content surfacing in CoMpanion. Exact technique and sequence are not defined.
4. **Two site environments:** Purple and green are separate instances; unpublishing green pages remains on the CX side, outside Jasmine's team's remit.
5. **No redirect capability:** Inbound links pointing to legacy pages must be identified and repaired at source where possible, especially elsewhere in the site, Learning Hub material and training documentation.
6. **Content preparation:** Mindy has created the pages. Brooke identified rewriting and simplification of language, final polish and use of the correct file location as outstanding work.
7. **Library architecture not validated:** A flat/root-only library model was proposed by José, but the impact on existing branch-folder and inherited metadata behaviour was unknown. Jenny is the named person to check with.
8. **Communication coordination:** Jasmine said she would tell Jenny to expect a meeting and alert Internal Comms that a flurry of workflow emails was expected on the 18th and related to this coordinated cutover. This was a commitment to communicate, not evidence notifications were sent.

## Actions and follow-ups (proposed, not Jira status)
| Priority | Owner / dependency | Action | Result needed |
|---|---|---|---|
| P0 | José or Brooke → Jenny | Arrange a short meeting during week of 9 Nov and reserve Jenny's support for 18 Nov | Agreed cutover contact, timing, responsibilities |
| P0 | José / Brooke / page owners | Assemble list of old and new URLs, classed as purple or green, with publish/archive/unpublish intent | Page-by-page cutover inventory |
| P0 | Jenny + CX team | Confirm sequence of publish vs archive, exact approvals and handling of green-site unpublishing | Explicit cutover steps and owners |
| P0 | CX team and relevant content owners | Check important inbound links to retiring pages, particularly Learning Hub and training resources; determine remediation | Safe archive list and link-fix exceptions |
| P1 | Mindy / Brooke / CX editors | Complete concise language and navigation improvements, document locations and page drafts | Draft pages ready ahead of go-live |
| P1 | José → Jenny | Validate whether root-only resource storage is compatible with existing library/document-set metadata inheritance, or agree a supported alternative | Confirmed document upload/metadata approach |
| P1 | Jasmine | Let Jenny know to expect a meeting; advise Internal Comms about expected automated emails | Communication acknowledged (not yet verified) |

## Open questions / decision gates
- Who is authorised to publish each purple page, and exactly how will Jenny operate the batch?
- Should replacement pages be published before old pages are archived, or vice versa?
- Which existing pages belong to the green instance and who can unpublish them?
- What is the remediation path for legacy URLs with inbound links that cannot be redirected?
- Can a document library without folders populate required Division, Branch and Resource Type metadata correctly?
- What action or validation ensures archived content no longer appears in CoMpanion?

## Recommended cutover gate
Do not retire a legacy page until its replacement is live and accessible, affected links are accounted for, and its archive/unpublish owner is clear. This is a risk-control recommendation derived from the discussion, **not a formally approved operational rule**.

## Source-of-truth note
This is a de-identified project-level summary in the GitHub reference repository. The organisational systems of record remain the relevant SharePoint/CoMWeb environment, Bitbucket/Confluence as designated, and Jira for tasks and ownership. No publication, Jira change, calendar invitation or organisational approval is implied by committing this summary.
