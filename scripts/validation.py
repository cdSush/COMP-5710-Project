# scripts/validation.py
import json
import argparse
import sys

# set up args for the two file paths
parser = argparse.ArgumentParser()
parser.add_argument("--requirements", "-r", required=True)
parser.add_argument("--expected", "-e", required=True)
args = parser.parse_args()

# read in both files
with open(args.requirements) as f:
    requirements = json.load(f)

with open(args.expected) as f:
    expected = json.load(f)

# build the parent children structure from requirements.json for comparison against expected_structure.json
actual = {}
for req in requirements:
    parent = req["parent"]
    req_id = req["requirement_id"]
    # suffix is what comes after parent id
    suffix = req_id[len(parent):]
    if suffix:
        actual.setdefault(parent, [])
        if suffix not in actual[parent]:
            actual[parent].append(suffix)

# check for anything missing or extra compared to expected_structure.json
errors = []
for parent, expected_children in expected.items():
    actual_children = actual.get(parent, [])
    for child in expected_children:
        if child not in actual_children:
            errors.append(f"  MISSING: {parent}{child} not found in requirements")
    for child in actual_children:
        if child not in expected_children:
            errors.append(f"  EXTRA:   {parent}{child} not in expected structure")

print(f"---Validation Report---")
# print and fail any mismatches
if errors:
    for e in errors:
        print(e)
    print("\nvalidation FAILED")
    sys.exit(1)
else:
    print("All structures match expected.")
    print("\nvalidation PASSED")