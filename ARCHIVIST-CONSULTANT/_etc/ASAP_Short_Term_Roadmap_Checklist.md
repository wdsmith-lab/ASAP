# ✅ ASAP Short-Term Roadmap – Post-Schema Lock

This document tracks the remaining near-term tasks before GPT deployment and broader metadata generation.

---

## 📦 1. Convert Sample Metadata Entries to Schema v1.2

- [x] Convert Bazza GT40 Collection entry to final schema
- [x] Convert Targa Florio Track entry to final schema
- [x] Convert one Livery Pack and one Collection
- [x] Store all as JSON + Markdown in `Seed_Metadata_Entries/`
## ✅ COMPLETED

- ✔ Bazza GT Collection + mods converted to Schema v1.2
    
- ✔ Targa Florio (track) converted
    
- ✔ GT40 Liveries Pack converted, with nuanced treatment and `curator_notes` addition
    
- ✔ Bundle of seed metadata entries exported
    
- ✔ Schema v1.3 (DRAFT) created to capture forward-looking structural change
---


## 🧪 2. Create Test Prompts and Expected Outputs

- [x] Create example prompt + output pairs for:
  - [x] `create_metadata_entry`
  - [x] `lookup_metadata_entry`
  - [x] `update_metadata_entry`
  - [x] `summarize_metadata_entry`
- [x] Save to `04_Tests/Prompt_Module_Examples/`

---

## 📘 3. Create ARCHIVIST README / Capabilities Brief

- [ ] Describe GPT scope, prompt modules, and metadata targets
- [ ] Include usage examples and known limitations
- [ ] Save as `ARCHIVIST_GPT_README.md` in `00_CORE/`

---

## 🧠 4. Refine Prompt Modules (v1.2 → v1.3 Prep)

- [ ] Integrate logic for `entry_version` tracking
- [ ] Improve `preservation_risk` inference heuristics
- [ ] Enable support for partial/fragmented metadata input

---

## 🛠️ 5. Build README + TOC Generator

- [ ] Write script to generate project TOC from folder structure
- [ ] Include version/status indicators if feasible
- [ ] Save to `99_Tools/` or `00_CORE/`

---

## 🟢 Optional Enhancements

- [ ] Finalize policy for `entry_version` use
- [ ] Create a metadata schema validator

---

## ✅ Completed Milestones

- [x] Schema v1.2 finalized and locked
- [x] Field-Level Guidance reconciled
- [x] Schema Index and Changelog synced
- [x] TECHNICAL-CONSULTANT seeded and active

