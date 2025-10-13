# LAI-PrEP Decision Tool v2.1 - File Inventory

## Core Files

### 1. `lai_prep_config.json` (650 lines)
**Purpose:** External configuration with all clinical parameters  
**Contains:**
- 7 populations with baseline attrition rates
- 13 barriers with impact scores
- 13 interventions with improvement estimates
- 8 healthcare settings
- 4 risk categories
- Algorithm parameters

**When to edit:** To update clinical evidence, add new interventions, or modify parameters

---

### 2. `lai_prep_decision_tool_v2_1.py` (1,200 lines)
**Purpose:** Enhanced main tool with all v2.1 features  
**Features:**
- Configuration-driven architecture
- Mechanism diversity scoring
- Logit-space calculations (optional)
- JSON export with explainability
- Confidence intervals
- Detailed rationales

**Import:** `from lai_prep_decision_tool_v2_1 import LAIPrEPDecisionTool, PatientProfile`

---

### 3. `cli.py` (450 lines)
**Purpose:** Command-line interface  
**Commands:**
- `assess` - Single patient assessment
- `batch` - Batch processing from CSV
- `validate` - Configuration validation
- `template` - Generate input template

**Usage:** `python cli.py assess -i patient.json -o results.json`

---

### 4. `test_edge_cases.py` (600 lines)
**Purpose:** Comprehensive unit tests  
**Test categories:**
- Edge cases (maximum barriers, conflicting signals, etc.)
- Logit vs linear comparison
- Mechanism diversity
- JSON export
- Error handling

**Usage:** `python test_edge_cases.py` or `pytest test_edge_cases.py -v`

---

## Example Files

### 5. `example_patient.json`
**Purpose:** Single patient example with documentation  
**Contains:** Complete patient profile with all valid options listed

**Usage:** `python cli.py assess -i example_patient.json -o results.json`

---

### 6. `example_patients.csv`
**Purpose:** Batch processing example with 10 diverse patients  
**Contains:** MSM, women, PWID, adolescents, pregnant individuals

**Usage:** `python cli.py batch -i example_patients.csv -o results/`

---

## Documentation

### 7. `README_v2_1.md` (300 lines)
**Purpose:** Comprehensive v2.1 documentation  
**Sections:**
- What's new in v2.1
- Quick start guide
- Detailed feature documentation
- API reference
- Examples
- CLI usage

---

### 8. `README.md` (250 lines)
**Purpose:** Original v2.0 documentation  
**Focus:** Configuration-driven architecture

---

### 9. `MIGRATION_GUIDE.md` (400 lines)
**Purpose:** v1.0 → v2.0 migration guide  
**Includes:** Code comparisons, update procedures, best practices

---

## Validation

### 10. `validate_config.py` (400 lines)
**Purpose:** Configuration validation script  
**Checks:**
- JSON syntax
- Required sections
- Valid ranges
- Cross-references
- Evidence documentation

**Usage:** `python validate_config.py lai_prep_config.json`

---

## Quick Start Commands

### 1. Single Assessment (Linear Method)
```bash
python cli.py assess \
  -i example_patient.json \
  -o results.json \
  --pretty \
  --verbose
```

### 2. Single Assessment (Logit Method)
```bash
python cli.py assess \
  -i example_patient.json \
  -o results_logit.json \
  --logit \
  --pretty
```

### 3. Batch Processing
```bash
python cli.py batch \
  -i example_patients.csv \
  -o batch_results/ \
  --summary \
  --verbose
```

### 4. Validate Configuration
```bash
python cli.py validate -c lai_prep_config.json
```

### 5. Generate Template
```bash
python cli.py template -o my_patient.json
```

### 6. Run Tests
```bash
python test_edge_cases.py
# or
pytest test_edge_cases.py -v
```

### 7. Validate Config (Standalone)
```bash
python validate_config.py lai_prep_config.json
```

---

## Python API Quick Reference

### Basic Usage

```python
from lai_prep_decision_tool_v2_1 import LAIPrEPDecisionTool, PatientProfile

# Initialize
tool = LAIPrEPDecisionTool()

# Create patient
profile = PatientProfile(
    population="MSM",
    age=30,
    current_prep_status="oral_prep",
    barriers=["SCHEDULING_CONFLICTS"],
    healthcare_setting="LGBTQ_CENTER",
    insurance_status="insured",
    recent_hiv_test=True
)

# Assess
assessment = tool.assess_patient(profile)

# Results
print(f"Risk: {assessment.attrition_risk}")
print(f"Success: {assessment.adjusted_success_rate:.1%}")
print(f"With interventions: {assessment.estimated_success_with_interventions:.1%}")

# Human-readable report
report = tool.generate_report(profile, assessment)
print(report)

# JSON export
json_output = assessment.to_json(profile)
```

### Logit Method

```python
# Use logit-space calculations
tool = LAIPrEPDecisionTool(use_logit=True)
assessment = tool.assess_patient(profile)
```

### JSON API Function

```python
from lai_prep_decision_tool_v2_1 import assess_patient_json

# Dictionary input
patient_data = {
    "population": "MSM",
    "age": 30,
    "current_prep_status": "oral_prep",
    ...
}

# Returns JSON output
results = assess_patient_json(patient_data, use_logit=False)
```

---

## File Dependencies

```
lai_prep_decision_tool_v2_1.py
├── Requires: lai_prep_config.json (auto-detected)
└── Imports: json, numpy (for logit), datetime, pathlib

cli.py
├── Requires: lai_prep_decision_tool_v2_1.py
└── Imports: click (install if needed: pip install click)

test_edge_cases.py
├── Requires: lai_prep_decision_tool_v2_1.py
│            lai_prep_config.json
└── Imports: pytest (install if needed: pip install pytest)

validate_config.py
├── Requires: None (standalone)
└── Imports: json, sys, pathlib
```

---

## Installation Checklist

- [ ] Download all core files
- [ ] Ensure `lai_prep_config.json` is in same directory or standard location
- [ ] (Optional) Install pytest: `pip install pytest --break-system-packages`
- [ ] (Optional) Install click for CLI: `pip install click --break-system-packages`
- [ ] Test configuration: `python cli.py validate -c lai_prep_config.json`
- [ ] Run example: `python cli.py assess -i example_patient.json -o test.json`
- [ ] (Optional) Run tests: `python test_edge_cases.py`

---

## Common Tasks

### Update Evidence Parameters

1. Open `lai_prep_config.json`
2. Find the parameter to update
3. Modify the value and evidence source
4. Update version number
5. Validate: `python validate_config.py lai_prep_config.json`
6. Test: `python test_edge_cases.py`

### Add New Intervention

1. Open `lai_prep_config.json`
2. Add entry to `"interventions"` section:
```json
"NEW_INTERVENTION": {
  "name": "New intervention name",
  "improvement": 0.10,
  "evidence_level": "emerging",
  "evidence_source": "Study citation",
  "note": "Implementation notes",
  "cost_level": "medium",
  "implementation_complexity": "medium",
  "applicable_populations": ["MSM", "CISGENDER_WOMEN"]
}
```
3. Validate configuration
4. Test with example patient

### Create Custom Configuration

1. Copy `lai_prep_config.json` to `custom_config.json`
2. Modify parameters as needed
3. Validate: `python validate_config.py custom_config.json`
4. Use in assessments:
```python
tool = LAIPrEPDecisionTool(config_path="custom_config.json")
```
or
```bash
python cli.py assess -i patient.json -o results.json -c custom_config.json
```

---

## Troubleshooting

### Configuration not found

**Error:** `ConfigurationError: Configuration file not found`

**Solution:** Place `lai_prep_config.json` in one of these locations:
- Same directory as Python file
- `config/lai_prep_config.json`
- `/mnt/user-data/outputs/lai_prep_config.json`

Or specify explicitly:
```python
tool = LAIPrEPDecisionTool(config_path="/path/to/config.json")
```

### Import Error

**Error:** `ModuleNotFoundError: No module named 'numpy'`

**Solution (for logit method):**
```bash
pip install numpy --break-system-packages
```

Or use linear method:
```python
tool = LAIPrEPDecisionTool(use_logit=False)
```

### Invalid Population/Barrier

**Error:** `ConfigurationError: Unknown population: xyz`

**Solution:** Check valid values in config file or example files:
- Populations: MSM, CISGENDER_WOMEN, TRANSGENDER_WOMEN, ADOLESCENT, PWID, PREGNANT_LACTATING, GENERAL
- Barriers: See `example_patient.json` for complete list

---

## Performance Notes

- **Single assessment:** <10ms
- **Batch processing (100 patients):** ~1 second
- **Configuration loading:** ~5ms (cached after first load)
- **Logit vs Linear:** Negligible difference (<1ms)

---

## Version Compatibility

| Version | Config Version | Python | NumPy (optional) |
|---------|---------------|--------|------------------|
| v2.1.0  | 2.0.0        | 3.7+   | Any              |
| v2.0.0  | 2.0.0        | 3.7+   | N/A              |
| v1.0.0  | N/A          | 3.7+   | N/A              |

---

## Support Resources

- **Documentation:** README_v2_1.md (comprehensive)
- **API Reference:** README_v2_1.md (API section)
- **Migration Guide:** MIGRATION_GUIDE.md (v1 to v2)
- **Examples:** example_patient.json, example_patients.csv
- **Tests:** test_edge_cases.py (shows usage patterns)

---

**Last Updated:** January 12, 2025  
**Tool Version:** 2.1.0  
**Config Version:** 2.0.0
