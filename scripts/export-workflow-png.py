"""Export the original SVG workflow to a PNG for the assignment report."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'.tools/vendor'))
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(channel='msedge',headless=True)
    svg=(R/'assets/slides-workflow.svg').read_text(encoding='utf-8')
    root=ET.fromstring(svg)
    page=b.new_page(viewport={'width':int(root.attrib['width']),'height':int(root.attrib['height'])},device_scale_factor=2)
    page.set_content('<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">'+svg+'</body></html>')
    page.evaluate('document.fonts.ready')
    page.locator('svg').screenshot(path=str(R/'assets/slides-workflow.png'))
    b.close()
print('Exported vertical workflow PNG.')
