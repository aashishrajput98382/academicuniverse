import zipfile
import xml.etree.ElementTree as ET
import os
import shutil

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

# Variant C: Warm Cream Paper Canvas (#FAF6F0) + Crisp White Cards (#FFFFFF) + Deep Black Accents (#111111)
C_CANVAS_CREAM = "FAF6F0"      # Warm cream paper background
C_CARD_WHITE   = "FFFFFF"      # Crisp white cards
C_CARD_BORDER  = "E5DDD0"      # Subtle warm border
C_DIVIDER      = "DDD4C6"      # Divider line
C_JET_BLACK    = "111111"      # Primary headings, titles, active badges, bold text
C_CHARCOAL     = "242220"      # High-contrast readable body copy
C_MUTED        = "635D56"      # Secondary descriptions, sub-bullets, footer text
C_HERO_BG      = "FFFFFF"      # Slide 1 hero card
C_HERO_BORDER  = "E2D8CA"      # Slide 1 hero border
C_INNER_CARD   = "F8F4ED"      # Slide 1 inner cards (cream)

# Featured Card (Slides 4, 5, 6, 10)
C_FEATURED_BG     = "141414"   # Deep Jet Black card
C_FEATURED_BORDER = "333333"
C_FEATURED_TITLE  = "F7F3EB"
C_FEATURED_LABEL  = "D8CEBD"
C_FEATURED_VALUE  = "FFFFFF"
C_FEATURED_MUTED  = "E2DCD2"

def generate_variant_c(src_pptx, dst_pptx):
    tmp_dir = os.path.abspath("scratch/pptx_unpack_c")
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
                    if sf is not None: sf.attrib['val'] = C_CANVAS_CREAM
                elif name == "Rectangle 2": # Top accent bar
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_JET_BLACK
                elif name == "Rounded Rectangle 3": # Big hero container
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_HERO_BG
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_HERO_BORDER
                elif name == "Rounded Rectangle 4": # Badge
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_JET_BLACK
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_JET_BLACK
                    for clr in sp.findall('.//p:txBody//a:srgbClr', ns):
                        clr.attrib['val'] = "F7F3EB"
                elif name == "TextBox 5": # Main Titles
                    for p_i, p in enumerate(txBody.findall('a:p', ns)):
                        target_col = C_JET_BLACK if p_i == 0 else (C_CHARCOAL if p_i == 1 else C_MUTED)
                        for clr in p.findall('.//a:srgbClr', ns):
                            clr.attrib['val'] = target_col
                elif name in ["Rounded Rectangle 6", "Rounded Rectangle 7", "Rounded Rectangle 8"]:
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_INNER_CARD
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
                    if sf is not None: sf.attrib['val'] = C_CANVAS_CREAM
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
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_FEATURED_BG
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_FEATURED_BORDER
                
                elif name == "TextBox 10" and slide_idx in [4, 5, 6, 10]:
                    for p_i, p in enumerate(txBody.findall('a:p', ns)):
                        p_txt = "".join([t.text for t in p.findall('.//a:t', ns) if t.text]).strip()
                        if p_i == 0 or "VERIFIED" in p_txt or "HOW OVERLAP" in p_txt or "TESTED" in p_txt or "Roadmap" in p_txt or "THANK YOU" in p_txt:
                            target_col = C_FEATURED_TITLE
                        elif p_txt.isupper() or p_txt.startswith("Step ") or "STUDENT SYSTEM" in p_txt or "LIVE SYNCED" in p_txt or "CLASSROOM" in p_txt or "FACULTY" in p_txt or "SYNC PROTOCOL" in p_txt or "GOOGLE SHEETS" in p_txt or "Student Prompt:" in p_txt or "Academic Universe AI:" in p_txt:
                            target_col = C_FEATURED_LABEL
                        else:
                            target_col = C_FEATURED_VALUE
                            
                        for r in p.findall('.//a:r', ns):
                            r_sf = r.find('.//a:solidFill/a:srgbClr', ns)
                            if r_sf is not None:
                                if r_sf.attrib.get('val') == '94A3B8':
                                    r_sf.attrib['val'] = C_FEATURED_MUTED
                                else:
                                    r_sf.attrib['val'] = target_col
                        def_sf = p.find('.//a:defRPr/a:solidFill/a:srgbClr', ns)
                        if def_sf is not None:
                            def_sf.attrib['val'] = target_col

                # All other cards (standard content cards)
                elif name.startswith("Rounded Rectangle"):
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_CARD_WHITE
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_CARD_BORDER

                # TextBoxes inside standard cards
                elif name.startswith("TextBox"):
                    for p in txBody.findall('a:p', ns):
                        def_sf = p.find('.//a:defRPr/a:solidFill/a:srgbClr', ns)
                        if def_sf is not None:
                            old_c = def_sf.attrib.get('val')
                            if old_c in ['38BDF8', '10B981']:
                                def_sf.attrib['val'] = C_JET_BLACK
                            elif old_c == 'F8FAFC':
                                def_sf.attrib['val'] = C_CHARCOAL
                            elif old_c == '94A3B8':
                                def_sf.attrib['val'] = C_MUTED
                        
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
        
    if os.path.exists(dst_pptx):
        os.remove(dst_pptx)
        
    with zipfile.ZipFile(dst_pptx, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root_dir, dirs, files in os.walk(tmp_dir):
            for file in files:
                abs_f = os.path.join(root_dir, file)
                rel_f = os.path.relpath(abs_f, tmp_dir)
                z_out.write(abs_f, rel_f)
                
    print(f"Generated {dst_pptx}")

if __name__ == "__main__":
    generate_variant_c("pptv2.pptx", "scratch/pptv2_white_cream_black_optC.pptx")
