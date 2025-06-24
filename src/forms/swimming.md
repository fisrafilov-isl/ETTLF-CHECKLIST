# Swimming Permission Form

> **Navigation:** [Main Checklist](../checklist.md) | [ROI Form](roi.md) | [Learning Support](ls.md) | [Swimming Form](swimming.md) | [Physical Activity](physical.md) | [Extensions](../extensions.md)

```mermaid
flowchart LR
  %% ===== LEGEND =====
  subgraph Legend[" "]
    direction LR
    LegendForm[["Form"]]:::form
    LegendField[Field]:::field
    LegendRadio(Radio Button):::answer
    LegendConsent[Consent]:::conditional
  end
  Legend ~~~ SwimmingForm

  %% ===== MAIN FORM =====
  SwimmingForm[["Swimming Permission Form"]]:::form
  
  %% ===== FORM FIELDS =====
  SwimmingForm --> SwimmingLevel[Swimming Ability Level]:::field
  SwimmingLevel --> Proficient(Proficient):::answer
  SwimmingLevel --> Intermediate(Intermediate):::answer
  SwimmingLevel --> Beginner(Beginner):::answer
  SwimmingLevel --> NoSwim(Doesn't know how to swim):::answer
  
  SwimmingForm --> PoolConsent[Pool Facilities Consent]:::conditional
  PoolConsent --> PoolYes(I/we confirm consent):::answer
  PoolConsent --> PoolNo(I/we do not consent):::answer
  
  SwimmingForm --> SeaConsent[Sea Swimming Consent]:::conditional
  SeaConsent --> SeaYes(I/we confirm consent):::answer
  SeaConsent --> SeaNo(I/we do not consent):::answer
  
  SwimmingForm --> RiskAcknowledgment[Risk Acknowledgment & Medical Disclosure]:::conditional

  %% ===== STYLING =====
  classDef form fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff;
  classDef field fill:#e3f2fd,stroke:#0d47a1,stroke-width:1px,color:#000;
  classDef answer fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px,color:#000;
  classDef conditional fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#000;
```

## Form Structure

### Swimming Ability Assessment
**Required field** - Multiple choice selection
- **Proficient**: Advanced swimming skills
- **Intermediate**: Basic swimming competency
- **Beginner**: Limited swimming ability
- **Doesn't know how to swim**: No swimming skills

### Pool Facilities Consent
**Required field** - Consent for swimming pool use
- Confirms parent authorization for pool activities
- Under boarding house staff supervision

### Sea Swimming Consent  
**Required field** - Consent for supervised sea activities
- Authorization for sea swimming under staff supervision
- Additional risk acknowledgment required

### Risk Acknowledgment
**Required field** - Legal disclaimer and medical disclosure
- Acknowledgment of inherent swimming risks
- Consent for participation under appropriate supervision
- Confirmation of medical condition disclosure
- Medical concerns affecting swimming safety

## Implementation Notes

### Boarding-Specific Form
- **Visible for**: Boarding students only
- **Condition**: Only appears if "Boarding Y/N" = Yes in ROI
- **Integration**: Part of boarding consent package

### Legal Compliance
- Digital signature capture required
- Risk acknowledgment with legal disclaimer
- Medical disclosure confirmation
- Parental consent documentation 