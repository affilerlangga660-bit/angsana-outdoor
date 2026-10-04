import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / 'index.html').read_text(encoding='utf-8')

# Ignore commented-out markup so the test checks the actual rendered HTML structure.
visible_html = re.sub(r'<!--.*?-->', '', HTML, flags=re.DOTALL)
open_labels = len(re.findall(r'<label\b', visible_html, flags=re.IGNORECASE))
close_labels = len(re.findall(r'</label\s*>', visible_html, flags=re.IGNORECASE))

if open_labels != close_labels:
    raise AssertionError(
        f'Label nesting is unbalanced: {open_labels} opening labels vs {close_labels} closing labels.'
    )

print(f'HTML markup check passed: {open_labels} valid label pairs.')
