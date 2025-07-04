# Prompt Test – create_metadata_entry

**Test ID**: `TEST_CREATE_001`  
**Prompt Module**: `create_metadata_entry`  
**Schema Version**: 1.2  
**Tested By**: WillDeeEss  
**Date**: 2025-07-01  

---

## 🎯 Objective

Test ARCHIVIST's ability to generate a full metadata entry from a pasted input description of a mod.  
This test checks for correct field population, schema compliance, and inferred values such as `preservation_risk`.

---

## 📝 Input Prompt

```
Please create a metadata entry for the following:

A Ford GT40 livery pack for Assetto Corsa. Includes skins from 1968 Gulf, Le Mans 1969, Shelby team, and others. Created by community artists and compiled by 'Skins4Legends'. No car mod included, just skins. Compatible with Legion’s GT40 mod. First appeared on RaceDepartment, now mostly shared through mirrors.
```

---

## ✅ Expected Output (Key Fields Only)

```json
{
  "Asset Title": "GT40 Classic Liveries Pack",
  "Mod Type": "Livery",
  "Simulator": "Assetto Corsa",
  "Author": "Various Community Artists",
  "Contributor(s)": "Compiled by user 'Skins4Legends'",
  "Status": "Preserved",
  "File Structure Notes": "Includes multiple subfolders under skins/ for GT40.",
  "Notes": "Compatible with the Legion GT40 mod.",
  "preservation_risk": "moderate",
  "Is Collection": true,
  "Tags": ["Livery", "GT40", "Skins", "1960s"],
  "schema_version": "1.2"
}
```

---

## 📌 Notes

- `preservation_risk` inferred from statement about mirror-only distribution  
- `Mod Type: Livery` appropriate because all assets are skins for a single vehicle  
- `Is Collection: true` included based on internal pack structure  
- Should not hallucinate authors or URLs — okay to leave blank or say “not specified”
