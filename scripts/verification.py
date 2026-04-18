# scripts/verification.py
import json
import argparse
import sys
import myLogger

logger = myLogger.giveMeLoggingObject() # logging for forensics

# set up args so we can pass in file paths from command line
parser = argparse.ArgumentParser()
parser.add_argument("--requirements", "-r", required=True)
parser.add_argument("--test-cases", "-t", required=True)
args = parser.parse_args()

# LOG 1: tracing inputs (checkpoint)
logger.info(f"FORENSIC ALERT: Starting verification. \nSource: {args.requirements}, \nTests: {args.test_cases}")

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
    # LOG 2: requirement skipped/missing (detection)
    logger.warning(f"FORENSIC ALERT: {len(missing)} requirements are missing test coverage")
    for m in sorted(missing):
        logger.info(f"Missing ID: {m}") # trace each req missing test cases
    print("\nverification FAILED")
    logger.error("FORENSIC ALERT: Verification Result: FAILED")
    sys.exit(1)
else:
    logger.info("FORENSIC ALERT: All requirements have test cases")
    logger.info("FORENSIC ALERT: Verification Result: PASSED")
    print("\nverification PASSED")