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

## Official publishing workflow — verified 10 October 2026

**Official workflow:** Bitbucket is the controlled project repository and execution platform; Confluence holds project documentation; Jira holds delivery work, ownership and status. The current publishing pipeline updates Confluence only.

### Configuration and secrets

| Scope | Variable | Purpose |
|---|---|---|
| Workspace | `ATLASSIAN_SITE` | Atlassian site URL |
| Workspace | `ATLASSIAN_EMAIL` | Integration account |
| Workspace | `JIRA_PROJECT_KEY` | Jira project configuration |
| Workspace | `CONFLUENCE_SPACE_KEY` | Space lookup identifier (`cex`) |
| Workspace or repository | `ATLASSIAN_API_TOKEN` | Authentication; must be **Secured** |

Use the variable scope actually configured in Bitbucket. Never include credentials or secret values in files or logs.

### Manual publishing controls

- `bitbucket-pipelines.yml` offers `validate-confluence-targets` (read-only) and `publish-to-existing-confluence-pages` (write operation).
- `scripts/publish_confluence.py` verifies space, page targets and source documents before any writes.
- Publishing replaces full page bodies and requires explicit approval: `CONFLUENCE_TARGETS_APPROVED=true`.
- Do not publish until validation succeeds and any manual edits worth keeping have been preserved.
- After publishing, check that headings, links, accessibility, `Last updated` metadata and page content display correctly.
- Do not add collaboration-only explanations or unofficial workflow descriptions to project documentation. The publishing preflight checks for this content and stops before writing.

### Target Confluence space and pages

The API returned space key `CS` and space ID `68452354` using the configured lookup `cex`. This discrepancy was observed during execution; don't assume these keys are interchangeable in other applications.

| Existing Confluence page | Verified page ID |
|---|---|
| SP-Refresh - Project Management | `1575911428` |
| SP-Refresh - Discovery and Content Audit | `1576009731` |
| SP-Refresh - Experience and Content Design | `1577189386` |
| SP-Refresh - Scoping Playback | `1575845898` |

### Execution evidence — 10 October 2026

Read-only validation resolved all four pages with no writes. Approved publication updated all four pages without creating or modifying Jira records. An additional import and execution test (Bitbucket build #1, 21 seconds) again updated all four pages. These results establish successful API publication, not a completed review of formatting, content fidelity or accessibility.

**Ongoing rule:** Bitbucket, Confluence and Jira are the only platforms named in the official publishing workflow. Project documentation must describe actual organisational processes, not informal editing arrangements.
