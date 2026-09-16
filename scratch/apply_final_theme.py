import zipfile
import xml.etree.ElementTree as ET
import os
import shutil
import win32com.client

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

# Design Tokens for White, Cream, and Black Theme
C_CANVAS_WHITE = "FFFFFF"      # Slide Background (Crisp Pure White)
C_CARD_CREAM   = "F7F3EB"      # Warm luxury cream for content cards
C_CARD_BORDER  = "DFD7CB"      # Subtle warm cream border
C_DIVIDER      = "E5DDD0"      # Footer divider line
C_JET_BLACK    = "111111"      # Primary headings, titles, active badges, bold text
C_CHARCOAL     = "242220"      # High-contrast readable body copy
C_MUTED        = "635D56"      # Secondary descriptions, sub-bullets, footer text
C_NESTED_WHITE = "FFFFFF"      # Inner nested cards (Slide 1)
C_HERO_BORDER  = "DFD7CB"      # Soft elegant border for slide 1 hero card

# Featured / Proof Cards (Slides 4, 5, 6, 10 right card)
C_FEATURED_BG     = "141414"   # Deep Jet Black card background
C_FEATURED_BORDER = "333333"   # Subtle border
C_FEATURED_TITLE  = "F7F3EB"   # Cream title
C_FEATURED_LABEL  = "D8CEBD"   # Warm cream label
C_FEATURED_VALUE  = "FFFFFF"   # Crisp White value
C_FEATURED_MUTED  = "E0DAD0"   # Bright warm cream for descriptions in black card

def update_theme_xml(theme_path):
    tree = ET.parse(theme_path)
    root = tree.getroot()
    clrScheme = root.find('.//a:clrScheme', ns)
    if clrScheme is not None:
        clrScheme.attrib['name'] = "White Cream Black"
        mapping = {
            'dk1': ('sysClr', {'val': 'windowText', 'lastClr': '111111'}),
            'lt1': ('sysClr', {'val': 'window', 'lastClr': 'FFFFFF'}),
            'dk2': ('srgbClr', {'val': '242220'}),
            'lt2': ('srgbClr', {'val': 'F7F3EB'}),
            'accent1': ('srgbClr', {'val': '111111'}),
            'accent2': ('srgbClr', {'val': 'D8CEBD'}),
            'accent3': ('srgbClr', {'val': '5A5550'}),
            'accent4': ('srgbClr', {'val': 'EDE4D4'}),
            'accent5': ('srgbClr', {'val': '2D2A26'}),
            'accent6': ('srgbClr', {'val': 'FAF6F0'}),
        }
        for elem in clrScheme:
            tag = elem.tag.split('}')[-1]
            if tag in mapping:
                elem.clear()
                sub_tag, attribs = mapping[tag]
                sub_elem = ET.SubElement(elem, f"{{{ns['a']}}}{sub_tag}", attribs)
    tree.write(theme_path, xml_declaration=True, encoding='utf-8')

def build_presentation(src_pptx, dst_pptx):
    tmp_dir = os.path.abspath("scratch/pptx_unpack_final")
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    
    with zipfile.ZipFile(src_pptx, 'r') as z:
        z.extractall(tmp_dir)
        
    # 1. Update theme
    theme_file = os.path.join(tmp_dir, "ppt/theme/theme1.xml")
    if os.path.exists(theme_file):
        update_theme_xml(theme_file)
        
    # 2. Update slides
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
            
            # Slide 1 (Title Slide)
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
                    for clr in sp.findall('.//p:txBody//a:srgbClr', ns):
                        clr.attrib['val'] = C_CARD_CREAM
                elif name == "TextBox 5": # Main Titles
                    for p_i, p in enumerate(txBody.findall('a:p', ns)):
                        target_col = C_JET_BLACK if p_i == 0 else (C_CHARCOAL if p_i == 1 else C_MUTED)
                        for clr in p.findall('.//a:srgbClr', ns):
                            clr.attrib['val'] = target_col
                elif name in ["Rounded Rectangle 6", "Rounded Rectangle 7", "Rounded Rectangle 8"]:
                    sf = spPr.find('.//a:solidFill/a:srgbClr', ns)
                    if sf is not None: sf.attrib['val'] = C_NESTED_WHITE
                    ln_sf = spPr.find('.//a:ln/a:solidFill/a:srgbClr', ns)
                    if ln_sf is not None: ln_sf.attrib['val'] = C_CARD_BORDER
                    for p_i, p in enumerate(txBody.findall('a:p', ns)):
                        target_col = C_JET_BLACK if p_i == 0 else C_CHARCOAL
                        for clr in p.findall('.//a:srgbClr', ns):
                            clr.attrib['val'] = target_col
            
            # Slides 2-10 (Content Slides)
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
                
                # Featured / Highlight Right Cards on slides 4, 5, 6, 10
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
                    if sf is not None: sf.attrib['val'] = C_CARD_CREAM
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
                
    print(f"Successfully generated {dst_pptx}")

def export_all_slides(pptx_file, output_folder):
    abs_pptx = os.path.abspath(pptx_file)
    abs_out = os.path.abspath(output_folder)
    os.makedirs(abs_out, exist_ok=True)
    
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    pres = ppt.Presentations.Open(abs_pptx, WithWindow=False)
    for idx, slide in enumerate(pres.Slides, 1):
        slide.Export(os.path.join(abs_out, f'slide_{idx}.png'), 'PNG', 1920, 1080)
    pres.Close()
    ppt.Quit()
    print(f"Exported all {idx} slides to {abs_out}")

if __name__ == "__main__":
    # Update pptv2.pptx directly
    build_presentation("scratch/pptv2_backup.pptx", "pptv2.pptx")
    export_all_slides("pptv2.pptx", "scratch/final_slides")
