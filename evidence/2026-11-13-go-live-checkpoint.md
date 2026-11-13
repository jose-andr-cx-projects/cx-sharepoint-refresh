# SharePoint Refresh — Go-live checkpoint

**Meeting date:** 13 November 2026 (inferred from reference to Monday 16, Tuesday 17 and Wednesday 18 November; confirm if needed)  
**Evidence:** `SharePoint refresh- Go live checkpoint.vtt` (user-supplied meeting transcript)  
**Participants heard:** Dennis Sartorello, Brooke Crawford, Jose Andrade  
**Status:** Meeting evidence and follow-up record; not formal organisational approval

## Executive summary

The team retained the 18 November 2026 go-live target despite a SharePoint outage restricting editing and configuration. Dennis indicated close of business Wednesday was an acceptable launch expectation. Following a discussion with Jenny, the operating plan was to publish the new pages together on the 18th, share each ready page's details with Jenny in Teams, and hold a final readiness touchpoint on Tuesday 17 November. Testing occurs incrementally in the development environment; a separate post-build UAT round was not planned. Technical publishing issues are to be directed to Jenny.

Document library governance is progressing but not intended to delay launch. The immediate minimum is sensible document titles/filenames; broader descriptions, keywords and tagging may be improved later. The CX Document Set concept without subfolders was explained, while the practical display of a group of files from Purple has **not yet been tested** due to the outage. The CoMpanion team accepted the knowledge-document approach; the final version is still dependent on completed page content.

## Findings by topic

### Launch, sequencing and testing
- **18 November:** Jenny recommended one coordinated batch publish, rather than incrementally exposing completed pages (Jose, ~04:03).
- **Readiness notifications:** As a page becomes ready, its details will be posted in Teams for Jenny (Jose, ~04:03).
- **Tuesday 17 November:** Final checkpoint with Jenny and walkthrough of the draft pages for the team (Jose ~05:25; Brooke/Dennis ~21:40–22:34).
- **Monday 16 November:** Block coordination/preparation time for the Tuesday walkthrough; Mindy to make one final attempt at suggested URL slugs (Dennis ~10:24–10:39, ~21:11–22:34).
- **Wednesday 18 November:** Dennis considered close-of-business publication acceptable given lost time from the outage (~20:38).
- **Testing:** Check pages as built in development; no distinct UAT afterwards was planned. Technical matters go through Jenny, with no separate DTS involvement described (Jose ~05:25).
- **Risk tolerance:** Dennis anticipated a strong first version but acknowledged possible dead links needing follow-up; this must remain an open QA/cutover risk, not be treated as permission to leave broken priority links (~23:26).

### Page content and employee pathways
- Brooke had updated links on her pages and judged most nearly ready (~01:28–01:48).
- The **Reach out to us** concept had been discussed with BLT; Dennis reported general support, with a preference not to publish email addresses and to route requests through Service Hub (~00:49–01:26).
- One page needs significant work according to a note from Mindy, but the transcript does not unambiguously identify its title (~00:22–00:40).

### Naming and governance
- Jose presented the working publishing governance proposal as a branch handover standard covering page descriptions, naming conventions and document metadata (~08:37–10:16).
- Dennis positively received the proposal but did **not** formally approve it; he indicated that Mindy would revisit proposed URL slugs on Monday (~10:16–10:39).
- Encoded spaces / `%20` in URLs remain unresolved; no material immediate findability blocker was established, but Jose flagged possible confusion and downstream implications (~06:44–07:46).
- Brooke volunteered to draft **role-based**, not person-name-based, ownership, auditing and maintenance responsibilities as part of the governance handover (~22:48–23:11).

### Intranet Documents library and CoMpanion
- Documents will use a CX **Document Set** rather than the existing Customer Relations folder. No extra nested folders initially; metadata is the proposed organising layer (Jose ~12:46–14:17; ~16:32–17:46).
- Jose asked editors to review proposed filename, title, descriptive metadata, keywords and relevant images/infographics for potential CoMpanion surfacing. He offered to implement the technical upload and refine the governance instructions (~11:04–12:40; ~14:19–17:46).
- **Go-live minimum:** Jose explicitly said good document titles and filenames are the main immediate concern; extra tagging/descriptions are beneficial, not launch-critical. Dennis began improving document names and deferred deeper tagging decisions (~15:20–16:30; ~19:41–20:36).
- Document collection/surfacing from the Purple library has **not been tested** because of the outage, despite an expectation it should be feasible (~07:48–08:35).
- The CoMpanion team accepted the knowledge navigation document approach; Jose still needs the final version after content stabilises (~05:10–05:25).

## Agreements, proposals and unresolved items

| Item | Evidence status | Next action |
|---|---|---|
| Publish all new pages together 18 Nov | Working plan agreed with Jenny, as relayed by Jose | Coordinate readiness notice and batch release |
| Publish by COB Wednesday | Dennis's acceptable fallback expectation | Align precise deployment window with Jenny |
| Checkpoint and walkthrough Tue 17 | Planned | Finalise drafts, links and demo sequence |
| Testing during build; no separate UAT | Working plan agreed with Jenny, as relayed by Jose | Keep evidence of page/link QA; log exceptions |
| CoMpanion knowledge document | Approach accepted by CoMpanion team | Finalise after content freeze; validate actual retrieval |
| CX Document Set, flat initially | Working configuration direction | Verify actual setup and per-file metadata behaviour |
| Naming first; richer tags later | Go-live prioritisation voiced by Jose and accepted in discussion | Confirm renamed documents before upload; backlog useful keywords/description work |
| Page URL slugs and %20 encoding | Unresolved | Mindy to attempt final adjustment on Monday |
| Role-based ownership and maintenance | Brooke to draft | Review against SOP and confirm with BLT after launch |
| Purple document group display | Untested | Test when outage ends |
| Broken inbound/outbound links | Acknowledged release risk | Prioritise critical links at cutover; track remainder |

## Action register

| Owner / function | Action | Timing indicated |
|---|---|---|
| Page editors / Brooke / Mindy | Finish page content and links, flag pages ready to Jenny via Teams | Before 17–18 Nov |
| Dennis / Brooke / Mindy | Prepare and conduct draft-page walkthrough; Monday readiness time | Monday 16 / Tuesday 17 |
| Jose | Coordinate final checkpoint with Jenny and batch publish readiness | Tuesday 17 |
| Mindy | Last attempt to improve suggested page URL slugs | Monday 16 |
| Jose | Upload documents into correct CX Document Set when access restored and titles are ready; confirm naming/metadata guidance | Monday onward, subject to outage |
| Dennis / content contributors | Confirm cleaner document titles; review optional tagging later | Before upload / subsequent iteration |
| Jose | Finalise CoMpanion navigation document once page content settled | Before release if feasible |
| Jose / Jenny | Test displaying/surfacing grouped library files on pages; resolve technical issues | When outage clears |
| Brooke | Draft role-based page ownership, auditing and maintenance responsibilities | Working draft for next phase |
| CX team / publisher | Post-publish verification; record and fix dead links or access issues | During and after launch |

## Implications for the publishing SOP

1. **Do not turn document keywords or image tagging into mandatory go-live gates.** Prioritise approved names/titles; continue richer discoverability work after publication.
2. **Keep two distinct controls:** mandatory CoMWeb platform metadata and CX recommended metadata.
3. **Link governance to actual CoMWeb permissions** (Jenny and authorised publisher), avoiding a new CX approval chain.
4. **Use a role-based maintenance model** rather than named-person-only assignments; retain operational assigned editors in SharePoint.
5. **Preserve technical unknowns** (file collections, encoded URLs, document-set behaviour and CoMpanion retrieval) as validation tasks, not confirmed capabilities.
6. **Maintain a cutover defect register**, particularly for legacy Purple links, and distinguish known critical failures from later enhancements.

## Suggested Teams update

**SharePoint Refresh — go-live checkpoint**

We're still working towards **Wednesday 18 November** for the CX front door, despite the SharePoint outage cutting into build time. The plan is to release the new pages together with Jenny, with a draft walkthrough and final readiness check on **Tuesday 17 November**.

The priority now is to close out page content, key links and document names. The CoMpanion knowledge-document approach has been accepted, and we're keeping the initial CX document library structure simple.

We're also shaping the longer-term publishing governance: clear page ownership, review responsibilities and lightweight metadata standards. A few technical items — URL slugs, grouped files and final link QA — still need validation as access returns.

**Next focus:** finish the draft pages, prepare Tuesday's walkthrough and flag anything that could affect launch.

## Record status

This note interprets only what was stated in the meeting transcript. Timing references refer to the 16–18 November launch sequence. It does not certify that pages are ready, that the outage is resolved, that publication occurred, or that the governance SOP has formal approval.
