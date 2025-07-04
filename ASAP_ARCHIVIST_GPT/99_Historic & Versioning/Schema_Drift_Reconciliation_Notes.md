# Schema Drift & Reconciliation Notes

## Context
Several metadata examples drifted from the locked ASAP_Metadata_Schema_v1.1. This document tracks those deviations and formalizes schema improvements.

---

## Common Drifts Observed
- Use of 'livery' and 'collection' types not in original `type` vocabulary
- `is_collection`, `contains_assets`, `collection_author` used informally
- QA fields like `extraction_test_status`, `duplicate_flag` in live metadata
- Flexible contributor notation (`Contributor(s)`), aligned with `converted_by`

---

## Actions Taken
- Added missing types and fields in schema v1.2
- Promoted QA and relationship fields to first-class optional fields
- Added `submission_type`, `contact_internal` for traceability

---

## Recommendations
- Archive legacy v1.1 as-is, adopt v1.2 going forward
- Use v1.2 as formal schema for ARCHIVIST prompt conditioning and field validation
- Update metadata tools/scripts to reflect new field vocabulary

---

## Notes for ARCHIVIST GPT
- Respect legacy metadata while conforming outputs to v1.2
- When updating legacy entries, gently flag schema mismatches for curator review
