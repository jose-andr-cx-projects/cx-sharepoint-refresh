# CX SharePoint Refresh — 18 November 2026 go-live page-export verification

**Reported cutover:** 18 November 2026 at 10:30am Melbourne time (user-confirmed; publisher/system audit not attached).
**Scope:** Seven supplied SharePoint HTML page exports.
**Evidence type:** Static saved page configuration including embedded CanvasContent1. This is NOT a browser or CoMpanion PVT session.
**Overall result:** Structural inspection completed; functional PVT remains pending.

## Seven supplied pages
1. Customer Experience (L1)
2. Understand who our customers are
3. Act on customer data and feedback
4. Improve your service for customers
5. Get training and grow your skills
6. Get help delivering customer service
7. Connect with the CX team

The seven exports contained 52 editorial-card configurations and 30 page quick-link destinations that matched the seven-page set (counts of configured instances, not independent successful click tests). Production URL strings and content blocks were extracted for all seven. These observations do not prove publication visibility, performance, accessibility, permissions or working destinations.

## PVT status by control

| Control | Status | Evidence / gap |
|---|---|---|
| Seven supplied page payloads | Static inspection complete | Seven unique title/page combinations, embedded page content |
| Page publication / access | User-reported go-live; independent PVT pending | Capture publisher confirmation and authorised employee open test |
| Quick links and editorial actions | Configured; click PVT pending | Test each link in browser with intended access profile |
| CoMpanion page routing | PVT pending | Repeat pre-cutover UAT prompts; record answer, source citation and URL |
| Legacy-page suppression | PVT pending | Approved old-to-new mapping and actual index/instruction behaviour missing |
| CX library 26-file retrieval | PVT pending | Existing 17 Nov evidence is diagnostic, not a 26/26 verification |
| CoMpanion guide deployment | Draft prepared, approval/deployment unverified | CX content owner and admin to confirm version and applied knowledge source |

## AI navigation guide status

A full working navigation guide was generated from the seven supplied exports on 18 Nov 2026. It includes source URLs, employee-intent routing, editorial destinations and seven suggested test questions; **it remains a draft**. Do not import the document or any controlled SharePoint configuration into a public repository without an organisational approval and classification check. Keep the approved operational guide in the authorised organisational knowledge source.

## Next verification sequence

1. Validate page opening/access and each configured link; record time, tester, expected vs actual URL, pass/partial/fail.
2. Approve and deploy the CoMpanion navigation guide including the exact approved legacy→new URL exclusion register.
3. Re-run the saved baseline questions, including correct source citations and legacy-page avoidance.
4. Complete the independent 26-document library checks (metadata, permissions, openable citations).
5. Confirm sign-off and record actual outcomes in Jira/Confluence, then reconcile with the authorised Bitbucket source.

**Source boundary:** CoMWeb/SharePoint, CoMpanion runtime, Jira and approved organisational records govern actual release and PVT truth. This GitHub file is staging evidence only, NOT proof of Bitbucket sync, Confluence publication, PVT sign-off or CoMpanion deployment.


## T0 — Page Analytics capture (18 November 2026)

**Evidence:** Eight user-supplied screenshots of SharePoint Page Analytics: one CoMWeb site homepage and seven refreshed CX pages. All screenshots have the **Last 7 days** filter selected and display 12–18 November 2026. **T0 is a mixed pre-/post-cutover snapshot**, not a clean first-week production performance measure, because the reported cutover was 18 November at 10:30am AEDT.

| Page | Unique viewers, last 7 days | Total views, last 7 days | Average time per user |
|---|---:|---:|---:|
| CoMWeb homepage (context/control, not a CX page) | Not reliably captured as a period total; 1.2K tooltip for 12 Nov UTC | 23K (rounded) | 8m 36s |
| Customer Experience (CX L1) | 15 | 58 | 2m 26s |
| Understand who our customers are | 5 | 39 | 3m 19s |
| Act on customer data and feedback | 5 | 64 | 3m 42s |
| Get training and grow your skills | 5 | 32 | 5m 07s |
| Get help delivering customer service | 5 | 34 | 3m 44s |
| Connect with the CX team | 5 | 50 | 4m 11s |
| Improve your service for customers | 5 | 33 | 4m 44s |
| **Seven CX pages combined (page-instance sum)** | **45** | **310** | **Do not sum/average without visit-level weights** |

**Interpretation controls:**
- The 45 unique-viewer figure is a sum of page-level values, **not 45 distinct people across the seven-page experience**; cross-page users can be counted multiple times.
- The CoMWeb 1.2K tooltip is tied to **Thursday 12 November 2026 UTC**, not established as the overall last-seven-days unique-viewer total. Homepage total views are rounded (23K), so avoid precise site-to-CX percentage comparisons.
- Page Analytics shows increases against the preceding seven days for several pages, but pre-launch preview/editor/test activity may be present. Do not interpret those percentage movements, high views per viewer, or time-on-page as launch success or employee task completion.
- Analytics is **usage context**, not publication approval, functional PVT, accessibility testing, correct-link validation or CoMpanion routing validation.
- All screenshots were captured in the **SharePoint edit-mode interface**; actual employee-access checks still require non-editor verification.

**Next comparable measurement:** Capture a complete post-launch seven-day window on **25 November 2026** (or later once the reporting window excludes pre-launch activity), retaining matching filters and the same eight page definitions. Check unique viewers, total views, per-page engagement, and — where instrumentation permits — journeys from CoMWeb to CX pages and onwards to authoritative resources. Mark CoMWeb-to-CX discovery as an **aspirational metric**, not measurable from the supplied screenshots alone.

**Status:** Analytics evidence recorded; no page analytics result constitutes functional PVT pass or CoMpanion deployment verification.

## CoMpanion guidance revision — official public website precedence (18 November 2026)

**Decision/request:** CoMpanion has access to the official City of Melbourne public website at https://www.melbourne.vic.gov.au/. For customer-facing facts, including Contact Centre and other service opening hours, public holiday exceptions, after-hours support, emergency council reporting, online self-service availability, and service-specific requirements, the guidance now directs CoMpanion to check the **current relevant official public page first** and cite its exact URL.

**Routing boundary:** Public website = customer-facing service facts; refreshed internal CX pages = CX navigation; authorised internal operational sources = staff instructions, mailroom procedures, confidential escalation numbers and rosters. The public website does not replace internal operating instructions. If sources conflict, flag the discrepancy for CX review rather than silently propagating stale hours.

**Safeguards:** Distinguish phone service hours from venue hours and online transaction availability; check exceptions; do not infer universal opening hours from an old publication or claim that 24/7 digital reporting equals 24/7 staffed response. For immediate emergencies use 000; for council-specific urgent issues consult the current official service-specific pathway.

**Artefact:** A revised operational CoMpanion guide was prepared outside the public GitHub staging mirror as `CoMpanion_CX_navigation_guide_PUBLIC_SOURCE_PRIORITY_2026-11-18.md`. It remains subject to CX owner approval, CoMpanion administrator deployment and production PVT. Public GitHub retains this decision and source-routing rule only, not the full internal operational guide.

**Suggested PVT:** Ask for current contact hours, a public holiday exception, after-hours urgent council reporting, an available online transaction and internal mailroom hours. Record the page/URL cited, correct public-vs-internal source, date, answer and pass/partial/fail.

## CoMpanion operating-hours snapshot — 18 November 2026

**Evidence:** Two user-supplied screenshots (one public City of Melbourne contact section, one internal mailroom section). These are source snapshots, not a standing guarantee of future hours. Exact employee-operational details belong in the authorised CoMpanion knowledge guide, not a public repo mirror.

**Public contact snapshot:**
- Telephone: 03 9658 9658; staffed Monday–Friday 7:30am–6:00pm, excluding public holidays.
- Melbourne Town Hall Customer Service Centre: 120 Swanston Street; Monday–Friday 8:30am–5:00pm, excluding public holidays.
- Postal address: GPO Box 1603, Melbourne VIC 3001.
- Accessibility: National Relay Service TTY 133 677, or speech assistance 1300 555 727, then request 03 9658 9658.

**Internal service snapshot:** Mailroom details and contact channels were supplied separately for inclusion in the controlled operational guide, with distinct hours and source precedence. Do not conflate public mailing address, Town Hall counter, telephone centre and internal mailroom.

**Guidance change:** The working CoMpanion knowledge guide now gives screenshot-confirmed contact hours directly, but the current relevant official public website overrides dated customer-facing values. The internal mailroom owner/system overrides dated internal information. For urgent council after-hours enquiries, check the specific official public-service pathway. Immediate emergency: 000.

**Deployment status:** Working guide prepared as `CoMpanion_CX_navigation_guide_VERIFIED_CONTACT_HOURS_2026-11-18.md`; approval, deployment and production scenario PVT remain unverified.

## Evidence reconciliation — 24 November 2026

Seven-page static inspection is complete for the supplied exports, not functional PVT. Two earlier CoMpanion document retrieval observations (T01/T02, each reported 7/8) are recorded in [library validation](document_metadata_validation.md); they do not establish webpage UAT/PVT or 26/26 library coverage. User continuity reports library testing activity completed, but no item-level result register or acceptance evidence was supplied for this reconciliation; retain full coverage as unverified. The team test script is a proposed scenario set, not execution evidence. For closure, reconcile actual per-item results, citation/permission checks, guide deployment and authorised employee page testing in organisational systems. Record pass/partial/fail/not tested, evidence date, owner and defect reference. T1 is due on/after 25 November, not yet established.
