"""Export the original SVG workflow to a PNG for the assignment report."""
from pathlib import Path
import sys
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'.tools/vendor'))
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(channel='msedge',headless=True)
    page=b.new_page(viewport={'width':1200,'height':1660},device_scale_factor=1)
    svg=(R/'assets/slides-workflow.svg').read_text(encoding='utf-8')
    page.set_content('<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">'+svg+'</body></html>')
    page.screenshot(path=str(R/'assets/slides-workflow.png'),full_page=True)
    b.close()
print('Exported vertical workflow PNG.')
