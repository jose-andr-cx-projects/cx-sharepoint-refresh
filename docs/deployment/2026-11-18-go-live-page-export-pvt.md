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
