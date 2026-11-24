# CX SharePoint Refresh

## Current status — 24 November 2026

**Phase: post-go-live stabilisation and closure.** Seven refreshed pages reported live on 18 November at 10:30 AEDT; seven static exports inspected. A 26-file upload was reported. Functional acceptance remains open. Six feedback submissions yielded seven proposed actions; effort review is prepared for team calibration. Proposed closure: 16 December, subject to acceptance.

- [Current next steps](delivery/next-steps.md)
- [Closure plan and handover gates](docs/deployment/project_closure_plan_2026-11-19.md)
- [Page PVT and analytics](docs/deployment/2026-11-18-go-live-page-export-pvt.md)
- [Library PVT evidence](docs/deployment/document_metadata_validation.md)
- [Feedback backlog](docs/deployment/2026-11-23-feedback-triage-backlog.md)
- [Effort review](docs/deployment/effort_by_deliverable_working_review_2026-11-23.md)

## Bitbucket-native project navigation (2026-10-26)

This is the intended CoM Bitbucket portfolio structure, staged in GitHub before approved transfer. Follow this map rather than assuming the repository is synchronised with Bitbucket.

| File | Purpose |
|---|---|
| [Project overview](project-overview.md) | Project purpose and existing assets |
| [Source contract](source-contract.md) | System authority, publication, review and approval |
| [Decision register](project-decisions.md) | Important proposals and decisions |
| [Evidence index](evidence/README.md) | Workshop / research references |
| [Next steps](delivery/next-steps.md) | Small increments; Jira remains delivery authority |
| [Companion](agent/companion.md) | Rovo navigation and execution boundaries |


> **Bitbucket transition (26 October 2026):** This GitHub repository is an existing project reference, not the intended ongoing CoM source of truth. The Bitbucket-first operating architecture and controlled Strategic OS intake are staged in [CX portfolio transition](https://github.com/jose-andr-cx-projects/cx-portfolio-context/tree/main/bitbucket-transition). Before replacing any organisational records, compare against the latest approved Bitbucket/Confluence/Jira sources. No ongoing cross-platform mirroring is intended. This note does not change the project's substantive decisions or status.


Project documentation for making CX information, tools and resources easier for employees to understand, find and use.

The work clarifies the role of CX content within the broader employee information ecosystem, including CoMWeb and the Digital Dashboard.

> How might we make CX information, tools and resources easier to understand, find and use, so that employees can confidently access what they need and content remains manageable over time?

## Start here

Read the [project overview](docs/project_overview.md) for the purpose, team, evidence and emerging direction.

| Document | What it covers |
|---|---|
| [Project overview](docs/project_overview.md) | Purpose, intended outcomes, team and current evidence |
| [Scope and delivery plan](docs/scope_and_delivery_plan.md) | Boundaries, dated phases, planned activities and decision points |
| [Discovery and content audit](docs/discovery_and_content_audit.md) | Current-state findings, employee research, benchmarking and outstanding audit work |
| [Experience and content design](docs/experience_and_content_design.md) | Design principles, proposed content homes and validation criteria |
| [Content governance and publishing SOP](docs/content_governance_and_publishing_sop.md) | Working end-to-end publishing process, governance decision rights and approval gates |
| [Decision log](docs/decision_log.md) | Material decisions and their status |
| [Risk and dependency log](docs/risk_and_dependency_log.md) | Risks, constraints, dependencies and responses |
| [Ways of working](docs/ways_of_working.md) | Roles, tools and delivery practices |
| [Scoping playback](docs/scoping_playback.md) | Evidence synthesis, proposed direction and alignment questions |

## Delivery phases

The following is the historical baseline plan, not current status. The proposed closure window is 19 November–16 December 2026.

| Dates (2026) | Phase |
|---|---|
| 11 August–1 September | BLT alignment and team formation |
| 2–22 September | Scoping |
| 23 September–13 October | Define and Develop |
| 14 October–3 November | Define and Deliver 1.0 |
| 4–24 November | Transition to governance and maintenance |

The timeline records planned delivery windows; it does not confirm completion or approval of outputs.

## Working direction

Discovery includes 12 interviews with employees across CX, current-state review, internal benchmarking and Digital input.

The emerging experience follows:

**Employee need → CoMWeb guidance → authoritative source or service → clear next step**

Working principles are employee needs first, one authoritative source and multiple ways in. Link to existing authoritative content where appropriate.

The seven exported pages establish the implemented page structure; broader hub direction, formal ownership and functional acceptance remain subject to validation. Current CoMWeb governance guidance and Sally’s preliminary framework remain provisional.

The working publishing SOP is available for closure review and BAU adoption; formal ownership and approval remain outstanding.

## How this documentation is used

**Confluence explains the work. Jira manages the work.** These Markdown files provide a maintainable copy of the project documentation; their presence does not imply changes have been published to Confluence or Jira.

Keep discovery evidence in the discovery document, future design logic in the design document, operational publishing logic in the governance SOP and material decisions in the decision log. Distinguish confirmed decisions from proposed directions and open questions.

The documentation was initially aligned with `CX Sharepoint Refresh (BLT)(2).pdf` and the project handover on 30 September 2026. Later project working updates should preserve the distinction between confirmed organisational decisions and project working artefacts.

## Production deployment handover (17 November 2026)

The SharePoint Refresh release has three components: **document library files, refreshed CX webpages, and the CoMpanion AI instruction/knowledge-navigation document**. See the [production deployment handover](docs/deployment/deployment_handover.md) and [team progress matrix](docs/deployment/deployment_progress_matrix.csv).

- Uploaded library files: PVT includes metadata, permissions, links, and CoMpanion document retrieval.
- Refreshed webpages: capture CoMpanion **UAT baseline before production deployment**, repeat scenarios in **PVT after deployment**.
- AI instruction: direct CoMpanion to new authoritative pages, excluding mapped legacy CX pages while they remain published for up to three weeks post go-live.
- [Prior documentation audit](docs/deployment/repository_documentation_audit_2026-11-17.md) and [document metadata/PVT validation](docs/deployment/document_metadata_validation.md) identify gaps, source limitations and follow-up checks.

**Mirror control:** These GitHub commits do not establish Bitbucket sync, live Jira status, Confluence publication, SharePoint deployment approval, or completed PVT. Before syncing GitHub to Bitbucket, confirm the latest remote branch diff and run existing pipeline **validate/preview-only**, never automatic publication.
