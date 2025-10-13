#!/usr/bin/env python3
"""
Example Usage Script for LAI-PrEP Bridge Period Decision Support Tool

This script demonstrates various use cases and features of the tool.
"""

from lai_prep_tool import (
    Configuration,
    BridgePeriodAssessor,
    PatientProfile,
    ReportGenerator
)


def example_1_basic_assessment():
    """Example 1: Basic patient assessment with standard output."""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Patient Assessment")
    print("=" * 70)

    # Load configuration
    config = Configuration('lai_prep_config.json')

    # Create assessor
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    # Create patient profile
    patient = PatientProfile(
        population='cisgender_women',
        current_prep_status='naive',
        barriers=['transportation', 'childcare', 'medical_mistrust'],
        healthcare_setting='community_health_center',
        age=28,
        insurance_status='insured'
    )

    # Perform assessment
    result = assessor.assess_patient(patient)

    # Generate and print report
    report = ReportGenerator.generate_text_report(result)
    print(report)


def example_2_oral_to_injectable_transition():
    """Example 2: Patient transitioning from oral PrEP (optimal scenario)."""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Oral to Injectable Transition")
    print("=" * 70)

    config = Configuration('lai_prep_config.json')
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    patient = PatientProfile(
        population='msm',
        current_prep_status='current_oral',  # Key: already on oral PrEP
        barriers=[],  # Minimal barriers
        healthcare_setting='private_practice',
        age=32,
        insurance_status='insured'
    )

    result = assessor.assess_patient(patient)

    # Show summary
    print(ReportGenerator.generate_summary(result))
    print(f"\nBaseline: {result.baseline_success_rate:.1%}")
    print(f"With oral→injectable transition: {result.predicted_with_interventions:.1%}")
    print(f"Improvement: +{(result.predicted_with_interventions - result.baseline_success_rate):.1%}")
    print("\nTop Recommendation:")
    print(f"  {result.recommended_interventions[0]['name']}")
    print(f"  Impact: +{result.recommended_interventions[0]['impact']:.1%}")
    print(f"  Evidence: {result.recommended_interventions[0]['evidence']}")


def example_3_high_barrier_pwid():
    """Example 3: Person who injects drugs with multiple barriers (challenging case)."""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: High-Barrier PWID Patient")
    print("=" * 70)

    config = Configuration('lai_prep_config.json')
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    patient = PatientProfile(
        population='pwid',
        current_prep_status='naive',
        barriers=[
            'unstable_housing',
            'substance_use',
            'legal_concerns',
            'medical_mistrust',
            'no_insurance'
        ],
        healthcare_setting='harm_reduction_service',
        age=34,
        insurance_status='uninsured'
    )

    result = assessor.assess_patient(patient)

    print(f"Risk Level: {result.risk_level.upper()}")
    print(f"Barriers: {len(patient.barriers)}")
    print(f"Baseline Success: {result.baseline_success_rate:.1%}")
    print(f"Adjusted (with barriers): {result.adjusted_success_rate:.1%}")
    print(f"Predicted (with interventions): {result.predicted_with_interventions:.1%}")

    relative_improvement = (
            (result.predicted_with_interventions - result.adjusted_success_rate)
            / result.adjusted_success_rate
    )
    print(f"Relative Improvement: {relative_improvement:.1%}")

    print("\nRecommended Interventions:")
    for i, intervention in enumerate(result.recommended_interventions, 1):
        print(f"{i}. {intervention['name']}")
        print(f"   Mechanisms: {', '.join(intervention['mechanisms'])}")


def example_4_adolescent_privacy_concerns():
    """Example 4: Adolescent with privacy concerns and parental barriers."""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Adolescent with Privacy Concerns")
    print("=" * 70)

    config = Configuration('lai_prep_config.json')
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    patient = PatientProfile(
        population='adolescents',
        current_prep_status='naive',
        barriers=['privacy_concerns', 'transportation', 'work_school_conflict'],
        healthcare_setting='community_health_center',
        age=19,
        insurance_status='insured'
    )

    result = assessor.assess_patient(patient)

    print(f"Age: {patient.age}")
    print(f"Success Rate: {result.adjusted_success_rate:.1%} → {result.predicted_with_interventions:.1%}")
    print(f"Risk Level: {result.risk_level}")

    print("\nKey Interventions for Adolescents:")
    for intervention in result.recommended_interventions:
        if 'youth' in intervention['name'] or 'privacy' in intervention['mechanisms']:
            print(f"  • {intervention['name']}")
            print(f"    {intervention['description']}")


def example_5_batch_assessment():
    """Example 5: Batch assessment of multiple patients."""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Batch Assessment")
    print("=" * 70)

    config = Configuration('lai_prep_config.json')
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    # Simulate cohort of patients
    patient_cohort = [
        {
            'population': 'msm',
            'current_prep_status': 'naive',
            'barriers': ['stigma'],
            'healthcare_setting': 'lgbtq_center',
            'insurance_status': 'insured'
        },
        {
            'population': 'cisgender_women',
            'current_prep_status': 'discontinued_oral',
            'barriers': ['transportation', 'childcare'],
            'healthcare_setting': 'community_health_center',
            'insurance_status': 'underinsured'
        },
        {
            'population': 'transgender_women',
            'current_prep_status': 'naive',
            'barriers': ['medical_mistrust', 'no_insurance'],
            'healthcare_setting': 'lgbtq_center',
            'insurance_status': 'uninsured'
        },
        {
            'population': 'pwid',
            'current_prep_status': 'naive',
            'barriers': ['unstable_housing', 'substance_use', 'legal_concerns'],
            'healthcare_setting': 'harm_reduction_service',
            'insurance_status': 'uninsured'
        }
    ]

    results = []
    for patient_data in patient_cohort:
        patient = PatientProfile(**patient_data)
        result = assessor.assess_patient(patient)
        results.append(result)

    # Calculate cohort statistics
    print(f"Cohort Size: {len(results)}")
    print(f"\nMean Baseline Success: {sum(r.baseline_success_rate for r in results) / len(results):.1%}")
    print(f"Mean Adjusted Success: {sum(r.adjusted_success_rate for r in results) / len(results):.1%}")
    print(f"Mean Predicted Success: {sum(r.predicted_with_interventions for r in results) / len(results):.1%}")

    # Risk distribution
    risk_counts = {}
    for result in results:
        risk_counts[result.risk_level] = risk_counts.get(result.risk_level, 0) + 1

    print("\nRisk Distribution:")
    for risk_level in ['low', 'moderate', 'high', 'very_high']:
        count = risk_counts.get(risk_level, 0)
        pct = 100 * count / len(results)
        print(f"  {risk_level.upper()}: {count} ({pct:.0f}%)")

    # Expected impact
    baseline_successes = sum(r.adjusted_success_rate for r in results)
    predicted_successes = sum(r.predicted_with_interventions for r in results)
    additional_successes = predicted_successes - baseline_successes

    print(f"\nExpected Additional Successes: {additional_successes:.1f} patients")


def example_6_json_output():
    """Example 6: Saving results as JSON for integration with other systems."""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: JSON Output for System Integration")
    print("=" * 70)

    config = Configuration('lai_prep_config.json')
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    patient = PatientProfile(
        population='general_population',
        current_prep_status='naive',
        barriers=['rural_location', 'transportation'],
        healthcare_setting='telehealth',
        age=45,
        insurance_status='insured'
    )

    result = assessor.assess_patient(patient)

    # Generate JSON
    json_output = result.to_json(indent=2)

    print("JSON Output Example (first 1000 characters):")
    print(json_output[:1000])
    print("...")

    # Save to file
    filename = 'example_assessment.json'
    with open(filename, 'w') as f:
        f.write(json_output)

    print(f"\nFull JSON saved to: {filename}")
    print("This can be imported into EHR systems, analyzed in R/Python, etc.")


def example_7_mechanism_analysis():
    """Example 7: Analyzing intervention mechanisms."""
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Intervention Mechanism Analysis")
    print("=" * 70)

    config = Configuration('lai_prep_config.json')
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    patient = PatientProfile(
        population='cisgender_women',
        current_prep_status='naive',
        barriers=['medical_mistrust', 'stigma', 'childcare'],
        healthcare_setting='community_health_center',
        insurance_status='insured'
    )

    result = assessor.assess_patient(patient)

    print("Interventions by Mechanism:\n")

    # Group interventions by mechanism
    mechanisms_dict = {}
    for intervention in result.recommended_interventions:
        for mechanism in intervention['mechanisms']:
            if mechanism not in mechanisms_dict:
                mechanisms_dict[mechanism] = []
            mechanisms_dict[mechanism].append(intervention['name'])

    for mechanism, interventions in sorted(mechanisms_dict.items()):
        print(f"{mechanism.replace('_', ' ').title()}:")
        for intervention_name in interventions:
            print(f"  • {intervention_name.replace('_', ' ').title()}")
        print()


def example_8_comparative_scenarios():
    """Example 8: Comparing different barrier scenarios."""
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Comparative Scenario Analysis")
    print("=" * 70)

    config = Configuration('lai_prep_config.json')
    assessor = BridgePeriodAssessor(config, enable_logging=False)

    scenarios = [
        {
            'name': 'Ideal: MSM, insured, no barriers',
            'profile': PatientProfile(
                population='msm',
                current_prep_status='current_oral',
                barriers=[],
                healthcare_setting='private_practice',
                insurance_status='insured'
            )
        },
        {
            'name': 'Moderate: Woman, 2 barriers',
            'profile': PatientProfile(
                population='cisgender_women',
                current_prep_status='naive',
                barriers=['transportation', 'childcare'],
                healthcare_setting='community_health_center',
                insurance_status='insured'
            )
        },
        {
            'name': 'Challenging: PWID, multiple barriers',
            'profile': PatientProfile(
                population='pwid',
                current_prep_status='naive',
                barriers=['unstable_housing', 'substance_use', 'legal_concerns', 'no_insurance'],
                healthcare_setting='harm_reduction_service',
                insurance_status='uninsured'
            )
        }
    ]

    print(f"{'Scenario':<35} {'Baseline':<10} {'Adjusted':<10} {'Predicted':<10} {'Improvement'}")
    print("-" * 80)

    for scenario in scenarios:
        result = assessor.assess_patient(scenario['profile'])
        improvement = result.predicted_with_interventions - result.adjusted_success_rate

        print(
            f"{scenario['name']:<35} "
            f"{result.baseline_success_rate:>8.1%}  "
            f"{result.adjusted_success_rate:>8.1%}  "
            f"{result.predicted_with_interventions:>8.1%}  "
            f"+{improvement:>6.1%}"
        )


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("LAI-PrEP BRIDGE PERIOD DECISION SUPPORT TOOL")
    print("Example Usage Demonstrations")
    print("Version 1.0.0")
    print("=" * 70)

    examples = [
        ("Basic Assessment", example_1_basic_assessment),
        ("Oral→Injectable Transition", example_2_oral_to_injectable_transition),
        ("High-Barrier PWID", example_3_high_barrier_pwid),
        ("Adolescent Privacy Concerns", example_4_adolescent_privacy_concerns),
        ("Batch Assessment", example_5_batch_assessment),
        ("JSON Output", example_6_json_output),
        ("Mechanism Analysis", example_7_mechanism_analysis),
        ("Comparative Scenarios", example_8_comparative_scenarios),
    ]

    for name, example_func in examples:
        try:
            example_func()
            input(f"\nPress Enter to continue to next example...")
        except KeyboardInterrupt:
            print("\n\nExamples interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ Error in example '{name}': {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 70)
    print("Examples complete!")
    print("=" * 70)
    print("\nFor more information, see README.md")
    print("For clinical guidance, see CLINICAL_GUIDE.md")
    print("For implementation support, see IMPLEMENTATION_GUIDE.md")


if __name__ == '__main__':
    main()