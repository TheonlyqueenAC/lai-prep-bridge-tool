feat(decision-tool): add best-case success floor for zero-barrier oral PrEP with recent HIV test

- Introduces `best_case_success_floor` parameter (default 0.85)
- Applies when current_prep_status == "oral_prep", recent_hiv_test is True, and there are no barriers
- Ensures best-case adjusted success rate is not underestimated, aligning with real-world outcomes when the bridge can be eliminated
- Preserves existing baseline and adjusted calculations; risk categorization logic unchanged

docs(readme): add guidance for re-running tests after upgrades

- Documented how to install dev requirements and run the test suite
- Added examples for verbose/quiet modes and running pytest directly
- Included instructions on reporting failures with environment details

chore(assets): add updated figure5.png

- Adds new version of Figure 5 asset used in documentation

Co-authored-by: AI Assistant <noreply@example.com>
Date: 2025-10-17 03:07 local
