# ✅ ASAP Metadata Version Locking Checklist

Use this checklist before finalizing and locking any new metadata schema version.

## 📁 Filename & Internal Consistency
- [ ] Filename suffix matches internal `Status:` (e.g., `_LOCKED.md` and `Status: Locked`)
- [ ] No old versions share the same suffix (clean up archives if needed)

## 📑 Content Confirmation
- [ ] Final pass for typos or formatting issues
- [ ] All new fields added to:
  - [ ] Schema file
  - [ ] Field-Level Guidance Table
  - [ ] Schema Index (status, location)
  - [ ] Changelog (noted and timestamped)

## 🔐 Locking Declaration
- [ ] Footer block added confirming locked status
- [ ] Maintainer/date fields filled in

## 🧠 Vault Sync Hygiene
- [ ] Obsidian vault updated with new version
- [ ] Previous draft archived or renamed

## 🧪 Optional
- [ ] Run consistency check script to validate status sync
      [[check_status_consistency]]

