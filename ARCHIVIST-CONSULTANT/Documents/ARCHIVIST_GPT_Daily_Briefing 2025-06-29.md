# ARCHIVIST GPT – Kindle Briefing Overview

---

## 🧠 Purpose and Function of ARCHIVIST GPT

ARCHIVIST GPT is a custom AI assistant built to support the **Automobile Simulation Archival Project (ASAP)**. Its core purpose is to assist in the **preservation, contextualization, and metadata creation** of community-made sim racing content — particularly for titles like Assetto Corsa, rFactor, Grand Prix Legends, and others.

ARCHIVIST specializes in:
- Generating metadata entries for cars, tracks, collections, and liveries
- Validating metadata against a controlled schema
- Summarizing mods for human readers
- Extracting structured data from unstructured text (readmes, forum posts)
- Assisting curators in resolving specific metadata fields

ARCHIVIST operates solely through **chat-based prompt modules**, and does not execute scripts or browse the web. It relies on:
- A shared schema (`ASAP_Metadata_Schema_v1.2`)
- A prompt-module architecture
- UID-based lookup for previously stored entries
- Clear interaction boundaries and human-in-the-loop design

---

## ✅ Summary of What We've Done So Far

- Established the purpose, boundaries, and personality of ARCHIVIST
- Created a draft metadata schema and refined it to v1.2
- Validated schema examples for liveries, collections, and car mods
- Reconciled inconsistencies and enforced use of `asset_uid`
- Built modular prompt templates:
  - `create_metadata_entry`
  - `validate_metadata_entry`
  - `summarize_metadata_entry`
  - `assist_with_field`
  - `extract_from_text`
- Created sample outputs for skin packs and collections
- Integrated preservation severity and contextual references
- Finalized guidance table and behavioral constraints

---

## 🔧 User Interface/API Summary (So Far)

ARCHIVIST operates via **prompt modules** with defined roles.

Each module acts like an API endpoint, with structured input/output:

- `create_metadata_entry`: Generates a new ASAP metadata record from description
- `summarize_metadata_entry`: Returns a human-readable paragraph from metadata
- `validate_metadata_entry`: Lists schema issues
- `assist_with_field`: Resolves a single field value (requires `asset_uid`)
- `extract_from_text`: Parses pasted content for structured metadata fields

All interactions must specify:
- A clear prompt
- A metadata object or `asset_uid`
- Explicit task context

ARCHIVIST remembers contextual entries from the vault and interprets responses accordingly.

---

## 🗺️ Anticipated Roadmap (Next Steps)

### Short-Term
- Finalize and lock `ASAP_Metadata_Schema_v1.2`
- Convert all sample metadata entries to match schema
- Refine prompt modules with advanced handling for:
  - Versioning
  - Licensing
  - Partial/fragmented data
- Improve logic around `preservation_risk` inference
- Create a README and vault TOC index generator module

### Mid-Term
- Build module for bulk ingestion of scraped text blocks
- Develop export tools for Obsidian-to-GPT sync pipeline
- Introduce detection of duplicate/near-duplicate entries
- Add change tracking or metadata versioning hinting

### Long-Term
- Define plug-in interface for semi-automated ingest into metadata databases
- Link ARCHIVIST to a mirror-checking tool or preservation crawler
- Support user account logins or contributor tracking
- Integrate with licensing normalizers or taxonomy authorities

---

## 🧭 Reflective Notes and Considerations

- **Schema Drift**: This phase surfaced inconsistencies that can multiply if not reconciled now. We caught them early.
- **UID Design**: Excellent decision to enforce `asset_uid` for every entry. It becomes the anchor point for every other module and lookup.
- **Vault Awareness**: ARCHIVIST should always make it clear when it's relying on seeded memory vs. what's provided. This guards against hallucination.
- **Prompt Integrity**: Maintaining clean prompt boundaries makes the tool modular and maintainable. This project has followed best practices here.
- **Missing Elements**: Versioning is going to matter soon — not just file versioning, but entry versioning. This could be inferred from `submission_type` and update flags.
- **Human Judgment**: This tool is shaping up to be an *amplifier*, not a replacement, for human archivists — which is the right design philosophy for something with a historical and preservationist mission.

---
