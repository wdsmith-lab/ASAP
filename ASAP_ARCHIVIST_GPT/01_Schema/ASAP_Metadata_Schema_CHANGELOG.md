---
title: ASAP Metadata Schema Changelog
status: active
last_updated: '2025-07-03'
---

# ASAP Metadata Schema – Changelog

## [v1.2] – Finalized

**Date**: 2025-06-30  
**Status**: Final  
**Summary**:
- Finalized field list for ASAP_Metadata_Schema_v1.2
- Added forward-compatible fields:
  - `schema_version` (declares schema used by metadata entries)
  - `last_updated` (supports hygiene, update tracking)
  - `entry_version` (permits version tracking of entry itself)
- Declared schema-level metadata block for tooling compatibility

### 2025-06-30 – Schema v1.2 Finalization Confirmed

- Confirmed Schema v1.2 as final
- Added guidance fields: `schema_version`, `last_updated`, `entry_version`
- Reconciled all field-level guidance into a single document:
  ASAP_Metadata_Field_Level_Guidance_Table_v1.2.md` (supersedes both prior versions)