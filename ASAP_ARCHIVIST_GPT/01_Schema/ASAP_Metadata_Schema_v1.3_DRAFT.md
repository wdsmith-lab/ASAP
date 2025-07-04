# ASAP Metadata Schema – Version 1.3 (DRAFT)

**Status**: Draft  
**Date**: 2025-07-01  
**Maintainer**: ASAP Project Team  
**Notes**: This is a working draft for ASAP Metadata Schema v1.3. All fields are subject to review prior to locking.

---

## ✅ New or Revised Fields Proposed for v1.3

### `curator_notes` (optional)
- **Type**: `string`
- **Description**: Allows human curators to leave internal-facing commentary about rationale, known gaps, edge cases, or classification notes that are not appropriate for end-user-facing `Notes` fields.
- **Use Case**: Clarify why a livery pack is treated as a single mod but also a collection; explain known missing components in a mod pack; flag review logic.

---

## ✅ Full Field List (includes all fields from v1.2)

```json
[
  "asset_uid",
  "Asset ID",
  "Asset Title",
  "Mod Type",
  "Simulator",
  "Author",
  "Contributor(s)",
  "Initial Source URL",
  "Known Mirrors",
  "Upload Date",
  "Creation Year (Est.)",
  "Status",
  "License/Distribution Terms",
  "Description",
  "File Name",
  "File Type",
  "File Size",
  "Checksum (SHA256)",
  "File Structure Notes",
  "Duplicate Flag",
  "Extraction Test Status",
  "Tags",
  "Series / Era",
  "Region",
  "Vehicle Type",
  "Track Type",
  "External References",
  "Notes",
  "Submission Type",
  "Submitted By",
  "Contact Info (Internal)",
  "Is Collection",
  "Collection ID",
  "Collection Name",
  "Collection Author",
  "Contains Assets",
  "schema_version",
  "entry_version",
  "last_updated",
  "preservation_risk",
  "preservation_notes",
  "last_verified",
  "curator_notes"
]
```

---

*This document will be incrementally updated as more v1.3 candidate fields are proposed or confirmed.*

