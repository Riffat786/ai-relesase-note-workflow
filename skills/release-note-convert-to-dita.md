SKILL 3: CONVERT FORMATTED TEXT TO DITA/XML
=============================================
TASK: Convert MCHP-formatted text into valid DITA (Darwin Information Typing Architecture) XML.

INPUT: Formatted text from SKILL 2

DITA TEMPLATE: The template is in templates/mchp_release_note.dita

CONVERSION RULES:

1. Root element must be: topic id="release_note"
2. Title: <title>Release Note - {{PRODUCT_NAME}} v{{VERSION}}</title>
3. Metadata in <prolog> section:
    - <prodname> = Product Name
    - version = Version number
    - <author> = Author/Company
    - date = Release Date in YYYY-MM-DD format
4. Body sections must use:
  - <section id="overview"> for Overview
  - <section id="new_features"> for New Features
  - <section id="bug_fixes"> for Bug Fixes
  - <section id="known_issues"> for Known Issues
  - <section id="installation"> for Installation Instructions
5. Text content in <p> elements (paragraphs)
6. Lists using <ul> (unordered) or <ol> (ordered) with <li> items
7. Code/paths in <codeblock> elements
8. All text must be XML-safe (escape &, <, >, ", ')

VALIDATION:
? All sections present
? Valid XML syntax
? All required metadata filled in
? Proper nesting of elements
? No unclosed tags
OUTPUT: Valid DITA XML saved to: output/dita_xml/release_note.dita
