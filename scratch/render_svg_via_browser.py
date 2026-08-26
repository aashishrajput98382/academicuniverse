"""
Render au.drawio.svg to high-res PNG using headless Edge browser via Selenium.
This approach properly renders <foreignObject> HTML text labels that PyMuPDF cannot handle.
"""
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

workspace = Path(__file__).resolve().parents[1]
svg_path = workspace / "docs" / "figures" / "au.drawio.svg"
output_path = workspace / "docs" / "paper" / "figure1_system_architecture_mermaid.png"

# Setup headless Edge
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--force-color-profile=srgb")
options.add_argument("--force-device-scale-factor=3")  # 3x for high DPI (effectively ~300 DPI)
options.add_argument("--window-size=1400,2600")

print("[STEP 1] Starting headless Edge browser...")
driver = webdriver.Edge(options=options)

try:
    # Navigate to SVG file
    file_url = svg_path.resolve().as_uri()
    print(f"[STEP 2] Loading SVG: {file_url}")
    driver.get(file_url)
    time.sleep(3)  # Wait for rendering

    # Get the SVG element dimensions
    svg_elem = driver.find_element("tag name", "svg")
    svg_width = svg_elem.get_attribute("width").replace("px", "")
    svg_height = svg_elem.get_attribute("height").replace("px", "")
    print(f"[INFO] SVG dimensions: {svg_width} x {svg_height}")

    # Resize window to fit SVG at 3x scale
    w = int(svg_width) + 40
    h = int(svg_height) + 40
    driver.set_window_size(w, h)
    time.sleep(2)

    # Take screenshot
    print("[STEP 3] Capturing full-page screenshot...")
    driver.save_screenshot(str(output_path.resolve()))
    print(f"[SUCCESS] Saved to {output_path}")
    print(f"[INFO] File size: {output_path.stat().st_size:,} bytes")

finally:
    driver.quit()
    print("[DONE] Browser closed.")
