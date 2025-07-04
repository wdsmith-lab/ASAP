# Prompt Test – extract_from_text

**Test ID**: `TEST_EXTRACT_001`  
**Prompt Module**: `extract_from_text`  
**Schema Version**: 1.2  
**Tested By**: WillDeeEss  
**Date**: 2025-07-01  

---

## 🎯 Objective

Test ARCHIVIST’s ability to extract usable metadata from an unstructured mod page text.

---

## 📝 Input Prompt

```
extract_from_text

Raw text:
"Welcome to the classic 1960s Targa Florio! Converted for Assetto Corsa by Albuzz. Originally built for rFactor, this historic 72km circuit brings the island roads to life. Credits to the original creators and all those who helped test and improve the layout. Still actively maintained by the community. Packaged as a .rar archive, drop it into your tracks folder and enjoy."
```

---

## ✅ Expected Output (Key Fields Only)

```json
{
  "Asset Title": "Targa Florio",
  "Simulator": "Assetto Corsa",
  "Author": "Albuzz",
  "Creation Year (Est.)": "",
  "Status": "Active",
  "File Type": "RAR Archive",
  "Description": "A historic conversion of the Targa Florio road circuit, originally built for rFactor and ported to Assetto Corsa by Albuzz."
}
```

---

## 📌 Notes

- Output should never guess missing values — only include confidently extracted fields
- Good test of conservative inference vs. hallucination
