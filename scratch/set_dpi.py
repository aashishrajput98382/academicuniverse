
from PIL import Image
im = Image.open(r"C:/github/academicuniverse/scratch/flowchart_raw_4k.png")
im.save(r"C:/github/academicuniverse/Academic_Universe_System_Flowchart_4K_500DPI.png", dpi=(500, 500), compress_level=1)
print(f"Final 4K 500DPI PNG generated successfully: {im.size} at 500 DPI")
