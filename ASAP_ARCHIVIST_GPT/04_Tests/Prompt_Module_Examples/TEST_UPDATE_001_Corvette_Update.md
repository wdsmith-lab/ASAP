# Prompt Test – update_metadata_entry

**Test ID**: `TEST_UPDATE_001`  
**Prompt Module**: `update_metadata_entry`  
**Schema Version**: 1.2  
**Tested By**: WillDeeEss  
**Date**: 2025-07-01  

---

## 🎯 Objective

Test ARCHIVIST’s ability to apply a targeted metadata update to an existing entry using a patch object and `asset_uid`.

---

## 📝 Input Prompt

```
update_metadata_entry

asset_uid: MOD_ACL_1969_CORVETTE

update_patch:
{
  "File Size": "1.2 GB",
  "Known Mirrors": [
    "https://example.com/acl_corvette69_download"
  ],
  "last_updated": "2025-07-01"
}
```

---

## ✅ Expected Output (Key Fields Only)

```json
{
  "asset_uid": "MOD_ACL_1969_CORVETTE",
  "File Size": "1.2 GB",
  "Known Mirrors": ["https://example.com/acl_corvette69_download"],
  "last_updated": "2025-07-01"
}
```

---

## 📌 Notes

- ARCHIVIST should return a confirmation block or the updated diff
- Should never modify fields not included in the patch
- Schema version should remain unchanged
