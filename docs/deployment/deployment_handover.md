# CX SharePoint Refresh — Production Deployment and Handover

**Decision date:** 17 November 2026  
**Status:** Working production handover; publishing approvals, named owners and exact URLs must be confirmed.  
**Scope:** The SharePoint Refresh project. CoMpanion is a verification channel within this release, **not a separate deployment**.

## Three deployment components

1. **Document library files — uploaded.** The CX document batch is reported complete (26 resources). Production Verification Testing (PVT) covers file access, required metadata, permissions, links and **CoMpanion retrieval as one document-library PVT check**. Uploaded does not mean PVT passed.
2. **Refreshed CX webpages — awaiting production publication.** Run **CoMpanion UAT on current published webpages before cutover**, retain questions/responses/citations/URLs as the baseline, then repeat the *same* scenarios in **production PVT after publication**. This CoMpanion-specific UAT supplements, rather than replaces, the incremental page QA described in the 13 November checkpoint.
3. **AI instruction document — to finalise, approve and deploy.** Define CX page/offer navigation, authoritative source precedence, and an explicit **legacy-page exclusion register** with preferred new URLs. Verify its effects in PVT. An instruction file alone cannot guarantee suppression of indexed legacy pages.

## Simple publishing handover matrix

| ID | Component | Action and handover evidence | Gate / timing | Owner (confirm) | Status |
|---|---|---|---|---|---|
| 01 | Library | Publish 26 CX resources; retain 26-file register and document-set URL | Before webpage go-live | CX content owner | **Uploaded — PVT outstanding** |
| 02 | Library | PVT: required metadata, files/permissions/links; CoMpanion natural-language retrieval across **all 26** resources; record returned *document* citations and exceptions | Following upload | CX + publisher | Pending verification |
| 03 | Webpages | CoMpanion **UAT baseline** on existing published CX pages; save fixed prompts, answers, source URLs, scores, gaps | **Before** refreshed page deployment | CX project team | Pending |
| 04 | Webpages | Batch publish approved new CX pages; record exact URLs, editor/publisher, date, access and link checks | After approvals and baseline captured | Production publishing team / Jenny route | Pending |
| 05 | AI instruction | Approve and deploy authoritative source guidance and **old→new URL exclusion mapping** | At cutover; **before** CoMpanion webpage PVT | CX content owner + CoMpanion administrator | Pending |
| 06 | Webpages | **PVT:** repeat the *same* webpage UAT prompts; confirm refreshed URLs and correct guidance; check no legacy-page recommendations or citations | **After** production deployment | CX + publisher + CoMpanion admin | Pending |
| 07 | Legacy transition | Keep legacy pages live but out of CoMpanion recommendations; log failures and request source/index exclusions where instruction guidance fails | Go-live until retirement | Publisher + CoMpanion admin | Pending |
| 08 | Legacy transition | Archive legacy pages once dependencies, inbound links and permissions cleared; verify replacement pathways and record sign-off | **Within three weeks after go-live**, subject to approval | Intranet owner / publisher + CX content owner | Pending |

### Publishing pack — fields to complete at handover

- Production publish date/time: **TBC**
- Approved page titles and target URLs: **TBC / attach page register**
- Legacy URL → preferred refreshed URL mapping: **TBC / attach register**
- CX content approval / accountable owner: **TBC**
- Authorised SharePoint publisher and contact: **TBC**
- CoMpanion instruction file version, location, administrator: **TBC**
- CoMpanion webpage baseline evidence location: **TBC**
- Library 26-file register and PVT results: **TBC**
- Escalation / fallback process: **TBC**
- Release and archival sign-offs: **TBC**

## PVT rules and exception handling

**Library:** Count a CoMpanion document retrieval pass only when it cites the intended document (not a webpage-only answer), the citation opens for an authorised employee, and the answer is substantively relevant. Measure retrieval across the complete uploaded set; do not claim that PDF metadata *caused* retrieval without a controlled test. Distinguish embedded PDF metadata from populated SharePoint columns.

**Webpages:** Compare post-release results against saved pre-release CoMpanion UAT. Correct destination means the approved **new** CX page. Capture legacy citations, wrong source selection, broken links, access failures and inaccurate navigation as defects.

**AI instruction and coexistence:** The legacy pages will remain published for up to three weeks post go-live. The instruction document must explicitly tell CoMpanion to omit each affected legacy page, prefer its mapped replacement and avoid obsolete citations. Confirm actual behaviour in production. When instruction-only exclusion fails, escalate to CoMpanion administrator for index/knowledge-source controls; do **not** silently archive pages or assume instruction priority over retrieval.

**Archival:** Archive only using the authorised CoMWeb procedure after assessing inbound links, owner agreement, redirects/alternatives and employee impact. Record the actual date, exceptions and sign-off.

## Relationship to existing evidence

- `evidence/2026-11-13-go-live-checkpoint.md` records the earlier 18 November coordinated batch plan and incremental build QA; the present deployment decision adds **CoMpanion-specific** webpage UAT/PVT and temporary legacy-page instructions, without rewriting the historic checkpoint.
- `docs/content_governance_and_publishing_sop.md` remains the broader working standard, not an approved organisational policy.
- Confluence is for approved project narrative; Jira for tracked status; this GitHub file is a **staging mirror**, not proof of Bitbucket/Confluence/Jira sync.

**Decision:** SharePoint Refresh deployment has three components—library, webpages and AI instruction. CoMpanion document reading belongs to **library PVT**. Webpage CoMpanion **UAT precedes** refreshed-page deployment; matching **PVT follows** deployment. Explicit legacy-page avoidance is required while old pages remain published for the three-week archiving window.
