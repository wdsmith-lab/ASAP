# Prompt Test – summarize_metadata_entry

**Test ID**: `TEST_SUMMARIZE_001`  
**Prompt Module**: `summarize_metadata_entry`  
**Schema Version**: 1.2  
**Tested By**: WillDeeEss  
**Date**: 2025-07-01  

---

## 🎯 Objective

Test ARCHIVIST's ability to produce a one-paragraph summary of a metadata entry for archival overviews or UI display.

---

## 📝 Input Prompt

```
summarize_metadata_entry for asset_uid: TRACK_TARGAFLORIO_ALBUZZ
```

---

## ✅ Expected Output (Summary)

```
Targa Florio by Albuzz is a preserved Assetto Corsa track mod recreating the historic Sicilian road circuit. Estimated to originate in 2015, the track is highly regarded for its atmosphere and layout. While no official source remains, it continues to circulate via mirrors. This version is based on community preservation and retains original file structure references.
```

---

## 📌 Notes

- ARCHIVIST should pull relevant facts from the metadata but not fabricate
- Summary must include: title, platform, status, year, and preservation context
- Avoid technical field names or JSON-style output
