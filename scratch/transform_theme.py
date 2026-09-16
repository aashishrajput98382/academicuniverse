import zipfile
import xml.etree.ElementTree as ET
import os
import shutil

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

# Design Tokens for White, Cream, and Black Theme
# Style Option A: Editorial Contrast (White canvas, warm cream cards, deep black accents & sharp black typography)
# Colors:
C_CANVAS_WHITE = "FFFFFF"      # Slide Background
C_CARD_CREAM   = "F7F3EB"      # Warm ivory/linen cream for content cards
C_CARD_BORDER  = "DFD7CB"      # Subtle warm cream border
C_DIVIDER      = "E5DDD0"      # Divider line
C_JET_BLACK    = "111111"      # Primary headings, titles, active badges, bold text
C_CHARCOAL     = "242220"      # High-contrast readable body copy
C_MUTED        = "635D56"      # Secondary descriptions, sub-bullets, footer text
C_NESTED_WHITE = "FFFFFF"      # Inner nested cards (Slide 1)
C_HERO_BORDER  = "222222"      # Border for slide 1 hero card

# Featured / Proof Cards (Slides 4, 5, 6, 10 right card):
# A deep, luxurious jet black anchor card with cream typography brings immense depth and sophistication
C_FEATURED_BG     = "141414"   # Deep Jet Black card background
C_FEATURED_BORDER = "333333"   # Crisp subtle border
C_FEATURED_TITLE  = "F7F3EB"   # Cream title
C_FEATURED_LABEL  = "D8CEBD"   # Warm cream label
C_FEATURED_VALUE  = "FFFFFF"   # White value
C_FEATURED_MUTED  = "A8A29A"   # Secondary muted in black card

def transform_presentation(src_pptx, dst_pptx, featured_style="black"):
    # featured_style: "black" (inverted dark card) or "cream" (richer warm cream card)
    
    # We will unpack to a temp dir, modify slide xmls, and repack
    tmp_dir = os.path.abspath("scratch/pptx_unpack")
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    
    with zipfile.ZipFile(src_pptx, 'r') as z:
        z.extractall(tmp_dir)
        
    for slide_idx in range(1, 11):
        slide_path = os.path.join(tmp_dir, f"ppt/slides/slide{slide_idx}.xml")
        if not os.path.exists(slide_path):
            continue
            
        tree = ET.parse(slide_path)
        root = tree.getroot()
        
        for sp in root.findall('.//p:sp', ns):
            name = sp.find('.//p:cNvPr', ns).attrib.get('name', '')
            spPr = sp.find('p:spPr', ns)
            txBody = sp.find('p:txBody', ns)
            
            # 1. Slide 1 (Title Slide)
            if slide_idx == 1:
                if name == "Rectangle 1": # Background
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_CANVAS_WHITE
                elif name == "Rectangle 2": # Top accent bar
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_JET_BLACK
                elif name == "Rounded Rectangle 3": # Big hero container
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_CARD_CREAM
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_HERO_BORDER
                elif name == "Rounded Rectangle 4": # Badge "LIVE PRODUCTION PLATFORM • 2026"
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_JET_BLACK
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_JET_BLACK
                    # text inside badge
                    for clr in sp.findall('.//p:txBody//a:srgbClr', ns):
                        clr.attrib['val'] = C_CARD_CREAM
                elif name == "TextBox 5": # Main Titles
                    # Paragraph 0: ACADEMIC UNIVERSE (AU)
                    # Paragraph 1: Next-Generation Intelligent Campus...
                    # Paragraph 2: A unified, production-deployed...
                    for p_i, p in enumerate(txBody.findall('a:p', ns)):
                        target_col = C_JET_BLACK if p_i == 0 else (C_CHARCOAL if p_i == 1 else C_MUTED)
                        for clr in p.findall('.//a:srgbClr', ns):
                            clr.attrib['val'] = target_col
                elif name in ["Rounded Rectangle 6", "Rounded Rectangle 7", "Rounded Rectangle 8"]:
                    # Presenter, Tech Stack, Deployment Status cards
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_NESTED_WHITE
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_CARD_BORDER
                    for p_i, p in enumerate(txBody.findall('a:p', ns)):
                        target_col = C_JET_BLACK if p_i == 0 else C_CHARCOAL
                        for clr in p.findall('.//a:srgbClr', ns):
                            clr.attrib['val'] = target_col
            
            # 2. Slides 2-10 (Content Slides)
            else:
                if name == "Rectangle 1": # Background
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_CANVAS_WHITE
                elif name == "TextBox 2": # Eyebrow Header
                    for clr in sp.findall('.//p:txBody//a:srgbClr', ns):
                        clr.attrib['val'] = C_JET_BLACK
                elif name == "TextBox 3": # Main Slide Title
                    for clr in sp.findall('.//p:txBody//a:srgbClr', ns):
                        clr.attrib['val'] = C_JET_BLACK
                elif name == "Rectangle 4": # Footer line
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_DIVIDER
                elif name == "TextBox 5": # Footer AU text
                    for clr in sp.findall('.//p:txBody//a:srgbClr', ns):
                        clr.attrib['val'] = C_MUTED
                elif name == "TextBox 6": # Footer slide number
                    for clr in sp.findall('.//p:txBody//a:srgbClr', ns):
                        clr.attrib['val'] = C_JET_BLACK
                
                # Check for Featured / Highlight Right Cards on slides 4, 5, 6, 10
                elif name == "Rounded Rectangle 9" and slide_idx in [4, 5, 6, 10]:
                    if featured_style == "black":
                        sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                        if sf is not None: sf.attrib['val'] = C_FEATURED_BG
                        ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                        if ln_sf is not None: ln_sf.attrib['val'] = C_FEATURED_BORDER
                    else: # cream style
                        sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                        if sf is not None: sf.attrib['val'] = "EDE4D4"
                        ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                        if ln_sf is not None: ln_sf.attrib['val'] = C_JET_BLACK
                
                elif name == "TextBox 10" and slide_idx in [4, 5, 6, 10]:
                    # Text inside right card
                    if featured_style == "black":
                        for p_i, p in enumerate(txBody.findall('a:p', ns)):
                            p_txt = "".join([t.text for t in p.findall('.//a:t', ns) if t.text]).strip()
                            # If header
                            if p_i == 0 or "VERIFIED" in p_txt or "HOW OVERLAP" in p_txt or "TESTED" in p_txt or "Roadmap" in p_txt or "THANK YOU" in p_txt:
                                target_col = C_FEATURED_TITLE
                            elif p_txt.isupper() or p_txt.startswith("Step ") or "STUDENT SYSTEM" in p_txt or "LIVE SYNCED" in p_txt or "CLASSROOM" in p_txt or "FACULTY" in p_txt or "SYNC PROTOCOL" in p_txt or "GOOGLE SHEETS" in p_txt or "Student Prompt:" in p_txt or "Academic Universe AI:" in p_txt:
                                target_col = C_FEATURED_LABEL
                            else:
                                target_col = C_FEATURED_VALUE
                                
                            # If runs have colors
                            for r in p.findall('.//a:r', ns):
                                r_sf = r.find('.//a:solidFill/a:srgbClr', ns)
                                if r_sf is not None:
                                    # check if it was muted text (like 94A3B8)
                                    if r_sf.attrib.get('val') == '94A3B8':
                                        r_sf.attrib['val'] = C_FEATURED_MUTED
                                    else:
                                        r_sf.attrib['val'] = target_col
                            # defRPr
                            def_sf = p.find('.//a:defRPr/a:solidFill/a:srgbClr', ns)
                            if def_sf is not None:
                                def_sf.attrib['val'] = target_col
                    else: # cream style
                        for p_i, p in enumerate(txBody.findall('a:p', ns)):
                            p_txt = "".join([t.text for t in p.findall('.//a:t', ns) if t.text]).strip()
                            if p_i == 0:
                                target_col = C_JET_BLACK
                            elif p_txt.isupper() or p_txt.startswith("Step "):
                                target_col = C_JET_BLACK
                            else:
                                target_col = C_CHARCOAL
                            for clr in p.findall('.//a:srgbClr', ns):
                                clr.attrib['val'] = target_col

                # All other cards (standard content cards)
                elif name.startswith("Rounded Rectangle"):
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_CARD_CREAM
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_CARD_BORDER

                # TextBoxes inside standard cards
                elif name.startswith("TextBox"):
                    for p in txBody.findall('a:p', ns):
                        p_txt = "".join([t.text for t in p.findall('.//a:t', ns) if t.text]).strip()
                        
                        # defRPr color
                        def_sf = p.find('.//a:defRPr/a:solidFill/a:srgbClr', ns)
                        if def_sf is not None:
                            old_c = def_sf.attrib.get('val')
                            if old_c in ['38BDF8', '10B981']: # former blue/green headings
                                def_sf.attrib['val'] = C_JET_BLACK
                            elif old_c == 'F8FAFC': # former white body
                                def_sf.attrib['val'] = C_CHARCOAL
                            elif old_c == '94A3B8': # former muted gray
                                def_sf.attrib['val'] = C_MUTED
                        
                        # runs colors
                        for r in p.findall('.//a:r', ns):
                            r_sf = r.find('.//a:solidFill/a:srgbClr', ns)
                            if r_sf is not None:
                                old_c = r_sf.attrib.get('val')
                                if old_c in ['38BDF8', '10B981']:
                                    r_sf.attrib['val'] = C_JET_BLACK
                                elif old_c == 'F8FAFC':
                                    r_sf.attrib['val'] = C_CHARCOAL
                                elif old_c == '94A3B8':
                                    r_sf.attrib['val'] = C_MUTED

        tree.write(slide_path, xml_declaration=True, encoding='utf-8')
        
    # Recompress to dst_pptx
    if os.path.exists(dst_pptx):
        os.remove(dst_pptx)
        
    with zipfile.ZipFile(dst_pptx, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root_dir, dirs, files in os.walk(tmp_dir):
            for file in files:
                abs_f = os.path.join(root_dir, file)
                rel_f = os.path.relpath(abs_f, tmp_dir)
                z_out.write(abs_f, rel_f)
                
    print(f"Generated {dst_pptx} with style {featured_style}")

if __name__ == "__main__":
    transform_presentation("pptv2.pptx", "scratch/pptv2_white_cream_black_optA.pptx", "black")
    transform_presentation("pptv2.pptx", "scratch/pptv2_white_cream_black_optB.pptx", "cream")
