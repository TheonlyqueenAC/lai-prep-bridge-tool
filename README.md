# 🏥 LAI-PrEP Bridge Period Decision Support Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![DOI](https://img.shields.io/badge/DOI-pending-lightgrey.svg)](https://doi.org/pending)

## 🎯 Overview

A comprehensive clinical decision support tool for optimizing Long-Acting Injectable (LAI) PrEP initiation by addressing the **bridge period** - the critical gap between PrEP prescription and first injection.

**The Problem:** Only 53% of patients prescribed LAI-PrEP successfully receive their first injection.

**The Solution:** Evidence-based interventions can increase this to 70%+ through systematic bridge period management.

### Key Features

✅ **Patient Risk Assessment** - Predict bridge period success probability  
✅ **Population-Specific Barriers** - Identify barriers for MSM, women, adolescents, PWID  
✅ **Evidence-Based Interventions** - Recommend proven strategies from implementation science  
✅ **Outcome Prediction** - Estimate improved success rates with interventions  
✅ **Healthcare System Analysis** - Assess organizational readiness and capacity  

---

## 📊 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/lai-prep-bridge-tool.git
cd lai-prep-bridge-tool

# Install dependencies
pip install -r requirements.txt

# Run the tool
python lai_prep_decision_tool.py
```

### Basic Usage

```python
from lai_prep_decision_tool import PatientProfile, assess_patient

# Create patient profile
patient = PatientProfile(
    age=24,
    population=Population.MSM,
    has_insurance=True,
    barriers=[Barrier.TRANSPORTATION, Barrier.SCHEDULING_CONFLICTS]
)

# Get assessment and recommendations
assessment = assess_patient(patient)
print(f"Bridge Success Probability: {assessment.success_probability:.1%}")
print(f"Recommended Interventions: {assessment.interventions}")
```

---

## 📖 Documentation

### For Clinicians
- **[Quick Reference Card](QUICK_REFERENCE_CARD.md)** - One-page clinical guide
- **[Non-Technical Guide](NON_TECHNICAL_GUIDE.md)** - Comprehensive implementation guide
- **[Implementation Checklist](IMPLEMENTATION_CHECKLIST.md)** - Step-by-step implementation

### For Developers
- **[Technical Documentation](TECHNICAL_DOCUMENTATION.md)** - Code architecture and API
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute
- **[Testing Guide](TESTING_GUIDE.md)** - Testing procedures

### For Healthcare Systems
- **[System Integration Guide](SYSTEM_INTEGRATION_GUIDE.md)** - EHR integration
- **[Data Privacy Guide](DATA_PRIVACY_SECURITY.md)** - HIPAA compliance
- **[Training Materials](TRAINING_MATERIALS.md)** - Staff training resources

---

## 🔬 Evidence Base

This tool is based on systematic implementation research detailed in:

**"Bridging the Gap: The PrEP Cascade Paradigm Shift for Long-Acting Injectable HIV Prevention"**  
*Submitted to: Viruses (MDPI) - Special Issue on Long-Acting Antiretrovirals*

### Key Evidence

- **53%** baseline LAI-PrEP initiation rate in real-world settings
- **70-85%** initiation with evidence-based interventions
- **1.5-2.0x** improvement with patient navigation
- **85-90%** success rate with oral-to-injectable transitions

### Supported Interventions

1. **Patient Navigation** - Addresses logistical and structural barriers
2. **RNA Testing** - Reduces bridge period from 33 to 10-14 days
3. **Oral-to-Injectable Transition** - Eliminates bridge for experienced users
4. **Telehealth Integration** - Improves access and follow-up
5. **Pharmacy-Based Delivery** - Reduces healthcare system barriers

---

## 🏆 Clinical Impact

### Expected Outcomes

| Intervention | Expected Improvement | Evidence Level |
|-------------|---------------------|----------------|
| Patient Navigation | +20-30% initiation | Strong |
| RNA Testing | +15-20% initiation | Moderate |
| Oral-to-Injectable | +30-35% initiation | Strong |
| Combined Approach | +40-50% initiation | Moderate |

### Populations Served

- **Men who have sex with men (MSM)**
- **Cisgender women**
- **Transgender women**
- **Adolescents and young adults (16-24)**
- **People who inject drugs (PWID)**
- **Pregnant and lactating individuals**

---

## 🛠️ System Requirements

### Minimum Requirements
- Python 3.8 or higher
- 100 MB disk space
- Internet connection (for web-based version)

### Recommended
- Python 3.10+
- 500 MB disk space
- EHR integration capability

### Supported Platforms
- Windows 10/11
- macOS 10.15+
- Linux (Ubuntu 20.04+)

---

## 📋 Project Status

### Version 1.0.0 (Current)
- ✅ Core decision algorithm
- ✅ Population-specific barriers
- ✅ Evidence-based interventions
- ✅ Clinical documentation
- ✅ Implementation guides

### Roadmap

**Version 1.1.0** (Q1 2026)
- [ ] EHR integration modules
- [ ] Outcome tracking dashboard
- [ ] Multi-language support

**Version 2.0.0** (Q3 2026)
- [ ] Real-time outcome analysis
- [ ] Machine learning enhancements
- [ ] Mobile application

---

## 🤝 Contributing

We welcome contributions from clinicians, researchers, and developers!

See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report bugs
- How to suggest features
- Development workflow
- Code style guidelines

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

### Citation

If you use this tool in your research or clinical practice, please cite:

```bibtex
@article{demidont2025bridging,
  title={Bridging the Gap: The PrEP Cascade Paradigm Shift for Long-Acting Injectable HIV Prevention},
  author={Demidont, A.C. and Backus, Kandis},
  journal={Viruses},
  year={2025},
  publisher={MDPI}
}
```

---

## 🔐 Privacy & Security

- **HIPAA Compliant** - All patient data handling follows HIPAA guidelines
- **No PHI Storage** - Tool runs locally, no cloud data storage
- **Open Source** - Full transparency and auditability
- **Secure by Design** - No external API calls with patient data

See [DATA_PRIVACY_SECURITY.md](DATA_PRIVACY_SECURITY.md) for details.

---

## 📞 Support & Contact

### For Clinical Questions
- **Email:** acdemidont@nyxdynamics.org
- **Clinical Consultation:** Schedule via website

### For Technical Support
- **GitHub Issues:** [Report bugs or request features](https://github.com/yourusername/lai-prep-bridge-tool/issues)
- **Discussions:** [Community forum](https://github.com/yourusername/lai-prep-bridge-tool/discussions)

### For Implementation Support
- **Implementation Guide:** See NON_TECHNICAL_GUIDE.md
- **Training Materials:** Available in /docs/training/

---

## 🙏 Acknowledgments

This work builds on research and implementation efforts from:

- **CDC Division of HIV Prevention** - PrEP guidelines and implementation science
- **WHO HIV Department** - Global PrEP recommendations
- **HPTN Network** - Clinical trial data (HPTN 083, 084)
- **Community Health Centers** - Real-world implementation insights
- **Patient Advocates** - Lived experience and barrier identification

---

## ⭐ Star This Repository

If you find this tool useful, please consider starring this repository to help others discover it!

---

## 📊 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/lai-prep-bridge-tool?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/lai-prep-bridge-tool?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/lai-prep-bridge-tool?style=social)

---

**Making LAI-PrEP accessible to all who need it.** 🏳️‍🌈❤️

*Last updated: October 2025*
