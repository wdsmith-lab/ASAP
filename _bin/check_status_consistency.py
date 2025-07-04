#!/usr/bin/env python3

import os
import re
import argparse
import json
import yaml

def extract_status_from_filename(filename):
    match = re.search(r'_([A-Z]{4,})\.md$', filename)
    return match.group(1).capitalize() if match else None

def extract_status_from_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines:
        return None
    if lines[0].strip() == '---':
        yaml_lines = []
        for line in lines[1:]:
            if line.strip() == '---':
                break
            yaml_lines.append(line)
        try:
            frontmatter = yaml.safe_load("".join(yaml_lines))
            return str(frontmatter.get("status")).capitalize() if "status" in frontmatter else None
        except yaml.YAMLError:
            return None
    return None

def extract_status_from_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            normalized = line.strip().lower()
            if 'status' in normalized:
                match = re.search(r'(?:\*\*)?status(?:\*\*)?\s*[:\-]\s*(.+)', line, re.IGNORECASE)
                if match:
                    raw = match.group(1).strip()
                    cleaned = re.sub(r'[\u2700-\u27BF\uE000-\uF8FF\uFE00-\uFE0F\u1F000-\u1FFFF]', '', raw)
                    cleaned = re.sub(r'^✅\s*', '', cleaned).strip()
                    return cleaned.capitalize()
    return None

def extract_status(filepath, mode="auto"):
    if mode == "yaml":
        return extract_status_from_yaml(filepath)
    elif mode == "markdown":
        return extract_status_from_markdown(filepath)
    else:  # auto
        yaml_status = extract_status_from_yaml(filepath)
        return yaml_status if yaml_status else extract_status_from_markdown(filepath)

def validate_markdown_status(folder, output_json=False, output_file=None, recursive=True, format_mode="auto"):
    print(f"🔍 Scanning for .md files in: {folder}\n")
    results = []

    walker = os.walk(folder) if recursive else [(folder, [], os.listdir(folder))]

    for root, _, files in walker:
        for filename in files:
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                file_status = extract_status_from_filename(filename)
                content_status = extract_status(full_path, format_mode)

                result = {
                    "file": os.path.relpath(full_path, folder),
                    "status_filename": file_status,
                    "status_content": content_status,
                    "match": file_status == content_status if file_status and content_status else None
                }

                if file_status and content_status:
                    if file_status != content_status:
                        print(f"❌ Mismatch in '{result['file']}': filename='{file_status}', content='{content_status}'")
                    else:
                        print(f"✅ '{result['file']}' is consistent.")
                elif file_status:
                    print(f"⚠️  '{result['file']}' has a filename status but no internal status.")
                elif content_status:
                    print(f"⚠️  '{result['file']}' has an internal status but no filename status.")
                else:
                    print(f"ℹ️  '{result['file']}' has no detectable status.")

                results.append(result)

    if output_json:
        json_output = json.dumps(results, indent=2)
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"📝 Output written to {output_file}")
        else:
            print("\n--- JSON Output ---\n")
            print(json_output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check status consistency between filename and content.")
    parser.add_argument('folder', nargs='?', default='.', help='Target folder (default: current directory)')
    parser.add_argument('--json', action='store_true', help='Output results as JSON')
    parser.add_argument('--out', help='Output file path for JSON results')
    parser.add_argument('--non-recursive', action='store_true', help='Disable recursive scanning')
    parser.add_argument('--format', choices=['auto', 'yaml', 'markdown'], default='auto',
                        help='Field extraction format: auto (default), yaml, or markdown')
    args = parser.parse_args()

    validate_markdown_status(
        args.folder,
        output_json=args.json,
        output_file=args.out,
        recursive=not args.non_recursive,
        format_mode=args.format
    )
