#!/usr/bin/env python3
"""
LAI-PrEP Bridge Period Decision Support Tool v2.0
Configuration-Driven Architecture

Based on: "Bridging the Gap: The PrEP Cascade Paradigm Shift for
Long-Acting Injectable HIV Prevention" and "Computational Validation
of LAI-PrEP Bridge Decision Support Tool"

This tool helps clinicians and healthcare systems:
1. Assess bridge period success probability for individual patients
2. Identify population-specific barriers
3. Recommend evidence-based interventions
4. Estimate improved outcomes with interventions
"""

import json
import os
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Tuple, Optional
from enum import Enum
from pathlib import Path


class ConfigurationError(Exception):
    """Raised when configuration file is invalid or missing"""
    pass


class Configuration:
    """Manages tool configuration from JSON file"""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration from JSON file

        Args:
            config_path: Path to configuration JSON file. If None, looks in default locations.
        """
        if config_path is None:
            config_path = self._find_config_file()

        self.config_path = config_path
        self.config = self._load_config()
        self._validate_config()

    def _find_config_file(self) -> str:
        """Find configuration file in standard locations"""
        search_paths = [
            "lai_prep_config.json",
            "config/lai_prep_config.json",
            str(Path(__file__).parent / "lai_prep_config.json"),
            "/mnt/user-data/outputs/lai_prep_config.json"
        ]

        for path in search_paths:
            if os.path.exists(path):
                return path

        raise ConfigurationError(
            f"Configuration file not found. Searched: {search_paths}"
        )

    def _load_config(self) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Invalid JSON in config file: {e}")
        except IOError as e:
            raise ConfigurationError(f"Cannot read config file: {e}")

    def _validate_config(self):
        """Validate required configuration sections exist"""
        required_sections = [
            'populations', 'barriers', 'interventions',
            'healthcare_settings', 'risk_categories', 'algorithm_parameters'
        ]

        missing = [s for s in required_sections if s not in self.config]
        if missing:
            raise ConfigurationError(
                f"Missing required config sections: {missing}"
            )

    def get_population_config(self, population: str) -> Dict:
        """Get configuration for specific population"""
        if population not in self.config['populations']:
            raise ConfigurationError(f"Unknown population: {population}")
        return self.config['populations'][population]

    def get_barrier_config(self, barrier: str) -> Dict:
        """Get configuration for specific barrier"""
        if barrier not in self.config['barriers']:
            raise ConfigurationError(f"Unknown barrier: {barrier}")
        return self.config['barriers'][barrier]

    def get_intervention_config(self, intervention: str) -> Dict:
        """Get configuration for specific intervention"""
        if intervention not in self.config['interventions']:
            raise ConfigurationError(f"Unknown intervention: {intervention}")
        return self.config['interventions'][intervention]

    def get_setting_config(self, setting: str) -> Dict:
        """Get configuration for specific healthcare setting"""
        if setting not in self.config['healthcare_settings']:
            raise ConfigurationError(f"Unknown setting: {setting}")
        return self.config['healthcare_settings'][setting]

    def get_algorithm_params(self) -> Dict:
        """Get algorithm parameters"""
        return self.config['algorithm_parameters']

    def get_risk_categories(self) -> Dict:
        """Get risk stratification categories"""
        return self.config['risk_categories']

    def get_clinical_guidance(self) -> Dict:
        """Get clinical guidance messages"""
        return self.config.get('clinical_guidance', {})


# Create enums dynamically from configuration
def create_enums_from_config(config: Configuration):
    """Create Enum classes from configuration"""

    # Population enum
    Population = Enum(
        'Population',
        {k: v['name'] for k, v in config.config['populations'].items()}
    )

    # Barrier enum
    Barrier = Enum(
        'Barrier',
        {k: v['name'] for k, v in config.config['barriers'].items()}
    )

    # Intervention enum
    Intervention = Enum(
        'Intervention',
        {k: v['name'] for k, v in config.config['interventions'].items()}
    )

    # Healthcare Setting enum
    HealthcareSetting = Enum(
        'HealthcareSetting',
        {k: v['name'] for k, v in config.config['healthcare_settings'].items()}
    )

    return Population, Barrier, Intervention, HealthcareSetting


@dataclass
class PatientProfile:
    """Patient characteristics affecting bridge period success"""
    population: str  # Population key from config
    age: int
    current_prep_status: str  # "naive", "oral_prep", "discontinued_oral"
    barriers: List[str] = field(default_factory=list)  # Barrier keys from config
    healthcare_setting: str = "COMMUNITY_HEALTH_CENTER"  # Setting key from config
    insurance_status: str = "insured"  # "insured", "uninsured", "underinsured"
    recent_hiv_test: bool = False  # Within 7 days
    transportation_access: bool = True
    childcare_needs: bool = False


@dataclass
class InterventionRecommendation:
    """Recommended intervention with expected impact"""
    intervention: str  # Intervention key from config
    intervention_name: str
    priority: str  # "Critical", "High", "Moderate"
    expected_improvement: float  # Percentage point improvement
    implementation_notes: str
    evidence_level: str  # "Strong", "Moderate", "Emerging"
    cost_level: str  # From config
    implementation_complexity: str  # From config


@dataclass
class BridgePeriodAssessment:
    """Complete assessment with predictions and recommendations"""
    baseline_success_rate: float
    adjusted_success_rate: float
    attrition_risk: str  # "Low", "Moderate", "High", "Very High"
    attrition_risk_category: Dict  # Full category info from config
    key_barriers: List[str]
    barrier_details: List[Dict]  # Full barrier info from config
    recommended_interventions: List[InterventionRecommendation]
    estimated_bridge_duration_days: Tuple[int, int]  # (min, max)
    estimated_success_with_interventions: float
    clinical_notes: List[str]
    population_info: Dict  # Full population info from config


class LAIPrEPDecisionTool:
    """Main decision support tool for LAI-PrEP implementation"""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize decision tool with configuration

        Args:
            config_path: Path to configuration JSON file
        """
        self.config = Configuration(config_path)
        self.params = self.config.get_algorithm_params()
        self.risk_categories = self.config.get_risk_categories()

    def assess_patient(self, profile: PatientProfile) -> BridgePeriodAssessment:
        """
        Perform complete bridge period assessment for a patient

        Args:
            profile: PatientProfile with patient characteristics

        Returns:
            BridgePeriodAssessment with predictions and recommendations
        """
        # Get population configuration
        pop_config = self.config.get_population_config(profile.population)
        baseline_attrition = pop_config['baseline_attrition']

        # Adjust for individual barriers
        barrier_adjustment = sum(
            self.config.get_barrier_config(barrier)['impact']
            for barrier in profile.barriers
        )

        # Apply barrier count adjustment
        barrier_count = len(profile.barriers)
        if barrier_count >= 3:
            barrier_adjustment += self.params['barrier_count_adjustment_factor']['3_plus_barriers']
        elif barrier_count == 2:
            barrier_adjustment += self.params['barrier_count_adjustment_factor']['2_barriers']
        elif barrier_count == 1:
            barrier_adjustment += self.params['barrier_count_adjustment_factor']['1_barrier']

        # Cap adjustment to prevent impossible values
        adjusted_attrition = min(
            self.params['max_attrition_ceiling'],
            baseline_attrition + barrier_adjustment
        )
        adjusted_success_rate = 1 - adjusted_attrition
        baseline_success_rate = 1 - baseline_attrition

        # Determine attrition risk category
        attrition_risk, risk_category = self._categorize_risk(adjusted_attrition)

        # Generate intervention recommendations
        recommendations = self._generate_recommendations(profile)

        # Calculate estimated success with interventions
        intervention_improvements = sum(
            self.config.get_intervention_config(rec.intervention)['improvement']
            for rec in recommendations[:3]  # Top 3 interventions
        )

        # Apply diminishing returns factor
        estimated_success = min(
            self.params['max_success_rate_with_interventions'],
            adjusted_success_rate + (
                    intervention_improvements *
                    self.params['intervention_diminishing_returns_factor']
            )
        )

        # Estimate bridge duration
        bridge_duration = self._estimate_bridge_duration(profile)

        # Generate clinical notes
        clinical_notes = self._generate_clinical_notes(
            profile, adjusted_attrition, pop_config
        )

        # Get barrier details
        barrier_details = [
            self.config.get_barrier_config(b) for b in profile.barriers
        ]

        return BridgePeriodAssessment(
            baseline_success_rate=baseline_success_rate,
            adjusted_success_rate=adjusted_success_rate,
            attrition_risk=attrition_risk,
            attrition_risk_category=risk_category,
            key_barriers=profile.barriers[:5],  # Top 5 barriers
            barrier_details=barrier_details[:5],
            recommended_interventions=recommendations,
            estimated_bridge_duration_days=bridge_duration,
            estimated_success_with_interventions=estimated_success,
            clinical_notes=clinical_notes,
            population_info=pop_config
        )

    def _categorize_risk(self, attrition_rate: float) -> Tuple[str, Dict]:
        """Categorize attrition risk level using configuration"""
        for category_name, category_info in self.risk_categories.items():
            threshold_min = category_info.get('threshold_min', 0)
            threshold_max = category_info.get('threshold_max', 1.0)

            if threshold_min <= attrition_rate < threshold_max:
                return category_info['label'], category_info

        # Default to VERY_HIGH if no match
        return self.risk_categories['VERY_HIGH']['label'], self.risk_categories['VERY_HIGH']

    def _generate_recommendations(
            self,
            profile: PatientProfile
    ) -> List[InterventionRecommendation]:
        """Generate prioritized intervention recommendations"""
        recommendations = []

        # Strategy 1: Eliminate the bridge (oral-to-injectable transitions)
        if profile.current_prep_status == "oral_prep":
            if profile.recent_hiv_test:
                int_config = self.config.get_intervention_config('SAME_DAY_SWITCHING')
                recommendations.append(InterventionRecommendation(
                    intervention='SAME_DAY_SWITCHING',
                    intervention_name=int_config['name'],
                    priority="Critical",
                    expected_improvement=int_config['improvement'] * 100,
                    implementation_notes=int_config['note'],
                    evidence_level=int_config['evidence_level'],
                    cost_level=int_config['cost_level'],
                    implementation_complexity=int_config['implementation_complexity']
                ))
            else:
                int_config = self.config.get_intervention_config('ORAL_TO_INJECTABLE')
                recommendations.append(InterventionRecommendation(
                    intervention='ORAL_TO_INJECTABLE',
                    intervention_name=int_config['name'],
                    priority="Critical",
                    expected_improvement=int_config['improvement'] * 100,
                    implementation_notes=int_config['note'],
                    evidence_level=int_config['evidence_level'],
                    cost_level=int_config['cost_level'],
                    implementation_complexity=int_config['implementation_complexity']
                ))

        # Strategy 2: Compress the bridge (accelerated testing)
        if not profile.recent_hiv_test:
            int_config = self.config.get_intervention_config('ACCELERATED_TESTING')
            recommendations.append(InterventionRecommendation(
                intervention='ACCELERATED_TESTING',
                intervention_name=int_config['name'],
                priority="High",
                expected_improvement=int_config['improvement'] * 100,
                implementation_notes=int_config['note'],
                evidence_level=int_config['evidence_level'],
                cost_level=int_config['cost_level'],
                implementation_complexity=int_config['implementation_complexity']
            ))

        # Strategy 3: Navigate the bridge (patient navigation)
        # Prioritize navigation for high-risk populations
        pop_config = self.config.get_population_config(profile.population)
        if pop_config['baseline_attrition'] > 0.50:  # High baseline risk
            # Use peer navigation for PWID, regular navigation for others
            nav_intervention = ('PEER_NAVIGATION' if profile.population == 'PWID'
                                else 'PATIENT_NAVIGATION')
            int_config = self.config.get_intervention_config(nav_intervention)
            recommendations.append(InterventionRecommendation(
                intervention=nav_intervention,
                intervention_name=int_config['name'],
                priority="High",
                expected_improvement=int_config['improvement'] * 100,
                implementation_notes=int_config['note'],
                evidence_level=int_config['evidence_level'],
                cost_level=int_config['cost_level'],
                implementation_complexity=int_config['implementation_complexity']
            ))

        # Barrier-specific interventions
        for barrier in profile.barriers:
            barrier_config = self.config.get_barrier_config(barrier)

            # Find interventions that address this barrier
            for int_key, int_config in self.config.config['interventions'].items():
                if 'addresses_barriers' in int_config:
                    if barrier in int_config['addresses_barriers']:
                        # Check if intervention is already recommended
                        if int_key not in [r.intervention for r in recommendations]:
                            # Check if applicable to this population
                            if ('applicable_populations' not in int_config or
                                    profile.population in int_config['applicable_populations']):
                                recommendations.append(InterventionRecommendation(
                                    intervention=int_key,
                                    intervention_name=int_config['name'],
                                    priority="High",
                                    expected_improvement=int_config['improvement'] * 100,
                                    implementation_notes=int_config['note'],
                                    evidence_level=int_config['evidence_level'],
                                    cost_level=int_config['cost_level'],
                                    implementation_complexity=int_config['implementation_complexity']
                                ))

        # PWID-specific intervention
        if profile.population == 'PWID':
            if profile.healthcare_setting != 'HARM_REDUCTION':
                if 'HARM_REDUCTION_INTEGRATION' not in [r.intervention for r in recommendations]:
                    int_config = self.config.get_intervention_config('HARM_REDUCTION_INTEGRATION')
                    recommendations.append(InterventionRecommendation(
                        intervention='HARM_REDUCTION_INTEGRATION',
                        intervention_name=int_config['name'],
                        priority="Critical",
                        expected_improvement=int_config['improvement'] * 100,
                        implementation_notes=int_config['note'],
                        evidence_level=int_config['evidence_level'],
                        cost_level=int_config['cost_level'],
                        implementation_complexity=int_config['implementation_complexity']
                    ))

        # Universal interventions - SMS/Text messaging
        if 'TEXT_MESSAGE_NAVIGATION' not in [r.intervention for r in recommendations]:
            int_config = self.config.get_intervention_config('TEXT_MESSAGE_NAVIGATION')
            recommendations.append(InterventionRecommendation(
                intervention='TEXT_MESSAGE_NAVIGATION',
                intervention_name=int_config['name'],
                priority="Moderate",
                expected_improvement=int_config['improvement'] * 100,
                implementation_notes=int_config['note'],
                evidence_level=int_config['evidence_level'],
                cost_level=int_config['cost_level'],
                implementation_complexity=int_config['implementation_complexity']
            ))

        # Setting-specific recommendations
        setting_config = self.config.get_setting_config(profile.healthcare_setting)
        if 'recommended_interventions' in setting_config:
            for int_key in setting_config['recommended_interventions']:
                if int_key not in [r.intervention for r in recommendations]:
                    int_config = self.config.get_intervention_config(int_key)
                    # Check applicability
                    if ('applicable_populations' not in int_config or
                            profile.population in int_config['applicable_populations']):
                        recommendations.append(InterventionRecommendation(
                            intervention=int_key,
                            intervention_name=int_config['name'],
                            priority="Moderate",
                            expected_improvement=int_config['improvement'] * 100,
                            implementation_notes=int_config['note'],
                            evidence_level=int_config['evidence_level'],
                            cost_level=int_config['cost_level'],
                            implementation_complexity=int_config['implementation_complexity']
                        ))

        # Sort by priority and expected improvement
        priority_order = {"Critical": 0, "High": 1, "Moderate": 2}
        recommendations.sort(
            key=lambda x: (priority_order[x.priority], -x.expected_improvement)
        )

        return recommendations

    def _estimate_bridge_duration(
            self,
            profile: PatientProfile
    ) -> Tuple[int, int]:
        """Estimate bridge period duration in days"""
        if profile.current_prep_status == "oral_prep" and profile.recent_hiv_test:
            return tuple(self.params['bridge_duration_oral_prep_recent_test'])
        elif profile.current_prep_status == "oral_prep":
            return tuple(self.params['bridge_duration_oral_prep_no_recent_test'])
        else:
            # PrEP-naive: depends on testing strategy and barriers
            if profile.recent_hiv_test:
                min_days, max_days = self.params['bridge_duration_naive_recent_test']
            else:
                min_days, max_days = self.params['bridge_duration_naive_no_recent_test']

            # Adjust max based on barrier count
            if len(profile.barriers) > 2:
                max_days = self.params['maximum_bridge_duration_days']

            return (min_days, max_days)

    def _generate_clinical_notes(
            self,
            profile: PatientProfile,
            attrition_rate: float,
            pop_config: Dict
    ) -> List[str]:
        """Generate clinical guidance notes"""
        notes = []
        guidance = self.config.get_clinical_guidance()

        # Risk level note
        _, risk_category = self._categorize_risk(attrition_rate)
        notes.append(
            f"{risk_category['icon']} {risk_category['label'].upper()}: "
            f"{risk_category['clinical_action']} ({attrition_rate:.0%} attrition risk)"
        )

        # Population-specific notes
        if 'clinical_notes' in pop_config:
            notes.append(f"📋 {pop_config['clinical_notes']}")

        # PrEP status notes
        if profile.current_prep_status == "oral_prep":
            if 'oral_prep_transition_priority' in guidance:
                notes.append(f"💊 {guidance['oral_prep_transition_priority']['message']}")
        elif profile.current_prep_status == "discontinued_oral":
            if 'discontinued_oral_prep' in guidance:
                notes.append(f"💊 {guidance['discontinued_oral_prep']['message']}")

        # Barrier-specific notes
        for barrier in profile.barriers:
            barrier_key = barrier.lower().replace(' ', '_').replace('/', '_')
            if barrier_key in guidance:
                notes.append(f"⚕️ {guidance[barrier_key]['message']}")

        # Setting-specific notes
        setting_key = profile.healthcare_setting.lower()
        if setting_key + '_setting' in guidance:
            notes.append(f"🏥 {guidance[setting_key + '_setting']['message']}")

        # Evidence base
        if 'evidence_base' in guidance:
            notes.append(f"📊 {guidance['evidence_base']['message']}")

        return notes

    def generate_report(
            self,
            profile: PatientProfile,
            assessment: BridgePeriodAssessment
    ) -> str:
        """Generate formatted clinical report"""
        report = []
        report.append("=" * 80)
        report.append("LAI-PrEP BRIDGE PERIOD ASSESSMENT")
        report.append(f"Tool Version: {self.config.config.get('version', 'Unknown')}")
        report.append("=" * 80)
        report.append("")

        # Patient characteristics
        report.append("PATIENT PROFILE")
        report.append("-" * 80)
        report.append(f"Population: {assessment.population_info['name']}")
        report.append(f"  Evidence Level: {assessment.population_info['evidence_level']}")
        report.append(f"  Evidence Source: {assessment.population_info['evidence_source']}")
        report.append(f"Age: {profile.age} years")
        report.append(f"Current PrEP Status: {profile.current_prep_status}")

        # Healthcare setting
        setting_config = self.config.get_setting_config(profile.healthcare_setting)
        report.append(f"Healthcare Setting: {setting_config['name']}")
        report.append(f"  Strengths: {', '.join(setting_config['strengths'])}")

        report.append(f"Insurance: {profile.insurance_status}")

        if profile.barriers:
            report.append(f"\nIdentified Barriers ({len(profile.barriers)}):")
            for barrier_key, barrier_detail in zip(
                    assessment.key_barriers,
                    assessment.barrier_details
            ):
                report.append(f"  • {barrier_detail['name']}")
                report.append(f"    Impact: +{barrier_detail['impact'] * 100:.1f} pts | "
                              f"Evidence: {barrier_detail['evidence_level']}")
        report.append("")

        # Risk assessment
        report.append("BRIDGE PERIOD SUCCESS PREDICTION")
        report.append("-" * 80)
        report.append(f"Population Baseline Success Rate: "
                      f"{assessment.baseline_success_rate:.1%}")
        report.append(f"  (Range: {assessment.population_info['attrition_range'][0] * 100:.0f}-"
                      f"{assessment.population_info['attrition_range'][1] * 100:.0f}% attrition)")
        report.append(f"Adjusted Success Rate (with barriers): "
                      f"{assessment.adjusted_success_rate:.1%}")
        report.append(f"Attrition Risk Level: {assessment.attrition_risk}")
        report.append(f"Estimated Bridge Duration: "
                      f"{assessment.estimated_bridge_duration_days[0]}-"
                      f"{assessment.estimated_bridge_duration_days[1]} days")
        report.append("")
        report.append(f"💡 With recommended interventions: "
                      f"{assessment.estimated_success_with_interventions:.1%} success")
        improvement = (assessment.estimated_success_with_interventions -
                       assessment.adjusted_success_rate) * 100
        report.append(f"   Potential improvement: +{improvement:.1f} percentage points "
                      f"({improvement / assessment.adjusted_success_rate * 100:.0f}% relative)")
        report.append("")

        # Recommendations
        report.append("RECOMMENDED INTERVENTIONS")
        report.append("-" * 80)
        for i, rec in enumerate(assessment.recommended_interventions[:5], 1):
            report.append(f"\n{i}. {rec.intervention_name}")
            report.append(f"   Priority: {rec.priority}")
            report.append(f"   Expected Improvement: +{rec.expected_improvement:.1f} percentage points")
            report.append(f"   Evidence Level: {rec.evidence_level}")
            report.append(f"   Cost: {rec.cost_level} | "
                          f"Complexity: {rec.implementation_complexity}")
            report.append(f"   Implementation: {rec.implementation_notes}")
        report.append("")

        # Clinical notes
        report.append("CLINICAL GUIDANCE")
        report.append("-" * 80)
        for note in assessment.clinical_notes:
            # Wrap long notes
            if len(note) > 76:
                words = note.split()
                lines = []
                current_line = words[0]
                for word in words[1:]:
                    if len(current_line + " " + word) <= 76:
                        current_line += " " + word
                    else:
                        lines.append(current_line)
                        current_line = "  " + word
                lines.append(current_line)
                report.extend(lines)
            else:
                report.append(note)
        report.append("")

        # Footer
        report.append("=" * 80)
        report.append("Based on: Demidont & Backus (2025). Bridging the Gap: The PrEP")
        report.append("Cascade Paradigm Shift for Long-Acting Injectable HIV Prevention.")
        report.append("Viruses. AND Demidont & Backus (2025). Computational Validation of")
        report.append("LAI-PrEP Bridge Decision Support Tool. Viruses.")
        report.append(f"Configuration Version: {self.config.config.get('version', 'Unknown')}")
        report.append("=" * 80)

        return "\n".join(report)


def main():
    """Example usage and testing"""
    print("LAI-PrEP BRIDGE PERIOD DECISION SUPPORT TOOL v2.0")
    print("Configuration-Driven Architecture")
    print("=" * 80)
    print()

    try:
        tool = LAIPrEPDecisionTool()
        print(f"✓ Configuration loaded: {tool.config.config_path}")
        print(f"✓ Version: {tool.config.config.get('version', 'Unknown')}")
        print()
    except ConfigurationError as e:
        print(f"❌ Configuration Error: {e}")
        print("\nPlease ensure lai_prep_config.json is in the current directory")
        return

    # Example 1: Young MSM on oral PrEP (best case scenario)
    print("EXAMPLE 1: Oral-to-Injectable Transition (Best Case)")
    print("-" * 80)
    profile1 = PatientProfile(
        population="MSM",
        age=28,
        current_prep_status="oral_prep",
        recent_hiv_test=True,
        healthcare_setting="COMMUNITY_HEALTH_CENTER",
        barriers=["SCHEDULING_CONFLICTS"],
        insurance_status="insured"
    )
    assessment1 = tool.assess_patient(profile1)
    print(tool.generate_report(profile1, assessment1))
    print("\n\n")

    # Example 2: Adolescent cisgender woman, PrEP-naive (moderate-high risk)
    print("EXAMPLE 2: Adolescent Woman, Multiple Barriers (High Risk)")
    print("-" * 80)
    profile2 = PatientProfile(
        population="ADOLESCENT",
        age=17,
        current_prep_status="naive",
        recent_hiv_test=False,
        healthcare_setting="COMMUNITY_HEALTH_CENTER",
        barriers=[
            "TRANSPORTATION",
            "PRIVACY_CONCERNS",
            "LIMITED_NAVIGATION_EXPERIENCE",
            "INSURANCE_DELAYS"
        ],
        insurance_status="insured",
        transportation_access=False
    )
    assessment2 = tool.assess_patient(profile2)
    print(tool.generate_report(profile2, assessment2))
    print("\n\n")

    # Example 3: PWID with multiple structural barriers (very high risk)
    print("EXAMPLE 3: Person Who Injects Drugs (Very High Risk)")
    print("-" * 80)
    profile3 = PatientProfile(
        population="PWID",
        age=35,
        current_prep_status="naive",
        recent_hiv_test=False,
        healthcare_setting="COMMUNITY_HEALTH_CENTER",
        barriers=[
            "HOUSING_INSTABILITY",
            "TRANSPORTATION",
            "LEGAL_CONCERNS",
            "HEALTHCARE_DISCRIMINATION",
            "COMPETING_PRIORITIES",
            "LACK_IDENTIFICATION",
            "SUBSTANCE_USE"
        ],
        insurance_status="uninsured",
        transportation_access=False
    )
    assessment3 = tool.assess_patient(profile3)
    print(tool.generate_report(profile3, assessment3))
    print("\n\n")

    # Example 4: Cisgender woman discontinuing oral PrEP
    print("EXAMPLE 4: Woman Re-Engaging After Oral PrEP Discontinuation")
    print("-" * 80)
    profile4 = PatientProfile(
        population="CISGENDER_WOMEN",
        age=32,
        current_prep_status="discontinued_oral",
        recent_hiv_test=False,
        healthcare_setting="COMMUNITY_HEALTH_CENTER",
        barriers=[
            "CHILDCARE",
            "TRANSPORTATION",
            "MEDICAL_MISTRUST"
        ],
        insurance_status="insured",
        childcare_needs=True,
        transportation_access=False
    )
    assessment4 = tool.assess_patient(profile4)
    print(tool.generate_report(profile4, assessment4))
    print("\n\n")

    # Summary statistics
    print("SUMMARY: IMPACT OF INTERVENTIONS")
    print("=" * 80)
    examples = [
        ("MSM on oral PrEP (same-day switch)", assessment1),
        ("Adolescent with barriers", assessment2),
        ("PWID with multiple barriers", assessment3),
        ("Woman re-engaging", assessment4)
    ]

    for name, assessment in examples:
        improvement = (assessment.estimated_success_with_interventions -
                       assessment.adjusted_success_rate) * 100
        relative = improvement / (assessment.adjusted_success_rate * 100) * 100
        print(f"{name}:")
        print(f"  Baseline: {assessment.adjusted_success_rate:.1%} → "
              f"With interventions: {assessment.estimated_success_with_interventions:.1%} "
              f"(+{improvement:.1f} pts, +{relative:.0f}% relative)")

    print("\n" + "=" * 80)
    print("Tool based on published evidence from HPTN 083, 084, PURPOSE-1, PURPOSE-2")
    print("and real-world implementation studies (CAN Community Health Network, 2023)")
    print("Configuration enables rapid updates without code changes")
    print("=" * 80)


if __name__ == "__main__":
    main()