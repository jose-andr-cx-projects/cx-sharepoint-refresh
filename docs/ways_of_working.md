# Ways of Working

Status: Draft  
Last updated: 30 September 2026

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

The preserved Bitbucket publishing pipeline is intended to read Markdown project docs and publish lightweight views to Confluence while creating or reusing a Jira Deliverable. Earlier execution encountered a Confluence-space-resolution problem involving `CONFLUENCE_SPACE_KEY`. **Publishing is not verified as fixed**. Do not mistake saved YAML, configured variables or a completed repository import for a validated migration.

**Boundary:** GitHub retains the maintained project Markdown mirror; Bitbucket provides the organisational pipeline/execution surface; Confluence and Jira remain the organisational systems for published documentation and delivery records, respectively.
