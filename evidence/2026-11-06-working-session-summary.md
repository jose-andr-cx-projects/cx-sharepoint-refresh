# CX SharePoint refresh: working session and go-live decisions

**Session:** 6 November 2026 (date inferred from meeting's next-week calendar references)  
**Source:** Teams transcript, `SharePoint update working space (1)(1).vtt`, supplied in chat.  
**Status:** Working-session record, not formal publishing approval. Check against Bitbucket, Confluence and Jira before adopting as organisational source of truth.

## Outcome
The team aligned on a **target first go-live of Wednesday 18 November 2026**, conditional on Digital/publishing readiness. **Monday 23 November** was discussed as a possible fallback, not adopted as the launch date. The preference is to release a minimum useful experience, then improve it rather than extending the first release to accommodate every requested change.

A controlled delivery goal was proposed: content and links ready, replacement pages ready, and legacy-page archive/cutover arrangements clarified. The actual switch-over depends on the publishing owners and is not a team-controlled commitment.

## Working decisions and design direction
1. **Improve distinction between employee-need navigation cards.** Research and BLT feedback suggest current Level 2 card headings overlap semantically. Rewrite headings/descriptors to make destinations unmistakable; do not reopen the overall employee-needs structure.
2. **Make quick links functional and direct.** They should skip an unnecessary navigation level and lead to a real task, service, form, dashboard or guidance. Keep the 'tools/resources' collection separate as a browsable bookshelf. Recheck specific links for complaints, customer feedback/insights, service requests, skills and Service Hub offerings.
3. **Use Service Hub as the common request pathway.** A generic 'Ask a CX team' / Service Hub entry point was favoured, while the exact position, wording and treatment of existing specialist inboxes still need implementation checks. A future email-to-Service-Hub approach was an idea, not an approved change.
4. **Prioritise link and asset readiness.** Page tiles have been substantially built but use temporary URLs. Store linked PDFs and Word files in the designated SharePoint document library, confirm permissions, and replace temporary links with destination-specific links. Start with workable filenames, improve conventions later.
5. **Keep some legacy content temporarily if replacing it would leave a gap.** Complaints management and other complex content may need an interim pathway. Do not archive a page without a viable destination; capture redesign needs for the next phase.
6. **Deprioritise the news feed for first go-live.** Current filtering behaviour is unclear; explore only if easily resolved, and do not sacrifice links/content readiness.
7. **Make section content clearer.** Consider a 'what is in this section' overview near the top and consistent related-page links across sections. Anchored navigation may not be feasible in the SharePoint configuration.
8. **CoMpanion enablement is dependent on final content and source access.** José has prepared an information-architecture/metadata document template. After content settles, populate it and ask Jenny to confirm the document library can be retrieved by CoMpanion and that its configuration supports the intended routing. Do not assume retrieval is validated.
9. **Communications focus on practical employee benefits.** Brooke's change plan contemplates a Viva Engage post plus a concise Comm News item. Prepare an advance branch/team note once cutover is confirmed; demonstrate how staff can find tools, navigate guidance and submit requests.

## Working plan and responsibilities
| When | Lead / contributors | Action | Evidence of completion |
|---|---|---|---|
| 6-10 Nov | José | Schedule three working check-ins: Tue 10 Nov 4-5pm; Thu 12 Nov 9:30-10:30am; Fri 13 Nov 11am-noon. Confirm actual invites and availability. | Calendar invites accepted |
| Early week of 9 Nov | José + Jenny, Jasmine if needed | Review Jenny's publishing guidance; verify access, permissions, technical owners, archiving/deactivation, sequencing, redirects/links and approval for 18 Nov cutover. Jenny's availability conflicts with end of Tuesday's 4-5pm slot, so a separate earlier contact may be necessary. | Documented technical cutover decision, owner and dependency |
| Early week of 9 Nov | José | Confirm document-library access and location and ask Jenny to validate CoMpanion's access/readability of IA metadata after final content. | Access and retrieval test results, or explicit blocker |
| Early week of 9 Nov | Mindy + Brooke | Finish staging the last SharePoint page, share editing links, walk through page editing; coordinate language and tile updates. | All relevant page editors can amend staged pages |
| By Thu 12 Nov | Page owners (with José facilitating) | Rewrite ambiguous cards, align quick links to tasks, replace placeholder URLs, upload required assets and flag missing destinations. | Draft ready for cross-page review |
| Fri 13 Nov | Team, coordinated by José | Inspect consistency across pages, link destinations, material gaps and pages not safe to retire; classify omissions as launch critical vs future backlog. | Shared readiness and exception list |
| Week of 16 Nov | Brooke + Dennis / team | Prepare internal transition guidance and communication; test the experience with a small number of staff. | Agreed messages and completed checks |
| Target Wed 18 Nov | Publishing owner(s), subject to Digital confirmation | Execute first cutover only after agreement on archiving and viable replacement links. | Verified live pages and old-page treatment |

**Jira remains the authority for assigned tasks, dates and states.** Table above captures meeting-level follow-up only; it is not evidence that calendar invites or Jira updates were performed.

## José's prioritised actions
- **P0:** Contact Jenny and confirm publishing/cutover process, timing, library permissions and required technical sign-off. Escalate to Jasmine if needed.
- **P0:** Send the three check-in invitations and make Friday the content/link readiness gate.
- **P1:** Facilitate a concise page-owner checklist: clear heading, clear purpose, meaningful quick links, valid final destinations, correct linked assets, explicit legacy-page disposition.
- **P1:** Review and validate the IA/CoMpanion metadata document with Jenny once destination content is stable.
- **P2:** Explore news-feed filtering only if quick and non-blocking; record any unresolved issue for subsequent governance.
- **P2:** Capture email-to-Service-Hub routing and more extensive legacy-page redesign as later improvements, not 18 November release scope.

## Risks / decisions still open
- **Technical dependency:** Final publication/deactivation steps and Digital approval are not confirmed.
- **Content completeness:** Some tiles point to temporary URLs; older pages cannot all be retired without suitable replacements.
- **Ownership:** Several specialist team inboxes and contact pathways need harmonisation without hiding useful request channels.
- **CoMpanion:** Source visibility and retrieval behaviour remain assumptions until tested.
- **Accessibility/usability:** Final page navigation, labels and links still require a practical smoke test.

## Release principle
**Launch the smallest coherent, navigable CX experience with working pathways. Preserve a safe fallback where a replacement is not ready. Record the rest for the next sprint or ongoing content governance.**
