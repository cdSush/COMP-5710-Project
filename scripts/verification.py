# scripts/verification.py
import json
import argparse
import sys

# set up args so we can pass in file paths from command line
parser = argparse.ArgumentParser()
parser.add_argument("--requirements", "-r", required=True)
parser.add_argument("--test-cases", "-t", required=True)
args = parser.parse_args()

# read in files
with open(args.requirements) as f:
    requirements = json.load(f)

with open(args.test_cases) as f:
    test_cases = json.load(f)

# pull out ids from each file for comparison
tested_ids = {tc["requirement_id"] for tc in test_cases}
req_ids = {req["requirement_id"] for req in requirements}

# find which reqs have test case or not
missing = req_ids - tested_ids
found = req_ids & tested_ids

print(f"---Verification Report---")
print(f"Total requirements: {len(req_ids)}")
print(f"Requirements with test cases: {len(found)}")
print(f"Requirements missing test cases: {len(missing)}")

# if anything is missing, print them out and exit with an error so ci fails
if missing:
    print("\nMissing test coverage for:")
    for m in sorted(missing):
        print(f"  - {m}")
    print("\nverification FAILED")
    sys.exit(1)
else:
    print("\nverification PASSED")