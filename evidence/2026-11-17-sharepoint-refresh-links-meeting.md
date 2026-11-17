# SharePoint Refresh: Link and library cutover working session

**Meeting date:** 17 November 2026  
**Source:** `SharePoint Refresh - Links.vtt`, user-supplied meeting transcript.  
**Evidence status:** Transcript-derived working record; speaker transcription may contain errors.  
**Repository status:** GitHub staging mirror, not confirmation of organisational Bitbucket/Confluence synchronisation.

## Purpose and progress

Dennis asked the team to review refreshed CX pages one by one and close out link destinations before the coordinated publishing checkpoint with Jenny. The team worked through page links, grouped reference resources, service request routes, dashboard access and learning content. Around four pages had been substantively reviewed when Dennis left the session; final page readiness and link tests remained outstanding.

## D-019: Go-live document library architecture and original Segments and Modes naming

**Decision status:** Confirmed go-live direction, implementation pending.  
**Decision makers/participants:** Dennis set the go-live direction; José clarified the change; Mindy confirmed the practical linking dependency.  
**Reference:** ~00:36:32–00:46:12; ~01:07:21–01:11:20.

1. For this release, group resource collections in **folders**, replacing the previously proposed flat-root/no-additional-folder structure for the affected resources.
2. The reason is specific to go-live: a flat document set with filtered views was considered desirable, but the team had **not validated** a direct link exposing only the relevant group of documents. It could not be delivered confidently within the available timeframe.
3. Restore the **original names** of the CX Segments and Modes package and constituent files. Dennis expressly rejected new names introduced during preparation and asked to return to the originals, retaining the **CX** prefix where it existed.
4. Restore the resource grouping under the existing suite structure, with the five original top-level resources/folders Dennis referenced. Confirm the exact hierarchy and exact filenames against the original shared folder before changing SharePoint. The transcript does not furnish a reliable full filename manifest.
5. Link individual customer segment/mode tiles **directly to their corresponding PDFs**. Link the **full CX Segments and Modes suite** to its containing collection folder.
6. Place the customer insight reports mentioned by Mindy in a distinct **Customer Insights Reports** folder, linked from the corresponding webpage. Confirm actual membership rather than infer counts from the conversation.
7. Move **Customer Segments Overview** out of the incorrect location into the appropriate suite grouping. Confirm its destination against the original source structure.

**Why:** Allow Mindy to complete working links to document groupings without inventing untested SharePoint filtered views.

**Consequences:** Previously flat file URLs may change on moving documents. Test direct-PDF links, collection links, access permissions and CoMpanion file citations after changes. Do not presume links update automatically. The original upload count of 26 documents is a starting reference, not proof of the final package after moves.

**Accountability:** José agreed to sort/revert the documents, then notify Mindy. Mindy to update page links. Actual file operations were not verified during this meeting record.

## D-020: Freeze new document filename conventions until post-final-sprint validation

**Decision status:** Confirmed deferral/freeze of the CX-proposed naming recommendation for go-live; future standard remains unapproved.  
**Reference:** ~01:10:49–01:11:20.

- **Freeze** the proposed new descriptive document naming convention and any prospective standardisation or bulk rename.
- **Do not apply it** to the current customer segment/mode package or other release documents.
- Preserve/reinstate existing approved/original filenames and use the operational folder structure needed for go-live.
- In the next sprint, **after the final delivery sprint**, assess whether the proposed naming rules are actually beneficial and feasible, together with folder versus filtered-view design, CoMpanion findability, metadata, permissions, links and long-term maintenance.
- Any post-project convention requires a separate owner-reviewed decision and validation. No adoption is implied by the earlier SOP or metadata recommendation.

**Distinction:** This freezes the *naming-standard recommendation*, not required SharePoint metadata, content accuracy, publishing permissions or basic link checks.

## Other content and publishing decisions

| Topic | Meeting direction | Transcript time | Qualification |
|---|---|---|---|
| Refreshed page names | Use employee-facing page title, with CX ownership signalled through metadata rather than forced title prefix | ~00:34:18–00:35:39 | Distinct from **document filenames** |
| Common help action | Use an existing generic Service Hub request link consistently on relevant pages | ~00:35:45–00:36:14; 00:45:29–00:45:39 | Confirm actual URL and applicable page placement |
| Customer research | Segment/mode cards link to the individual PDF; full suite links to folder; Customer Insights reports have their own folder | ~00:39:11–00:46:43 | Verify membership and URLs |
| Customer measures | A green-page source was selected as an interim destination for measures; further dashboard/training and permissions links discussed | ~00:48:01–00:58:33 | Not proof all links were resolved |
| Learning and support | Link to existing Learning Hub resources and practical CX tools rather than create new content for go-live | ~01:01:14–01:05:28 | Validate availability |
| Pages and metadata | Track SharePoint page ID, H1/display title, slug and unique description; Brooke preferred proposed, page-specific descriptions | ~01:14:05–01:20:12 | URL rename needs authorised editor/publisher confirmation |
| Publishing checkpoint | Brief Jenny at 1pm on first four pages and remaining work; final page links still being completed | ~01:11:33–01:13:36 | Meeting plan, not proof of production publication |

## Immediate actions

- [ ] **José:** compare the 26 uploaded documents against the original Segments and Modes source, preserving precise original names and folder membership.
- [ ] **José:** create or restore the agreed collection folders, move files, then verify permissions and URLs; record changed paths and send Mindy the final destinations.
- [ ] **Mindy:** link specific segment/mode tiles to their PDFs and the complete suite to its folder; link Customer Insights Reports folder.
- [ ] **Mindy/Brooke:** complete remaining page links, descriptions and content refinements; raise unresolved dependencies.
- [ ] **CX team / Jenny:** confirm H1-based target URL slugs and authorised publication workflow; perform production link and access checks.
- [ ] **Project team:** preserve the naming-standard proposal as **deferred**, and revisit only after the final sprint with evidence from actual use.

## Relationship to prior recommendations

This meeting supersedes the go-live implementation assumption in **D-014** that the CX library should have no extra subfolders. The flat structure remains a possible future design subject to testing.

Earlier working naming recommendations in `docs/deployment/document_metadata_validation.md` and `docs/content_governance_and_publishing_sop.md` are **not approved requirements** and are frozen for release, with original file names retained.

No SharePoint file move, rename, production publication, Jira/Confluence update or Bitbucket sync is claimed by this repository record.
