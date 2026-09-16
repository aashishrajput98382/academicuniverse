import os
import win32com.client

def export_pptx(pptx_file, output_folder):
    abs_pptx = os.path.abspath(pptx_file)
    abs_out = os.path.abspath(output_folder)
    os.makedirs(abs_out, exist_ok=True)
    
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    pres = ppt.Presentations.Open(abs_pptx, WithWindow=False)
    for idx, slide in enumerate(pres.Slides, 1):
        slide.Export(os.path.join(abs_out, f'slide_{idx}.png'), 'PNG', 1920, 1080)
    pres.Close()
    ppt.Quit()
    print(f"Exported {abs_pptx} to {abs_out}")

if __name__ == "__main__":
    export_pptx("scratch/pptv2_white_cream_black_optA.pptx", "scratch/preview_optA")
    export_pptx("scratch/pptv2_white_cream_black_optB.pptx", "scratch/preview_optB")
