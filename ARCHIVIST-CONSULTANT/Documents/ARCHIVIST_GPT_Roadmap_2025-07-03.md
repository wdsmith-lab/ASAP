# 📍 ARCHIVIST GPT – Updated Roadmap (July 3, 2025)

## ✅ Completed (since last roadmap)

- Finalized and locked `ASAP_Metadata_Schema_v1.2`
- Integrated `asset_uid` and `schema_version` into all entries
- Added `preservation_risk`, `last_verified`, `curator_notes`, and versioning fields
- Completed conversion of sample entries (Cars, Tracks, Liveries, Collections)
- Implemented YAML frontmatter for key files (Schema, Changelog)
- Created README and formal test cases for all prompt modules:
  - `create_metadata_entry`
  - `lookup_metadata_entry`
  - `update_metadata_entry`
  - `summarize_metadata_entry`
  - `assist_with_field`
  - `extract_from_text`
  - `validate_metadata_entry`
- Designed ARCHIVIST GPT role logic, behavior, and module boundaries
- Created working Obsidian vault with organized TOC and test harness structure
- Separated technical roles (via TECHNICAL-CONSULTANT) and design roles (this session)

---

## 📍 Short-Term Goals (Next Focus)

> Target: July 3–10

- [x] Add YAML-aware logic to prompt module outputs (optional frontmatter)
- [ ] Add more examples for non-AC simulators (e.g., rFactor, AMS1, GPL)
- [x] Document versioning policies for metadata entries
- [x] Define how ARCHIVIST should respond to schema version mismatch
- [x] Update README to reflect locked schema state + v1.3 staging
- [x] Consider `duplicate_flag` enforcement logic (early detection & override flow)
- [x] Draft input templates or intake forms for human-assisted submissions

---

## 🧭 Mid-Term Goals

> Target: July 10–Late July

- [ ] Develop logic for bulk `extract_from_text` operations
- [ ] Enable multi-entry parsing from a single file or paste
- [ ] Create pipeline for ingesting from existing unstructured sources
- [ ] Begin logic for deduplication warnings across similar entries
- [ ] Explore version tracking for assets (e.g., `entry_version` lifecycle)
- [ ] Begin preparing for schema v1.3: 
  - More flexible mod types
  - `curator_notes` adoption
  - Cross-sim field support
- [ ] Create vault-to-database export logic (flat JSON or vault subset)

---

## 🔭 Long-Term Goals

> Target: August and beyond

- [ ] Add plug-in interface for mirrored file checks or automated preservation risk assessment
- [ ] Interface with external tools: checksum generators, download verifiers, etc.
- [ ] Build submission UI for contributors outside chat interface
- [ ] Implement change history for individual entries
- [ ] Link schema definitions with formal validation engine (e.g., JSON Schema)
- [ ] Archive publishing or public portal preparation
