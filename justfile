# 📦 ASAP Vault Automation – justfile

# Commit and push changes with a default message
push:
    git add .
    git commit -m "📝 vault update"
    git push

# Pull latest from remote
pull:
    git pull

# Check git status
status:
    git status

# Run the status checker script on the vault
check-status format="auto":
    python3 _bin/check_status_consistency.py . --format {{format}}

# Run check and output as JSON
check-status-json format="auto":
    python3 _bin/check_status_consistency.py . --format {{format}} --json

# Lint all Markdown files using markdownlint-cli
lint:
    npx markdownlint "**/*.md"

# Open Obsidian from vault root (if obsidian CLI is installed)
obsidian:
    obsidian .
