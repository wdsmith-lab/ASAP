# ARCHIVIST GPT – Schema Version Mismatch Policy

**Status**: Active  
**Adopted**: 2025-07-03  
**Location**: ARCHIVIST-CONSULTANT/Standards/Schema_Version_Mismatch_Policy.md  
**Maintainer**: ARCHIVIST-CONSULTANT

---

## 🎯 Purpose

This document outlines how ARCHIVIST GPT should respond when encountering metadata entries with a `schema_version` that differs from its internal active schema version.

---

## 📐 Internal Assumption

ARCHIVIST GPT currently assumes and operates with the latest locked schema:

```
schema_version: "1.2"
```

All entries are expected to match this version unless explicitly migrated or flagged.

---

## 🧭 Mismatch Detection & Behavior

ARCHIVIST checks the `schema_version` field (in JSON body or YAML frontmatter) and compares it to its internal schema.

| Mismatch Type | Action |
|---------------|--------|
| **Older version** (e.g. `v1.1`) | Warn user and offer to migrate to `v1.2` |
| **Newer version** (e.g. `v1.3`) | Warn user: unsupported schema – entry may not be safe to update |
| **Missing version** | Warn user and assume legacy structure – request confirmation or suggest validation |
| **Match (`v1.2`)** | Proceed normally without warning |

---

## ⚠️ GPT Behavior Summary

When version mismatch is detected:

```text
“This entry uses schema version v1.1, but I operate on v1.2. I can migrate it for you to preserve compatibility.”
```

Or:

```text
“This entry uses a newer schema version (v1.3) than I currently support. Please confirm compatibility or wait for an updated ARCHIVIST version.”
```

---

## 🧪 Modules That Should Implement Version Checks

- `create_metadata_entry`
- `update_metadata_entry`
- `validate_metadata_entry`

These modules should fail safe rather than corrupt schema-compliant entries.

---

## 🔧 Optional Override: `--force`

For automated workflows, the ARCHIVIST agent (or external tooling) may support a `--force` option to bypass version mismatch warnings.

This allows batch processing where strict enforcement would be overly rigid, but should be used with care.

---

This policy ensures safe evolution of the schema while allowing humans and tools to manage transitions between schema versions gracefully.
