# Duplicate Detection & `duplicate_flag` Policy

**Status**: Active  
**Adopted**: 2025-07-03  
**Maintainer**: ARCHIVIST-CONSULTANT  
**Location**: ARCHIVIST-CONSULTANT/Standards/Duplicate_Detection_Policy.md

---

## 🎯 Purpose

This policy outlines how ARCHIVIST GPT should detect and respond to potential duplicate metadata entries, using the `duplicate_flag` field as a classification mechanism.

---

## 🔁 Duplicate Detection: When and Why

ARCHIVIST must avoid creating duplicate entries for the same mod across:
- Different mirrors or sources
- Identical assets repackaged
- Human error (same mod submitted twice)

Preventing duplication maintains archive clarity, reduces clutter, and enables better linkage across entries.

---

## 🧪 When ARCHIVIST Should Check for Duplicates

Primarily in:
- `create_metadata_entry`
- `validate_metadata_entry`

ARCHIVIST should:
- Search for existing entries by `Asset Title`, `Simulator`, and `Initial Source URL`
- Present any match to the user before proceeding

---

## 🧠 GPT Prompt Logic

If a potential duplicate is found:

```text
❗ A similar entry may already exist in the archive (Asset UID: MOD_GT40_BAZZA_AC).

Would you like to:
[A] View the existing entry
[B] Create a new one anyway (mark as possible duplicate)
[C] Cancel
```

If the user confirms creation, set:

```json
"duplicate_flag": "human-level"
```

And append a note in `Notes` or `curator_notes` field:
> “Possible duplicate of MOD_GT40_BAZZA_AC – intentionally archived separately.”

---

## 🧾 `duplicate_flag` Enum (v1.3+)

| Value           | Description |
|----------------|-------------|
| `"no"`          | Entry has no known duplicates |
| `"system-level"`| Automatically detected as a likely duplicate |
| `"human-level"` | Curator or user flags this as a known duplicate |
| `"superseded"`  | This entry was replaced by another asset |

This field allows both soft and hard linkage, without enforcing absolute uniqueness.

---

## 🛠 Manual Override Support

ARCHIVIST should always allow the user to:
- Override duplicate warnings
- Provide justification via `Notes` or `curator_notes`
- Choose to continue with metadata creation

---

## 🧩 Future Work (Planned)

- Hash-based duplicate detection (file checksum matching)
- URL and filename heuristic scoring
- Visual cues in UI (if built) for linking entries

This ensures curators have both automation and agency in maintaining archive quality.

