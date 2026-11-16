# SharePoint Refresh — Prior documentation requests: GitHub mirror audit

**Audit date:** 17 November 2026  
**Target:** `jose-andr-cx-projects/cx-sharepoint-refresh` GitHub staging mirror, default branch.  
**Method:** Compare the current repository tree and selected content with the user's retrievable prior project instructions. **A file's presence is not proof its contents are current, approved, synced to Bitbucket or published to Confluence.**

| Prior request / decision | GitHub evidence | Audit outcome / action |
|---|---|---|
| Initial September project breakdown: overview, scope/delivery, discovery, design, decisions, risks, ways of working, playback | `docs/project_overview.md`, `scope_and_delivery_plan.md`, `discovery_and_content_audit.md`, `experience_and_content_design.md`, `decision_log.md`, `risk_and_dependency_log.md`, `ways_of_working.md`, `scoping_playback.md` | **Present**; full source-to-source content parity not asserted |
| October governance/publishing SOP | `docs/content_governance_and_publishing_sop.md` | **Present**, updated 11 Nov; remains working proposed SOP, not approved policy |
| 9 October design review and employee-first six-card approach | `docs/experience_and_content_design.md` | **Present**; technical and approval status retained as provisional |
| Confluence publishing/source selection and 4Ds work vs information taxonomy | `publishing.json`, `scripts/publish_confluence.py`, `bitbucket-pipelines.yml` | **Present**; preview-only/approval gates retained; no actual Confluence publication claimed |
| 23 Oct working session, 29 Oct feedback synthesis | `docs/2026-10-23_sharepoint_working_session.md`, `docs/2026-10-29_sharepoint_stakeholder_feedback_synthesis.md` | **Present** |
| 6 Nov working session, 9 Nov publishing cutover, 13 Nov go-live checkpoint | `evidence/2026-11-06-working-session-summary.md`, `evidence/2026-11-09-publishing-cutover-discussion.md`, `evidence/2026-11-13-go-live-checkpoint.md` | **Present**; historical dates/plans not overwritten |
| 11–16 Nov Site Pages and document library metadata governance, PDF Title/Subject/Keywords, Description/Keywords caps, Resource Type taxonomy, and Segments/Modes vocabulary | Existing SOP describes these fields generally, but **no dedicated 26-file metadata register or latest detailed rules found in current tree** | **Gap**. Obtain actual approved register and latest governance artefacts before importing exact field values; do not fabricate a metadata register. See `docs/deployment/document_metadata_validation.md` |
| Single CX AI knowledge-navigation source / CoMpanion instruction document | SOP recommends it; `agent/companion.md` is **project-agent guidance**, not the CoMpanion knowledge-navigation instruction | **Gap**. Define and approve the actual CoMpanion instruction source separately, including legacy URL exclusions. |
| 16 Nov CX document uploads and CoMpanion T01/T02 observations | No dedicated PVT record in tree before audit | **Gap addressed:** `docs/deployment/document_metadata_validation.md`; treat T01/T02 as observed post-upload diagnostics, not proof of metadata causation |
| 17 Nov SharePoint production handover; three components, webpage UAT baseline then PVT, legacy archive within three weeks | No dedicated deployment handover in tree before audit | **Gap addressed:** `docs/deployment/deployment_handover.md` and `deployment_progress_matrix.csv` |
| Other interview/meeting transcript requests, Jira story changes, Teams posts | Some evidence notes exist, Jira is work authority | **Not fully verified**. No Jira, Confluence or Bitbucket live parity check undertaken; refrain from marking these synced or completed. |

## Open sync and governance checks

1. Confirm `docs/deployment/` content against the actual live Jira and SharePoint page register before cutover; names and dates still TBC.
2. Import the **actual**, approved 26-file document metadata register and most recent governance rulebook rather than reconstructing values from conversational summaries.
3. Add the approved CoMpanion CX information-architecture instruction file and specific legacy→new URL pairs; do not confuse it with `agent/companion.md`.
4. Update the decision register to distinguish post-13-Nov CoMpanion UAT/PVT decisions from the older incremental QA plan.
5. Sync GitHub → Bitbucket **only after explicit remote/branch diff verification**, even though the project owner reports no downstream Bitbucket changes; do not force-push. Validate `publishing.json` and existing Confluence page IDs before any publishing pipeline is run.
6. Keep Jira as delivery/status authority and Confluence as approved narrative authority; GitHub is an interim mirror/staging location per `source-contract.md`.
