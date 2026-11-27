# Intent-led resource curation | Customer Segments prototype

**Date:** 26 November 2026
**Status:** Draft-page feasibility demonstrated 27 November; not approved for production.
**Scope:** Existing page in draft, prototype resource and intent-selector lists, existing library comparator. No production publication claimed.

## Design challenge

> How might we present the right CX resources to employees based on what they are trying to achieve, regardless of where those resources are stored?

Hypothesis: a metadata-driven reference catalogue can help employees find relevant resources without knowing their storage location, while allowing editors to maintain one reference per resource rather than editing multiple pages.

This extends the existing employee-need → CoMweb guidance → authoritative source → next step model. It does not reverse the go-live folder and filename decisions D-019/D-020. Existing files, folders, permissions and names stay unchanged.

## Prototype experience

Use the Customer Segments and Modes offer within the existing L2 "Understand who our customers are" experience as the design context, not a new production page.

Page heading: Find customer segments and modes resources.
Intro: Choose what you are trying to achieve to find relevant guides, tools and evidence.

Four proposed intents:
- Understand our customers
- Plan or design a service
- Improve customer interactions
- Find research and evidence

Show all approved resources by default; allow filtering by intent and resource type. Each card shows an employee-facing title, short purpose, type, source and a direct authoritative link. A resource may match several intents. Provide clear filters/reset, a no-results message and a plain list alternative. Exact clickable intent tiles are a stretch goal; native list filters are the initial baseline.

## A/B technical approach

A: existing document library, filtered view with existing metadata and links where authorised. Test whether folder-scoped and cross-folder views can expose the right subset, and whether native link items support the same experience.
B: Microsoft Lists / SharePoint list, one reference per canonical resource; embed a saved public view (public within the authorised test site) using the modern List web part. Use gallery formatting if supported, otherwise standard list formatting. No SPFx, Power Apps or automation required for the initial test.

The list owns curation metadata only. The originating library, page or external publisher owns the content. A copied description is an editorial summary, not an alternate authoritative document. Do not create the list as a new source of truth for documents.

## List configuration

Proposed list name: CX Resource Catalogue (PoC). Create in an authorised test site where the test page can access the list. Create fields with simple internal names first; verify actual internal names before formatting.

| Display / suggested internal name | Type | Rule |
|---|---|---|
| Title / Title | Single line text | Required; friendly display label, not a filename rename |
| Description / ResourceDescription | Single line text | Required; max 255 characters; when and why to use |
| Resource URL / ResourceUrl | Hyperlink | Required before publishing; verified canonical destination |
| Resource Type / ResourceType | Choice | Reuse approved existing choices |
| Topic / Topic | Choice, multiple | Segments; Modes; Research (proposed local tags) |
| Employee need / EmployeeNeed | Choice, multiple | Four intents above |
| Source / ResourceSource | Choice | Library; CoMweb; External |
| Content owner / ContentOwner | Person | Named accountable contact; confirm role |
| Status / PublicationState | Choice | Draft (default); Published; Retired; prototype-only values |
| Display order / DisplayOrder | Number | Optional; ascending |
| Next review / NextReview | Date | Confirm existing review rules |

Resource Type choices must align with existing approved taxonomy (see metadata validation note); prototype examples use Toolkit, Reference and Publication rather than inventing Guide/Research types. Reuse existing fields where possible. Enable list version history if permitted. Do not treat a status filter as security or approval: only approved, non-sensitive, broadly accessible metadata may enter an employee-readable list. Keep unapproved records in a restricted test environment.

## Synthetic seed records

These are invented, non-sensitive fixtures, not a live organisational register. Replace only within the authorised tenant using approved titles, URLs and metadata. No actual internal URLs or controlled source files are stored here.

| ID | Display title | Type | Topics | Intents (1–4 as above) | Source | Order |
|---|---|---|---|---|---|---|
| P01 | Customer segments overview | Reference | Segments | 1,2,3 | Library | 10 |
| P02 | Customer segment profiles | Reference | Segments | 1,2,4 | Library | 20 |
| P03 | Segments and modes toolkit | Toolkit | Segments; Modes | 2,3 | Library | 30 |
| P04 | Customer modes overview | Reference | Modes | 1,3 | CoMweb | 40 |
| P05 | Customer research summary | Publication | Research; Segments | 2,4 | Library | 50 |
| P06 | Australian demographic evidence | Reference | Research | 4 | External | 60 |

All fixtures begin Draft, with URLs and owners unset. In the authorised test environment populate verified destinations and then mark approved test records Published. Example external source candidate: https://www.abs.gov.au/ (select and verify a task-relevant destination before use). For additional coverage add two more approved representative resources and one retired test record. Never link confidential or draft source material to an employee-facing view.

## Saved views and page wiring

- Employee resources: PublicationState = Published; sort DisplayOrder ascending then Title; show Title, description, ResourceType, ResourceSource, ResourceUrl; enable interactive EmployeeNeed and ResourceType filters if supported.
- Intent-specific views: same published filter plus one EmployeeNeed membership condition. Test multi-choice contains semantics in tenant; if unsupported, use native filter pane or separate controlled single-choice mapping only after assessing duplication/maintenance.
- Administration: all records; grid editing, owner, status, URL, review date and topics.
- Review due: active published records with NextReview on or before today (test relative-date filter syntax); separately flag missing review date.
- Retired: administrative only; excluded from employee views.

Add the List web part to an unpublished or authorised test page, select catalogue and saved view, disable unnecessary commands if available. Test whether the list is selectable from the page's site and whether visitors can use filters without edit rights. If gallery rendering or filter pane is unavailable in the embedded web part, use the standard list or a link to the full filtered list. Do not assume custom formatting or cross-site web parts are enabled.

Optional second iteration: a four-row intent selector list connected through native dynamic filtering. Confirm multi-value field compatibility, default/reset behaviour, and accessibility before adoption. No custom development until baseline evidence warrants it.

## Maintenance workflow

Add: verify canonical source and permission, create one reference, tag intents, assign owner, review and publish through authorised process.
Update: edit catalogue metadata once; validate all consuming views. Update original content at source; no catalogue edit if link and description remain accurate.
Retire: remove from published views, retain administrative history; separately confirm source lifecycle with its owner.
Review: use due/missing-review views; no automated reminder until manual workflow proves useful.
Broken links: flag and withdraw or repair; avoid stale recommendations. Test restricted sources with a normal employee account; metadata must not disclose restricted content.

## Feasibility test script

Initial test plan below; see the dated implementation evidence for observed outcomes. Record date, role, actual result, elapsed time, evidence location in authorised systems, defect and next action.

| ID | Test | Expected outcome |
|---|---|---|
| F01 | Create list and embed on test page | Authorised editor can configure; standard employee can read |
| F02 | Select intent 1 then 2 then 4 | Matching fixture IDs 01/02/04; 01/02/03/05; 02/05/06 respectively (before extra records) |
| F03 | Filter intent 2 and Toolkit | P03 only; reset restores all published fixtures |
| F04 | Open library, page and external references | Each reaches verified authoritative destination without duplicate files |
| F05 | Add one approved resource and assign two intents | Appears in both matching views without page edit |
| F06 | Update title/description/link once | Changes reflected across consuming views; record refresh delay |
| F07 | Retire a record | Removed from every employee view; admin history retained |
| F08 | Test draft, restricted and broken destinations | No inappropriate disclosure; access controls enforced at source; broken links identified |
| F09 | Keyboard/mobile/screen reader smoke test | Filters and links usable; meaningful labels, focus and readable layout |
| F10 | Repeat tasks using library comparator | Measure same outcomes and identify metadata/configuration differences |
| F11 | Optional CoMpanion retrieval | Relevant verified citations; no unsupported links or restricted content; record actual retrieval scope |
| F12 | Check approval boundary and direct list URL | No draft/confidential metadata exposed; existing governance preserved |

## Evaluation and decision gate

Run a small directional test with 3–5 employees and one editor if available. Use equivalent tasks on both approaches, alternate order to reduce learning bias. Suggested tasks: find a customer profile; find a tool to design a service; find demographic evidence; update one resource and retire another.

Proposed thresholds (not measured): relevant authoritative resource within 30 seconds for simple tasks; routine metadata update within 60 seconds; zero duplicate source documents; zero routine page edits; no access or disclosure failures. Record median time, individual task success, steps, confidence, editor maintenance time and any duplicated metadata. Small sample is directional only.

Choose library if equivalent discovery and maintenance are possible without a second catalogue. Choose list if mixed-source, multi-intent curation demonstrably improves usability or maintenance enough to justify a separate reference layer. Hold if permissions, approval or accessibility cannot be satisfied. CoMpanion is optional and must not block the human discovery test.

## Evidence and boundaries

Related project sources: [Experience design](../experience_and_content_design.md), [Publishing SOP](../content_governance_and_publishing_sop.md), [Metadata validation](../deployment/document_metadata_validation.md), [Decision log](../decision_log.md), [Source contract](../../source-contract.md).
Technical references to verify in tenant:
- https://support.microsoft.com/en-us/sharepoint/pages-in-sharepoint/use-the-list-web-part
- https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/view-gallery-formatting
- https://support.microsoft.com/en-au/sharepoint/sites-pages/connect-web-parts-in-sharepoint
- https://support.microsoft.com/en-au/sharepoint/documents-and-library/add-a-link-in-a-document-library

This is a staged proposal in GitHub; compare with current approved Bitbucket sources before transfer. No approval, tenant configuration, production publication, CoMpanion list retrieval, Jira update or Confluence sync is claimed. Keep experiment outside closure-critical work unless explicitly approved.


## Implementation evidence — 26–27 November 2026

**Status:** Working draft-page feasibility prototype demonstrated in an editor session; not production-approved or employee-validated. Evidence is from the working-session screenshots and discussion, not an independent tenant inspection.

| Area | Observed progress | Remaining validation |
|---|---|---|
| Page | New-page creation unavailable to the editor; used an existing page in draft instead | Confirm approved test location and standard employee access before publication |
| Resource catalogue | SharePoint list configured and populated for the Customer Segments and Modes experiment | Verify authoritative destinations, metadata completeness and permissions |
| Intent selector | Separate intent list connected to resource list using native dynamic filtering; selecting an intent displayed matching resources on the draft page | Test all intents, reset/default state and multiple-intent membership systematically |
| Choice values | Initial mismatch corrected by aligning independent EmployeeNeed choices; Playbook then appeared in filtered results | Validate consistent exact values across both lists; do not assume full many-to-many support |
| Presentation | Gallery/card formatting iterated; intent-selector styling explored using list formatting | Final appearance, links, keyboard and mobile behaviour remain to be checked |
| Web part headings | Current editor UI inherits list name; no editable title or hide-title control found | Proposed user-facing list names: “What are you trying to achieve?” and “Explore relevant resources”; rename not confirmed; retest connection if renamed |

### Feasibility test status
- F01: Partial pass — list embedded on existing draft page; normal employee access not tested.
- F02: Partial pass — native dynamic intent filtering demonstrated and one choice mismatch corrected; complete fixture matrix and many-to-many behaviour not verified.
- F03–F12: Not formally signed off; no measured timing, library comparator result, access/accessibility validation or CoMpanion retrieval evidence recorded here.

### Design learning and next action
Native list-to-list filtering is a credible low-code path for presenting resources by employee intent independently of storage location. It is not yet evidence that the experience is easier to use or cheaper to maintain than the library comparator. Keep original filenames, folders and authoritative resource locations unchanged. No SPFx or custom application is required for the demonstrated interaction.

Next contained increment: complete a small intent-to-resource test matrix, including a resource tagged to two intents, all-intents/reset behaviour and direct links; then verify employee access and compare maintenance with the library approach. Confirm whether user-facing list renaming resolves inherited headings without breaking the connection. Record exact formatting JSON only after the working version is recovered and sanitised.

### 27 November project coordination
The working update reported the dynamic-list proof of concept, findability exploration, refreshed project documentation, sprint-task updates and consolidation of outstanding activities and feedback for closure. These are reported coordination activities, not independent confirmation of Jira or production status. Keep the prototype as an optional enhancement opportunity, separate from closure-critical PVT, legacy retirement, analytics T1, feedback remediation and BAU acceptance. No production publication or cross-platform synchronisation is asserted.
