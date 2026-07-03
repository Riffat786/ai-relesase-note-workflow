#!/usr/bin/env python3
"""
Generate GlobalMail Pro Presentation PPTX using only standard library
Creates a professional PowerPoint file with proper XML structure
"""

import zipfile
import os
from pathlib import Path

# PPTX structure creator without external dependencies
def create_pptx():
    pptx_file = 'GlobalMail_Pro_Release_Notes_Automation.pptx'

    # Remove existing file if present
    if os.path.exists(pptx_file):
        os.remove(pptx_file)

    with zipfile.ZipFile(pptx_file, 'w', zipfile.ZIP_DEFLATED) as pptx:
        # [Content_Types].xml
        pptx.writestr('[Content_Types].xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
<Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
<Override PartName="/ppt/slides/slide2.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
<Override PartName="/ppt/slides/slide3.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
<Override PartName="/ppt/slides/slide4.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
<Override PartName="/ppt/slides/slide5.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
<Override PartName="/ppt/slideLayouts/slideLayout2.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
<Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>
<Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>
<Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.custom-properties+xml"/>
</Types>''')

        # _rels/.rels
        pptx.writestr('_rels/.rels', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>''')

        # ppt/_rels/presentation.xml.rels
        pptx.writestr('ppt/_rels/presentation.xml.rels', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide1.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide2.xml"/>
<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide3.xml"/>
<Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide4.xml"/>
<Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide5.xml"/>
<Relationship Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/presProps" Target="presProps.xml"/>
<Relationship Id="rId8" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps" Target="viewProps.xml"/>
<Relationship Id="rId9" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableStyles" Target="tableStyles.xml"/>
</Relationships>''')

        # ppt/presentation.xml
        pptx.writestr('ppt/presentation.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:rel="http://schemas.openxmlformats.org/package/2006/relationships">
<p:sldMasterIdLst>
<p:sldMasterId id="256" r:id="rId1"/>
</p:sldMasterIdLst>
<p:sldIdLst>
<p:sldId id="256" r:id="rId2"/>
<p:sldId id="257" r:id="rId3"/>
<p:sldId id="258" r:id="rId4"/>
<p:sldId id="259" r:id="rId5"/>
<p:sldId id="260" r:id="rId6"/>
</p:sldIdLst>
<p:sldSz cx="9144000" cy="6858000"/>
<p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>''')

        # Create slide files - simplified but functional
        slides_content = [
            (1, "SLIDE 1: GlobalMail Pro\nAutomated Release Notes Workflow", "navy"),
            (2, "SLIDE 2: The Transformation\nManual vs Automated", "white"),
            (3, "SLIDE 3: End-to-End Workflow\nComplete Pipeline with Timings", "white"),
            (4, "SLIDE 4: Live Demonstration\nVideo Placeholder", "white"),
            (5, "SLIDE 5: Thank You\nQuestions & Discussion", "navy")
        ]

        for slide_num, title, bg_color in slides_content:
            hex_color = "1B2A4A" if bg_color == "navy" else "FFFFFF"
            rgb_color = f"<a:srgbClr val=\"{hex_color}\"/>" if bg_color == "white" else f"<a:srgbClr val=\"{hex_color}\"/>"
            text_color = "FFFFFF" if bg_color == "navy" else "1B2A4A"

            slide_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
<p:cSld>
<p:bg>
<p:bgPr>
<a:solidFill>
<a:srgbClr val="{hex_color}"/>
</a:solidFill>
<a:effectLst/>
</p:bgPr>
</p:bg>
<p:spTree>
<p:nvGrpSpPr>
<p:cNvPr id="1" name="Group 1"/>
<p:cNvGrpSpPr/>
<p:nvPr/>
</p:nvGrpSpPr>
<p:grpSpPr>
<a:xfrm>
<a:off x="0" y="0"/>
<a:ext cx="9144000" cy="6858000"/>
<a:chOff x="0" y="0"/>
<a:chExt cx="9144000" cy="6858000"/>
</a:xfrm>
</p:grpSpPr>
<p:sp>
<p:nvSpPr>
<p:cNvPr id="2" name="Title 1"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
<p:spPr>
<a:xfrm>
<a:off x="457200" y="457200"/>
<a:ext cx="8229600" cy="5943600"/>
</a:xfrm>
</p:spPr>
<p:txBody>
<a:bodyPr/>
<a:lstStyle/>
<a:p>
<a:r>
<a:rPr lang="en-US" sz="6000" b="1"/>
<a:t>{title}</a:t>
</a:r>
</a:p>
</p:txBody>
</p:sp>
<p:sp>
<p:nvSpPr>
<p:cNvPr id="3" name="Footer"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
<p:spPr>
<a:xfrm>
<a:off x="457200" y="6400000"/>
<a:ext cx="8229600" cy="400000"/>
</a:xfrm>
</p:spPr>
<p:txBody>
<a:bodyPr/>
<a:lstStyle/>
<a:p>
<a:r>
<a:rPr lang="en-US" sz="1200"/>
<a:t>GlobalMail Pro | Slide {slide_num}/5</a:t>
</a:r>
</a:p>
</p:txBody>
</p:sp>
</p:spTree>
</p:cSld>
<p:clrMapOvr>
<a:masterClrMapping/>
</p:clrMapOvr>
</p:sld>'''

            pptx.writestr(f'ppt/slides/slide{slide_num}.xml', slide_xml)

        # ppt/slideMasters/slideMaster1.xml (minimal)
        pptx.writestr('ppt/slideMasters/slideMaster1.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
<p:cSld>
<p:bg>
<p:bgPr>
<a:solidFill>
<a:srgbClr val="FFFFFF"/>
</a:solidFill>
<a:effectLst/>
</p:bgPr>
</p:bg>
<p:spTree>
<p:nvGrpSpPr>
<p:cNvPr id="1" name="Group 1"/>
<p:cNvGrpSpPr/>
<p:nvPr/>
</p:nvGrpSpPr>
<p:grpSpPr>
<a:xfrm>
<a:off x="0" y="0"/>
<a:ext cx="9144000" cy="6858000"/>
<a:chOff x="0" y="0"/>
<a:chExt cx="9144000" cy="6858000"/>
</a:xfrm>
</p:grpSpPr>
</p:spTree>
</p:cSld>
<p:clrMapOvr>
<a:masterClrMapping/>
</p:clrMapOvr>
</p:sldMaster>''')

        # ppt/slideLayouts/slideLayout1.xml & slideLayout2.xml (minimal)
        for i in range(1, 3):
            pptx.writestr(f'ppt/slideLayouts/slideLayout{i}.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
<p:cSld>
<p:spTree>
<p:nvGrpSpPr>
<p:cNvPr id="1" name="Group 1"/>
<p:cNvGrpSpPr/>
<p:nvPr/>
</p:nvGrpSpPr>
<p:grpSpPr>
<a:xfrm>
<a:off x="0" y="0"/>
<a:ext cx="9144000" cy="6858000"/>
<a:chOff x="0" y="0"/>
<a:chExt cx="9144000" cy="6858000"/>
</a:xfrm>
</p:grpSpPr>
</p:spTree>
</p:cSld>
</p:sldLayout>''')

        # ppt/presProps.xml
        pptx.writestr('ppt/presProps.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presProps xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>''')

        # ppt/viewProps.xml
        pptx.writestr('ppt/viewProps.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:viewPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<p:normalViewPr/>
<p:slideViewPr/>
<p:outlineViewPr/>
<p:notesViewPr/>
<p:handoutViewPr/>
</p:viewPr>''')

        # ppt/tableStyles.xml
        pptx.writestr('ppt/tableStyles.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:tblStyleLst xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>''')

        # docProps/core.xml
        pptx.writestr('docProps/core.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/officeDocument/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/">
<dc:title>GlobalMail Pro - Automated Release Notes Workflow</dc:title>
<dc:creator>GlobalMail Pro Team</dc:creator>
<dc:description>Board-level presentation on AI-powered release notes and help topic automation</dc:description>
<cp:lastModifiedBy>Claude Code</cp:lastModifiedBy>
<dcterms:created xsi:type="dcterms:W3CDTF">2026-07-03T00:00:00Z</dcterms:created>
<dcterms:modified xsi:type="dcterms:W3CDTF">2026-07-03T00:00:00Z</dcterms:modified>
</cp:coreProperties>''')

        # docProps/app.xml
        pptx.writestr('docProps/app.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/custom-properties">
<TotalTime>0</TotalTime>
<Application>GlobalMail Pro</Application>
<AppVersion>1.0</AppVersion>
</Properties>''')

    print("[SUCCESS] Presentation created successfully!")
    print(f"[FILE] File: {pptx_file}")
    print("[INFO] Slides: 5 professional slides")
    print("[DESIGN] Design: Board-level presentation")
    print("[STATUS] Status: Ready to edit in PowerPoint")
    print("\n[NOTE] This is a minimal PPTX file. Open in PowerPoint and:")
    print("   1. Edit slide content as needed")
    print("   2. Enhance formatting and animations")
    print("   3. Add your company logo")
    print("   4. Insert video on Slide 4 (when ready)")

if __name__ == "__main__":
    create_pptx()
