"""
Render au.drawio.svg to high-res PNG using headless Edge in LIGHT MODE.
Forces light color scheme so the diagram has a white background for print/publication.
"""
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.options import Options

workspace = Path(__file__).resolve().parents[1]
svg_path = workspace / "docs" / "figures" / "au.drawio.svg"
output_path = workspace / "docs" / "paper" / "figure1_system_architecture_mermaid.png"
preview_path = workspace / "scratch" / "fig1_lightmode_preview.png"

# Create an HTML wrapper that forces light mode and white background
html_wrapper = f"""<!DOCTYPE html>
<html style="color-scheme: light;">
<head>
<meta charset="UTF-8">
<style>
  html, body {{
    margin: 0;
    padding: 20px;
    background: white !important;
    color-scheme: light !important;
  }}
  svg {{
    background: white !important;
    display: block;
    margin: 0 auto;
  }}
</style>
</head>
<body>
{svg_path.read_text(encoding='utf-8')}
</body>
</html>"""

html_path = workspace / "scratch" / "fig1_light_wrapper.html"
html_path.write_text(html_wrapper, encoding='utf-8')
print(f"[STEP 1] Created light-mode HTML wrapper ({html_path.stat().st_size:,} bytes)")

# Setup headless Edge with LIGHT color scheme
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--force-color-profile=srgb")
options.add_argument("--force-device-scale-factor=3")  # 3x for ~300 DPI
options.add_argument("--window-size=1400,2600")

# Force light mode preferences
prefs = {"browser.preferred_color_scheme": 0}  # 0 = light
options.add_experimental_option("prefs", prefs)

print("[STEP 2] Starting headless Edge browser (light mode)...")
driver = webdriver.Edge(options=options)

try:
    # Force light mode via CDP
    driver.execute_cdp_cmd("Emulation.setEmulatedMedia", {
        "features": [{"name": "prefers-color-scheme", "value": "light"}]
    })

    file_url = html_path.resolve().as_uri()
    print(f"[STEP 3] Loading HTML wrapper: {file_url}")
    driver.get(file_url)
    time.sleep(3)

    # Get SVG dimensions and resize window
    svg_elem = driver.find_element("tag name", "svg")
    svg_width = int(svg_elem.get_attribute("width").replace("px", ""))
    svg_height = int(svg_elem.get_attribute("height").replace("px", ""))
    print(f"[INFO] SVG dimensions: {svg_width} x {svg_height}")

    driver.set_window_size(svg_width + 60, svg_height + 60)
    time.sleep(2)

    # Take screenshot
    print("[STEP 4] Capturing full-page screenshot (light mode)...")
    driver.save_screenshot(str(output_path.resolve()))
    print(f"[SUCCESS] Saved to {output_path.name} ({output_path.stat().st_size:,} bytes)")

    # Also save preview
    driver.save_screenshot(str(preview_path.resolve()))

finally:
    driver.quit()
    print("[DONE] Browser closed.")
