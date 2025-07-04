
# ASAP Metadata Schema v1.1 (Locked)

**Version**: 1.1  
**Status**: Superseded  
**Anchored**: PMB:PHASE-1 (Adam)  
**Scope**: ASAP:AC – Initial Implementation

---

## Core Fields

### Identification
- **title**: Main name of the mod (string)
- **version**: Release version or tag (string, optional)
- **type**: 'car', 'track', 'collection' (string, controlled vocabulary)

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
- **files**: List of files in archive (optional for now)

### Context & Classification
- **era**: Decade or period (e.g. '1960s', 'Modern')
- **class**: GT, F1, Prototype, etc. (string or list)
- **country**: Country of origin (string or list)
- **track_type**: Permanent, Temporary, Hillclimb, etc. (for tracks only)

### Rich Context & Notes
- **description**: General overview or detailed history (string)
- **notes**: Informal but helpful notes, e.g. “Working AI line exists” or “Conflicting claims of authorship”
- **media**: Links to videos, images, showcase articles (string or list)

---

## Extension Fields (Future-Ready but Optional)

- **collection_id**: ID to indicate which collection (if any) this asset belongs to
- **initial_seed**: Boolean or tag to indicate if this was part of original human-fed archive construction
- **enhancements**: List of submods or enhancements (e.g. sound packs, liveries)
- **redistributable**: Flag based on known rights status (true/false/unknown)

---

## Notes
- Controlled vocabularies should be enforced for fields like `type`, `class`, `track_type`, `country`, `era` where applicable.
- Future extension: Community metadata layer, cross-linking, and deprecated asset lineage.

---

*This schema is locked and versioned as part of PHASE-1 (Adam) under the ASAP Vault Initiative.*
