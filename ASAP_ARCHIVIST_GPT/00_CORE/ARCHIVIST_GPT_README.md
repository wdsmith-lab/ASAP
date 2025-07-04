# ARCHIVIST GPT – Project Readme

**Version**: v1.0  
**Status**: Active  
**Maintainer**: WillDeeEss  
**Location**: 00_CORE/ARCHIVIST_GPT_README.md  
**Date**: 2025-07-01  

---

## 📌 Purpose & Scope

`ARCHIVIST-GPT` is a specialized GPT agent designed to generate, update, summarize, and manage structured metadata entries for sim racing mods across multiple platforms — starting with Assetto Corsa, and eventually extending to rFactor, Automobilista, Grand Prix Legends, and others.

Its function is archival in nature: to help preserve at-risk or scattered sim racing mods with meaningful, schema-compliant entries in the ASAP metadata archive.

---

## 🧠 Core Behaviors

ARCHIVIST operates under strict schema alignment and structured prompt module logic:

- Validates all entries against ASAP Metadata Schema (currently v1.2)
- Applies preservation-aware logic (e.g., risk inference, license tagging)
- Distinguishes between mod types: Cars, Tracks, Liveries, Collections, etc.
- Operates in cooperation with TECHNICAL-CONSULTANT and CONSULTANT

ARCHIVIST is schema-aware but not schema-defining.

---

## 🧩 Prompt Modules

| Prompt Module              | Description |
|---------------------------|-------------|
| `create_metadata_entry`   | Generates a full metadata entry from a user-supplied mod description |
| `lookup_metadata_entry`   | Retrieves a metadata entry from the archive using a unique asset ID |
| `update_metadata_entry`   | Applies a patch or update to an existing entry using UID and field data |
| `assist_with_field`       | Suggests a value for a missing field based on known context |
| `extract_from_text`       | Parses raw text (forum posts, readmes) to extract metadata |
| `summarize_metadata_entry`| Outputs a narrative-style mod summary based on existing metadata |
| `validate_metadata_entry` | Checks an entry for schema compliance and required fields |

Prompt modules are stored in `03_Prompt_Modules/` and documented individually.

---

## 🧪 Testing & Examples

Test prompts for each module live in:

📂 `04_Tests/Prompt_Module_Examples/`

Each test includes:
- ✅ Input prompt
- ✅ Expected output
- ✅ Module and schema version
- ✅ Commentary on expected behavior

These can be used to regression test future ARCHIVIST versions or validate vault compliance.

---

## ⚠️ Limitations (v1.0)

- Metadata schema locking must be enforced externally (no in-GPT enforcement)
- No database connection or automatic entry persistence (yet)
- Simulator support is Assetto Corsa-focused during early phases
- No native schema drift detection
- Entry versioning is manual

---

## 📎 Recommended Companion Roles

- `ASAP_TECHNICAL-CONSULTANT` for scripting and schema tooling
- `ASAP_ARCHIVIST-CONSULTANT` (this role) for development design and documentation


---

## 📘 YAML Frontmatter (New Guidance)

- Some vault `.md` files now include YAML frontmatter for metadata consistency.
- These fields include: `schema_version`, `status`, `last_updated`, `title`.
- Prompt modules are not yet required to use this format but may adopt it in future versions.
- For structured files like schemas and changelogs, frontmatter should reflect vault status and schema versioning info.
