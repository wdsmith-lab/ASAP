# ✅ ChatGPT Session Boot Checklist for the ASAP Vault

This guide helps you start a new ChatGPT session (with either `ASAP_TECHNICAL-CONSULTANT` or `ARCHIVIST-CONSULTANT`) in a way that reflects your current vault state and dev environment.

---

## 🧭 1. Prep Locally Before You Start the Session

### 🔃 Push Latest Vault Changes to GitHub

bash

CopyEdit

`cd /mnt/c/Users/Computer/Projects/ASAP just push`

Make sure all edits, new files, or generated content are committed and pushed to:

🔗 [https://github.com/wdsmith-lab/ASAP](https://github.com/wdsmith-lab/ASAP)

---

## 🧾 2. Open ChatGPT and Provide Context

When starting a session:

### 🗣️ Paste This (or similar):

markdown

CopyEdit

`I'm working from the current state of my public GitHub repo: https://github.com/wdsmith-lab/ASAP  Please assume the vault contents reflect that repo unless I paste updated file content.`

If needed, also clarify which assistant is in use (e.g. `ASAP_TECHNICAL-CONSULTANT`) and your working focus (e.g., linting, prompts, schema, scripting).

---

## 📂 3. Paste File Contents (When Needed)

If you want ChatGPT to:

- Review a script, Markdown file, YAML block, etc.
    
- Generate diffs or new content
    
- Help debug or refactor
    

Use fenced code blocks:

<pre> ```markdown # Example.md Your content here ``` </pre>

✅ This gives the assistant a stable working copy  
✅ Works across all assistants and formats

---

## 🧰 4. Reference Key Paths

If referring to a file or folder from the vault, use relative paths:

swift

CopyEdit

`_bin/check_status_consistency.py ARCHIVIST-CONSULTANT/Documents/TECHNICAL_to_ARCHIVIST_Handoff_2025-07-01.md ASAP_ARCHIVIST_GPT/01_Schema/ASAP_Metadata_Schema_v1.2.md`

✅ This ensures clarity  
✅ Works regardless of assistant memory

---

## 🔐 Optional Security Reminder

If you _do_ make the repo private later:

- Mention it explicitly
    
- Upload specific files manually or paste them inline