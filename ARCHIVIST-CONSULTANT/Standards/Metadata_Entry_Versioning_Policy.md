# Metadata Entry Versioning & Changelog Policy

**Status**: Active  
**Adopted**: 2025-07-03  
**Maintainer**: ARCHIVIST-CONSULTANT  
**Location**: ARCHIVIST-CONSULTANT/Standards/Metadata_Entry_Versioning_Policy.md

---

## 🔢 Versioning Fields in Use

| Field             | Purpose |
|------------------|---------|
| `entry_version`  | Describes the version of the metadata record itself |
| `schema_version` | Locks the entry to the version of the schema used at time of creation |
| `last_updated`   | ISO 8601 date of most recent modification to the metadata record |

---

## 📐 `entry_version` Policy

ARCHIVIST follows a simplified semantic versioning pattern:

- `v1.0`: Initial entry creation
- `v1.0 → v1.1`: Minor corrections (e.g., mirrors, spelling, formatting)
- `v1.1 → v2.0`: Major field changes, schema migrations, authorship revisions

Patch-level versions (e.g., `v1.0.1`) are supported if needed but not required for basic use.

---

## 🕓 `last_updated` Policy

This field must reflect the actual last time the metadata record was edited.  
All changes — major or minor — should update this date.

Format: `YYYY-MM-DD`

---

## 🧾 `schema_version`

Frozen at time of entry creation. Updated only via manual schema migration and version bump.

---

## 🧠 Changelog Support (Optional)

Each entry may optionally include a `changelog` field structured as a list:

```json
"changelog": [
  {
    "version": "v1.1",
    "date": "2025-07-03",
    "author": "WillDeeEss",
    "note": "Added new mirror and fixed license formatting"
  },
  {
    "version": "v1.0",
    "date": "2025-06-28",
    "author": "ARCHIVIST",
    "note": "Initial entry created via GPT module"
  }
]
```

This is intended for human readability and future scripting.  
Prompt modules should not generate this by default, but may do so when explicitly requested.

---

## 🔒 Version Enforcement

While schema version and status are enforced externally, prompt modules should honor the versioning pattern above when:
- Editing metadata entries
- Generating new ones with reference to older records
- Performing summaries that touch on archival evolution

