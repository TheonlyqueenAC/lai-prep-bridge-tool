# LAI-PrEP Bridge Period Decision Support Tool - Usage Guide

## Overview

This tool helps clinicians and healthcare systems assess bridge period success probability, identify barriers, and implement evidence-based interventions for Long-Acting Injectable Pre-Exposure Prophylaxis (LAI-PrEP) implementation.

## Key Features

1. **Risk Assessment**: Calculates baseline and adjusted bridge period success rates
2. **Population-Specific Analysis**: Tailored predictions for MSM, women, adolescents, PWID, etc.
3. **Barrier Identification**: Evaluates 13 different structural barriers
4. **Evidence-Based Recommendations**: Prioritized interventions with expected impact
5. **Outcome Prediction**: Estimates success rates with recommended interventions

## Installation & Requirements

```bash
# Requires Python 3.7 or higher
# No additional dependencies needed - uses only standard library

python3 lai_prep_decision_tool.py
```

## Quick Start

### Run Example Cases
```python
python3 lai_prep_decision_tool.py
```

This will run 4 example cases demonstrating different risk profiles:
- MSM on oral PrEP (best case scenario)
- Adolescent with multiple barriers (high risk)
- Person who injects drugs (very high risk)
- Woman re-engaging after oral PrEP discontinuation

### Create Custom Assessment

```python
from lai_prep_decision_tool import (
    LAIPrEPDecisionTool, 
    PatientProfile, 
    Population, 
    Barrier,
    HealthcareSetting
)

# Initialize tool
tool = LAIPrEPDecisionTool()

# Create patient profile
profile = PatientProfile(
    population=Population.CISGENDER_WOMEN,
    age=28,
    current_prep_status="naive",  # Options: "naive", "oral_prep", "discontinued_oral"
    recent_hiv_test=False,  # HIV test within 7 days
    healthcare_setting=HealthcareSetting.COMMUNITY_HEALTH_CENTER,
    barriers=[
        Barrier.TRANSPORTATION,
        Barrier.CHILDCARE,
        Barrier.MEDICAL_MISTRUST
    ],
    insurance_status="insured"  # Options: "insured", "uninsured", "underinsured"
)

# Perform assessment
assessment = tool.assess_patient(profile)

# Generate report
report = tool.generate_report(profile, assessment)
print(report)
```

## Available Options

### Populations
- `Population.MSM` - Men who have sex with men
- `Population.CISGENDER_WOMEN` - Cisgender women
- `Population.TRANSGENDER_WOMEN` - Transgender women
- `Population.ADOLESCENT` - Adolescents (16-24 years)
- `Population.PWID` - People who inject drugs
- `Population.PREGNANT_LACTATING` - Pregnant/lactating individuals
- `Population.GENERAL` - General population

### Healthcare Settings
- `HealthcareSetting.ACADEMIC_MEDICAL_CENTER`
- `HealthcareSetting.COMMUNITY_HEALTH_CENTER`
- `HealthcareSetting.PRIVATE_PRACTICE`
- `HealthcareSetting.PHARMACY`
- `HealthcareSetting.HARM_REDUCTION` - SSP/harm reduction services
- `HealthcareSetting.LGBTQ_CENTER`
- `HealthcareSetting.MOBILE_CLINIC`
- `HealthcareSetting.TELEHEALTH`

### Barriers
- `Barrier.TRANSPORTATION`
- `Barrier.CHILDCARE`
- `Barrier.HOUSING_INSTABILITY`
- `Barrier.INSURANCE_DELAYS`
- `Barrier.SCHEDULING_CONFLICTS`
- `Barrier.MEDICAL_MISTRUST`
- `Barrier.PRIVACY_CONCERNS`
- `Barrier.HEALTHCARE_DISCRIMINATION`
- `Barrier.COMPETING_PRIORITIES`
- `Barrier.LIMITED_NAVIGATION_EXPERIENCE`
- `Barrier.LEGAL_CONCERNS`
- `Barrier.LACK_IDENTIFICATION`
- `Barrier.SUBSTANCE_USE`

### Interventions (Automatically Recommended)
- Oral-to-injectable transitions (85-90% success)
- Same-day switching protocols
- Patient navigation programs
- Accelerated HIV testing (RNA + Ag/Ab)
- Transportation support
- Childcare support
- Text message navigation
- Peer navigation
- Telehealth counseling
- Expedited insurance authorization
- Mobile/community-based delivery
- Harm reduction integration
- Bundled payment models

## Evidence Base

The tool is based on:
- **Clinical Trials**: HPTN 083 (4,566 MSM/transgender women), HPTN 084 (3,224 women), PURPOSE-1 (5,338 women), PURPOSE-2 (2,183 diverse participants)
- **Real-World Data**: CAN Community Health Network Study (52.9% injection initiation rate)
- **Implementation Studies**: San Francisco PrEP navigation, Trio Health persistence data, Atlanta Ryan White Clinics

### Key Evidence
- LAI-PrEP efficacy: >96% across all populations
- Persistence once initiated: 81-83% (vs. ~52% for oral PrEP)
- Bridge period attrition: 47% overall (varies by population)
- Oral-to-injectable success: 85-90% (vs. 53% for PrEP-naive)

## Clinical Use Cases

### 1. Individual Patient Assessment
Use before LAI-PrEP prescription to:
- Predict likelihood of successful initiation
- Identify barriers requiring proactive intervention
- Select evidence-based interventions

### 2. Program Planning
Use for population-level planning:
- Compare success rates across different delivery models
- Estimate resource needs for navigation programs
- Prioritize interventions based on local population

### 3. Quality Improvement
Use for implementation monitoring:
- Track actual vs. predicted success rates
- Identify gaps in intervention delivery
- Guide program modifications

### 4. Research & Evaluation
Use for implementation science:
- Stratify populations for targeted studies
- Compare intervention effectiveness
- Model cost-effectiveness scenarios

## Interpreting Results

### Success Rate Predictions
- **>70%**: Low attrition risk - standard protocols appropriate
- **55-70%**: Moderate risk - navigation recommended
- **40-55%**: High risk - multiple interventions needed
- **<40%**: Very high risk - intensive support required

### Intervention Priorities
- **Critical**: Must implement for reasonable success probability
- **High**: Strongly recommended, substantial impact expected
- **Moderate**: Beneficial but not essential

### Expected Improvements
Numbers represent percentage point improvements in success rate:
- **>30 points**: Transformative (e.g., same-day switching)
- **15-30 points**: High impact (e.g., navigation, harm reduction integration)
- **8-15 points**: Moderate impact (e.g., barrier-specific interventions)
- **<8 points**: Incremental (e.g., SMS reminders)

## Limitations

1. **Population-level predictions**: Individual outcomes may vary
2. **Additive model**: Assumes interventions have independent effects (reality: synergistic)
3. **Limited real-world data**: Some populations lack implementation evidence (PURPOSE-3, 4, 5 ongoing)
4. **Setting-specific factors**: Local context may affect baseline rates
5. **Conservative estimates**: Tool uses conservative (lower) estimates where evidence varies

## Updates & Future Development

This tool will be updated as:
- PURPOSE-3 (U.S. women), PURPOSE-4 (PWID), PURPOSE-5 (global) data emerge
- HPTN 102/103 implementation studies report results
- Real-world implementation data accumulates
- Once-yearly lenacapavir enters Phase 3

## Citation

If using this tool in research or clinical programs, please cite:

Demidont, A.C.; Backus, K. (2025). Bridging the Gap: The PrEP Cascade Paradigm Shift for Long-Acting Injectable HIV Prevention. *Viruses*, 1, 0.

## Support & Contact

For questions, bug reports, or feature requests:
- Email: acdemidont@nyxdynamics.org
- GitHub: [Add repository URL]

## License

[Specify license - MIT, Apache 2.0, etc.]

---

**Disclaimer**: This tool is for clinical decision support only. It does not replace clinical judgment and should be used in conjunction with current CDC and WHO guidelines for LAI-PrEP implementation.
