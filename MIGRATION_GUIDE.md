# Migration Guide: LAI-PrEP Tool v1.0 → v2.0

## Overview

Version 2.0 introduces a configuration-driven architecture that separates clinical evidence parameters from code logic. This guide explains the changes and how to migrate.

## Key Changes

### Architecture

| Aspect | v1.0 | v2.0 |
|--------|------|------|
| **Parameters** | Hard-coded in Python | External JSON config |
| **Updates** | Requires code changes | Edit JSON file only |
| **Validation** | None | Automatic validation |
| **Evidence Tracking** | Comments in code | Structured in config |
| **Versioning** | Code version only | Code + config versions |

### What's New

✅ **Configuration System**
- All clinical parameters in `lai_prep_config.json`
- No code changes needed for parameter updates
- Version control for configuration
- Automatic validation

✅ **Enhanced Metadata**
- Evidence levels (strong/moderate/emerging)
- Evidence sources documented
- Cost levels for interventions
- Implementation complexity ratings

✅ **Improved Flexibility**
- Easy to test different parameter sets
- A/B testing capabilities
- Regional customization
- Site-specific configurations

✅ **Better Maintenance**
- Clear separation of concerns
- Easier peer review
- Simplified updates
- Audit trail

## Code Comparison

### v1.0 (Hard-Coded)

```python
class LAIPrEPDecisionTool:
    # Hard-coded parameters
    BASE_ATTRITION = 0.47
    
    POPULATION_ATTRITION = {
        Population.MSM: 0.45,
        Population.CISGENDER_WOMEN: 0.55,
        # ...
    }
    
    INTERVENTION_EFFECTS = {
        Intervention.PATIENT_NAVIGATION: {
            "improvement": 0.15,
            "evidence": "Strong",
            "note": "1.5-fold increase..."
        },
        # ...
    }
```

### v2.0 (Configuration-Driven)

**Python Code:**
```python
class LAIPrEPDecisionTool:
    def __init__(self, config_path=None):
        self.config = Configuration(config_path)
        self.params = self.config.get_algorithm_params()
```

**Configuration File (`lai_prep_config.json`):**
```json
{
  "populations": {
    "MSM": {
      "baseline_attrition": 0.45,
      "evidence_level": "strong",
      "evidence_source": "HPTN 083 (n=4,566)"
    }
  },
  "interventions": {
    "PATIENT_NAVIGATION": {
      "improvement": 0.15,
      "evidence_level": "strong",
      "cost_level": "medium",
      "implementation_complexity": "medium"
    }
  }
}
```

## Migration Steps

### Step 1: Update File Structure

**Old structure:**
```
project/
├── lai_prep_decision_tool.py
```

**New structure:**
```
project/
├── lai_prep_decision_tool_v2.py
├── lai_prep_config.json
└── README.md
```

### Step 2: Update Import Statements

**v1.0:**
```python
from lai_prep_decision_tool import (
    LAIPrEPDecisionTool,
    PatientProfile,
    Population,
    Barrier,
    Intervention,
    HealthcareSetting
)
```

**v2.0:**
```python
from lai_prep_decision_tool_v2 import (
    LAIPrEPDecisionTool,
    PatientProfile,
    # Note: Enums are strings now, not enum classes
)
```

### Step 3: Update Code Usage

**v1.0 - Using Enum Classes:**
```python
profile = PatientProfile(
    population=Population.MSM,  # Enum
    barriers=[Barrier.TRANSPORTATION],  # Enum list
    healthcare_setting=HealthcareSetting.COMMUNITY_HEALTH_CENTER  # Enum
)
```

**v2.0 - Using String Keys:**
```python
profile = PatientProfile(
    population="MSM",  # String key from config
    barriers=["TRANSPORTATION"],  # String keys from config
    healthcare_setting="COMMUNITY_HEALTH_CENTER"  # String key from config
)
```

### Step 4: Initialize Tool

**v1.0:**
```python
tool = LAIPrEPDecisionTool()
```

**v2.0 - Default Config:**
```python
tool = LAIPrEPDecisionTool()  # Automatically finds config file
```

**v2.0 - Custom Config:**
```python
tool = LAIPrEPDecisionTool(config_path="/path/to/config.json")
```

### Step 5: Access Results

**v1.0:**
```python
assessment = tool.assess_patient(profile)
print(assessment.baseline_success_rate)
print(assessment.recommended_interventions[0].intervention.value)
```

**v2.0:**
```python
assessment = tool.assess_patient(profile)
print(assessment.baseline_success_rate)  # Same
print(assessment.recommended_interventions[0].intervention_name)  # String now
```

## Updating Parameters

### Old Way (v1.0)

To update patient navigation effectiveness:

1. Open `lai_prep_decision_tool.py`
2. Find the `INTERVENTION_EFFECTS` dictionary
3. Modify the hard-coded value:
```python
INTERVENTION_EFFECTS = {
    Intervention.PATIENT_NAVIGATION: {
        "improvement": 0.18,  # Changed from 0.15
        # ...
    }
}
```
4. Save and restart

**Problems:**
- Requires code editing
- No version tracking
- No evidence documentation
- Risk of syntax errors
- Harder to peer review

### New Way (v2.0)

To update patient navigation effectiveness:

1. Open `lai_prep_config.json`
2. Find the intervention section
3. Modify the JSON:
```json
{
  "interventions": {
    "PATIENT_NAVIGATION": {
      "improvement": 0.18,
      "evidence_level": "strong",
      "evidence_source": "Updated meta-analysis 2025",
      "note": "New data shows 18% improvement vs previous 15%"
    }
  }
}
```
4. Update version number:
```json
{
  "version": "2.0.1",
  "last_updated": "2025-01-15"
}
```
5. Save - changes take effect immediately

**Benefits:**
- No code editing required
- Version tracked
- Evidence documented
- JSON validation prevents errors
- Easier peer review
- Can A/B test configurations

## Validation

### v1.0

No built-in validation. Errors only discovered at runtime.

### v2.0

Automatic validation on load:

```python
from lai_prep_decision_tool_v2 import Configuration, ConfigurationError

try:
    config = Configuration("lai_prep_config.json")
    print("✓ Configuration valid")
    print(f"✓ Version: {config.config['version']}")
    print(f"✓ Populations: {len(config.config['populations'])}")
    print(f"✓ Interventions: {len(config.config['interventions'])}")
except ConfigurationError as e:
    print(f"❌ Configuration error: {e}")
```

## Testing Different Parameters

### v1.0

Testing different parameters required:
1. Creating code branches
2. Manual code modifications
3. Commenting out/in different values
4. Risk of losing original values

### v2.0

Testing different parameters:
1. Create config variants:
```
configs/
├── lai_prep_config_baseline.json
├── lai_prep_config_conservative.json
├── lai_prep_config_optimistic.json
```

2. Load different configs:
```python
# Test baseline parameters
tool_baseline = LAIPrEPDecisionTool("configs/lai_prep_config_baseline.json")

# Test conservative parameters
tool_conservative = LAIPrEPDecisionTool("configs/lai_prep_config_conservative.json")

# Compare results
assessment_baseline = tool_baseline.assess_patient(profile)
assessment_conservative = tool_conservative.assess_patient(profile)
```

## Regional Customization

### Example: Sub-Saharan Africa Configuration

Create `lai_prep_config_ssa.json` with regional adjustments:

```json
{
  "version": "2.0.0-SSA",
  "description": "Sub-Saharan Africa customized parameters",
  
  "populations": {
    "CISGENDER_WOMEN": {
      "baseline_attrition": 0.60,
      "note": "Higher baseline due to structural barriers in SSA"
    }
  },
  
  "interventions": {
    "MOBILE_DELIVERY": {
      "improvement": 0.15,
      "note": "Higher impact in SSA due to transportation challenges",
      "cost_level": "high",
      "implementation_complexity": "high"
    }
  },
  
  "healthcare_settings": {
    "COMMUNITY_HEALTH_CENTER": {
      "typical_barrier_reduction": 0.08,
      "note": "CHCs more prevalent in SSA"
    }
  }
}
```

Load region-specific config:

```python
tool_ssa = LAIPrEPDecisionTool("configs/lai_prep_config_ssa.json")
```

## Backwards Compatibility

### Converting v1.0 Code to v2.0

**Automated conversion script:**

```python
# convert_v1_to_v2.py

def convert_profile_v1_to_v2(v1_profile):
    """Convert v1 PatientProfile to v2 format"""
    return PatientProfile(
        population=v1_profile.population.name,  # Enum to string
        age=v1_profile.age,
        current_prep_status=v1_profile.current_prep_status,
        barriers=[b.name for b in v1_profile.barriers],  # Enum list to string list
        healthcare_setting=v1_profile.healthcare_setting.name,  # Enum to string
        insurance_status=v1_profile.insurance_status,
        recent_hiv_test=v1_profile.recent_hiv_test,
        transportation_access=v1_profile.transportation_access,
        childcare_needs=v1_profile.childcare_needs
    )
```

## Common Issues

### Issue 1: Configuration Not Found

**Error:**
```
ConfigurationError: Configuration file not found
```

**Solution:**
```python
# Option 1: Put config in same directory as Python file
tool = LAIPrEPDecisionTool()

# Option 2: Specify path
tool = LAIPrEPDecisionTool(config_path="/path/to/config.json")

# Option 3: Use environment variable
import os
os.environ['LAI_PREP_CONFIG'] = "/path/to/config.json"
tool = LAIPrEPDecisionTool()
```

### Issue 2: Invalid Population Key

**Error:**
```
ConfigurationError: Unknown population: msm
```

**Solution:**
```python
# Keys are case-sensitive and must match config
profile = PatientProfile(
    population="MSM",  # Correct (uppercase)
    # not "msm" or "Msm"
)
```

### Issue 3: JSON Syntax Error

**Error:**
```
ConfigurationError: Invalid JSON in config file
```

**Solution:**
1. Validate JSON at https://jsonlint.com
2. Common errors:
   - Missing comma after field
   - Trailing comma before closing brace
   - Unquoted keys
   - Single quotes instead of double quotes

**Example of invalid JSON:**
```json
{
  "populations": {
    "MSM": {
      "baseline_attrition": 0.45
      "evidence_level": "strong"  // Missing comma above!
    }
  }
}
```

**Fixed:**
```json
{
  "populations": {
    "MSM": {
      "baseline_attrition": 0.45,
      "evidence_level": "strong"
    }
  }
}
```

## Performance

### v1.0
- Enum lookups: O(1)
- All data in memory
- Fast but inflexible

### v2.0
- String key lookups: O(1) with dictionary
- Config loaded once at init
- Negligible performance difference (<1ms per assessment)
- Added flexibility worth minimal overhead

## Best Practices

### 1. Version Control

Track both code and configuration:

```
git add lai_prep_decision_tool_v2.py
git add lai_prep_config.json
git commit -m "Update patient navigation evidence to 18%"
```

### 2. Configuration Comments

Document changes in config:

```json
{
  "version": "2.0.1",
  "last_updated": "2025-01-15",
  "changelog": [
    "2.0.1 (2025-01-15): Updated PATIENT_NAVIGATION to 18% based on meta-analysis",
    "2.0.0 (2025-01-12): Initial configuration-driven release"
  ]
}
```

### 3. Testing

Always test after configuration changes:

```python
def test_config_changes():
    """Test configuration loading and basic functionality"""
    try:
        tool = LAIPrEPDecisionTool()
        
        # Test basic assessment
        profile = PatientProfile(
            population="MSM",
            age=30,
            current_prep_status="naive"
        )
        assessment = tool.assess_patient(profile)
        
        assert 0 <= assessment.baseline_success_rate <= 1
        assert 0 <= assessment.adjusted_success_rate <= 1
        assert len(assessment.recommended_interventions) > 0
        
        print("✓ All tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    test_config_changes()
```

### 4. Peer Review

Configuration changes are easier to review than code changes:

```bash
# Show configuration changes
git diff lai_prep_config.json

# Review shows clear parameter changes:
# - "improvement": 0.15,
# + "improvement": 0.18,
# + "evidence_source": "Updated meta-analysis 2025",
```

## Support

For migration assistance:

- **Email**: acdemidont@nyxdynamics.org
- **Documentation**: README.md
- **Configuration Reference**: See lai_prep_config.json comments

## Summary

| Feature | v1.0 | v2.0 |
|---------|------|------|
| **Ease of Updates** | ❌ Requires code editing | ✅ Edit JSON only |
| **Evidence Tracking** | ⚠️ Comments in code | ✅ Structured metadata |
| **Validation** | ❌ None | ✅ Automatic |
| **A/B Testing** | ❌ Difficult | ✅ Easy |
| **Regional Customization** | ❌ Requires code forks | ✅ Multiple configs |
| **Peer Review** | ⚠️ Code review needed | ✅ Parameter review |
| **Version Control** | ⚠️ Code only | ✅ Code + config |
| **Performance** | ✅ Fast | ✅ Fast |
| **Flexibility** | ❌ Low | ✅ High |
| **Maintenance** | ⚠️ Complex | ✅ Simple |

**Recommendation**: Migrate to v2.0 for better maintainability and flexibility. The configuration-driven architecture significantly simplifies updates and enables advanced use cases like A/B testing and regional customization.
