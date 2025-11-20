import os
import re

BASE_DIR = "docs/blog"
YEARS = [str(y) for y in range(2015, 2021)]
ul_items = []

og_title_re = re.compile(r'<meta\s+property="og:title"\s+content="([^"]+)"')

for year in reversed(YEARS):
    year_dir = os.path.join(BASE_DIR, year)
    if not os.path.isdir(year_dir):
        continue
    for fname in sorted(os.listdir(year_dir), reverse=True):
        if fname.endswith('.html'):
            fpath = os.path.join(year_dir, fname)
            with open(fpath, encoding='utf-8') as f:
                html = f.read()
            m = og_title_re.search(html)
            title = m.group(1) if m else fname
            rel_path = os.path.relpath(fpath, BASE_DIR)
            ul_items.append(f'<li><a href="blog/{rel_path}">{title}</a></li>')

print('<ul>')
for item in ul_items:
    print(item)
print('</ul>')
