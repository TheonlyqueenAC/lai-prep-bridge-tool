# LAI-PrEP Bridge Period Decision Support Tool v2.0

## Configuration-Driven Architecture

### Overview

The LAI-PrEP Bridge Period Decision Support Tool helps clinicians and healthcare systems assess bridge period success probability, identify population-specific barriers, recommend evidence-based interventions, and estimate improved outcomes for patients prescribed long-acting injectable pre-exposure prophylaxis (LAI-PrEP).

**Version 2.0** introduces a configuration-driven architecture that separates clinical evidence parameters from code logic, enabling rapid updates without code changes.

### Key Features

✅ **Evidence-Based**: Built on data from HPTN 083, 084, PURPOSE-1, PURPOSE-2 (>15,000 participants)  
✅ **Validated at Scale**: Computationally validated on 21.2M patients (UNAIDS global target)  
✅ **Configuration-Driven**: All parameters externalized to JSON for easy updates  
✅ **Population-Specific**: Tailored predictions for 7 key populations  
✅ **Barrier-Aware**: Identifies and quantifies 13 structural barriers  
✅ **Intervention-Focused**: Recommends from 13 evidence-based interventions  
✅ **Setting-Adapted**: Optimized for 8 healthcare delivery settings  

### What's New in v2.0

#### Configuration System
- **External Configuration**: All clinical parameters in `lai_prep_config.json`
- **No Code Changes Needed**: Update evidence without touching Python code
- **Version Control**: Configuration includes version tracking and evidence sources
- **Validation**: Automatic validation of configuration integrity

#### Enhanced Features
- **Evidence Levels**: Each parameter tagged with evidence quality (strong/moderate/emerging)
- **Cost & Complexity**: Interventions rated for implementation planning
- **Regional Data**: Includes UNAIDS global distribution parameters
- **Flexible Enums**: Population/barrier/intervention enums created from config

#### Improved Clinical Guidance
- **Structured Notes**: Clinical guidance organized by context
- **Risk Categories**: Four-level risk stratification with actionable guidance
- **Implementation Details**: Cost and complexity ratings for each intervention

### Installation

```bash
# Clone or download the files
# Ensure both files are in the same directory:
# - lai_prep_decision_tool_v2.py
# - lai_prep_config.json

# No external dependencies required (pure Python 3.7+)
python3 lai_prep_decision_tool_v2.py
```

### Quick Start

#### Basic Usage

```python
from lai_prep_decision_tool_v2 import LAIPrEPDecisionTool, PatientProfile

# Initialize tool (automatically finds config file)
tool = LAIPrEPDecisionTool()

# Create patient profile
profile = PatientProfile(
    population="CISGENDER_WOMEN",
    age=25,
    current_prep_status="naive",
    barriers=["TRANSPORTATION", "CHILDCARE"],
    healthcare_setting="COMMUNITY_HEALTH_CENTER",
    insurance_status="insured"
)

# Assess patient
assessment = tool.assess_patient(profile)

# Generate clinical report
report = tool.generate_report(profile, assessment)
print(report)
```

#### Using Custom Configuration

```python
# Specify custom config file location
tool = LAIPrEPDecisionTool(config_path="/path/to/custom_config.json")
```

### Configuration Structure

The `lai_prep_config.json` file contains all clinical parameters:

```json
{
  "version": "2.0.0",
  "populations": {
    "MSM": {
      "name": "Men who have sex with men",
      "baseline_attrition": 0.45,
      "evidence_level": "strong",
      "evidence_source": "HPTN 083 (n=4,566)",
      ...
    }
  },
  "barriers": {
    "TRANSPORTATION": {
      "name": "Transportation barriers",
      "impact": 0.10,
      "evidence_level": "strong",
      ...
    }
  },
  "interventions": {
    "PATIENT_NAVIGATION": {
      "name": "Patient navigation program",
      "improvement": 0.15,
      "evidence_level": "strong",
      "cost_level": "medium",
      ...
    }
  }
}
```

### Populations Supported

1. **MSM** - Men who have sex with men
2. **CISGENDER_WOMEN** - Cisgender women  
3. **TRANSGENDER_WOMEN** - Transgender women
4. **ADOLESCENT** - Adolescents (16-24 years)
5. **PWID** - People who inject drugs
6. **PREGNANT_LACTATING** - Pregnant/lactating individuals
7. **GENERAL** - General population

### Barriers Identified

The tool assesses 13 structural barriers:

- **Transportation** - Lack of reliable transportation
- **Childcare** - Need for childcare during appointments
- **Housing Instability** - Homelessness or unstable housing
- **Insurance Delays** - Prior authorization requirements
- **Scheduling Conflicts** - Work/school conflicts
- **Medical Mistrust** - Historical/ongoing medical racism
- **Privacy Concerns** - Disclosure concerns
- **Healthcare Discrimination** - Past discrimination experiences
- **Competing Priorities** - Other health/life needs
- **Limited Navigation Experience** - Lack of healthcare navigation skills
- **Legal Concerns** - Criminalization fears
- **Lack of Identification** - Missing government ID
- **Substance Use** - Active substance use (harm reduction: no abstinence required)

### Interventions Recommended

The tool recommends from 13 evidence-based interventions:

**Strategy 1: Eliminate the Bridge**
- Oral-to-injectable transition (+35 pts)
- Same-day switching protocol (+40 pts)

**Strategy 2: Compress the Bridge**
- Accelerated HIV testing (+10 pts)

**Strategy 3: Navigate the Bridge**
- Patient navigation program (+15 pts)
- Peer navigation support (+12 pts)
- SMS/text message navigation (+5 pts)

**Barrier-Specific Interventions**
- Transportation support (+8 pts)
- Childcare support (+8 pts)
- Expedited authorization (+10 pts)
- Mobile delivery (+12 pts)
- Harm reduction integration (+15 pts)

**System-Level**
- Telehealth counseling (+6 pts)
- Bundled payment model (+8 pts)

### Healthcare Settings

Optimized for 8 delivery settings:

1. Academic Medical Center
2. Community Health Center
3. Private Practice
4. Pharmacy-Based Care
5. Harm Reduction/SSP
6. LGBTQ Community Center
7. Mobile Clinic
8. Telehealth-Integrated

### Risk Stratification

Four-level risk categorization:

- **LOW** (<40% attrition): Standard protocols appropriate
- **MODERATE** (40-55% attrition): Standard navigation recommended
- **HIGH** (55-70% attrition): Prioritize navigation and barrier removal
- **VERY HIGH** (≥70% attrition): Multiple intensive interventions required

### Updating the Configuration

To update clinical parameters:

1. **Open** `lai_prep_config.json`
2. **Modify** the relevant parameters
3. **Save** the file
4. **Run** the tool - changes take effect immediately

#### Example: Updating Evidence

```json
{
  "interventions": {
    "PATIENT_NAVIGATION": {
      "improvement": 0.18,  // Updated from 0.15 based on new study
      "evidence_level": "strong",
      "evidence_source": "Updated meta-analysis 2025 (n=15 studies)",
      "note": "Updated with latest implementation data showing 18% improvement"
    }
  }
}
```

### Validation

The tool includes built-in validation:

```python
from lai_prep_decision_tool_v2 import Configuration, ConfigurationError

try:
    config = Configuration("lai_prep_config.json")
    print("✓ Configuration valid")
except ConfigurationError as e:
    print(f"❌ Configuration error: {e}")
```

### Output Format

The tool generates structured assessments:

```python
assessment = tool.assess_patient(profile)

# Access key metrics
print(f"Baseline success: {assessment.baseline_success_rate:.1%}")
print(f"Adjusted success: {assessment.adjusted_success_rate:.1%}")
print(f"With interventions: {assessment.estimated_success_with_interventions:.1%}")
print(f"Risk level: {assessment.attrition_risk}")

# Access recommendations
for rec in assessment.recommended_interventions:
    print(f"- {rec.intervention_name}: +{rec.expected_improvement:.1f} pts")
    print(f"  Priority: {rec.priority} | Evidence: {rec.evidence_level}")
```

### Clinical Report

Generate formatted clinical reports:

```python
report = tool.generate_report(profile, assessment)
print(report)
```

Sample output:

```
================================================================================
LAI-PrEP BRIDGE PERIOD ASSESSMENT
Tool Version: 2.0.0
================================================================================

PATIENT PROFILE
--------------------------------------------------------------------------------
Population: Cisgender women
  Evidence Level: strong
  Evidence Source: HPTN 084 (n=3,224), PURPOSE-1 (n=5,338)
Age: 25 years
Current PrEP Status: naive
Healthcare Setting: Community health center
...

BRIDGE PERIOD SUCCESS PREDICTION
--------------------------------------------------------------------------------
Population Baseline Success Rate: 45.0%
Adjusted Success Rate (with barriers): 33.0%
Attrition Risk Level: High attrition risk

💡 With recommended interventions: 51.4% success
   Potential improvement: +18.4 percentage points (56% relative)

RECOMMENDED INTERVENTIONS
--------------------------------------------------------------------------------
1. Patient navigation program
   Priority: High
   Expected Improvement: +15.0 percentage points
   Evidence Level: strong
   ...
```

### Evidence Base

The tool is based on:

- **HPTN 083**: n=4,566 MSM and transgender women
- **HPTN 084**: n=3,224 cisgender women  
- **PURPOSE-1**: n=5,338 cisgender women (including 56 adolescents aged 16-17)
- **PURPOSE-2**: n=2,183 diverse participants
- **CAN Community Health Network**: Real-world implementation data (2021-2023)
- **Trio Health**: Persistence data (2021-2024)

### Publications

This tool is described in:

1. **Demidont, A.C. & Backus, K.** (2025). Bridging the Gap: The PrEP Cascade Paradigm Shift for Long-Acting Injectable HIV Prevention. *Viruses*.

2. **Demidont, A.C. & Backus, K.** (2025). Computational Validation of LAI-PrEP Bridge Decision Support Tool at UNAIDS Global Target Scale. *Viruses*.

### API Reference

#### LAIPrEPDecisionTool

Main decision support class.

**Methods:**
- `__init__(config_path=None)`: Initialize with optional config path
- `assess_patient(profile)`: Perform complete assessment
- `generate_report(profile, assessment)`: Generate formatted report

#### PatientProfile

Patient characteristics dataclass.

**Attributes:**
- `population`: str - Population key (e.g., "MSM", "CISGENDER_WOMEN")
- `age`: int - Patient age in years
- `current_prep_status`: str - "naive", "oral_prep", or "discontinued_oral"
- `barriers`: List[str] - List of barrier keys
- `healthcare_setting`: str - Setting key (e.g., "COMMUNITY_HEALTH_CENTER")
- `insurance_status`: str - "insured", "uninsured", or "underinsured"
- `recent_hiv_test`: bool - HIV test within 7 days
- `transportation_access`: bool - Has reliable transportation
- `childcare_needs`: bool - Requires childcare support

#### BridgePeriodAssessment

Assessment results dataclass.

**Attributes:**
- `baseline_success_rate`: float - Population baseline
- `adjusted_success_rate`: float - Adjusted for barriers
- `estimated_success_with_interventions`: float - With recommended interventions
- `attrition_risk`: str - Risk category label
- `key_barriers`: List[str] - Identified barriers
- `recommended_interventions`: List[InterventionRecommendation]
- `estimated_bridge_duration_days`: Tuple[int, int] - (min, max) days
- `clinical_notes`: List[str] - Guidance messages

### Troubleshooting

**Configuration not found:**
```
ConfigurationError: Configuration file not found
```
- Ensure `lai_prep_config.json` is in the same directory as the Python file
- Or specify path: `LAIPrEPDecisionTool(config_path="/path/to/config.json")`

**Invalid population:**
```
ConfigurationError: Unknown population: XYZ
```
- Check that population key matches config file
- Valid keys: MSM, CISGENDER_WOMEN, TRANSGENDER_WOMEN, ADOLESCENT, PWID, PREGNANT_LACTATING, GENERAL

**Invalid JSON:**
```
ConfigurationError: Invalid JSON in config file
```
- Validate JSON syntax at https://jsonlint.com
- Check for missing commas, quotes, or brackets

### Contributing

To update clinical parameters:

1. Review latest evidence
2. Update `lai_prep_config.json`
3. Include evidence source and date
4. Update `version` field
5. Test with validation script
6. Document changes in version notes

### License

Open source under MIT License. See LICENSE file.

### Contact

**Primary Author**: Adrian C. Demidont, DO  
**Email**: acdemidont@nyxdynamics.org  
**Organization**: Nyx Dynamics, LLC

**Co-Author**: Kandis Backus, PharmD  
**Organization**: Gilead Sciences, Inc.

### Citation

If you use this tool in research or clinical practice, please cite:

```
Demidont, A.C. & Backus, K. (2025). Computational Validation of a Clinical 
Decision Support Algorithm for Long-Acting Injectable PrEP Bridge Period 
Navigation at UNAIDS Global Target Scale. Viruses, 17(1), XX.

Demidont, A.C. & Backus, K. (2025). Bridging the Gap: The PrEP Cascade 
Paradigm Shift for Long-Acting Injectable HIV Prevention. Viruses, 1(1), XX.
```

### Version History

**v2.0.0** (2025-01-12)
- Configuration-driven architecture
- External JSON configuration file
- Enhanced validation and error handling
- Evidence level tagging
- Cost and complexity ratings
- Improved clinical guidance system

**v1.0.0** (2025-01-10)
- Initial release
- Hard-coded parameters
- Basic functionality

---

**Tool Version**: 2.0.0  
**Last Updated**: January 12, 2025  
**Configuration Version**: 2.0.0
