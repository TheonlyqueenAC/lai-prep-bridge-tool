#!/usr/bin/env python3
"""
LAI-PrEP Bridge Period Decision Support Tool

Based on: "Bridging the Gap: The PrEP Cascade Paradigm Shift for 
Long-Acting Injectable HIV Prevention"

This tool helps clinicians and healthcare systems:
1. Assess bridge period success probability for individual patients
2. Identify population-specific barriers
3. Recommend evidence-based interventions
4. Estimate improved outcomes with interventions
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from enum import Enum


class Population(Enum):
    """Patient population categories with distinct barrier profiles"""
    MSM = "Men who have sex with men"
    CISGENDER_WOMEN = "Cisgender women"
    TRANSGENDER_WOMEN = "Transgender women"
    ADOLESCENT = "Adolescent (16-24 years)"
    PWID = "People who inject drugs"
    PREGNANT_LACTATING = "Pregnant/lactating individuals"
    GENERAL = "General population"


class HealthcareSetting(Enum):
    """Type of healthcare delivery setting"""
    ACADEMIC_MEDICAL_CENTER = "Academic medical center"
    COMMUNITY_HEALTH_CENTER = "Community health center"
    PRIVATE_PRACTICE = "Private practice"
    PHARMACY = "Pharmacy-based care"
    HARM_REDUCTION = "Harm reduction/SSP"
    LGBTQ_CENTER = "LGBTQ community center"
    MOBILE_CLINIC = "Mobile clinic"
    TELEHEALTH = "Telehealth-integrated"


class Barrier(Enum):
    """Barriers to bridge period navigation"""
    TRANSPORTATION = "Transportation barriers"
    CHILDCARE = "Childcare needs"
    HOUSING_INSTABILITY = "Housing instability"
    INSURANCE_DELAYS = "Insurance authorization delays"
    SCHEDULING_CONFLICTS = "Scheduling conflicts"
    MEDICAL_MISTRUST = "Medical mistrust"
    PRIVACY_CONCERNS = "Privacy/confidentiality concerns"
    HEALTHCARE_DISCRIMINATION = "Healthcare discrimination experience"
    COMPETING_PRIORITIES = "Competing health/life priorities"
    LIMITED_NAVIGATION_EXPERIENCE = "Limited healthcare navigation experience"
    LEGAL_CONCERNS = "Criminalization/legal concerns"
    LACK_IDENTIFICATION = "Lack of government ID"
    SUBSTANCE_USE = "Active substance use"


class Intervention(Enum):
    """Evidence-based bridge period interventions"""
    ORAL_TO_INJECTABLE = "Oral-to-injectable transition"
    PATIENT_NAVIGATION = "Patient navigation program"
    ACCELERATED_TESTING = "Accelerated HIV testing (RNA + Ag/Ab)"
    SAME_DAY_SWITCHING = "Same-day switching protocol"
    TRANSPORTATION_SUPPORT = "Transportation vouchers/support"
    CHILDCARE_SUPPORT = "Childcare vouchers/on-site care"
    TEXT_MESSAGE_NAVIGATION = "SMS/text message navigation"
    PEER_NAVIGATION = "Peer navigator support"
    TELEHEALTH_COUNSELING = "Telehealth bridge counseling"
    EXPEDITED_AUTHORIZATION = "Expedited insurance authorization"
    MOBILE_DELIVERY = "Mobile/community-based delivery"
    HARM_REDUCTION_INTEGRATION = "SSP/harm reduction integration"
    BUNDLED_PAYMENT = "Bundled payment model"


@dataclass
class PatientProfile:
    """Patient characteristics affecting bridge period success"""
    population: Population
    age: int
    current_prep_status: str  # "naive", "oral_prep", "discontinued_oral"
    barriers: List[Barrier] = field(default_factory=list)
    healthcare_setting: HealthcareSetting = HealthcareSetting.COMMUNITY_HEALTH_CENTER
    insurance_status: str = "insured"  # "insured", "uninsured", "underinsured"
    recent_hiv_test: bool = False  # Within 7 days
    transportation_access: bool = True
    childcare_needs: bool = False


@dataclass
class InterventionRecommendation:
    """Recommended intervention with expected impact"""
    intervention: Intervention
    priority: str  # "Critical", "High", "Moderate"
    expected_improvement: float  # Percentage point improvement in success rate
    implementation_notes: str
    evidence_level: str  # "Strong", "Moderate", "Emerging"


@dataclass
class BridgePeriodAssessment:
    """Complete assessment with predictions and recommendations"""
    baseline_success_rate: float
    adjusted_success_rate: float
    attrition_risk: str  # "Low", "Moderate", "High", "Very High"
    key_barriers: List[Barrier]
    recommended_interventions: List[InterventionRecommendation]
    estimated_bridge_duration_days: Tuple[int, int]  # (min, max)
    estimated_success_with_interventions: float
    clinical_notes: List[str]


class LAIPrEPDecisionTool:
    """Main decision support tool for LAI-PrEP implementation"""
    
    # Base attrition rates from CAN Community Health Network Study
    BASE_ATTRITION = 0.47  # 47% general population
    
    # Population-specific attrition rates (from manuscript projections)
    POPULATION_ATTRITION = {
        Population.MSM: 0.45,  # 40-50%, using midpoint 45%
        Population.CISGENDER_WOMEN: 0.55,  # 50-60%, using midpoint
        Population.TRANSGENDER_WOMEN: 0.50,  # Estimated between MSM and women
        Population.ADOLESCENT: 0.65,  # 60-70%
        Population.PWID: 0.75,  # 70-80%
        Population.PREGNANT_LACTATING: 0.55,  # Similar to cisgender women
        Population.GENERAL: 0.47
    }
    
    # Intervention effectiveness (additive percentage point improvements)
    INTERVENTION_EFFECTS = {
        Intervention.ORAL_TO_INJECTABLE: {
            "improvement": 0.35,  # 85-90% success vs 53% = ~35 point improvement
            "evidence": "Strong",
            "note": "1.5-fold improvement in relative odds. Eliminates most bridge barriers."
        },
        Intervention.SAME_DAY_SWITCHING: {
            "improvement": 0.40,  # Complete elimination of bridge if recent test
            "evidence": "Strong",
            "note": "If HIV testing within 7 days, can inject same day"
        },
        Intervention.PATIENT_NAVIGATION: {
            "improvement": 0.15,  # 10-40% improvement, using conservative estimate
            "evidence": "Strong",
            "note": "1.5-fold increase in initiation rate (SF study), 10-40% in cancer care"
        },
        Intervention.ACCELERATED_TESTING: {
            "improvement": 0.10,  # Reduces bridge duration, prevents time-dependent attrition
            "evidence": "Moderate",
            "note": "RNA testing reduces window period from 33-45 days to 10-14 days"
        },
        Intervention.TRANSPORTATION_SUPPORT: {
            "improvement": 0.08,
            "evidence": "Moderate",
            "note": "Key barrier for women and PWID populations"
        },
        Intervention.CHILDCARE_SUPPORT: {
            "improvement": 0.08,
            "evidence": "Moderate",
            "note": "Critical for women with caregiving responsibilities"
        },
        Intervention.TEXT_MESSAGE_NAVIGATION: {
            "improvement": 0.05,
            "evidence": "Moderate",
            "note": "SMS reminders improve appointment attendance"
        },
        Intervention.PEER_NAVIGATION: {
            "improvement": 0.12,
            "evidence": "Moderate",
            "note": "Particularly effective for key populations with lived experience"
        },
        Intervention.TELEHEALTH_COUNSELING: {
            "improvement": 0.06,
            "evidence": "Emerging",
            "note": "Reduces visit burden but still requires in-person testing/injection"
        },
        Intervention.EXPEDITED_AUTHORIZATION: {
            "improvement": 0.10,
            "evidence": "Moderate",
            "note": "Insurance delays are major cause of bridge period attrition"
        },
        Intervention.MOBILE_DELIVERY: {
            "improvement": 0.12,
            "evidence": "Moderate",
            "note": "Brings services to patients, eliminates transportation barrier"
        },
        Intervention.HARM_REDUCTION_INTEGRATION: {
            "improvement": 0.15,
            "evidence": "Emerging",
            "note": "Essential for PWID populations - leverages existing trust"
        },
        Intervention.BUNDLED_PAYMENT: {
            "improvement": 0.08,
            "evidence": "Emerging",
            "note": "Reduces authorization delays and administrative burden"
        }
    }
    
    # Barrier impact on attrition (additional attrition risk)
    BARRIER_IMPACTS = {
        Barrier.TRANSPORTATION: 0.10,
        Barrier.CHILDCARE: 0.08,
        Barrier.HOUSING_INSTABILITY: 0.15,
        Barrier.INSURANCE_DELAYS: 0.12,
        Barrier.SCHEDULING_CONFLICTS: 0.05,
        Barrier.MEDICAL_MISTRUST: 0.10,
        Barrier.PRIVACY_CONCERNS: 0.08,
        Barrier.HEALTHCARE_DISCRIMINATION: 0.12,
        Barrier.COMPETING_PRIORITIES: 0.08,
        Barrier.LIMITED_NAVIGATION_EXPERIENCE: 0.10,
        Barrier.LEGAL_CONCERNS: 0.15,
        Barrier.LACK_IDENTIFICATION: 0.10,
        Barrier.SUBSTANCE_USE: 0.12
    }
    
    def __init__(self):
        """Initialize the decision tool"""
        pass
    
    def assess_patient(self, profile: PatientProfile) -> BridgePeriodAssessment:
        """
        Perform complete bridge period assessment for a patient
        
        Args:
            profile: PatientProfile with patient characteristics
            
        Returns:
            BridgePeriodAssessment with predictions and recommendations
        """
        # Calculate baseline success rate
        baseline_attrition = self.POPULATION_ATTRITION[profile.population]
        
        # Adjust for individual barriers
        barrier_adjustment = sum(
            self.BARRIER_IMPACTS.get(barrier, 0) for barrier in profile.barriers
        )
        
        # Cap adjustment to prevent impossible values
        adjusted_attrition = min(0.95, baseline_attrition + barrier_adjustment)
        adjusted_success_rate = 1 - adjusted_attrition
        baseline_success_rate = 1 - baseline_attrition
        
        # Determine attrition risk category
        attrition_risk = self._categorize_risk(adjusted_attrition)
        
        # Generate intervention recommendations
        recommendations = self._generate_recommendations(profile)
        
        # Calculate estimated success with interventions
        intervention_improvements = sum(
            self.INTERVENTION_EFFECTS[rec.intervention]["improvement"] 
            for rec in recommendations[:3]  # Top 3 interventions
        )
        # Diminishing returns - use 70% of combined effect
        estimated_success = min(0.95, adjusted_success_rate + (intervention_improvements * 0.7))
        
        # Estimate bridge duration
        bridge_duration = self._estimate_bridge_duration(profile)
        
        # Generate clinical notes
        clinical_notes = self._generate_clinical_notes(profile, adjusted_attrition)
        
        return BridgePeriodAssessment(
            baseline_success_rate=baseline_success_rate,
            adjusted_success_rate=adjusted_success_rate,
            attrition_risk=attrition_risk,
            key_barriers=profile.barriers[:5],  # Top 5 barriers
            recommended_interventions=recommendations,
            estimated_bridge_duration_days=bridge_duration,
            estimated_success_with_interventions=estimated_success,
            clinical_notes=clinical_notes
        )
    
    def _categorize_risk(self, attrition_rate: float) -> str:
        """Categorize attrition risk level"""
        if attrition_rate < 0.40:
            return "Low"
        elif attrition_rate < 0.55:
            return "Moderate"
        elif attrition_rate < 0.70:
            return "High"
        else:
            return "Very High"
    
    def _generate_recommendations(self, profile: PatientProfile) -> List[InterventionRecommendation]:
        """Generate prioritized intervention recommendations"""
        recommendations = []
        
        # Strategy 1: Eliminate the bridge (oral-to-injectable transitions)
        if profile.current_prep_status == "oral_prep":
            if profile.recent_hiv_test:
                recommendations.append(InterventionRecommendation(
                    intervention=Intervention.SAME_DAY_SWITCHING,
                    priority="Critical",
                    expected_improvement=40.0,
                    implementation_notes="Patient has recent HIV test (<7 days) and is on oral PrEP. "
                                       "Can administer first injection same day, completely eliminating bridge period.",
                    evidence_level="Strong"
                ))
            else:
                recommendations.append(InterventionRecommendation(
                    intervention=Intervention.ORAL_TO_INJECTABLE,
                    priority="Critical",
                    expected_improvement=35.0,
                    implementation_notes="Patient currently on oral PrEP. Transition pathway has 85-90% success rate "
                                       "vs 53% for PrEP-naive patients. Schedule injection within 7 days of recent testing.",
                    evidence_level="Strong"
                ))
        elif profile.current_prep_status == "discontinued_oral":
            recommendations.append(InterventionRecommendation(
                intervention=Intervention.PATIENT_NAVIGATION,
                priority="High",
                expected_improvement=15.0,
                implementation_notes="Patient discontinued oral PrEP - likely due to adherence challenges. "
                                   "LAI-PrEP addresses this but navigation critical for re-engagement.",
                evidence_level="Strong"
            ))
        
        # Strategy 2: Compress the bridge (accelerated testing)
        if not profile.recent_hiv_test:
            recommendations.append(InterventionRecommendation(
                intervention=Intervention.ACCELERATED_TESTING,
                priority="High",
                expected_improvement=10.0,
                implementation_notes="Dual testing (4th-gen Ag/Ab + RNA) reduces window period to 10-14 days. "
                                   "WHO July 2025 guidance supports simplified rapid testing approach.",
                evidence_level="Strong"
            ))
        
        # Strategy 3: Navigate the bridge (patient navigation)
        if profile.population in [Population.ADOLESCENT, Population.PWID, Population.CISGENDER_WOMEN]:
            nav_type = Intervention.PEER_NAVIGATION if profile.population == Population.PWID else Intervention.PATIENT_NAVIGATION
            recommendations.append(InterventionRecommendation(
                intervention=nav_type,
                priority="High" if profile.population == Population.PWID else "High",
                expected_improvement=15.0 if nav_type == Intervention.PEER_NAVIGATION else 15.0,
                implementation_notes=f"Population-tailored navigation essential for {profile.population.value}. "
                                   f"1.5x improvement in initiation rates demonstrated.",
                evidence_level="Strong"
            ))
        
        # Barrier-specific interventions
        if Barrier.TRANSPORTATION in profile.barriers:
            if profile.healthcare_setting == HealthcareSetting.MOBILE_CLINIC:
                recommendations.append(InterventionRecommendation(
                    intervention=Intervention.MOBILE_DELIVERY,
                    priority="High",
                    expected_improvement=12.0,
                    implementation_notes="Mobile delivery brings services to patient, eliminating transportation barrier.",
                    evidence_level="Moderate"
                ))
            else:
                recommendations.append(InterventionRecommendation(
                    intervention=Intervention.TRANSPORTATION_SUPPORT,
                    priority="High",
                    expected_improvement=8.0,
                    implementation_notes="Provide ride-share vouchers or public transit passes. "
                                       "Key barrier for women and PWID populations.",
                    evidence_level="Moderate"
                ))
        
        if Barrier.CHILDCARE in profile.barriers:
            recommendations.append(InterventionRecommendation(
                intervention=Intervention.CHILDCARE_SUPPORT,
                priority="High",
                expected_improvement=8.0,
                implementation_notes="Provide on-site childcare or childcare vouchers. "
                                   "Critical for women with caregiving responsibilities.",
                evidence_level="Moderate"
            ))
        
        if Barrier.INSURANCE_DELAYS in profile.barriers:
            recommendations.append(InterventionRecommendation(
                intervention=Intervention.EXPEDITED_AUTHORIZATION,
                priority="High",
                expected_improvement=10.0,
                implementation_notes="Implement expedited authorization pathway. Insurance delays major cause of attrition.",
                evidence_level="Moderate"
            ))
        
        # PWID-specific
        if profile.population == Population.PWID:
            if profile.healthcare_setting != HealthcareSetting.HARM_REDUCTION:
                recommendations.append(InterventionRecommendation(
                    intervention=Intervention.HARM_REDUCTION_INTEGRATION,
                    priority="Critical",
                    expected_improvement=15.0,
                    implementation_notes="Integrate LAI-PrEP into syringe service programs (SSP). "
                                       "Essential for PWID - leverages existing trust relationships. "
                                       "PURPOSE-4 trial will provide implementation evidence.",
                    evidence_level="Strong"
                ))
        
        # Universal interventions
        recommendations.append(InterventionRecommendation(
            intervention=Intervention.TEXT_MESSAGE_NAVIGATION,
            priority="Moderate",
            expected_improvement=5.0,
            implementation_notes="SMS reminders at 48h and 24h before appointments. Low-cost, high-reach intervention.",
            evidence_level="Moderate"
        ))
        
        if profile.healthcare_setting in [HealthcareSetting.COMMUNITY_HEALTH_CENTER, 
                                         HealthcareSetting.ACADEMIC_MEDICAL_CENTER]:
            recommendations.append(InterventionRecommendation(
                intervention=Intervention.TELEHEALTH_COUNSELING,
                priority="Moderate",
                expected_improvement=6.0,
                implementation_notes="Virtual counseling reduces visit burden while maintaining engagement. "
                                   "Still requires in-person testing/injection.",
                evidence_level="Emerging"
            ))
        
        # Sort by priority and expected improvement
        priority_order = {"Critical": 0, "High": 1, "Moderate": 2}
        recommendations.sort(key=lambda x: (priority_order[x.priority], -x.expected_improvement))
        
        return recommendations
    
    def _estimate_bridge_duration(self, profile: PatientProfile) -> Tuple[int, int]:
        """Estimate bridge period duration in days"""
        if profile.current_prep_status == "oral_prep" and profile.recent_hiv_test:
            return (0, 3)  # Same-day to 3 days
        elif profile.current_prep_status == "oral_prep":
            return (7, 14)  # Need recent test
        else:
            # PrEP-naive: depends on testing strategy and barriers
            min_days = 14 if profile.recent_hiv_test else 21
            max_days = 35 if len(profile.barriers) <= 2 else 56
            return (min_days, max_days)
    
    def _generate_clinical_notes(self, profile: PatientProfile, attrition_rate: float) -> List[str]:
        """Generate clinical guidance notes"""
        notes = []
        
        # Attrition risk
        if attrition_rate >= 0.70:
            notes.append(f"⚠️ VERY HIGH attrition risk ({attrition_rate:.0%}). Multiple intensive interventions required.")
        elif attrition_rate >= 0.55:
            notes.append(f"⚠️ HIGH attrition risk ({attrition_rate:.0%}). Prioritize navigation and barrier removal.")
        elif attrition_rate >= 0.40:
            notes.append(f"⚠️ MODERATE attrition risk ({attrition_rate:.0%}). Standard navigation recommended.")
        else:
            notes.append(f"✓ LOW attrition risk ({attrition_rate:.0%}). Standard protocols appropriate.")
        
        # Population-specific notes
        if profile.population == Population.ADOLESCENT:
            notes.append("🔍 Adolescents: Address temporal discounting, transportation dependence, privacy concerns. "
                        "PURPOSE-1 demonstrated zero infections in 56 adolescents aged 16-17.")
        elif profile.population == Population.PWID:
            notes.append("🔍 PWID: Harm reduction approach essential. No abstinence requirement. "
                        "PURPOSE-4 trial (ongoing) will provide critical implementation evidence.")
        elif profile.population == Population.CISGENDER_WOMEN:
            notes.append("🔍 Women: Address medical mistrust, structural barriers. "
                        "HPTN 084 showed 89% superior efficacy; PURPOSE-1 had zero infections in 5,338 women.")
        elif profile.population == Population.TRANSGENDER_WOMEN:
            notes.append("🔍 Transgender women: ADDRESS healthcare discrimination, hormone interaction concerns. "
                        "PURPOSE-2 showed 96% reduction in HIV incidence across all gender identities.")
        
        # Barrier-specific notes
        if Barrier.MEDICAL_MISTRUST in profile.barriers:
            notes.append("⚕️ Medical mistrust present. Provide culturally concordant support; "
                        "acknowledge historical/ongoing medical racism.")
        
        if Barrier.HOUSING_INSTABILITY in profile.barriers:
            notes.append("🏠 Housing instability complicates follow-up. Ensure multiple contact methods; "
                        "consider mobile/community-based delivery.")
        
        # Current PrEP status
        if profile.current_prep_status == "oral_prep":
            notes.append("💊 Currently on oral PrEP: PRIORITY for transition pathway. "
                        "85-90% initiation success vs 53% for PrEP-naive.")
        elif profile.current_prep_status == "discontinued_oral":
            notes.append("💊 Discontinued oral PrEP: LAI-PrEP addresses adherence challenges that led to discontinuation. "
                        "~50% discontinue oral PrEP within 6-12 months.")
        
        # Setting-specific notes
        if profile.healthcare_setting == HealthcareSetting.PHARMACY:
            notes.append("💊 Pharmacy-based care: Leverage extended hours and convenient access. "
                        "Address reimbursement and private space barriers.")
        elif profile.healthcare_setting == HealthcareSetting.HARM_REDUCTION:
            notes.append("💉 Harm reduction setting: Ideal for PWID populations. "
                        "Low-barrier protocols, no abstinence requirement.")
        
        # Evidence base
        notes.append("📊 Evidence: >15,000 participants across HPTN 083, 084, PURPOSE-1, PURPOSE-2. "
                    ">96% efficacy, 81-83% persistence once initiated.")
        
        return notes
    
    def generate_report(self, profile: PatientProfile, assessment: BridgePeriodAssessment) -> str:
        """Generate formatted clinical report"""
        report = []
        report.append("=" * 80)
        report.append("LAI-PrEP BRIDGE PERIOD ASSESSMENT")
        report.append("=" * 80)
        report.append("")
        
        # Patient characteristics
        report.append("PATIENT PROFILE")
        report.append("-" * 80)
        report.append(f"Population: {profile.population.value}")
        report.append(f"Age: {profile.age} years")
        report.append(f"Current PrEP Status: {profile.current_prep_status}")
        report.append(f"Healthcare Setting: {profile.healthcare_setting.value}")
        report.append(f"Insurance: {profile.insurance_status}")
        if profile.barriers:
            report.append(f"Identified Barriers ({len(profile.barriers)}):")
            for barrier in profile.barriers:
                report.append(f"  • {barrier.value}")
        report.append("")
        
        # Risk assessment
        report.append("BRIDGE PERIOD SUCCESS PREDICTION")
        report.append("-" * 80)
        report.append(f"Population Baseline Success Rate: {assessment.baseline_success_rate:.1%}")
        report.append(f"Adjusted Success Rate (with barriers): {assessment.adjusted_success_rate:.1%}")
        report.append(f"Attrition Risk Level: {assessment.attrition_risk}")
        report.append(f"Estimated Bridge Duration: {assessment.estimated_bridge_duration_days[0]}-"
                     f"{assessment.estimated_bridge_duration_days[1]} days")
        report.append("")
        report.append(f"💡 With recommended interventions: {assessment.estimated_success_with_interventions:.1%} success")
        report.append(f"   Potential improvement: +{(assessment.estimated_success_with_interventions - assessment.adjusted_success_rate)*100:.1f} percentage points")
        report.append("")
        
        # Recommendations
        report.append("RECOMMENDED INTERVENTIONS")
        report.append("-" * 80)
        for i, rec in enumerate(assessment.recommended_interventions[:5], 1):
            report.append(f"\n{i}. {rec.intervention.value}")
            report.append(f"   Priority: {rec.priority}")
            report.append(f"   Expected Improvement: +{rec.expected_improvement:.1f} percentage points")
            report.append(f"   Evidence Level: {rec.evidence_level}")
            report.append(f"   Implementation: {rec.implementation_notes}")
        report.append("")
        
        # Clinical notes
        report.append("CLINICAL GUIDANCE")
        report.append("-" * 80)
        for note in assessment.clinical_notes:
            report.append(f"• {note}")
        report.append("")
        
        # Footer
        report.append("=" * 80)
        report.append("Based on: Demidont & Backus (2025). Bridging the Gap: The PrEP Cascade")
        report.append("Paradigm Shift for Long-Acting Injectable HIV Prevention. Viruses.")
        report.append("=" * 80)
        
        return "\n".join(report)


def main():
    """Example usage and testing"""
    tool = LAIPrEPDecisionTool()
    
    print("LAI-PrEP BRIDGE PERIOD DECISION SUPPORT TOOL")
    print("=" * 80)
    print()
    
    # Example 1: Young MSM on oral PrEP (best case scenario)
    print("EXAMPLE 1: Oral-to-Injectable Transition (Best Case)")
    print("-" * 80)
    profile1 = PatientProfile(
        population=Population.MSM,
        age=28,
        current_prep_status="oral_prep",
        recent_hiv_test=True,
        healthcare_setting=HealthcareSetting.COMMUNITY_HEALTH_CENTER,
        barriers=[Barrier.SCHEDULING_CONFLICTS],
        insurance_status="insured"
    )
    assessment1 = tool.assess_patient(profile1)
    print(tool.generate_report(profile1, assessment1))
    print("\n\n")
    
    # Example 2: Adolescent cisgender woman, PrEP-naive (moderate-high risk)
    print("EXAMPLE 2: Adolescent Woman, Multiple Barriers (High Risk)")
    print("-" * 80)
    profile2 = PatientProfile(
        population=Population.ADOLESCENT,
        age=17,
        current_prep_status="naive",
        recent_hiv_test=False,
        healthcare_setting=HealthcareSetting.COMMUNITY_HEALTH_CENTER,
        barriers=[
            Barrier.TRANSPORTATION,
            Barrier.PRIVACY_CONCERNS,
            Barrier.LIMITED_NAVIGATION_EXPERIENCE,
            Barrier.INSURANCE_DELAYS
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
        population=Population.PWID,
        age=35,
        current_prep_status="naive",
        recent_hiv_test=False,
        healthcare_setting=HealthcareSetting.COMMUNITY_HEALTH_CENTER,
        barriers=[
            Barrier.HOUSING_INSTABILITY,
            Barrier.TRANSPORTATION,
            Barrier.LEGAL_CONCERNS,
            Barrier.HEALTHCARE_DISCRIMINATION,
            Barrier.COMPETING_PRIORITIES,
            Barrier.LACK_IDENTIFICATION,
            Barrier.SUBSTANCE_USE
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
        population=Population.CISGENDER_WOMEN,
        age=32,
        current_prep_status="discontinued_oral",
        recent_hiv_test=False,
        healthcare_setting=HealthcareSetting.COMMUNITY_HEALTH_CENTER,
        barriers=[
            Barrier.CHILDCARE,
            Barrier.TRANSPORTATION,
            Barrier.MEDICAL_MISTRUST
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
        print(f"{name}:")
        print(f"  Baseline: {assessment.adjusted_success_rate:.1%} → "
              f"With interventions: {assessment.estimated_success_with_interventions:.1%} "
              f"(+{improvement:.1f} points)")
    
    print("\n" + "=" * 80)
    print("Tool based on published evidence from HPTN 083, 084, PURPOSE-1, PURPOSE-2")
    print("and real-world implementation studies (CAN Community Health Network, 2023)")
    print("=" * 80)


if __name__ == "__main__":
    main()
