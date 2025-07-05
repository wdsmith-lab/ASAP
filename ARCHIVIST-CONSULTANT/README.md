# ARCHIVIST-CONSULTANT Vault

This Obsidian vault supports the development of a specialized GPT agent known as **ARCHIVIST**, for the **Automobile Simulation Archival Project (ASAP)**.  
This vault and session (`ARCHIVIST-CONSULTANT`) serve as the design, documentation, and schema oversight layer during GPT development.

---

## 🎯 Purpose

This vault provides:
- A locked and versioned **metadata schema** (`ASAP_Metadata_Schema_v1.2`)
- A full suite of **prompt modules** and tests
- Versioning, field-level guidance, and roadmap strategy
- YAML-aware and schema-compliant metadata architecture
- Sample entries for cars, tracks, collections, and liveries
- Internal documentation for use with OpenAI GPT Builder

---

## 📁 Folder Overview

| Folder | Contents |
|--------|----------|
| `01_Schema/` | Metadata schema (LOCKED & DRAFT), changelogs, guidance table, and sample entries |
| `02_Metadata_Examples/` | Sample metadata entries for various mod types (cars, tracks, collections, liveries) |
| `03_Prompt_Modules/` | All prompt modules used by ARCHIVIST (create, lookup, update, summarize, assist, etc.) |
| `04_Tests/` | Structured test cases for validating prompt module behavior |
| `00_CORE/` | Readme, GPT briefing documents, role scope, roadmap |
| `ARCHIVIST-CONSULTANT/Documents/` | Handoff notes and GPT coordination records |
| `ARCHIVIST-CONSULTANT/Reports/` | Meeting summaries, YAML policy, roadmap progress |
| `ARCHIVIST-CONSULTANT/Standards/` | Formal documentation: versioning, schema rules, field behavior |

---

## 🧭 Start Here

To begin working with this vault:
- Open `ASAP_Metadata_Schema_v1.2_LOCKED.md` in `01_Schema/` for schema reference
- Review `ARCHIVIST_GPT_README.md` in `00_CORE/` for module summary and test locations
- Use `Prompt_Module_Create_Metadata_Entry.md` and its peers in `03_Prompt_Modules/` to design prompt workflows
- See `04_Tests/Prompt_Module_Examples/` for real input/output expectations

---

## 🤝 Working With ARCHIVIST-CONSULTANT

This vault works in tandem with:
- `ARCHIVIST` GPT (the metadata entry generator)
- `TECHNICAL-CONSULTANT` GPT (tooling and scripting assistant)
- You (WillDeeEss), as project owner, lead curator, and architect

All changes, schema locks, and design moves are tracked through this vault to support long-term sustainability of ASAP metadata infrastructure.

