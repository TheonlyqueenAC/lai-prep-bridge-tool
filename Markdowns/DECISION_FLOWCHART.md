# LAI-PrEP Bridge Period Decision Flowchart
## Step-by-Step Visual Guide for Clinical Decision Making

---

```
═══════════════════════════════════════════════════════════════════════════
                    PATIENT REQUESTS/IS PRESCRIBED LAI-PrEP
═══════════════════════════════════════════════════════════════════════════
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 1: Is patient currently taking ORAL PrEP?                        │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                   YES                                   NO
                    │                                     │
                    ▼                                     ▼
        ┌───────────────────────┐           ┌───────────────────────┐
        │  HIV test in last     │           │  Go to STEP 2:        │
        │  7 days?              │           │  Population           │
        └───────────────────────┘           │  Assessment           │
                    │                       └───────────────────────┘
        ┌───────────┴───────────┐
       YES                      NO
        │                        │
        ▼                        ▼
┌──────────────────┐    ┌──────────────────┐
│  🎯 PRIORITY 1   │    │  🎯 PRIORITY 2   │
│  Same-Day Switch │    │  Rapid Transit.  │
├──────────────────┤    ├──────────────────┤
│ Success: 90%     │    │ Success: 85-90%  │
│ Bridge: 0-3 days │    │ Bridge: 7-14 days│
│                  │    │                  │
│ ACTION:          │    │ ACTION:          │
│ • Inject TODAY   │    │ • Order HIV test │
│ • Or within 3    │    │ • Same-day if    │
│   days max       │    │   possible       │
│ • Submit ins.    │    │ • Schedule inj.  │
│   auth same day  │    │   for next week  │
│                  │    │ • Submit ins.    │
│ ✓ DONE!          │    │   auth TODAY     │
└──────────────────┘    └──────────────────┘
```

---

```
═══════════════════════════════════════════════════════════════════════════
                    STEP 2: POPULATION & BARRIER ASSESSMENT
                         (For patients NOT on oral PrEP)
═══════════════════════════════════════════════════════════════════════════
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  What population does the patient belong to?                            │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
    ┌─────────┐                  ┌─────────┐                  ┌──────────┐
    │   MSM   │                  │  Women  │                  │Adolescent│
    │ Base:55%│                  │ Base:45%│                  │ Base:35% │
    └─────────┘                  └─────────┘                  └──────────┘
        │                             │                             │
        │                             │                             │
        ▼                             ▼                             ▼
    ┌─────────┐                  ┌──────────┐                 ┌──────────┐
    │Trans    │                  │  PWID    │                 │ Other    │
    │Women    │                  │ Base:25% │                 │Population│
    │Base:50% │                  │          │                 │          │
    └─────────┘                  └──────────┘                 └──────────┘
                                      │
                                      │
                                      ▼
═══════════════════════════════════════════════════════════════════════════
                           BARRIER ASSESSMENT
═══════════════════════════════════════════════════════════════════════════

Check ALL that apply - each barrier reduces success rate by ~10%:

☐ Transportation barriers
☐ Childcare needs
☐ Housing instability  
☐ Insurance delays expected
☐ Scheduling conflicts
☐ Medical mistrust
☐ Privacy concerns
☐ Healthcare discrimination history
☐ Competing priorities
☐ Limited healthcare experience
☐ Legal/criminalization concerns (PWID)
☐ No government ID
☐ Active substance use

                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  CALCULATE ADJUSTED SUCCESS RATE:                                       │
│                                                                          │
│  Baseline (population) - (10% × number of barriers) = Adjusted Rate    │
│                                                                          │
│  Example: Women (45%) with 3 barriers (30%) = 15% success              │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
                              Go to STEP 3
```

---

```
═══════════════════════════════════════════════════════════════════════════
                    STEP 3: RISK CATEGORIZATION & INTERVENTION
═══════════════════════════════════════════════════════════════════════════
                                      │
                    What is the ADJUSTED success rate?
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
┌───────────────┐            ┌────────────────┐           ┌────────────────┐
│   >70%        │            │   50-69%       │           │    30-49%      │
│   LOW RISK    │            │   MODERATE     │           │   HIGH RISK    │
├───────────────┤            ├────────────────┤           ├────────────────┤
│ Standard      │            │ Navigation     │           │ Multiple       │
│ protocols OK  │            │ recommended    │           │ interventions  │
│               │            │                │           │ required       │
│ ACTIONS:      │            │ ACTIONS:       │           │                │
│ • Text        │            │ • Assign       │           │ ACTIONS:       │
│   reminders   │            │   navigator    │           │ • Navigator    │
│ • Rapid HIV   │            │ • Text         │           │   (required)   │
│   testing     │            │   reminders    │           │ • Accelerated  │
│ • Schedule    │            │ • Rapid        │           │   testing      │
│   injection   │            │   testing      │           │ • Transport    │
│               │            │ • Address 1-2  │           │   support      │
│ Expected:     │            │   key barriers │           │ • Barrier-     │
│ 70-85%        │            │                │           │   specific     │
│ success       │            │ Expected:      │           │   support      │
│               │            │ 60-75%         │           │ • Close f/u    │
└───────────────┘            │ success        │           │                │
                             └────────────────┘           │ Expected:      │
                                                          │ 40-60%         │
                                                          │ success        │
                                                          └────────────────┘
                                      │
                                      ▼
                             Go to STEP 4

        ┌─────────────────────────────┐
        │      <30%                   │
        │   VERY HIGH RISK            │
        ├─────────────────────────────┤
        │ System redesign needed      │
        │ Traditional clinic will     │
        │ FAIL                        │
        │                             │
        │ ACTIONS:                    │
        │ • Intensive navigation      │
        │ • ALL barrier supports      │
        │ • Consider:                 │
        │   - Mobile delivery         │
        │   - Harm reduction site     │
        │   - Peer navigators         │
        │   - Alternative setting     │
        │                             │
        │ Expected: 30-45% success    │
        │ (with intensive support)    │
        └─────────────────────────────┘
```

---

```
═══════════════════════════════════════════════════════════════════════════
                    STEP 4: INTERVENTION SELECTION MATRIX
═══════════════════════════════════════════════════════════════════════════

Based on patient characteristics, SELECT interventions:

┌─────────────────────────────────────────────────────────────────────────┐
│  IF PATIENT IS:                    THEN IMPLEMENT:                      │
├─────────────────────────────────────────────────────────────────────────┤
│  • PWID                           → SSP/Harm Reduction Integration      │
│                                     (CRITICAL - +15 points)             │
│                                   → Peer Navigator (+12 points)         │
│                                   → Mobile delivery if possible         │
│                                     (+12 points)                        │
│                                                                          │
│  • Adolescent                     → Youth-specific navigator            │
│                                     (+15 points)                        │
│                                   → Transportation support              │
│                                     (+8 points)                         │
│                                   → Privacy protections                 │
│                                   → Flexible scheduling                 │
│                                                                          │
│  • Woman with children            → Childcare support (+8 points)       │
│                                   → Transportation (+8 points)          │
│                                   → Female/culturally matched           │
│                                     navigator (+15 points)              │
│                                                                          │
│  • Medical mistrust present       → Culturally concordant navigator     │
│                                   → Extra education/counseling          │
│                                   → Address historical harms            │
│                                                                          │
│  • Housing instability            → Mobile delivery (+12 points)        │
│                                   → Multiple contact methods            │
│                                   → SSP integration if available        │
│                                                                          │
│  • Insurance delays likely        → Submit auth SAME DAY as Rx          │
│                                   → Expedited pathway (+10 points)      │
│                                   → Daily follow-up on status           │
│                                                                          │
│  • Transportation barrier         → Uber/Lyft vouchers (+8 points)      │
│                                   → Public transit passes               │
│                                   → Mobile delivery (+12 points)        │
└─────────────────────────────────────────────────────────────────────────┘

UNIVERSAL INTERVENTIONS (All patients):
✓ Text message reminders (+5 points)
✓ Accelerated HIV testing (RNA + Ag/Ab) (+10 points)  
✓ Navigator contact within 24h of prescription
✓ Clear timeline communication
```

---

```
═══════════════════════════════════════════════════════════════════════════
                    STEP 5: CALCULATE FINAL SUCCESS PREDICTION
═══════════════════════════════════════════════════════════════════════════
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Baseline Rate - Barrier Impact + Intervention Impact = Final Estimate  │
│                                                                          │
│  NOTE: Use 70% of combined intervention effects (diminishing returns)   │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
                              ┌───────────────┐
                              │  Is final     │
                              │  estimate     │
                              │  >70%?        │
                              └───────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                   YES                                   NO
                    │                                     │
                    ▼                                     ▼
        ┌───────────────────────┐           ┌───────────────────────┐
        │  ✓ ACCEPTABLE PLAN    │           │  ⚠ NEED MORE          │
        │                       │           │    INTERVENTION       │
        │  Proceed with         │           │                       │
        │  selected             │           │  • Add more           │
        │  interventions        │           │    supports           │
        │                       │           │  • Consider           │
        │  Go to STEP 6         │           │    alternative        │
        │                       │           │    delivery model     │
        │                       │           │  • Reassess           │
        │                       │           │    barriers           │
        └───────────────────────┘           └───────────────────────┘
```

---

```
═══════════════════════════════════════════════════════════════════════════
                    STEP 6: IMPLEMENTATION & FOLLOW-UP
═══════════════════════════════════════════════════════════════════════════

DAY 0 (Prescription Visit):
┌─────────────────────────────────────────────────────────────────────────┐
│  ☐ Complete barrier assessment                                          │
│  ☐ Select interventions based on this flowchart                         │
│  ☐ Order HIV testing (expedited/stat)                                   │
│  ☐ Submit insurance authorization (same day!)                           │
│  ☐ Assign patient navigator (if moderate-very high risk)                │
│  ☐ Provide transportation voucher (if needed)                           │
│  ☐ Schedule tentative injection appointment                             │
│  ☐ Set up text reminders                                                │
│  ☐ Give patient clear timeline and expectations                         │
│  ☐ Document barriers and plan in chart                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
DAY 1 (Next Business Day):
┌─────────────────────────────────────────────────────────────────────────┐
│  ☐ Navigator contacts patient                                           │
│  ☐ Confirm understanding and motivation                                 │
│  ☐ Address any new barriers                                             │
│  ☐ Confirm appointment times                                            │
│  ☐ Check insurance authorization status                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
DAY 2-7:
┌─────────────────────────────────────────────────────────────────────────┐
│  ☐ HIV testing completed                                                │
│  ☐ Results reviewed (same day or next day)                              │
│  ☐ Navigator provides results and confirms injection appointment        │
│  ☐ Text reminders sent (48h and 24h before)                            │
│  ☐ Insurance authorization confirmed or escalated                       │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
DAY 7-28 (Target):
┌─────────────────────────────────────────────────────────────────────────┐
│  ☐ FIRST INJECTION ADMINISTERED                                         │
│  ☐ Patient education on injection-site reactions                        │
│  ☐ Schedule next injection (2 months or 6 months)                       │
│  ☐ Provide contact info for questions                                   │
│  ☐ Hand off to retention program                                        │
│  ☐ Document outcome in tracking system                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
                            ✓ SUCCESS!

IF PATIENT MISSES APPOINTMENT:
┌─────────────────────────────────────────────────────────────────────────┐
│  SAME DAY:                                                               │
│  • Call patient                                                          │
│  • Identify barrier that caused miss                                     │
│  • Problem-solve                                                         │
│  • Reschedule for ASAP (within 3 days if possible)                     │
│                                                                          │
│  IF CAN'T REACH:                                                         │
│  • Text message                                                          │
│  • Try alternate contact method                                          │
│  • Attempt contact daily for 3 days                                      │
│  • Consider home visit or outreach (if very high risk)                  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

```
═══════════════════════════════════════════════════════════════════════════
                    SPECIAL POPULATIONS QUICK PATH
═══════════════════════════════════════════════════════════════════════════

PWID FAST TRACK:
┌─────────────────────────────────────────────────────────────────────────┐
│  Traditional clinic = FAILURE                                            │
│                                                                          │
│  ✓ MUST partner with SSP/harm reduction                                 │
│  ✓ Bring services TO the patient                                        │
│  ✓ Use peer navigators                                                  │
│  ✓ Low-barrier (no ID, no abstinence, flexible)                        │
│  ✓ Rapid HIV testing at SSP site                                        │
│  ✓ Mobile delivery if SSP partnership not possible                      │
│                                                                          │
│  Expected: 30-40% success (vs. <10% in traditional clinic)             │
└─────────────────────────────────────────────────────────────────────────┘

ADOLESCENT FAST TRACK:
┌─────────────────────────────────────────────────────────────────────────┐
│  Key barriers: Transportation, Privacy, Navigation                       │
│                                                                          │
│  ✓ Youth-specific navigator (essential)                                 │
│  ✓ Transportation without parental involvement                          │
│  ✓ Confidential scheduling and communication                            │
│  ✓ School-friendly appointment times                                    │
│  ✓ Bundle appointments (test + inject same day if possible)            │
│  ✓ Text-based communication (preferred by youth)                        │
│                                                                          │
│  Expected: 35-50% success (with navigation, vs. <20% without)          │
└─────────────────────────────────────────────────────────────────────────┘

ORAL PrEP PATIENT FAST TRACK:
┌─────────────────────────────────────────────────────────────────────────┐
│  YOUR EASIEST WIN!                                                       │
│                                                                          │
│  Recent HIV test? → INJECT TODAY                                        │
│  No recent test? → Order test, inject within 7 days                     │
│                                                                          │
│  ✓ Streamlined protocol                                                 │
│  ✓ Same-day insurance authorization                                     │
│  ✓ Minimal wait time                                                    │
│  ✓ Build on existing relationship                                       │
│                                                                          │
│  Expected: 85-90% success                                               │
│  DO NOT let these patients fall through cracks!                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## CLINICAL PEARLS

💡 **The #1 Thing**: Identify oral PrEP patients and transition them FAST

💡 **The #2 Thing**: Assign a navigator for anyone with 3+ barriers or very high-risk populations

💡 **The #3 Thing**: Submit insurance authorization THE SAME DAY as prescription (don't wait for HIV test)

💡 **What NOT to Do**: Prescribe and hope. Without proactive intervention, 47% won't initiate.

💡 **PWID Specific**: Traditional clinic will fail. You MUST use harm reduction approach.

💡 **Timeline Matters**: Every extra day increases attrition. Aim for <14 days oral PrEP transition, <28 days new patients.

---

*Use this flowchart at every LAI-PrEP prescription to systematically identify risks and implement evidence-based interventions.*

*Based on: Demidont & Backus (2025). Bridging the Gap: The PrEP Cascade Paradigm Shift for LAI-PrEP. Viruses.*
