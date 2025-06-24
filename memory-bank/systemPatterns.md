# System Patterns: OpenApply Checklist Architecture

## System Architecture Overview

The OpenApply checklist system uses a dynamic, decision-tree based architecture that adapts the required documents and forms based on user selections and profile data.

### Core Design Patterns

#### 1. Dynamic Checklist Pattern
- **Conditional Logic**: Checklist items appear/disappear based on programme selection and boarding preferences
- **Progressive Disclosure**: Additional requirements revealed as users make selections
- **State Management**: User selections stored and referenced throughout the flow

#### 2. Document Management Pattern
- **Single Source of Truth**: Each document type has one canonical collection method
- **Conditional Requirements**: Documents required based on user attributes (nationality, programme, boarding)
- **Upload Validation**: File type, size, and content validation before acceptance

#### 3. Form Splitting Strategy
- **Basic vs Extended**: Learning Support form splits based on boarding requirements
- **Consolidation**: Related forms combined to reduce user fatigue (e.g., sports consent + preferences)
- **Legal Compliance**: Forms designed to maintain digital signature validity

### Component Relationships

#### Programme Selection Gateway
```
Registration of Interest
    ↓
Programme Selection (TLF/E&T)
    ↓
Boarding Decision (Yes/No)
    ↓
Dynamic Checklist Generation
```

#### Conditional Document Flow
```
Learning Support Form:
  - Boarding = No  → Basic Form (allergies, sports, etc.)
  - Boarding = Yes → Extended Form (+ medical info)

Visa Documents:
  - Cyprus/EU = No → Full visa document checklist
  - Cyprus/EU = Yes → Skip visa requirements

Passport Requirements:
  - Cypriot Citizens → Passport OR ID card accepted
  - Non-Cypriot → Passport only
  - Residence Permit → Not accepted
```

#### Form Integration Points
1. **OpenApply Forms** - Custom forms with digital signature capability
2. **Document Uploads** - File upload with categorization
3. **External Systems** - DocuSign integration for enrollment contracts
4. **Validation Rules** - Real-time validation and error handling

### Key Technical Decisions

#### 1. Form Segmentation Strategy
- **Learning Support Form Split**: Separate basic/extended versions instead of conditional fields
- **Single Visa Collection**: Multiple visa documents collected under one checklist item with multiple fields
- **Consent Form Consolidation**: Swimming and sports consent potentially merged to reduce form count

#### 2. Legal Compliance Architecture
- **Digital Signature Clauses**: Embedded in enrollment form to cover all supplementary forms
- **Parent Authorization**: Single designated parent can sign on behalf of family
- **Security Requirements**: OpenApply username/password responsibility clauses

#### 3. Data Flow Patterns
- **Profile-Driven Logic**: Nationality field drives visa requirements
- **Selection-Driven Logic**: Programme and boarding choices drive form requirements
- **Status-Driven Logic**: Form completion status drives progression

### Integration Architecture

#### OpenApply Platform Integration
- **Custom Forms**: Built within OpenApply form builder
- **Checklist Logic**: Implemented using OpenApply's conditional checklist features
- **File Management**: Leverages OpenApply's document categorization
- **Workflow Automation**: Uses OpenApply's status change triggers

#### External System Integration
- **DocuSign**: Enrollment contract signing workflow
- **School Database**: Student information synchronization
- **Communication System**: Automated email notifications

### Error Handling Patterns
- **Validation Feedback**: Real-time form validation with clear error messages
- **Progress Preservation**: Ability to save partial progress and return later
- **Fallback Options**: Manual upload options when automated forms fail
- **Support Escalation**: Clear pathways to human assistance when needed 