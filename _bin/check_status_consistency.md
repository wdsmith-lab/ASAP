# ✅ `check_status_consistency.py`

**Purpose**:  
Validates whether the `status` field inside a `.md` file matches its filename suffix (e.g., `_LOCKED.md`, `_DRAFT.md`, etc.).

Supports both **YAML frontmatter** and **Markdown-formatted** inline fields.

---

## 🧪 What It Checks

- ✅ YAML frontmatter field `status: Locked` (if present)
- ✅ Markdown content with `**Status**: Locked`, `Status: Locked`, etc.
- ✅ Filename suffix (e.g. `_LOCKED.md`)
- ❌ Flags mismatches, missing data, or malformed formats

---

## ⚙️ Usage

```bash
python3 check_status_consistency.py [folder] [options]
```

### Options:

| Option              | Description                                     |
|---------------------|-------------------------------------------------|
| `--format`          | `auto` (default), `yaml`, or `markdown`         |
| `--non-recursive`   | Limit to a single folder                        |
| `--json`            | Output results as JSON                          |
| `--out <file>`      | Write JSON output to specified file             |

---

## 📁 Examples

```bash
# Default: recursive, auto format
python3 check_status_consistency.py ~/vault/ASAP

# Only check YAML frontmatter
python3 check_status_consistency.py . --format yaml

# Output JSON
python3 check_status_consistency.py . --json --out results.json
```

---

## 🧭 Related Documentation

- ✅ See also: [`ASAP_Schema_Locking_Checklist`](../01_Schema/ASAP_Schema_Locking_Checklist.md)

---

## 🛠 Notes

- Fields are normalized (case-insensitive, emoji-stripped)
- YAML frontmatter takes precedence in `--format auto`
- Script is located in: `_bin/check_status_consistency.py`
