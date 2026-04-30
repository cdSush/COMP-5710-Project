# COMP-5710-Project
Final Project for COMP 5710: Software Quality Assurance

Members:
- Cole Suchan (cds0122)
- Bryson LeBlanc (bwl0016)
- Helen Grogan (hkg0017)

This project uses Python scripts, JSON files, and GitHub Actions to verify and validate regulatory requirements from 21 CFR 117.130.

## Project Objectives

- Parse a CFR markdown file into structured atomic requirements
- Generate test cases for selected requirements
- Verify that all requirements have corresponding test cases
- Validate that requirement structure matches expected structure
- Automate all checks using GitHub Actions on every push

## Prerequisites

- Python 3.8 or higher
- Git
- No additional packages needed, all scripts use Python standard library

## How to Reproduce Locally

Clone the repo:

    git clone https://github.com/ColeHelenBryson/ColeHelenBryson-SQA2026-AUBURN.git
    cd ColeHelenBryson-SQA2026-AUBURN

The 10 selected requirements, expected structure, and test cases are already in the real outputs/ folder. To run verification and validation against them:

### Windows

    python scripts/verification.py -r "real outputs/requirements.json" -t "real outputs/test_cases.json"

    python scripts/validation.py -r "real outputs/requirements.json" -e "real outputs/expected_structure.json"

### Mac/Linux

    python3 scripts/verification.py -r "real outputs/requirements.json" -t "real outputs/test_cases.json"

    python3 scripts/validation.py -r "real outputs/requirements.json" -e "real outputs/expected_structure.json"

Note: generate_requirements.py and generate_test_cases.py are also in the scripts/ folder if you want to see how the outputs were originally generated. Pointing them at real outputs/ will overwrite the curated 10-rule selection, so write to a different folder if you run them.

## CI with GitHub Actions

The workflow in .github/workflows/project-action.yml runs on every push to main. It has three jobs: build, run-verification, and run-validation. Both verification and validation need to pass for the build to succeed.

## Expected Output

Verification:

    ---Verification Report---
    Total requirements: 10
    Requirements with test cases: 10
    Requirements missing test cases: 0

    verification PASSED

Validation:

    ---Validation Report---
    All structures match expected.

    validation PASSED