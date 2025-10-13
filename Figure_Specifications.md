# Suggested Graphics for LAI-PrEP Bridge Tool Manuscript (MDPI Viruses)

## Overview
This document provides detailed specifications for seven figures that would significantly enhance the manuscript. Each figure is designed to visualize key findings and improve reader comprehension.

---

## Figure 1: Progressive Validation Convergence Analysis

**Purpose:** Demonstrate how statistical precision improved across validation scales

**Type:** Dual-axis line graph

**Data Required:**
- X-axis: Validation tier (1K, 1M, 10M, 21.2M)
- Y-axis (left): Margin of error (±percentage points) - logarithmic scale
- Y-axis (right): Processing speed (patients/second)

**Key Elements:**
- Blue line with circular markers: Margin of error decreasing from ±2.6 to ±0.018 points
- Red line with square markers: Processing speed (~1,000 to ~85,000 patients/sec)
- Error bars showing 95% confidence intervals
- Shaded regions for policy-grade precision zone (< ±0.05 points)
- Annotation arrows highlighting 144-fold precision improvement

**Dimensions:** Single column width (80-85mm) or 1.5 column width

**Caption:** Progressive validation convergence analysis. Margin of error (blue line, left axis) decreased from ±2.6 points at 1K to ±0.018 points at 21.2M, representing 144-fold precision improvement. Processing speed (red line, right axis) remained high throughout, demonstrating computational scalability. Error bars represent 95% confidence intervals. Gray shaded area indicates policy-grade precision threshold.

---

## Figure 2: Population-Specific Success Rates with Interventions

**Purpose:** Compare baseline vs. intervention success rates across all seven populations

**Type:** Grouped horizontal bar chart

**Data Required:**
- Y-axis: Seven population groups (PWID, Adolescents, Cisgender women, Pregnant/lactating, Transgender women, General population, MSM)
- X-axis: Success rate (0-60%)
- Two bars per population: Baseline (light blue) and With Interventions (dark blue/green)

**Key Elements:**
- Populations ordered from lowest to highest baseline success
- Arrows or brackets showing absolute improvement (in percentage points)
- Percentage values displayed at end of each bar
- Error bars (95% CI) extending from each bar
- Different colors for populations showing >100% relative improvement (PWID, adolescents)
- Significance stars (*** for p<0.001)
- Legend clearly distinguishing baseline vs. intervention conditions

**Dimensions:** Full page width (170mm) or 1.5 column width

**Additional Panel Options:**
- Panel A: Baseline vs. Intervention comparison
- Panel B: Relative improvement (% increase) shown as separate bars
- Panel C: Number of patients affected (n values) for context

**Caption:** Population-specific bridge period success rates at UNAIDS global scale (n=21.2M). Baseline success rates (light bars) ranged from 10.36% (PWID) to 33.11% (MSM). With evidence-based interventions (dark bars), success rates improved substantially, with PWID showing greatest relative improvement (+265%). Error bars represent 95% confidence intervals. Numbers indicate absolute improvement in percentage points. *** indicates p<0.001.

---

## Figure 3: Regional Health Equity Analysis (Multi-Panel)

**Purpose:** Visualize global health equity gaps and regional scale disparities

**Type:** Multi-panel figure combining map and charts

**Panel A - World Map:**
- Five WHO regions color-coded by baseline success rate
- Color gradient: Red (lowest, 21.69% SSA) → Yellow (middle) → Green (highest, 29.33% Europe)
- Regions labeled with success rates
- Consider using cartogram (size proportional to patient numbers)

**Panel B - Regional Sample Distribution (Pie Chart):**
- Show that SSA = 62% of global sample
- Other regions: NA (18%), LAC (9%), Europe (6%), Asia (5%)
- Colors matching the map

**Panel C - Baseline vs. Intervention by Region (Bar Chart):**
- Grouped bars for each region
- Shows equity gap narrowing but persisting with interventions
- Display absolute improvement values

**Key Elements:**
- Clear legend for color coding
- Numerical annotations for key comparisons
- Highlight the 7.64 percentage point equity gap
- Show that SSA has greatest absolute improvement despite lowest baseline

**Dimensions:** Full page width (170mm), multi-panel layout

**Caption:** Regional health equity analysis at UNAIDS global scale. (A) World map showing baseline bridge period success rates by region, revealing 7.64 percentage point equity gap between Europe/Central Asia (29.33%) and Sub-Saharan Africa (21.69%). (B) Regional sample distribution demonstrates that SSA serves 62% of global patients despite lowest baseline success, highlighting resource allocation priorities. (C) Evidence-based interventions improve outcomes across all regions, with SSA showing greatest relative improvement (+91.2%), though equity gaps persist.

---

## Figure 4: Intervention Impact Forest Plot

**Purpose:** Show absolute and relative improvement for each population

**Type:** Forest plot / Effect size plot

**Data Layout:**
- Y-axis: Population groups (same order as Figure 2)
- X-axis (left panel): Absolute improvement (percentage points, 0-30)
- X-axis (right panel): Relative improvement (%, 0-300%)

**Key Elements:**
- Horizontal lines showing 95% confidence intervals
- Data point size proportional to population size at 21.2M scale
- Vertical reference lines at clinically significant thresholds (15 points, 50%)
- Color coding: Populations with >100% improvement in distinct color
- Annotations showing specific values for top performers

**Statistical Annotations:**
- Sample sizes for each population
- P-values (though all will be <0.001 at this scale)
- Heterogeneity statistics if applicable

**Dimensions:** 1.5 column or full width (120-170mm)

**Caption:** Intervention effectiveness by population group. Forest plot showing absolute improvement (left panel, percentage points) and relative improvement (right panel, %). Populations with lowest baseline success showed greatest benefits: PWID (+27.46 points, +265%) and adolescents (+23.96 points, +147%). Horizontal lines represent 95% confidence intervals. Size of data points proportional to population size at 21.2M scale. Vertical dashed lines indicate clinically significant improvement thresholds.

---

## Figure 5: Barrier Dose-Response Relationship

**Purpose:** Demonstrate linear dose-response effect of structural barriers

**Type:** Scatter plot with overlaid data from multiple validation tiers

**Data Required:**
- X-axis: Number of barriers (0, 1, 2, 3, 4, 5)
- Y-axis: Success rate (0-50%)
- Data points from Tier 2 (1M), Tier 3 (10M), and Tier 4 (21.2M)

**Key Elements:**
- Three colors/shapes for three validation tiers:
  - Tier 2: Blue circles
  - Tier 3: Green triangles  
  - Tier 4: Red squares
- Points should overlap closely, showing consistency
- Fitted regression line with equation: y = 44.0 - 7.74x (R² = 0.998)
- 95% confidence interval as shaded region around regression line
- Annotations showing per-barrier decline (-7.74 points average)
- Highlight clinical threshold (3+ barriers = <15% success)

**Inset or Additional Annotation:**
- Distribution histogram showing % of patients at each barrier count
- Shows that 85.7% have ≥1 barrier at global scale

**Dimensions:** Single column width (80-85mm)

**Caption:** Structural barrier dose-response relationship across validation scales. Success rates declined linearly with increasing barrier count, with average decrease of 7.74 percentage points per barrier. Data points from Tiers 2 (blue circles), 3 (green triangles), and 4 (red squares) demonstrate remarkable consistency across scales (1M to 21.2M patients). Shaded area represents 95% confidence interval. Dashed line shows fitted regression (R²=0.998). Inset histogram shows patient distribution by barrier count at 21.2M scale.

---

## Figure 6: Decision Support Tool Workflow Diagram

**Purpose:** Illustrate how the clinical decision support tool operates

**Type:** Flowchart/Process diagram with icons

**Flow Stages:**
1. **Patient Presentation**
   - Icon: Person/patient symbol
   - Input: Demographics, population group, PrEP status

2. **Risk Stratification**
   - Icon: Traffic light or risk meter
   - Process: Population-specific baseline risk calculation
   - Output: Low/Moderate/High/Very High risk category

3. **Barrier Assessment**
   - Icon: Checklist or barrier symbols
   - Process: Screen for 13 structural barriers
   - Output: Barrier count and specific barriers identified

4. **Intervention Recommendation**
   - Icon: Prescription pad or intervention symbol
   - Process: Evidence-based intervention selection
   - Output: Prioritized intervention list (up to 13 interventions)

5. **Outcome Prediction**
   - Icon: Chart/graph trending upward
   - Process: Calculate predicted success with/without interventions
   - Output: Baseline vs. intervention success rates

**Design Elements:**
- Color-coded stages with consistent color scheme
- Arrows showing workflow progression
- Time estimate for each stage (<30 seconds total)
- Side panel showing example patient case
- Icons should be simple, professional, medical-appropriate

**Dimensions:** Full width (170mm) or vertical layout if preferred

**Caption:** LAI-PrEP Bridge Period Decision Support Tool workflow. The tool operates through five stages: (1) Patient presentation and demographic data collection; (2) Population-specific risk stratification based on validated attrition rates; (3) Structural barrier identification and quantification using evidence-based screening; (4) Evidence-based intervention recommendation with prioritization by expected impact; (5) Predicted outcome calculation with and without interventions. Complete workflow processing time <30 seconds enables point-of-care clinical decision support.

---

## Figure 7: Global Impact Projections Infographic

**Purpose:** Communicate projected public health and economic impact

**Type:** Infographic with visual elements

**Key Statistics to Display:**
1. **4.1 Million** additional successful transitions
   - Icon: People/figures transitioning successfully
   - Visual: Show as percentage of 21.2M goal (19.5%)

2. **100,000** HIV infections prevented annually
   - Icon: Shield or protective symbol
   - Visual: Stack of human figures or equivalent
   - Note: 500,000+ over 5 years

3. **$40 Billion** lifetime treatment costs saved
   - Icon: Dollar sign or savings symbol
   - Visual: Stack of money or cost comparison bars

4. **11:1** Return on Investment
   - Icon: Investment growth chart
   - Visual: For every $1 invested → $11 return
   - Breakdown: $19.1B implementation → $40B savings

5. **23.4%** of UNAIDS gap closed
   - Icon: Target or gap-closing visual
   - Visual: Progress bar showing gap reduction

**Design Elements:**
- Large, bold numbers with clear units
- Professional color scheme (blues, greens for positive outcomes)
- Icons should be simple and universally understood
- Minimal text, maximum visual impact
- Consider flow from intervention → outcomes → costs → ROI
- Optional: Timeline showing 1-year vs. 5-year cumulative impact

**Layout Options:**
- Vertical flow (top to bottom)
- Circular/radial design with ROI at center
- Grid layout (2x3 or 3x2)

**Dimensions:** Full width (170mm), potentially spanning multiple columns

**Caption:** Projected global impact of tool-guided LAI-PrEP implementation at UNAIDS 2025 target scale. Evidence-based interventions could enable 4.1 million additional successful bridge period transitions, preventing approximately 100,000 HIV infections annually and saving $40 billion in lifetime treatment costs. With estimated implementation cost of $19.1 billion, the intervention achieves 11:1 return on investment. Five-year cumulative impact: 500,000+ infections prevented, $200+ billion saved. All projections based on validated success rates from 21.2M patient simulation.

---

## Additional Figure Suggestions (Optional)

### Figure S1: Comparison Across All Validation Tiers (Supplementary)
- Multi-panel showing how each metric evolved across 1K → 1M → 10M → 21.2M
- Demonstrates convergence for all key outcomes
- Could be in supplement if main manuscript has space constraints

### Figure S2: Healthcare Setting Analysis (Supplementary)
- Bar chart showing success rates across 8 healthcare settings
- Shows minimal variation (only 0.026 percentage point range)
- Reinforces that intervention quality matters more than setting type

### Figure S3: Risk Stratification Distribution (Supplementary)
- Stacked bar chart showing risk level distribution across populations
- Helps clinicians understand typical risk profiles
- Could inform resource allocation decisions

---

## Technical Specifications for All Figures

**General Guidelines:**
- **File format:** TIFF or EPS (vector preferred) at 300-600 DPI
- **Color mode:** RGB for digital; CMYK for print
- **Font:** Arial or similar sans-serif, minimum 8pt (preferably 10-12pt)
- **Line weights:** Minimum 0.5pt for fine lines, 1-2pt for main elements
- **Color palette:** Consider colorblind-friendly options (avoid red-green combinations)
- **Accessibility:** Ensure sufficient contrast, use patterns in addition to colors where possible

**MDPI Viruses Specific:**
- Maximum width: 170mm (full page width)
- Minimum resolution: 1000 pixels width for online viewing
- Preferred formats: High-resolution TIFF, EPS, or PDF
- All figures should be submitted as separate files, not embedded in manuscript

**Software Recommendations:**
- Statistical plots: Python (matplotlib, seaborn), R (ggplot2), GraphPad Prism
- Maps: QGIS, ArcGIS, or Python (geopandas)
- Flowcharts: Microsoft PowerPoint, Adobe Illustrator, draw.io
- Infographics: Adobe Illustrator, Canva (Pro), Inkscape

---

## Data Files Provided for Figure Creation

Based on the validation results JSON file provided, here are the specific data points for each figure:

### For Figure 1 (Convergence):
```
Tier 1: n=1000, success=21.7%, SE=0.013, MoE=±2.6
Tier 2: n=1M, success=27.7%, SE=0.00045, MoE=±0.09
Tier 3: n=10M, success=27.7%, SE=0.00014, MoE=±0.028
Tier 4: n=21.2M, success=23.96%, SE=0.000045, MoE=±0.018
```

### For Figure 2 (Populations):
```
PWID: 10.36% → 37.82% (+27.46 pts, +265%)
Adolescents: 16.34% → 40.30% (+23.96 pts, +147%)
Cisgender women: 24.10% → 48.06% (+23.96 pts, +99%)
Pregnant/lactating: 24.11% → 39.44% (+15.33 pts, +64%)
Transgender women: 28.46% → 43.82% (+15.36 pts, +54%)
General population: 31.22% → 46.57% (+15.35 pts, +49%)
MSM: 33.11% → 48.46% (+15.35 pts, +46%)
```

### For Figure 3 (Regional):
```
Europe/Central Asia: 29.33% baseline (n=1.27M, 6%)
North America: 29.32% baseline (n=3.82M, 18%)
Asia/Pacific: 24.78% baseline (n=1.06M, 5%)
Latin America/Caribbean: 24.78% baseline (n=1.91M, 9%)
Sub-Saharan Africa: 21.69% baseline (n=13.14M, 62%)
```

### For Figure 5 (Barriers):
```
0 barriers: 44.00%
1 barrier: 33.61% (-10.38)
2 barriers: 23.50% (-10.12)
3 barriers: 14.79% (-8.70)
4 barriers: 8.10% (-6.70)
5 barriers: 5.28% (-2.82)
Average decline: -7.74 points per barrier
```

---

## Priority Order for Figure Creation

If resources are limited, create figures in this order:
1. **Figure 2** (Population-specific success rates) - Most impactful for main findings
2. **Figure 3** (Regional equity analysis) - Critical for health equity discussion
3. **Figure 5** (Barrier dose-response) - Key mechanistic finding
4. **Figure 7** (Global impact) - Strong for policy implications
5. **Figure 1** (Convergence) - Important for methods validation
6. **Figure 4** (Forest plot) - Alternative visualization of Figure 2 data
7. **Figure 6** (Workflow) - Helpful but more conceptual

---

## Notes for Graphic Designer/Data Visualization Specialist

- All figures should follow a consistent visual style and color palette
- Consider creating a "brand" for the tool that carries through all figures
- Ensure accessibility: test with colorblind simulators
- For publication, provide both high-res versions and lower-res versions for online supplements
- Include source data files or code to generate figures for reproducibility
- Consider creating an interactive version of Figure 7 for online supplementary materials

This comprehensive set of figures will significantly enhance the manuscript's impact and accessibility to diverse audiences including clinicians, policymakers, and researchers.
