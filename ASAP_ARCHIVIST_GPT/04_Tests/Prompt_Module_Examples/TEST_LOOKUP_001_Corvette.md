# Prompt Test – lookup_metadata_entry

**Test ID**: `TEST_LOOKUP_001`  
**Prompt Module**: `lookup_metadata_entry`  
**Schema Version**: 1.2  
**Tested By**: WillDeeEss  
**Date**: 2025-07-01  

---

## 🎯 Objective

Test ARCHIVIST’s ability to retrieve a full metadata entry given a known `asset_uid`.  
This validates direct asset retrieval and return format.

---

## 📝 Input Prompt

```
lookup_metadata_entry for asset_uid: MOD_ACL_1969_CORVETTE
```

---

## ✅ Expected Output (Key Fields Only)

```json
{
  "Asset ID": "MOD_ACL_1969_CORVETTE",
  "Asset Title": "1969 Chevrolet Corvette C3 (AC Legends)",
  "Mod Type": "Car",
  "Simulator": "Assetto Corsa",
  "Author": "Bazza",
  "Status": "Active",
  "schema_version": "1.2",
  "entry_version": "v1.0"
}
```

---

## 📌 Notes

- ARCHIVIST should search local metadata archive using `asset_uid`
- Full metadata entry is returned as-is with no interpretation or modification
- If entry is missing or incomplete, GPT should raise a structured error or fallback message

