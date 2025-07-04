# ARCHIVIST GPT – Full Documentation

## PART I – USER-FACING GUIDE

---

### 1. What is ARCHIVIST GPT?

ARCHIVIST GPT is a specialized assistant that supports the **Automobile Simulation Archival Project (ASAP)**. It helps preserve sim racing history by creating and validating metadata entries for cars, tracks, collections, and liveries using the ASAP Metadata Schema.

It operates via structured interactions in a chat window using prompt modules. You can request it to extract metadata from forum posts, generate summaries, validate JSON, or help classify mods.

---

### 2. What ARCHIVIST Can and Cannot Do

**ARCHIVIST CAN:**
- Create new metadata entries from links, text, or descriptions
- Summarize existing entries
- Extract metadata from readmes, forum posts, and webpages
- Validate metadata against the ASAP schema
- Assist with field-level decisions (e.g., region, class, tags)

**ARCHIVIST CANNOT:**
- Download or inspect actual files
- Verify download links
- Replace curators for complex lineage/historical verification
- Make edits to external tools or vaults autonomously

---

### 3. How to Use ARCHIVIST in the Chat

Each interaction is based on a prompt module. You describe what you need and ARCHIVIST responds.

**Example – Create New Metadata:**
```
Please create a metadata entry for this mod:
https://example.com/download/gt40-mod-1968
Sim: Assetto Corsa
Author: Bazza
It’s a 1968 GT40 with historical skins.
```

**Example – Summarize an Entry:**
```
Please summarize the metadata entry with asset_uid: MOD_ACL_GT40_1968
```

---

### 4. Modules You Can Use

- `create_metadata_entry`
- `update_metadata_entry`
- `validate_metadata_entry`
- `summarize_metadata_entry`
- `extract_from_text`
- `assist_with_field`

---

### 5. Best Practices and Tips

- Use structured language and provide as much detail as possible
- Provide `asset_uid` for existing mods
- Use code blocks for JSON or metadata
- Use the validator before submitting metadata
- If unsure, ask ARCHIVIST to assist with just one field

---

### 6. Vault Integration Notes

ARCHIVIST is aware of seeded example metadata from your Obsidian vault.

- With `asset_uid`, it will attempt a lookup
- If nothing is found, it will prompt for details
- Helps ensure continuity between metadata, prompt examples, and schema evolution

---

## PART II – DEVELOPER/API DOCUMENTATION

---

### 7. GPT Interface as API Surface

Each prompt module behaves like an API endpoint. Inputs are text or structured blocks, and outputs are either JSON metadata or rationale-rich suggestions.

**Module Structure:**
- `task_type`: [create | update | validate | summarize | extract | assist]
- `input`: mod description or metadata
- `output`: markdown, JSON, or field suggestion

---

### 8. Input/Output Formats

**Accepted Input Types:**
- Natural language description (chat prompt)
- JSON metadata objects
- asset_uid for internal lookups

**Output Formats:**
- JSON metadata
- Human-readable summaries
- Validation reports
- Suggestions per field

---

### 9. Prompt Module Reference

**`create_metadata_entry`**
- Input: Mod description, forum link, or readme
- Output: Full JSON metadata record

**`validate_metadata_entry`**
- Input: Metadata object
- Output: Validation results

**`assist_with_field`**
- Input: `asset_uid`, field name, and question
- Output: Suggestions with rationale

**`summarize_metadata_entry`**
- Input: `asset_uid` or full metadata
- Output: 1–2 paragraph summary

**`extract_from_text`**
- Input: Unstructured text (readme, forum post)
- Output: Structured metadata elements

---

### 10. UID Anchoring and Lookups

Every entry must include an `asset_uid`. This unique identifier serves as the link between metadata, chat interactions, and archive files.

ARCHIVIST supports UID-driven operations:
- Lookup summaries
- Validate or update entries
- Provide field-level feedback

Vault-seeded UIDs allow internal memory reference within context.

---

## APPENDIX A – Metadata Fields Summary

- asset_uid
- asset_title
- mod_type
- simulator
- author
- contributor(s)
- initial_source_url
- known_mirrors
- upload_date
- creation_year_est
- status
- preservation_risk
- description
- license
- tags
- region
- vehicle_type
- track_type
- series/era
- notes
- file_name
- file_type
- file_size
- checksum_sha256
- file_structure_notes
- is_collection
- collection_id
- collection_name
- collection_author
- contains_assets
- last_verified
- preservation_notes
- submission_type
- submitted_by
- contact_info_internal

---

## APPENDIX B – Example Metadata Entry

```json
{
  "asset_uid": "MOD_ACL_GT40_1968",
  "asset_title": "1968 Ford GT40 (AC Legends)",
  "mod_type": "Car",
  "simulator": "Assetto Corsa",
  "author": "Bazza",
  "status": "Preserved",
  "preservation_risk": "low",
  "tags": ["GT", "Historic", "Ford"],
  "is_collection": false
}
```

---
