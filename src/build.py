# Bouwt index.html uit src/template.html met het LessonUp-logo erin.
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
logo = (root / 'src' / 'logo.svg').read_text(encoding='utf-8')
logo = re.sub(r'\sclass="[^"]*"', '', logo).replace('fill="none"', 'fill="none" aria-hidden="true"', 1)
html = (root / 'src' / 'template.html').read_text(encoding='utf-8').replace('__LOGO__', logo)
(root / 'index.html').write_text(html, encoding='utf-8')
print('index.html', len(html))
