# Decision Log

Status: Draft  
Last updated: 17 November 2026

## Purpose

Record material decisions that affect scope, direction, content placement, design, implementation, governance, ownership or delivery sequencing.

## Decision statuses

- Proposed
- Pending
- Confirmed
- Revisit
- Superseded

## Decision register

| ID | Decision | Status | Evidence / source | Impact |
|---|---|---|---|---|
| D-001 | Confluence explains the work; Jira manages the work | Confirmed | Project operating model | Separates durable project context from active delivery |
| D-002 | Project roles: Tanya Sponsor; Dennis Project Lead; José Project Manager; Mindy UX Lead; Brooke Implementation Lead | Confirmed | Project setup | Establishes working accountability |
| D-003 | Simplification over migration | Proposed | Current-state findings and employee research | Existing content must earn its place |
| D-004 | Lead with employee need and CX offer rather than team structure | Proposed | Employee research and Digital direction | Shapes IA and navigation |
| D-005 | Future Jira phase containers are created only when active | Confirmed | Project operating model | Keeps Jira focused on active work |
| D-006 | Employee interviews are a primary scoping evidence source | Confirmed | 12 interviews completed | Discovery findings must shape future design |
| D-007 | Content and important inbound links must be audited before movement or retirement | Confirmed | Current-state / CoMpanion implications | Prevents broken employee pathways |
| D-008 | BLT playback validates direction, scope and approach rather than detailed page design | Confirmed | Scoping workshop | Keeps detailed design separate from scoping alignment |
| D-009 | Detailed structure and mock-up feedback occurs after Define and Develop work | Confirmed | Scoping workshop | Defines next value drop |
| D-010 | Use current CoMWeb governance direction as a working design input | Confirmed | Digital alignment / current CoMWeb direction | Shapes content placement and authoritative-source decisions |
| D-011 | Treat CoMWeb as a pathway, not a repository | Proposed | BLT playback evidence | Favors orientation and linking over duplication |
| D-012 | Use multiple content homes where employee needs differ | Proposed | Employee research and Digital alignment | Supports CoMWeb + Digital Dashboard model |

| D-013 | Adopt a minimum CX publishing SOP that reuses current CoMWeb Site Pages fields and workflows: mandatory Name, Content Editor, Division, Branch; CX operating standard for accountable Team and Description; no new metadata columns for go-live | Proposed CX operating standard; pending CoMWeb/branch validation | CX Site Pages and Intranet Documents screenshots; CoMWeb Editor Training Manual; CX seven-page IA; 11 Nov working agreement | Update `docs/content_governance_and_publishing_sop.md`; confirm fields, owners, permissions and review automation with Jenny |
| D-014 | Prefer existing CX Intranet Document Set, no additional CX subfolders initially; prioritise Name, Description, Keywords and Resource Type for CoMpanion findability | **Superseded for go-live by D-019**; flat/views model may be re-evaluated post-project | Intranet Documents screenshot and page-design discussions; 17 Nov links meeting | Go-live uses folders for required collections; metadata verification remains relevant |


| D-015 | Treat the SharePoint Refresh release as three components: uploaded document library resources, refreshed CX webpages and an AI instruction document; CoMpanion document retrieval is only one check within library PVT | Confirmed project deployment approach; production sign-off pending | User deployment decision 17 Nov 2026; `docs/deployment/deployment_handover.md` | Adds handover matrix and discrete verification by component |
| D-016 | Capture CoMpanion **webpage UAT baseline before** refreshed pages publish; repeat identical questions as **production PVT after** publication | Confirmed project testing approach | User deployment decision 17 Nov 2026; prior 13 Nov meeting record preserved as historical evidence | Gives a pre/post source-navigation comparison without treating document-upload results as a clean baseline |
| D-017 | Retain legacy CX pages for up to three weeks after go-live while they are retired through authorised process; instruct CoMpanion to omit mapped old URLs and prefer refreshed pages, and verify that behaviour in PVT | Confirmed transition approach; URLs/admin control to be finalised | User deployment decision 17 Nov 2026 | Requires old-to-new URL mapping, instruction admin confirmation, exception handling and post-release archive sign-off |
| D-018 | Use 26 uploaded CX documents for natural-language document discovery tests within library PVT; distinguish retrieval evidence from proof that metadata caused retrieval | Confirmed test scope; live PVT pending | CoMpanion T01/T02 post-upload observations and user scope decision 16–17 Nov 2026 | Preserve per-file citations/permissions and verify SharePoint columns separately from embedded PDF metadata |

| D-019 | For go-live, use folders for grouped CX documents because a flat library with linkable filtered views was not proven in time; restore original CX Segments and Modes filenames and groupings; individual cards link to PDFs, full suite to folder, and Customer Insights Reports to its folder | **Confirmed release direction; implementation pending** | 17 Nov 2026 `SharePoint Refresh - Links.vtt` ~00:38–00:46 and ~01:07–01:11; `evidence/2026-11-17-sharepoint-refresh-links-meeting.md` | Supersedes D-014's no-folder proposal for release; requires exact original-name comparison, file moves and refreshed link/PVT checks |
| D-020 | **Freeze** the proposed new document naming convention; use original approved filenames for go-live and validate naming rules only **after the final project sprint** | **Confirmed deferral; naming standard unapproved** | 17 Nov 2026 `SharePoint Refresh - Links.vtt` ~01:10:49–01:11:20; meeting evidence | No further bulk naming changes for go-live; review separately in next sprint and after final-sprint evidence |

## Working principle

Document decisions, not every discussion.
