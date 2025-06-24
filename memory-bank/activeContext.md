# Active Context: Current Project Status

## Current Work Focus

### Immediate Priority: Cross-Referenced Flowchart System
Project has been reorganized with files moved to `~/src` directory. Focus is now on creating interconnected flowcharts that reference each other for better navigation and understanding.

### NEW ARCHITECTURE: Cross-Referenced Flowcharts

#### File Structure:
- `~/src/01_ROI.md` - Registration of Interest form flow
- `~/src/Checklist.md` - Main checklist process flow  
- `~/src/Extensions.md` - Suggestions for additional functionality

#### Cross-Reference Strategy:
- Each flowchart links to related flowcharts
- Consistent `[[]]` subroutine shapes for all checklist items
- Unified color coding across all charts
- Bidirectional navigation between related processes

### ENHANCED UNDERSTANDING: Complete Checklist Requirements

#### Based on Ilya's Latest Requirements:

**Programme Options:**
1. **TLF with boarding** - Scholarship programme with boarding
2. **TLF without boarding** - Scholarship programme day school
3. **E&T with boarding** - Paid programme with boarding  
4. **E&T without boarding** - Paid programme day school

**Learning Support Form Split:**
- **Day School Only**: Basic questions (allergies, sports, etc.)
- **Boarding Students**: Extended form with additional medical information

**New Mandatory Requirements:**
1. Learning support form (split based on boarding)
2. Visa documents (waiting from Nicos until June 21st)
3. Signed contract with foundation (TLF only)
4. School contract signed (Enrollment Form + DocuSign)
5. Swimming consent form
6. Sports participation consent form
7. School report from last school (2 years, English translation)
8. Student passport photo
9. Parent passport photo (one parent sufficient)
10. Parent consent form (emergency authorization)
11. Boarding code of conduct (available after July 1st)

**Optional Requirements:**
1. Portfolio
2. Olympiads, certificates, achievements
3. Sport preferences

### Current Implementation Status

#### Completed:
- Basic flowchart structures created
- Cross-reference concept established
- Consistent styling approach defined

#### In Progress:
- ROI dependency field identification
- Checklist item numbering removed
- Cross-referencing implementation

#### Pending Dependencies:
- **Nicos**: Visa document list (June 21st deadline)
- **Anna**: Learning support form field breakdown
- **Head of Boarding**: Boarding code of conduct (starts July 1st)
- **Legal Review**: Consent form templates (after June 21st)

## Updated Next Steps

### Immediate Actions:
1. **Create Cross-Referenced Flowcharts**: Link ROI and Checklist flows
2. **Remove Item Numbers**: Clean up checklist for better readability
3. **Add Extensions Documentation**: Comprehensive suggestions file
4. **Update File Locations**: Ensure all references point to ~/src

### Architecture Decisions:

#### Learning Support Form:
- Single form with conditional fields based on boarding status
- Additional medical section appears only for boarding students
- Consult with Anna for exact field breakdown

#### Visa Documents:
- Single checklist item with multiple document fields
- Conditional display based on nationality (Cyprus/EU vs international)
- Include criminal background check (справка о несудимости)

#### Sports and Swimming:
- Consider merging consent forms to reduce form fatigue
- Include sport preferences in sports participation form

## Current Stakeholder Status

### Active:
- **Fazil**: Implementing cross-referenced flowchart system
- **Ilya**: Provided comprehensive requirements update

### Awaiting:
- **Anna**: Learning support / medical form consultation
- **Nicos**: Official visa document list
- **Head of Boarding**: Boarding rules and procedures
- **Legal**: Consent form templates

### Timeline Critical:
- **June 21st**: Parent/student meeting deadline
- **June 21st**: Visa document specifications from Nicos
- **July 1st**: Head of boarding starts

## Integration Points

### OpenApply Workflow:
1. ROI form submission triggers checklist appearance
2. Conditional logic based on programme selection (TLF vs E&T)
3. Boarding status affects Learning Support form complexity
4. Nationality determines visa requirements
5. Grade level affects IB course options

### Legal Compliance:
- Digital signature validity maintained through consent clauses
- Single parent authorization for subsequent forms
- OpenApply account security requirements
- Cyprus law compliance for all signatures

## Risk Areas

### Timeline Pressure:
- June 21st deadline approaching
- Multiple stakeholder dependencies
- Complex conditional logic requirements

### Technical Complexity:
- OpenApply platform limitations
- Conditional form display challenges
- Cross-reference navigation implementation

### Stakeholder Coordination:
- Multiple approval processes required
- Varying availability of key personnel
- Integration with existing school systems 