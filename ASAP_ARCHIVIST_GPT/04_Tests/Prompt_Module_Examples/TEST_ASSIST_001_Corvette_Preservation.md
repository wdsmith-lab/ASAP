# Prompt Test – assist_with_field

**Test ID**: `TEST_ASSIST_001`  
**Prompt Module**: `assist_with_field`  
**Schema Version**: 1.2  
**Tested By**: WillDeeEss  
**Date**: 2025-07-01  

---

## 🎯 Objective

Test ARCHIVIST’s ability to provide a helpful suggestion for a missing field in a metadata entry, using all known context.

---

## 📝 Input Prompt

```
assist_with_field

asset_uid: MOD_ACL_1969_CORVETTE  
field_name: preservation_risk  
known_values:  
{
  "Status": "Active",
  "Known Mirrors": [],
  "Initial Source URL": "https://thracing.de/ac-legends-gt-classics-by-bazza/"
}
```

---

## ✅ Expected Output

```
"moderate"
```

---

## 📌 Notes

- Should infer from lack of mirrors, community legacy, and wide sharing
- Response should include brief justification or option to override
