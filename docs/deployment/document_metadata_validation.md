# Document library metadata and CoMpanion PVT — validation note

**Recorded:** 17 November 2026. **Source:** user-confirmed upload and CoMpanion retrieval tests; not a SharePoint export.

## Scope

A batch of **26 CX files** was reported prepared and uploaded to the CX Intranet Document Set on 16 November 2026. Includes CX Branch Playbook, service/customer research reports, CXVoices guidance, and Segments and Modes resources. Confirm actual file count, final file names, permissions, and publication approval using the authoritative SharePoint register.

## Publishing metadata working conventions

- Employee-oriented descriptive file names; avoid duplicate copies and misleading `FINAL`/`v2` suffixes.
- Clear **Description** (SharePoint field) for purpose and when to use; intended <=255 characters in the working approach.
- Search-oriented **Keywords**, employee terms, synonyms and relevant topic vocabulary; intended <=255 characters pending confirmation of field configuration.
- Use existing SharePoint **Resource Type** choices, not invented taxonomy. Controlled values previously identified: Briefs; Checklist; GPA; Manual; Meetings; Performance; Policy; Position Description; Presentation; Procedure; Publication; Reference; Specification; Surveys; Toolkit; Working Notes.
- Collection tag: **Segments and Modes**; where applicable, customer group and mode subtopic terms.
- **Embedded PDF Title/Subject/Keywords do not automatically populate SharePoint library columns.** Validate both layers separately. Confirm inheritance of Division and Branch from the Document Set.
- The earlier customer segments source was identified as **Draft and Confidential**; check publication permissions and content approval independently of retrieval success.

These are working rules and observations, not evidence the exact fields are configured or already populated for every file. The approved CSV/register and current SOP remain the source for individual metadata values.

## Post-upload CoMpanion observations (not a causal metadata test)

- **T01 — CX branch help:** CoMpanion cited `Customer Experience Branch Playbook.pdf` at `CoMWeb/Shared Documents/Customer Experience/`; an observed 7/8 quality score was discussed. PDF internal keywords match the new metadata, but SharePoint version 7.0 and embedded 2025 creation dates **do not establish when it was indexed**. Keep T01 as post-upload diagnostic rather than clean pre-upload baseline.
- **T02 — customer segments:** CoMpanion cited `Segments and Modes - Playbook.pdf`, `Segments and Modes - Introduction.pdf`, and `Customer Segments - Overview.pdf`; observed 7/8, with citation destination verification outstanding.
- These results demonstrate *findability in live CoMpanion responses*, **not** that Description or Keywords themselves caused retrieval. Body text, filenames, metadata and indexing may all contribute.

## Library PVT — within SharePoint Refresh deployment

Run **one natural-language retrieval scenario for each of 26 uploaded documents**, recording the exact question, expected filename, CoMpanion answer, actual source URL, pass/partial/fail, and issues. PVT also checks that files open for intended staff, SharePoint columns match approved register, library links resolve, and confidential material is permissioned appropriately. Webpage-only answers are **not passes** for file-specific PVT.

The webpage CoMpanion **UAT baseline** and **post-deployment PVT** are separate activities under the webpage component of the SharePoint release (see `deployment_handover.md`). Do not use the earlier 8-question generic baseline as evidence of a pre-document-upload state.
