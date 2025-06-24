# OpenApply Checklist - Current Flow

> **Navigation:** [Main Checklist](checklist.md) | [ROI Form](forms/roi.md) | [Learning Support](forms/ls.md) | [Swimming Form](forms/swimming.md) | [Physical Activity](forms/physical.md) | [Extensions](extensions.md)

## Current Admission Process for TLF & E&T Programmes

### Sequential Checklist Items

- ROI form: "Submit Registration of Interest" // form
- LS form: "Submit Form for Learning Support (IB: Technology Leaders Scholarship)" // form
- Swimming form: "Submit Swimming Permission Form" // form (boarding only) 
- Physical activity form: "Submit Physical Activity & Gym Use Consent Form" // form (boarding only)
- Visa documents: "Submit Visa Documents" // document submission (E&T/TLF non-EU citizens only)
- Personal references: "Upload two personal references from teachers/tutors" // document submission
- Video: "Upload a video introduction about the applicant's motivation (2-5 minutes)" // form
- Proof of achievements: "Upload proof of achievements" // document submission
- Portfolio: "Upload Portfolio with personal projects" // document submission
- Wait for response: "Receive an email with the next steps" // to do

## Current Process Flow

```mermaid
flowchart LR
  %% ===== LEGEND =====
  subgraph Legend[" "]
    direction LR
    LegendForm[["Form"]]:::form
    LegendDocument[["Document Submission"]]:::document
    LegendTodo[["To-Do Item"]]:::todo
    LegendStart([Start/End]):::start
    LegendEndpoint([Endpoint]):::endpoint
  end
  Legend ~~~ Start

  %% ===== START =====
  Start([Application Process Start]):::start
  
  %% ===== MAIN CHECKLIST ITEM =====
  ROI[["Submit Registration of Interest"]]:::form
  
  %% ===== SUBSEQUENT CHECKLIST ITEMS =====
  subgraph AfterROI[" "]
    direction TB
    LS[["Submit Form for Learning Support<br/>IB: Technology Leaders Scholarship"]]:::form
    References[["Upload two personal references<br/>from teachers/tutors"]]:::document
    Video[["Upload a video introduction about<br/>the applicant's motivation (2-5 minutes)"]]:::form
    Achievements[["Upload proof of achievements"]]:::document
    Portfolio[["Upload Portfolio with<br/>personal projects"]]:::document
    Wait[["Receive an email with<br/>the next steps"]]:::todo
    
    LS ~~~ References ~~~ Video ~~~ Achievements ~~~ Portfolio ~~~ Wait
  end
  
  %% ===== BOARDING-SPECIFIC FORMS =====
  subgraph BoardingForms["Boarding Students Only"]
    direction TB
    Swimming[["Submit Swimming Permission Form"]]:::form
    Physical[["Submit Physical Activity & Gym Use Consent Form"]]:::form
    
    Swimming ~~~ Physical
  end
  
  %% ===== VISA DOCUMENTS =====
  subgraph VisaDocs["E&T/TLF Non-EU Citizens Only"]
    direction TB
    VisaSubmission[["Submit Visa Documents"]]:::document
    
    VisaSubmission --> CriminalCheck[Criminal Background Check]:::field
    VisaSubmission --> HealthInsurance[Health Insurance Certificate]:::field
    VisaSubmission --> SponsorLetter[Sponsor Letter]:::field
    VisaSubmission --> StudentVisa[Student Visa Application]:::field
    VisaSubmission --> FinancialProof[Financial Support Documentation]:::field
  end
  
  %% ===== FLOW =====
  Start --> ROI
  ROI --> AfterROI
  ROI --> |if Boarding = Yes| BoardingForms
  ROI --> |if E&T/TLF + Non-EU| VisaDocs
  
  %% ===== END POINT =====
  AfterROI --> End([Awaiting School Response]):::endpoint
  BoardingForms --> End
  VisaDocs --> End
  
  %% ===== STYLING =====
  classDef start fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#fff;
  classDef form fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff;
  classDef document fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#fff;
  classDef todo fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff;
  classDef link fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff;
  classDef field fill:#fff9c4,stroke:#f9a825,stroke-width:1px,color:#000;
  classDef endpoint fill:#F44336,stroke:#B71C1C,stroke-width:3px,color:#fff;
```

## Item Type Legend

| Type | Description | Visual Style |
|------|-------------|--------------|
| **form** | Interactive form to be completed in OpenApply | Blue |
| **document submission** | File upload requirement | Orange |
| **to do** | Action item or waiting status | Purple |

## Process Notes

- This represents the current flow in OpenApply
- Items appear simultaneously after ROI submission  
- No conditional logic is currently implemented
- The process is the same regardless of boarding status or nationality
- Future iterations will add conditional branching based on Registration of Interest responses

## Implementation Status

### Current State
- **Simple Linear Flow**: All items appear after ROI submission
- **No Conditional Logic**: Same process for all programme types
- **Manual Processing**: School reviews applications individually

### Future Enhancements
- **Conditional Checklist Items**: Based on programme selection and boarding status
- **Automated Routing**: Different flows for TLF vs E&T programmes
- **Dynamic Requirements**: Visa documents only for non-EU boarding students

---

**Cross-References:**
- [ROI Form Details →](forms/roi.md) - Registration of Interest logic and conditions
- [Implementation Extensions →](Extensions.md) - Suggested enhancements and additional functionality 