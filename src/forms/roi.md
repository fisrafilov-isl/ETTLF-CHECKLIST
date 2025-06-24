
# Registration of Interest

> **Navigation:** [Main Checklist](../checklist.md) | [ROI Form](roi.md) | [Learning Support](ls.md) | [Swimming Form](swimming.md) | [Physical Activity](physical.md) | [Extensions](../extensions.md)

```mermaid
flowchart LR
  %% ===== LEGEND =====
  subgraph Legend[" "]
    direction LR
    LegendForm[["Form"]]:::start
    LegendDocument[["Document"]]:::checklist
    LegendField[Field]:::field
    LegendAnswer(Answer):::answer
    LegendConditional[Conditional]:::conditional
    LegendDecision{Decision}:::decision
  end
  Legend ~~~ ROI

  %% ===== MAIN FORM =====
  ROI[["Submit Registration of Interest"]]:::start
  ROI --> Grade[Grade]:::field

  %% ===== CONDITIONAL PROGRAMME FIELDS =====
  Grade --> |if Grade:PP3-G12|IBProg[IB Programme Y/N]:::conditional
  Grade --> |if Grade:WFC-G8|WFProg[WF Programme Y/N]:::conditional  
  Grade --> |if Grade:PP3-G3|MONTProg[MONT Programme Y/N]:::conditional
  Grade --> |if Grade:G6-G12|Boarding[Boarding Y/N]:::conditional

  %% ===== BOARDING CONDITIONAL FIELDS =====
  Boarding --> BoardingYes(Yes):::answer
  Boarding --> BoardingNo(No):::answer
  
  ROI --> Nationality[Student Nationality]:::field
  
  %% ===== VISA DOCUMENTS: E&T/TLF + NATIONALITY =====
  IBE&T --> VisaCheck{Check Student Nationality}:::decision
  IBTLF --> VisaCheck
  Nationality -.-> |nationality info| VisaCheck
  
  VisaCheck --> |Cyprus/EU| NoVisaDocs[No Visa Documents Required]:::field
  VisaCheck --> |Non-EU| VisaDocsRequired[Visa Documents Required]:::field
  
  %% ===== CHECKLIST ITEM =====
  VisaDocsRequired --> VisaDocsChecklist[["Submit Visa Documents"]]:::checklist

  %% ===== IB CONDITIONAL FIELDS =====
  Grade --> |if Grade:G9-G11|IBTracks[IB Tracks]:::conditional
  Grade --> |if Grade:G11-G12|IBCourse[IB Course]:::conditional

  IBTracks --> IBRed(IB):::answer
  IBTracks --> IBE&T(IB E&T):::answer
  IBTracks --> IBTLF(IB TLF):::answer

  IBCourse --> IBCP(IB CP):::answer
  IBCourse --> IBDP(IB DP):::answer

  %% ===== STYLING =====
  classDef start fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff;
  classDef field fill:#e3f2fd,stroke:#0d47a1,stroke-width:1px,color:#000;
  classDef answer fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px,color:#000;
  classDef conditional fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#000;
  classDef decision fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000;
  classDef checklist fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#fff;
  classDef endpoint fill:#ffcdd2,stroke:#d32f2f,stroke-width:1px,color:#000;
```

## Field Visibility Rules

### Grade Selection
**Always visible** - Determines which programme fields appear

### Citizenship
**Always visible** - Multiple choice field with all world countries
- **EU citizens:** No additional requirements
- **Non-EU citizens:** Visa documents required

### IB Programme Y/N
**Visible for grades:** PP3, PP4, PP5, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12

### WF Programme Y/N  
**Visible for grades:** Waldorf Family Club/Pareklisia, PP3, PP4, PP5, G1, G2, G3, G4, G5, G6, G7, G8

### MONT Programme Y/N
**Visible for grades:** PP3, PP4, PP5, G1, G2, G3

### Boarding Y/N
**Visible for grades:** G6, G7, G8, G9, G10, G11, G12

### Visa Documents Required (collected in subsequent checklist items)
**Visible for:** Non-EU citizens only
**Condition:** Only if Citizenship ≠ EU country

### IB Tracks (Multiple Choice: IB / IB E&T / IB TLF)
**Visible for grades:** G9, G10, G11
**Condition:** Only if "IB Programme Y/N" = Yes

### IB Course (Multiple Choice: IB CP / IB DP)
**Visible for grades:** G11, G12  
**Condition:** Only if "IB Programme Y/N" = Yes


