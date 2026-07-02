SKILL 2: FORMAT CONTENT TO MCHP STANDARDS
===========================================
TASK: Reformat the extracted text to meet MCHP documentation standards.

INPUT: Plain extracted text from release-note-writer.md

MCHP STANDARDS TO APPLY:

1. Document must have metadata section (Product, Version, Date, Author)
2. Organize into required sections:
- Overview
- New Features
- Bug Fixes
- Known Issues
- Installation Instructions
- Technical Specifications

FORMATTING RULES:
- Define ALL acronyms on first use (e.g., "CAN (Controller Area Network)")
- Use proper capitalization for product names
- Ensure consistent list formatting
- Mark code/file paths clearly
- Use date format: Month DD, YYYY
- Remove marketing hype, keep factual
- Fix grammar and sentence structure
- Number installation steps clearly
- Check that all acronyms are defined

QUALITY CHECKS:
- All sections are complete
- No incomplete sentences
- Features are verified (not "coming soon")
- Known issues are clearly described
- Installation steps are complete

OUTPUT: Formatted text saved to: output/mchp_formatted/formatted_content.txt
