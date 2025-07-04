# ASAP Metadata Field Level Guidance Table

**Version**: 1.2  
**Status**: Final  
**Date Finalized**: 2025-06-30

This document provides detailed field-level instructions for how ARCHIVIST GPT should interpret, validate, and assist with the ASAP Metadata Schema.

---
# ARCHIVIST Field-Level Guidance Table

This table defines how the ARCHIVIST GPT should understand, handle, and generate values for each field in the ASAP_Metadata_Schema_v1.2.

---

## Core Fields

| Field              | Type           | Required       | Description                                   | Guidance                                                                                                                      |
| ------------------ | -------------- | -------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `asset_uid`        | string         | ✅              | Globally unique identifier for metadata entry | Required for linking, cross-referencing, and integrity. GPT may generate using deterministic naming or flag for curator input |
| `title`            | string         | ✅              | Asset's display name                          | Extract or generate clearly, never infer loosely                                                                              |
| `version`          | string         | Optional       | Release or revision tag                       | Use if explicitly stated                                                                                                      |
| `type`             | enum           | ✅              | Mod classification (`car`, `track`, etc.)     | Use strict vocab (`car`, `track`, `collection`, `livery`, etc.)                                                               |
| `author`           | string or list | ✅              | Original creator(s)                           | Must be grounded in source; don’t hallucinate                                                                                 |
| `converted_by`     | string or list | Optional       | Porter or adaptor (if applicable)             | Only populate if stated                                                                                                       |
| `origin_sim`       | string         | Optional       | Simulator of original asset                   | Use when mod is a port                                                                                                        |
| `based_on`         | string or list | Optional       | Source lineage                                | Link to parent mod ID or name                                                                                                 |
| `influenced_by`    | string or list | Optional       | Inspirations                                  | Use where stated (e.g. “inspired by x”)                                                                                       |
| `source_url`       | string or list | ✅              | Where discovered                              | Must be linkable, include original thread if possible                                                                         |
| `download_url`     | string or list | Optional       | Working mirrors or links                      | Must be verifiable; multiple preferred                                                                                        |
| `submission_notes` | string         | Optional       | Curation context                              | Use for archivist commentary or submission context                                                                            |
| `submitted_by`     | string/email   | Optional       | User/curator name                             | GPT should not invent this                                                                                                    |
| `tags`             | list           | ✅              | Classifiers (e.g. “Le Mans”, “WIP”)           | Generate based on structured understanding                                                                                    |
| `file_name`        | string         | ✅              | Archive name                                  | Use source file or inferred from link when obvious                                                                            |
| `checksum_sha256`  | string         | ✅ if available | File integrity hash                           | Leave blank or flag if unknown                                                                                                |
| `checksum_md5`     | string         | Optional       | Secondary hash                                | Optional fallback                                                                                                             |
| `files`            | list           | Optional       | File manifest                                 | Only used in extended contexts                                                                                                |
| `file_test_status` | enum           | Optional       | Archive extraction success                    | Accept curator QA input or flag for manual check                                                                              |
| `duplicate_flag`   | enum           | Optional       | Degree of overlap with known mods             | Do not generate; flag only if curator provides                                                                                |
| `era`              | string         | ✅              | Historical time frame (e.g. “1980s”)          | Infer based on vehicle context                                                                                                |
| `class`            | string or list | ✅              | GT, F1, etc.                                  | Use sim/racing vocab                                                                                                          |
| `country`          | string or list | ✅              | National origin                               | Use origin of car/mod or context                                                                                              |
| `track_type`       | string         | Optional       | Track classification                          | Required only for track mods                                                                                                  |
| `description`      | string         | ✅              | Summary of asset                              | Generate in neutral, informative style                                                                                        |
| `notes`            | string         | Optional       | Contextual insight or warnings                | Use freely for curator-friendly commentary                                                                                    |
| `media`            | string or list | Optional       | Images, showcase links                        | Include when links found or embedded in source                                                                                |

---

## Extension Fields

| Field               | Type    | Required | Description                             | Guidance                                    |
| ------------------- | ------- | -------- | --------------------------------------- | ------------------------------------------- |
| `is_collection`     | boolean | Optional | Whether this is a collection            | Flag automatically if `type == collection`  |
| `collection_id`     | string  | Optional | Parent collection ID                    | Populate if asset is part of a known pack   |
| `contains_assets`   | list    | Optional | Child asset IDs                         | Populate from verified entries or structure |
| `collection_author` | string  | Optional | Curator of pack                         | Use if stated, not inferred                 |
| `related_assets`    | list    | Optional | Related mod IDs                         | Link only when known                        |
| `submission_type`   | string  | Optional | `initial_seed`, `user_submission`, etc. | Choose from list                            |
| `redistributable`   | enum    | Optional | Rights status                           | `explicit`, `unclear`, `no`, `open-license` |
| `contact_internal`  | string  | Internal | Curator contact info                    | Not for GPT to generate                     |

---

## Preservation Fields

| Field                | Type   | Required | Description               | Guidance                                            |
| -------------------- | ------ | -------- | ------------------------- | --------------------------------------------------- |
| `preservation_risk`  | enum   | ✅        | `very low` → `extinct`    | Infer based on number of links or stated volatility |
| `preservation_notes` | string | Optional | Justification/context     | Use curator logic                                   |
| `last_verified`      | date   | Optional | Date of last mirror check | GPT should not guess; leave blank or flag           |
