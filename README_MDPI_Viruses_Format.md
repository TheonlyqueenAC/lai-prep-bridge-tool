# LAI-PrEP Bridge Algorithm - MDPI Viruses Format

## Summary of Changes

Your manuscript has been successfully reformatted for submission to MDPI's **Viruses** journal. The original Springer Nature format has been converted to meet MDPI's specific requirements.

## New Title

**Computational Validation of a Clinical Decision Support Algorithm for Long-Acting Injectable PrEP Bridge Period Navigation at UNAIDS Global Target Scale**

This title clearly indicates:
- ✅ Computational/algorithmic validation approach
- ✅ Clinical decision support purpose
- ✅ LAI-PrEP bridge period focus
- ✅ UNAIDS global scale (21.2M patients)
- ✅ Policy relevance

## Files Delivered

1. **LAI_PrEP_Bridge_Tool_MDPI_Viruses.tex** - Complete reformatted manuscript
2. **Figure_Specifications.md** - Detailed specifications for 7 suggested figures
3. **This README** - Summary of changes

## Major Format Changes

### 1. Document Class
- Changed from `sn-jnl` (Springer Nature) to `mdpi` with `viruses` journal option
- Updated to MDPI's template structure

### 2. Title and Authors
- Simplified title format (no short title variant)
- Updated author format with ORCID placeholders
- Reformatted affiliations to MDPI style

### 3. Abstract Structure
- Combined the structured abstract sections into a single flowing abstract
- Added "Simple Summary" (required by MDPI for broader audience)
- Removed "Research in Context" sections (Springer-specific)

### 4. Keywords
- Reformatted using MDPI's `\keyword{}` command
- Maintained same keywords for consistency

### 5. Section Structure
- Maintained core section organization (Introduction, Methods, Results, Discussion, Conclusions)
- Removed "Research in Context" subsections
- Combined "Materials and Methods" into single section
- Reformatted all subsections to MDPI style

### 6. Tables
- All 13 tables reformatted with MDPI styling
- Used `\small` for better fit where needed
- Maintained all data and statistical information

### 7. References
- Changed from numbered Vancouver style to MDPI ACS format
- Reformatted all 10 references
- Updated citation format throughout text using `\cite{}`

### 8. End Matter
- Added MDPI-specific sections:
  - Author Contributions
  - Funding
  - Institutional Review Board Statement
  - Informed Consent Statement
  - Data Availability Statement
  - Acknowledgments
  - Conflicts of Interest

### 9. Figures
- Created 7 figure placeholders with detailed captions
- Each includes comments for figure content specifications
- See Figure_Specifications.md for complete details

## What You Need to Do Next

### 1. Required Files
You need to create or obtain the MDPI class file:
- Download from: https://www.mdpi.com/authors/latex
- Place `mdpi.cls` in a `Definitions/` subdirectory
- Or adjust the document class path in the .tex file

### 2. Create Figures
Use the detailed specifications in `Figure_Specifications.md` to create 7 figures:
- Figure 1: Progressive Validation Convergence
- Figure 2: Population-Specific Success Rates
- Figure 3: Regional Health Equity Analysis
- Figure 4: Intervention Impact Forest Plot
- Figure 5: Barrier Dose-Response Relationship
- Figure 6: Decision Support Tool Workflow
- Figure 7: Global Impact Projections

All data needed for figures is provided in the specifications document.

### 3. ORCID IDs
Update these placeholders in the manuscript:
- Line 81-82: Replace `0000-0000-0000-000X` with actual ORCID IDs

### 4. Funding Information
- Line 687: Add funding sources if applicable
- Currently states "no external funding"

### 5. Correspondence Information
- Lines 101-102: Verify correspondence email is correct

## Suggested Graphics (Priority Order)

### ESSENTIAL (Create First):
1. **Figure 2** - Population-specific success rates
   - Most impactful visualization of main findings
   - Shows intervention benefits across populations

2. **Figure 3** - Regional health equity analysis
   - Critical for health equity discussion
   - Includes world map and regional comparisons

3. **Figure 5** - Barrier dose-response
   - Key mechanistic finding showing barrier impact
   - Demonstrates validation consistency

### HIGH PRIORITY:
4. **Figure 7** - Global impact infographic
   - Strong for policy implications
   - Shows ROI and public health impact

5. **Figure 1** - Convergence analysis
   - Important for methods validation
   - Shows progressive precision improvement

### NICE TO HAVE:
6. **Figure 4** - Intervention effectiveness forest plot
   - Alternative visualization of Figure 2 data
   - Good for detailed analysis

7. **Figure 6** - Tool workflow diagram
   - Conceptual/explanatory
   - Helps readers understand implementation

## Key Features Preserved

✅ All statistical data and results maintained
✅ All 13 tables included with full data
✅ Complete progressive validation results (1K → 21.2M)
✅ Regional and population-specific analyses
✅ Health equity gap quantification
✅ Global impact projections
✅ All references properly formatted

## Key Features Added

✅ Simple Summary for broader audience
✅ MDPI-compliant formatting throughout
✅ Detailed figure specifications document
✅ Author contribution statements
✅ Data availability statement
✅ Seven figure placeholders with full captions

## Manuscript Statistics

- **Total Length:** ~8,500 words (excluding references)
- **Tables:** 13 (all core validation data)
- **Figures:** 7 (recommended, with detailed specs)
- **References:** 10 (key clinical trials and guidelines)
- **Sample Sizes Validated:** 1K, 1M, 10M, 21.2M patients

## MDPI Viruses Submission Requirements

When ready to submit:
1. Main manuscript file (.tex or .pdf)
2. All figure files (separate, high resolution)
3. Supplementary materials (if any)
4. Cover letter
5. Suggested reviewers (optional)

**Journal Metrics:**
- Impact Factor: Check current IF on MDPI website
- Open Access: Yes (Article Processing Charge applies)
- Average time to first decision: ~2-4 weeks
- Average time to publication: ~4-6 weeks after acceptance

## Quality Checks Before Submission

- [ ] MDPI class files properly installed
- [ ] All figures created and inserted
- [ ] ORCID IDs updated
- [ ] References verified and complete
- [ ] Funding statement accurate
- [ ] All authors have approved
- [ ] Supplementary materials prepared (if needed)
- [ ] Cover letter written
- [ ] Manuscript compiled successfully without errors

## Technical Notes

**Compilation:**
```bash
pdflatex LAI_PrEP_Bridge_Tool_MDPI_Viruses.tex
bibtex LAI_PrEP_Bridge_Tool_MDPI_Viruses
pdflatex LAI_PrEP_Bridge_Tool_MDPI_Viruses.tex
pdflatex LAI_PrEP_Bridge_Tool_MDPI_Viruses.tex
```

**Hardware Specifications:**
All validation computations were performed on:
- **Processor:** Apple M4 Max
- **Memory:** 36GB unified memory
- **Operating System:** macOS Sequoia 15.5

**Required Packages:** (loaded by mdpi.cls)
- graphicx, amsmath, booktabs, hyperref, cleveref, natbib, and others

## Contact and Support

**MDPI LaTeX Support:** latex@mdpi.com
**Viruses Editorial Office:** viruses@mdpi.com
**MDPI Author Services:** https://www.mdpi.com/authors

## Additional Resources

- MDPI Author Guidelines: https://www.mdpi.com/journal/viruses/instructions
- LaTeX Template Download: https://www.mdpi.com/authors/latex
- Figure Preparation Guidelines: https://www.mdpi.com/authors/figures
- Reference Formatting Tool: https://www.mdpi.com/authors/references

---

## Questions or Issues?

If you encounter any issues with compilation or formatting, the most common causes are:
1. Missing mdpi.cls file in Definitions/ folder
2. Missing figure files
3. Special characters not properly escaped
4. Bibliography style file not found

Refer to the MDPI support resources above or contact latex@mdpi.com with your log file.

---

**Document prepared:** October 12, 2025
**Format:** MDPI Viruses journal
**Status:** Ready for figure insertion and final review before submission
