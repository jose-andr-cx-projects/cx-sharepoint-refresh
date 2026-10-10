# Ways of Working

Status: Draft  
Last updated: 10 October 2026

## Working rule

**Epics group the work.**  
**Stories and Tasks are the visible sprint cards.**  
**Sub-tasks are optional.**  
**Confluence explains the work.**  
**Jira manages the work.**

## Team

| Role | Person |
|---|---|
| Sponsor | Tanya Wolkenberg |
| Project Lead | Dennis Sartorello |
| Project Manager | José Andrade |
| UX Lead | Mindy Nam |
| Implementation Lead | Brooke Crawford |

## Tool model

| Tool | Purpose |
|---|---|
| Confluence | Project context, evidence, design logic, decisions, risks and agreed outputs |
| Jira | Active delivery, sprint planning, ownership, status and blockers |
| Miro | Workshops, mapping and collaborative synthesis |
| Figma | Prototype and experience design |
| SharePoint / CoMWeb | Published employee experience |
| Teams | Day-to-day collaboration |

## Jira hierarchy

Initiative  
↓  
Active Deliverable / phase  
↓  
Epic  
↓  
Story / Task  
↓  
Optional Sub-task

## Current epics

### Understand the current experience

Current-state review, content mapping, usage evidence and constraints.

### Understand needs and expectations

Employee interviews, audience definition, role of CX SharePoint and benchmarking.

### Establish content foundations

Content inventory, candidate content, classification and ownership gaps.

### Establish delivery foundations

Confluence, Jira, Digital engagement, working rhythm and playback.

## Documentation rule

If someone needs to know **why**, go to Confluence.

If someone needs to know **who is doing what by when**, go to Jira.

## Evidence rule

Workshop comments and stakeholder requests are evidence, not automatic requirements.

Use:

- Reported
- Observed
- Validated
- Open
- Future signal

## Source

Project operating model established during scoping; current evidence updated from `CX Sharepoint Refresh (BLT)(2).pdf`.

## Bitbucket publishing configuration — verified 10 October 2026

**Scope:** CX SharePoint Refresh Bitbucket repository in the `jose-andr` Bitbucket workspace. Confirmed by José with screenshots of Bitbucket's workspace and repository variable settings. This is a configuration snapshot, not a claim that the pipeline is currently successful.

### Environment-variable ownership

| Bitbucket scope | Variable | Handling |
|---|---|---|
| Workspace → Pipelines → Workspace variables | `ATLASSIAN_SITE` | Shared; retained when an individual repository is deleted |
| Workspace → Pipelines → Workspace variables | `ATLASSIAN_EMAIL` | Shared; retained when an individual repository is deleted |
| Workspace → Pipelines → Workspace variables | `JIRA_PROJECT_KEY` | Shared; retained when an individual repository is deleted |
| Workspace → Pipelines → Workspace variables | `CONFLUENCE_SPACE_KEY` | Shared; retained when an individual repository is deleted |
| Repository → Pipelines → Repository variables | `ATLASSIAN_API_TOKEN` | Repository-specific secret; must be recreated after repository deletion/import, with **Secured** enabled |

**Do not store variable values, tokens or credentials in GitHub, Bitbucket YAML, or this documentation.** Workspace variables are not part of the repository export/import. Ensure that the existing workspace remains in place.

### Repository reset / GitHub import checklist

1. Preserve the existing `bitbucket-pipelines.yml` externally before deleting the Bitbucket repository. José reported this file has already been saved (10 October 2026).
2. Check for unmerged branches, pull requests, repository-specific permissions, webhooks and other settings before deletion. These have **not** been independently verified.
3. Confirm that a usable Atlassian API token can be retrieved from secure storage or replaced; a secured variable's value cannot simply be read back from the Bitbucket UI.
4. Recreate/import the repository from the maintained GitHub source: `jose-andr-cx-projects/cx-sharepoint-refresh`.
5. Verify the four **workspace** variables still exist; **do not recreate them as repository variables** unless there is a deliberate scope change.
6. Re-add only `ATLASSIAN_API_TOKEN` at the **repository** scope, marked **Secured**.
7. Restore `bitbucket-pipelines.yml` and review it before enabling/running pipelines. Avoid automatic Jira or Confluence writes until publication logic and permissions are validated.
8. Run a controlled publication test, check outcomes in Jira and Confluence, and record any failures or changes.

### Publishing workflow status

As of 10 October 2026, GitHub now versions both `bitbucket-pipelines.yml` and `scripts/publish_confluence.py`. The **current proposed pipeline** is manually triggered, has separate read-only validation and publish commands, requests lowercase `cex` and checks observed space ID `68452354`, and targets four existing `SP-Refresh` Confluence pages. It **does not create Jira records**. The previous all-in-one pipeline that created/reused a Jira Deliverable is superseded for this publishing route. **Read-only validation and the first controlled four-page publication both succeeded in Bitbucket on 10 October 2026 (build log screenshots). A post-publication visual/content review in Confluence is still outstanding.** Bitbucket's running copy may differ until the repository is synchronised from GitHub; don't assume a GitHub commit updates Bitbucket automatically.

**Boundary:** Bitbucket is the official controlled project repository and pipeline execution environment; Confluence and Jira are the organisational records for published knowledge and delivery. GitHub is a convenient collaboration mirror for ChatGPT-supported work and is not the organisational source of truth.


### Controlled publishing code

- Source-controlled files: `bitbucket-pipelines.yml` and `scripts/publish_confluence.py` in the GitHub mirror.
- Import or synchronise those same revisions into Bitbucket before running its pipelines. Do not maintain a separate edited Bitbucket-only version.
- Execute `validate-confluence-targets` first. Only after reviewing all four target matches and manual content changes should `publish-to-existing-confluence-pages` be run.
- Credentials remain exclusively in Bitbucket variables, never in repository files.


### Read-only validation evidence — 10 October 2026

Bitbucket `validate-confluence-targets` completed successfully (build log screenshot supplied by José):

- Requested URL key `cex`; Confluence API returned key `CS`, space ID `68452354`. The distinction is observed, not yet explained independently. Do not assume the two keys are interchangeable.
- All four existing target page mappings resolved uniquely under the returned space ID:

| Page | Validated ID |
|---|---|
| SP-Refresh - Project Management | `1575911428` |
| SP-Refresh - Discovery and Content Audit | `1576009731` |
| SP-Refresh - Experience and Content Design | `1577189386` |
| SP-Refresh - Scoping Playback | `1575845898` |

- Log concluded `READ-ONLY VALIDATION PASSED` and `No pages created or updated.`
- **Next gate:** Before any publishing run, confirm target-space ownership, ensure manual page edits are preserved or knowingly replaced, and explicitly approve publication. The mirrored script includes a `CONFLUENCE_TARGETS_APPROVED=true` publication gate; explicit user approval was given and the Bitbucket publishing command included this gate; the four API updates completed.
- Maintain the Bitbucket-tested implementation as operational authority. Sync validated changes into the GitHub collaboration mirror, not the other way around by default.


### Controlled publishing run — 10 October 2026

**Evidence:** User-supplied Bitbucket build log screenshot. The explicit publish command was `CONFLUENCE_TARGETS_APPROVED=true PUBLISH_MODE=publish python3 scripts/publish_confluence.py`.

- Confluence returned key `CS` and space ID `68452354`, matching the previously tested target ID.
- Preflight uniquely resolved all four mapped pages.
- The build reported `UPDATED` for page IDs `1575911428`, `1576009731`, `1577189386`, and `1575845898`.
- Final output: `Four existing pages updated. No Jira operations performed.`
- **Verified:** Pipeline reached four successful Confluence API update calls without a reported runtime failure. **Not yet verified:** visual presentation, content fidelity, completeness, links, formatting, or whether readers see the intended output. Review these in Confluence before treating publication quality as approved.
- **Operating rule:** Bitbucket remains the official publishing implementation and source. GitHub mirrors the tested implementation for collaboration. Keep the manual validation run before publishing; explicit `CONFLUENCE_TARGETS_APPROVED=true` enables the write step and must be used only following human approval.


### Reimport end-to-end test — 10 October 2026

**Evidence:** User-supplied Bitbucket pipeline build #1 screenshot after deleting/recreating the Bitbucket repository and importing from the GitHub collaboration mirror. **Result: Passed for import and publishing execution.**

- Bitbucket branch: `main`; displayed source commit: `5e8e39d` (*Refresh Experience and Content Design last-updated metadata*).
- Custom pipeline: `publish-to-existing-confluence-pages`; execution completed successfully in 21 seconds (observed screenshot).
- Execution used `CONFLUENCE_TARGETS_APPROVED=true PUBLISH_MODE=publish python3 scripts/publish_confluence.py`.
- Confirmed Confluence response: API key `CS`, space ID `68452354`.
- All four existing page targets resolved and successfully returned `UPDATED` in the build log:
  - Project Management: `1575911428` (30,796 HTML characters)
  - Discovery and Content Audit: `1576009731` (6,554 HTML characters)
  - Experience and Content Design: `1577189386` (21,622 HTML characters)
  - Scoping Playback: `1575845898` (2,910 HTML characters)
- Build reported: `Four existing pages updated; no Jira operations performed.`

**Boundary of verification:** This establishes that the recreated Bitbucket repository could execute the imported publishing files and update all four existing pages in Confluence. It does **not** independently confirm exact content fidelity, visual formatting, links, accessibility or that every published document's Last updated metadata was refreshed correctly. Check these separately in Confluence. The date-stamping GitHub workflow's automatic execution and future mirror synchronisation are also not demonstrated by this test.

**Architectural result:** Keep the current manual GitHub collaboration mirror → Bitbucket official repository → Confluence controlled publishing workflow. No further sync optimisation is required at this stage.
