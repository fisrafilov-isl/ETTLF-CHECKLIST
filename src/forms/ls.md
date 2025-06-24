# Learning Support Form

> **Navigation:** [Main Checklist](../checklist.md) | [ROI Form](roi.md) | [Learning Support](ls.md) | [Swimming Form](swimming.md) | [Physical Activity](physical.md) | [Extensions](../extensions.md)

```mermaid
flowchart LR
  %% ===== LEGEND =====
  subgraph Legend[" "]
    direction LR
    LegendForm[["Form"]]:::form
    LegendSection[Section]:::section
    LegendField[Field]:::field
    LegendDecision{Decision}:::decision
    LegendSkip[Skip]:::skip
  end
  Legend ~~~ LSForm
  LSForm[["Learning Support Form"]]:::form
  
  %% UNIVERSAL SECTIONS
  LSForm --> Universal[Universal Section]:::section
  Universal --> Allergies[Allergies & Dietary]:::field
  Universal --> Sports[Basic Sports Info]:::field
  Universal --> Emergency[Emergency Contacts]:::field
  
  %% CONDITIONAL BOARDING SECTION
  LSForm --> BoardingCheck{Boarding Student?}:::decision
  BoardingCheck --> |Yes| BoardingSection[Extended Medical Section]:::section
  BoardingCheck --> |No| Skip[Skip Extended Section]:::skip
  
  BoardingSection --> Medical[Detailed Medical History]:::field
  BoardingSection --> Vaccination[Vaccination Records]:::field
  BoardingSection --> Medications[Current Medications]:::field
  BoardingSection --> Psychological[Psychological Support Needs]:::field
  
  %% STYLING
  classDef form fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff;
  classDef section fill:#e3f2fd,stroke:#0d47a1,stroke-width:1px,color:#000;
  classDef field fill:#fff9c4,stroke:#f9a825,stroke-width:1px,color:#000;
  classDef decision fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000;
  classDef skip fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px,color:#000;
```

## Form Structure

### Universal Section (All Students)

#### Allergies & Dietary Requirements
**Required section** - Essential health and safety information
- **Food allergies**: Specific allergens and severity levels
- **Environmental allergies**: Pollen, dust, animals, etc.
- **Dietary restrictions**: Religious, medical, or personal preferences
- **Emergency medication**: EpiPen, inhalers, or other emergency treatments
- **Severity levels**: Mild, moderate, severe reactions

#### Basic Sports Information
**Required section** - Physical activity participation
- **Sports participation consent**: General authorization for school sports
- **Physical limitations**: Any restrictions on activities
- **Previous injuries**: Relevant medical history affecting sports
- **Preferred activities**: Student interests and preferences
- **Medical clearance**: Health status for physical activities

#### Emergency Contacts
**Required section** - Critical contact information
- **Primary emergency contact**: Parent/guardian with full details
- **Secondary emergency contact**: Alternative family member or friend
- **Medical emergency contacts**: Family doctor, specialist physicians
- **Authorization for medical treatment**: Consent for emergency care
- **Pickup authorization**: Who can collect the student

### Extended Medical Section (Boarding Students Only)

#### Detailed Medical History
**Required for boarding** - Comprehensive health background
- **Chronic conditions**: Diabetes, asthma, epilepsy, etc.
- **Mental health history**: Depression, anxiety, ADHD, etc.
- **Surgical history**: Previous operations and recovery details
- **Family medical history**: Genetic conditions and hereditary risks
- **Growth and development**: Any developmental concerns

#### Vaccination Records
**Required for boarding** - Complete immunization status
- **Standard vaccinations**: MMR, DPT, Polio, etc.
- **COVID-19 vaccination**: Current status and booster records
- **Travel vaccinations**: Hepatitis, Yellow Fever, etc.
- **Tuberculosis screening**: TB test results and dates
- **Medical exemptions**: Religious or medical vaccination waivers

#### Current Medications
**Required for boarding** - Medication management
- **Prescription medications**: Current drugs, dosages, and schedules
- **Over-the-counter medications**: Regular supplements or treatments
- **Administration instructions**: How and when to give medications
- **Storage requirements**: Refrigeration, controlled substances, etc.
- **Emergency medications**: EpiPen, rescue inhalers, seizure medications

#### Psychological Support Needs
**Required for boarding** - Mental health and behavioral support
- **Learning differences**: Dyslexia, ADHD, autism spectrum, etc.
- **Behavioral concerns**: Social anxiety, depression, anger management
- **Support strategies**: Effective coping mechanisms and interventions
- **Professional support**: Therapists, counselors, psychiatrists
- **Trigger situations**: Known stressors or problematic scenarios

## Implementation Notes

### Conditional Logic
- **Universal sections** appear for all TLF and E&T students
- **Extended medical section** only appears when boarding is selected
- **Integration with ROI**: Boarding status from Registration of Interest determines form complexity

### Medical Consultation Required
**Questions for Anna (Learning Support Coordinator):**
1. Exact field breakdown for basic vs. extended medical sections
2. Required vs. optional fields in each section
3. Integration with existing medical record requirements
4. Vaccination record format and validation requirements
5. Medication administration protocols for boarding students
6. Emergency response procedures and contact protocols

### Data Protection & Privacy
- **GDPR compliance** for sensitive medical information
- **Access controls** limiting who can view medical details
- **Secure storage** of vaccination records and medical history
- **Parent consent** for sharing medical information with relevant staff

### Integration Points
- **School nurse** receives relevant medical information
- **Boarding staff** get essential emergency and medication details
- **Sports coordinators** access physical activity restrictions
- **Academic support** team receives learning difference information