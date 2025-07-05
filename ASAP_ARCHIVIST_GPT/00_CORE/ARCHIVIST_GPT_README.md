# ARCHIVIST GPT – Project Readme

**Version**: v1.0  
**Status**: Active  
**Maintainer**: WillDeeEss  
**Location**: 00_CORE/ARCHIVIST_GPT_README.md  
**Date**: 2025-07-03  

---

## 📌 Purpose & Scope

`ARCHIVIST-GPT` is a specialized GPT agent designed to generate, update, summarize, and manage structured metadata entries for sim racing mods across multiple platforms — starting with Assetto Corsa, and eventually extending to rFactor, Automobilista, Grand Prix Legends, and others.

Its function is archival in nature: to help preserve at-risk or scattered sim racing mods with meaningful, schema-compliant entries in the ASAP metadata archive.

---

## 🧠 Core Behaviors

ARCHIVIST operates under strict schema alignment and structured prompt module logic:

- Validates all entries against the **locked** ASAP Metadata Schema v1.2
- Applies preservation-aware logic (e.g., risk inference, license tagging)
- Distinguishes between mod types: Cars, Tracks, Liveries, Collections, etc.
- Operates in cooperation with TECHNICAL-CONSULTANT and CONSULTANT
- Supports YAML frontmatter in output (optional)

ARCHIVIST is schema-aware but not schema-defining.

---

## 📐 Schema Status

- ✅ `ASAP_Metadata_Schema_v1.2` is **LOCKED**
  - Location: `01_Schema/ASAP_Metadata_Schema_v1.2_LOCKED.md`
  - YAML frontmatter now included

- 🧪 Schema v1.3 is in early staging
  - New fields under consideration: `curator_notes`, expanded mod type logic, changelog support
  - Track staging in: `01_Schema/ASAP_Metadata_Schema_v1.3_DRAFT.md` and `ARCHIVIST-CONSULTANT/Standards/`

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

---

## 🧪 Testing & Examples

Test prompts for each module live in:

📂 `04_Tests/Prompt_Module_Examples/`

Each test includes:
- ✅ Input prompt
- ✅ Expected output
- ✅ Module and schema version
- ✅ Commentary on expected behavior

---

## ⚠️ Limitations (v1.0)

- Metadata schema locking must be enforced externally (now documented)
- No database connection or automatic entry persistence (yet)
- Simulator support is Assetto Corsa-focused during early phases
- Entry versioning is manual (policy now documented)
- Schema version mismatch handling is enforced by logic, not runtime schema introspection

---

## 📘 YAML Frontmatter (New Guidance)

- Some `.md` files in the vault now use YAML frontmatter for metadata hygiene
- Fields: `schema_version`, `status`, `last_updated`, `title`
- Optional for metadata entries; currently used in schemas, changelogs, standards
- Prompt modules may output frontmatter on request, but default to JSON/Markdown

---

## 📎 Recommended Companion Roles

- `ASAP_TECHNICAL-CONSULTANT` for scripting and schema tooling
- `ASAP_ARCHIVIST-CONSULTANT` (this role) for development design and documentation

---

## 📥 Intake Templates

To assist human contributors and facilitate ARCHIVIST module submissions, two intake templates are provided in:

📁 `ASAP_ARCHIVIST-GPT/Templates/`

- `ASAP_Metadata_Intake_Template.md` – a Markdown form curators can fill manually in Obsidian or Git workflows.
- `ASAP_Metadata_Intake_Promptable.txt` – a lightweight version meant for copy-paste into ARCHIVIST GPT.

These templates help standardize inputs, reduce drift, and prepare data for conversion to schema-compliant entries.
