# Physical Activity & Gym Use Consent Form

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
    LegendText[Text Input]:::text
  end
  Legend ~~~ PhysicalForm

  %% ===== MAIN FORM =====
  PhysicalForm[["Physical Activity & Gym Use Consent Form"]]:::form
  
  %% ===== FORM FIELDS =====
  PhysicalForm --> GymConsent[Gym Facilities Consent]:::conditional
  GymConsent --> GymYes(I/we confirm consent):::answer
  GymConsent --> GymNo(I/we do not consent):::answer
  
  PhysicalForm --> SportsBackground[Previous Sports Experience]:::field
  SportsBackground --> SportsText[List sports practiced before]:::text
  
  PhysicalForm --> HealthConfirmation[Health & Medical Disclosure]:::conditional

  %% ===== STYLING =====
  classDef form fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff;
  classDef field fill:#e3f2fd,stroke:#0d47a1,stroke-width:1px,color:#000;
  classDef answer fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px,color:#000;
  classDef conditional fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#000;
  classDef text fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px,color:#000;
```

## Form Structure

### Gym Facilities Consent
**Required field** - Consent for gym facility access
- **I/we confirm consent**: Authorization for gym use
- **I/we do not consent**: Opt-out of gym activities
- Under boarding house staff supervision

### Previous Sports Experience
**Optional field** - Text input for sports background
- List sports child practiced before coming to Island School
- Helps staff understand student's athletic background
- Free text input field

### Health Confirmation & Medical Disclosure
**Required field** - Health status and medical information
- Confirmation that child is in good health
- Agreement to inform school of medical conditions
- Understanding of qualified staff supervision
- Acknowledgment of safe environment protocols

## Implementation Notes

### Boarding-Specific Form
- **Visible for**: Boarding students only
- **Condition**: Only appears if "Boarding Y/N" = Yes in ROI
- **Integration**: Part of boarding consent package

### Sports Program Integration
- **Background Information**: Collected for program planning
- **Medical Clearance**: Required for participation
- **Safety Protocols**: Staff supervision and safe environment
- **Risk Management**: Medical condition disclosure requirements

### Legal Compliance
- Digital signature capture required
- Health status confirmation
- Medical disclosure agreement
- Qualified supervision acknowledgment 