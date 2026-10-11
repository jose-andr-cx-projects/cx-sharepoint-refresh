# Ways of Working

Status: Draft  
Last updated: 12 October 2026

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

## Operating-model adjustment — 12 October 2026

**Status: adopted for project reporting; review at retrospective.**

### Original intent and observed shift

The original scoping model above treated Jira as the team's active sprint board, with stories/tasks representing day-to-day delivery. In practice, the team coordinates work through workshops, Miro, Figma, Teams and delivery conversations rather than consistently updating Jira. This is an observed way-of-working adjustment, not a judgement that the team has failed to adopt a required process.

For the remainder of the refresh, **Jira is the lightweight project progress and milestone record**, not a duplicate task board. Keep the original model above as the historical baseline for retrospective comparison. Do not rewrite historical tickets to imply daily Jira usage.

### Revised responsibilities

| Surface | Operating use after 12 October |
|---|---|
| Jira | Epics and selected outcome-level tickets; evidence-linked progress, unresolved dependencies and phase visibility; Project Manager maintains reconciliation |
| Confluence | Authoritative project narrative: scope, research, decisions, designs, evidence, outcomes, risks and governance; show related Jira keys |
| GitHub project repository | Versioned Markdown source for project documentation and Confluence publication pipeline; include Jira keys in relevant sections |
| Miro / Figma | Actual collaborative synthesis and design work; link relevant outputs from Confluence rather than duplicate |
| Teams / workshops | Day-to-day coordination and decisions; material outcomes transferred to the appropriate authoritative document |
| SharePoint | Published employee-facing experience |

### Two-way traceability convention

- In each relevant Confluence section, add a short **Jira tracking** line with the existing key(s), e.g. `CFT-2982`. Use ordinary Jira issue links when the confirmed Jira base URL is known; do not guess URLs or issue numbers.
- In each corresponding Jira issue, add a link to its authoritative Confluence page/section (and supporting Miro/Figma artefact only when necessary), a concise evidence/outcome statement, and an outstanding gap if any.
- Keep Jira issue titles and status transitions aligned to *the actual acceptance criteria*. Creating a document or defining a method does not prove the underlying inventory, feasibility test or agreement is complete.
- Do not automatically close an epic because several constituent tickets have closed. Record the remaining outcome-level gap.
- During the next Confluence publication run, verify the Jira tracking lines survive Markdown-to-Confluence transformation. GitHub updates alone do not demonstrate that Confluence has synchronised.

### Retrospective questions

1. Did maintaining Jira as an evidence-led milestone view provide adequate leadership visibility?
2. How much administrative effort did we avoid compared with managing every activity in Jira?
3. Where did the absence of live ticket updates lead to uncertainty or missing accountability?
4. Were Jira-to-Confluence links accurate, reciprocal and worth maintaining?
5. Which minimum practices should be kept for future CX projects?

### Change record

- **10 October:** documented intent — Jira manages active delivery.
- **12 October:** operational shift — the team uses collaborative tools to deliver; Project Manager retrospectively reconciles Jira against verified project evidence. Test this lighter model through the next delivery phase and review at retrospective.
