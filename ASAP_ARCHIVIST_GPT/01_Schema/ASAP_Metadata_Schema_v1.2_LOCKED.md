---
title: ASAP Metadata Schema
schema_version: '1.2'
status: locked
last_updated: '2025-07-03'
---

# ASAP Metadata Schema – Version 1.2

**Schema Version**: 1.2  
**Status**: ✅ Locked  
**Scope**: All supported simulators (Assetto Corsa, rFactor, AMS, GPL, etc.)
**Date Finalized**: 2025-06-30  
**Maintained by**: ASAP Project Team  
**Notes**: This is the official, locked version of the ASAP Metadata Schema v1.2.  
Any future changes must be proposed through schema versioning procedures.

---
# ASAP Metadata Schema

## Core Fields

### Identification
- **asset_uid**: Required string. Globally unique identifier for this metadata entry. Used for cross-linking, version tracking, and local asset mapping. Stable across schema versions.
- **title**: Main name of the mod (string)
- **version**: Release version or tag (string, optional)
- **type**: 'car', 'track', 'collection', 'livery', 'soundpack', 'physics mod' (controlled vocabulary)

### Authors & Provenance
- **author**: Original creator(s) (string or list)
- **converted_by**: If applicable, who ported or adapted the mod (string or list, optional)
- **origin_sim**: Original simulation platform the mod was based on (string, optional)

### Genealogy
- **based_on**: Links or references to previous mods/assets this derives from (string or list, optional)
- **influenced_by**: Additional inspiration sources (string or list, optional)

### Acquisition & Discovery
- **source_url**: Where the asset/mod was discovered (string or list)
- **download_url**: Direct link or location if available (string or list)
- **submission_notes**: Human-submitted background information (string, optional)
- **submitted_by**: Who submitted this info (name/alias/email, optional)
- **tags**: List of classification tags (list of strings)

### File Data & Validation
- **file_name**: Name of the archive or directory structure
- **checksum_sha256**: Primary SHA256 hash (string)
- **checksum_md5**: (optional) Secondary hash
- **files**: List of files in archive (optional)
- **file_test_status**: 'passed', 'partial', 'failed', 'not tested' (enum)
- **duplicate_flag**: 'no', 'partial', 'yes', 'unclear' (enum)

### Context & Classification
- **era**: Decade or period (e.g. '1960s', 'Modern')
- **class**: GT, F1, Prototype, etc. (string or list)
- **country**: Country of origin (string or list)
- **track_type**: Permanent, Temporary, Hillclimb, etc. (for tracks only)

### Rich Context & Notes
- **description**: General overview or detailed history (string)
- **notes**: Informal but helpful notes
- **media**: Links to videos, images, showcase articles (string or list)

---

## Extension & Collection Fields

- **is_collection**: Boolean flag
- **collection_id**: ID to indicate which collection (if any) this asset belongs to
- **contains_assets**: List of asset IDs included in this collection
- **collection_author**: Author or compiler of the collection
- **related_assets**: List of other directly related asset IDs
- **submission_type**: 'initial_seed', 'user_submission', 'archive_discovery', etc.
- **redistributable**: 'explicit', 'unclear', 'no', 'open-license' (enum)
- **contact_internal**: Internal curator contact info

---

## Preservation

- **preservation_risk**: 'very low', 'low', 'moderate', 'high', 'very high', 'extinct' (enum)  
  Likelihood that the asset will become unavailable online without intervention.
- **preservation_notes**: Optional notes regarding why the asset is at risk or recovery observations.
- **last_verified**: Date (YYYY-MM-DD) the availability of sources was last manually or automatically confirmed.

---

## 🔧 Forward-Compatible Metadata Fields

### `schema_version`
- **Description**: Declares which version of the metadata schema this entry conforms to.
- **Format**: String
- **Example**: `"1.2"`

### `last_updated`
- **Description**: The date this metadata entry was last modified or updated.
- **Format**: ISO date string (YYYY-MM-DD)
- **Example**: `2025-06-30`

### `entry_version`
- **Description**: Version identifier for the metadata entry itself. Starts at v1.0 and should increment with each significant update.
- **Format**: String
- **Example**: `"v1.0"`
---

✅ **LOCKED VERSION** – No further edits permitted.  
For schema change requests, initiate a new schema draft (v1.3 or later) and document in the changelog.
