#!/usr/bin/env python3
"""
GitHub Readiness Verification Script
Checks if all necessary files are present before pushing to GitHub
"""

import os
import sys
from pathlib import Path


def check_file(filepath, required=True):
    """Check if a file exists and return status"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else ("❌" if required else "⚠️")
    req_text = "(REQUIRED)" if required else "(recommended)"
    return exists, f"{status} {filepath} {req_text}"


def main():
    print("=" * 70)
    print("LAI-PrEP Tool - GitHub Readiness Check")
    print("=" * 70)
    print()

    # Track overall status
    all_required_present = True

    # Define files to check
    files_to_check = {
        "CRITICAL (must have)": [
            ("lai_prep_decision_tool_v2_1.py", True),
            ("lai_prep_config.json", True),
            ("lai_prep_config_FIXED.json", True),  # Check for FIXED version
            ("test_edge_cases.py", True),
            ("README.md", True),
        ],
        "HIGHLY RECOMMENDED": [
            ("START_HERE.md", False),
            ("QUICK_REFERENCE.md", False),
            ("CHANGELOG.md", False),
        ],
        "DOCUMENTATION": [
            ("TEST_FIXES_AND_ANALYSIS.md", False),
            ("EXECUTIVE_SUMMARY.md", False),
            ("COMPLETE_PROJECT_SUMMARY.md", False),
            ("MANUSCRIPT_INTEGRATION_GUIDE.md", False),
        ],
        "REPOSITORY STANDARD": [
            (".gitignore", False),
            ("LICENSE", False),
            ("requirements.txt", False),
        ],
        "MANUSCRIPT FILES": [
            ("MANUSCRIPT_REVISIONS.tex", False),
        ]
    }

    # Check each category
    for category, files in files_to_check.items():
        print(f"\n{category}:")
        print("-" * 50)

        for filepath, required in files:
            exists, message = check_file(filepath, required)
            print(f"  {message}")

            if required and not exists:
                all_required_present = False

    # Special checks
    print("\n" + "=" * 70)
    print("SPECIAL CHECKS:")
    print("-" * 50)

    # Check if using FIXED config
    has_original = os.path.exists("lai_prep_config.json")
    has_fixed = os.path.exists("lai_prep_config_FIXED.json")

    if has_fixed and not has_original:
        print("  ⚠️  ATTENTION: Rename lai_prep_config_FIXED.json to lai_prep_config.json")
        print("     OR include both and document which to use")
    elif has_original and has_fixed:
        print("  ✅ Both config files present - document which to use in README")
    elif has_original and not has_fixed:
        print("  ⚠️  WARNING: Only original config found - may have test failures")
        print("     Consider using the FIXED version from previous chat")

    # Check for Python cache
    if os.path.exists("__pycache__"):
        print("  ⚠️  __pycache__ directory exists - ensure .gitignore is set up")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY:")
    print("-" * 50)

    if all_required_present:
        print("  ✅ All required files are present!")
        print("  ✅ Ready to push to GitHub")
        print()
        print("  Next steps:")
        print("    1. Review GITHUB_PUSH_CHECKLIST.md")
        print("    2. Ensure you're using the FIXED config")
        print("    3. Run: git init (if not already done)")
        print("    4. Run: git add .")
        print("    5. Run: git commit -m 'Initial commit'")
        print("    6. Create GitHub repo and push")
    else:
        print("  ❌ Some required files are missing")
        print("  📋 Review the checklist above")
        print("  📁 Locate missing files from previous chats")
        print()
        print("  Missing files are marked with ❌")
        print("  You can find them in previous chat outputs")

    # Additional recommendations
    if not os.path.exists("README.md"):
        print("\n  💡 TIP: README.md should include:")
        print("     - Project description")
        print("     - Installation instructions")
        print("     - Usage examples")
        print("     - Test results (94% pass rate)")
        print("     - Citation information")

    print("\n" + "=" * 70)
    print()

    return 0 if all_required_present else 1


if __name__ == "__main__":
    sys.exit(main())