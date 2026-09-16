
from PIL import Image
im = Image.open(r"C:/github/academicuniverse/scratch/standard_flowchart_raw.png")
im.save(r"C:/github/academicuniverse/Academic_Universe_Standard_Flowchart_4K_500DPI.png", dpi=(500, 500), compress_level=1)
print(f"Final Standard 4K 500DPI PNG generated successfully: {im.size} at 500 DPI")
