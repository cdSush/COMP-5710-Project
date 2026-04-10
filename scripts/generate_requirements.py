# scripts/generate_requirements.py
"""
This script parses a Markdown file containing requirements and atomic rules, then generates a structured JSON file with requirement details.
Arguments:
    --input / -i   : Path to the input Markdown (.md) file containing requirements.
    --output / -o  : Path to the output JSON file where parsed requirements will be saved.
    --cfr / -c     : CFR section identifier (e.g., "21 CFR 117.130") to be used as the "source" field for each requirement.
                     This argument is treated as a string and can contain spaces; if using in a terminal, enclose in quotes (e.g., "21 CFR 117.130").
Functionality:
    - Reads the input Markdown file, extracting requirement IDs and atomic rule descriptions.
    - Associates each atomic rule with its parent requirement and the provided CFR section.
    - Outputs a JSON file containing a list of requirement objects, each with an ID, description, source, and parent.
Note:
    The CFR section argument is not validated for format; it is used as provided.
"""
import json
import re
import argparse

def rightmost_alpha(req_id):
    matches = re.findall(r'[A-Za-z]', req_id)
    return matches[-1] if matches else None

# ---------- Arguments ----------
parser = argparse.ArgumentParser(description="Generate requirement JSON from CFR Markdown")
parser.add_argument("--input", "-i", required=True, help="Input Markdown file (.md)")
parser.add_argument("--output", "-o", required=True, help="Output JSON file")
parser.add_argument("--structure", "-s", required=True, help="Output structured JSON file")
parser.add_argument("--cfr", "-c", required=True, help="CFR section (e.g., 21 CFR 117.130)")
args = parser.parse_args()

INPUT_MD = args.input
OUTPUT_REQUIREMENTS_JSON = args.output
OUTPUT_STRUCTURED_JSON = args.structure
CFR_SECTION = args.cfr

# ---------- Read File ----------
with open(INPUT_MD, "r") as f:
    lines = [line.strip() for line in f if line.strip()]


requirements = []
structure_map = {}
current_req = None

arrow_pattern = r"(?:→|\\u2192)"
# ---------- Parse ----------
for line in lines:

    # Fix bad character conversion from file read
    line = line.replace("Â§", "§").replace("â€“", "–").replace("â†’", "→")
    # Capture REQ ID
    req_match = re.search(rf"{arrow_pattern}\s*(REQ-[\d\.]+-\d+)", line)
    if req_match:
        current_req = req_match.group(1)
        continue

    # Capture atomic rules
    atomic_match = re.match(rf"^(.*?)\s*{arrow_pattern}\s*([A-Z]\d*)$", line)
    if atomic_match and current_req:
        description = atomic_match.group(1).strip()
        suffix = atomic_match.group(2)

        requirement_id = f"{current_req}{suffix}"

        # Parent logic
        if len(suffix) == 1:
            parent = current_req
        else:
            parent = f"{current_req}{suffix[0]}"

        requirements.append({
            "requirement_id": requirement_id,
            "description": description,
            "source": CFR_SECTION,
            "parent": parent
        })

        structure_char = rightmost_alpha(requirement_id)
        if parent[-1:].isalpha():
            while parent[-1:].isalpha():
                parent = parent[:-1]
                if parent in structure_map:
                    if structure_char not in structure_map[parent]:
                        structure_map[parent].append(structure_char)
                else:
                    structure_map[parent] = [structure_char]
        else:
            if parent in structure_map:
                if structure_char not in structure_map[parent]:
                    structure_map[parent].append(structure_char)
            else:
                structure_map[parent] = [structure_char]


# ---------- Save ----------
with open(OUTPUT_REQUIREMENTS_JSON, "w") as f:
    json.dump(requirements, f, indent=2)

with open(OUTPUT_STRUCTURED_JSON, "w") as f:
    json.dump(structure_map, f, indent=2)

print(f"Saved {len(requirements)} requirements → {OUTPUT_REQUIREMENTS_JSON}")

