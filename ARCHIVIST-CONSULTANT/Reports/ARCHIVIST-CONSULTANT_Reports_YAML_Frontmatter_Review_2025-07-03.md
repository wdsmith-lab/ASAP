# YAML Frontmatter Adoption – ARCHIVIST GPT

**Date**: 2025-07-03  
**Session**: ARCHIVIST-CONSULTANT  
**Author**: ARCHIVIST-CONSULTANT (ChatGPT)  
**Location**: ARCHIVIST-CONSULTANT/Reports/

---

## ✅ Summary

This document records the final understanding and policy surrounding the use of YAML frontmatter within the ASAP vault and ARCHIVIST GPT development.

---

## 📌 Key Agreements

- **YAML frontmatter** is now supported and encouraged for structured Markdown files such as:
  - `ASAP_Metadata_Schema_v1.2_LOCKED.md`
  - `ASAP_Metadata_Schema_CHANGELOG.md`
  - Any future schema drafts, roadmap files, changelogs, or structured technical documentation

- Frontmatter blocks include:
  ```yaml
  ---
  schema_version: "1.2"
  status: "locked"
  last_updated: "2025-07-01"
  title: "ASAP Metadata Schema"
  ---
  ```

- The following metadata fields are typical in frontmatter:
  - `schema_version`
  - `status`
  - `last_updated`
  - `title`

---

## ⚠️ Prompt Module Guidance

- Prompt modules are **not yet required** to emit or parse YAML frontmatter.
- Support for frontmatter in prompt output or ingestion may be introduced in **v2.x** workflows.
- Until then, prompt modules should operate against traditional body-format entries.

---

## ✅ Actions Already Taken

- Frontmatter added to:
  - `ASAP_Metadata_Schema_v1.2_LOCKED.md`
  - `ASAP_Metadata_Schema_CHANGELOG.md`
- `ARCHIVIST_GPT_README.md` updated with frontmatter usage guidance

---

This document serves as an internal record of alignment and deployment status as of July 3, 2025.
