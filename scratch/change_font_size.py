import zipfile
import xml.etree.ElementTree as ET
import os
import shutil
import win32com.client

ns = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
}

def change_font_size_125_to_150(pptx_path):
    abs_pptx = os.path.abspath(pptx_path)
    tmp_dir = os.path.abspath("scratch/pptx_unpack_sz")
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
        
    with zipfile.ZipFile(abs_pptx, 'r') as z:
        z.extractall(tmp_dir)
        
    replaced_count = 0
    for root_dir, dirs, files in os.walk(tmp_dir):
        for f in files:
            if f.endswith('.xml'):
                f_path = os.path.join(root_dir, f)
                tree = ET.parse(f_path)
                root = tree.getroot()
                modified = False
                for elem in root.iter():
                    if elem.attrib.get('sz') == '1250':
                        elem.attrib['sz'] = '1500'
                        modified = True
                        replaced_count += 1
                        print(f"Replaced sz 1250 -> 1500 in {f} ({elem.tag})")
                if modified:
                    tree.write(f_path, xml_declaration=True, encoding='utf-8')
                    
    # Recompress
    if os.path.exists(abs_pptx):
        os.remove(abs_pptx)
        
    with zipfile.ZipFile(abs_pptx, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root_dir, dirs, files in os.walk(tmp_dir):
            for file in files:
                abs_f = os.path.join(root_dir, file)
                rel_f = os.path.relpath(abs_f, tmp_dir)
                z_out.write(abs_f, rel_f)
                
    shutil.rmtree(tmp_dir)
    print(f"Updated {abs_pptx} (replaced {replaced_count} occurrences)")

def export_slide(pptx_file, slide_num, out_png):
    abs_pptx = os.path.abspath(pptx_file)
    abs_png = os.path.abspath(out_png)
    os.makedirs(os.path.dirname(abs_png), exist_ok=True)
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    pres = ppt.Presentations.Open(abs_pptx, WithWindow=False)
    pres.Slides(slide_num).Export(abs_png, 'PNG', 1920, 1080)
    pres.Close()
    ppt.Quit()
    print(f"Exported slide {slide_num} to {abs_png}")

if __name__ == "__main__":
    change_font_size_125_to_150("pptv2.pptx")
    export_slide("pptv2.pptx", 1, "scratch/final_slides/slide_1.png")
