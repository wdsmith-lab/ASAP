
- a curation_notes (internal) field?  ie., I would like to comment on the Bazza GT Classics pack that only 3 assets are listed in the "contains" field, and that is known, while the actual car list is 11 (verify.)
  
  ## 🧩 Candidate Field for v1.3: `curator_notes`

|Field|Value|
|---|---|
|**Name**|`curator_notes`|
|**Type**|`string` (Optional)|
|**Purpose**|Allow human curators to leave internal comments, context, or caveats within a metadata entry|
|**Use Cases**|- Explain known omissions or simplifications (e.g., partial collection listing)|
- Clarify future tasks (e.g., “needs verification”)  
- Preserve curator decision logic or constraints  
- Distinguish from end-user-facing `Notes` field 

---

We'll do a track and a livery pack next, but before that, please have at look at COLLECTION_MISC_CARPACK_001 and let me know how the fields there compare to Schema v1.2, and let's see if there are any fields there we might want to consider for Schema v1.3. It seems during that phase, Adam and I were working with a tags fields, for example.

###### ChatGPT said:

Thanks — I’ve reviewed the structure of `COLLECTION_MISC_CARPACK_001.json`. Here’s how it compares to **Schema v1.2**, and a few ideas it surfaces for **Schema v1.3** planning:

---

## ✅ Comparison to Schema v1.2

### ✅ Fields Present and Compatible

All of these are already defined in v1.2:

- Core fields: `Asset ID`, `Asset Title`, `Mod Type`, `Simulator`, `Author`, etc.
    
- Provenance and packaging: `Initial Source URL`, `Known Mirrors`, `File Type`, `File Size`, etc.
    
- Collection-specific: `Is Collection`, `Collection ID`, `Collection Name`, `Contains Assets`
    

No schema-breaking inconsistencies.

---

## ⚠️ Field of Note: `Tags`

- Present in this entry: ✅
    
- In Schema v1.2: ✅ (`Tags` is defined as a freeform list)
    

No issue here — but worth noting that this tag use could be **expanded in v1.3** to support:

- Tag schema validation or controlled vocabularies
    
- Suggested tag categories (e.g., vehicle, era, type, origin)
    
- Possible hierarchical/tag taxonomy tools
    

---

## 🧠 Fields NOT Present in This Entry (but required by v1.2)

These will need to be added if converting to v1.2:

- `asset_uid`
    
- `schema_version`
    
- `entry_version`
    
- `last_updated`
    
- `preservation_risk`
    
- `preservation_notes`
    
- `last_verified`
    

This is expected, as this entry predates the v1.2 changes.

---

## 🧪 Possible Schema v1.3 Candidates (Inspired by This Entry and Past Work)

| Proposed Field                                     | Purpose                                                                          |
| -------------------------------------------------- | -------------------------------------------------------------------------------- |
| `tag_categories` (optional)                        | Distinguish curated tags by type (e.g., "vehicle", "mod class", "theme")         |
| `related_collections` (optional list of Asset IDs) | Let collections link laterally to similar packs                                  |
| `group_notes`                                      | Add curator commentary on the rationale behind assembled collections             |
| `source_thread_url` (optional)                     | Separate field from `Initial Source URL` for forums or discussion links          |
| `discovery_context` (optional string)              | Human-added detail about how it was found, especially useful for “orphaned” mods |

---

Would you like me to:

- Convert this entry to v1.2 format now?
    
- Capture the potential v1.3 field suggestions in a roadmap planning doc?
    

Either way, you’ve got a clean base to work from.