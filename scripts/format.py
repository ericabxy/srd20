#!/usr/bin/env python
import os
import sys

import markdown

for path in sys.argv[1:]:
    with open(path) as file:
        content = markdown.markdown(file.read( ))
    with open('templates/main') as file:
        template = file.read()
    title = os.path.basename(path).replace('_', ' ')
    name = os.path.basename(path).lower().replace('_', '-')
    name = name.replace(':', '')
    html = template.format(title=title, content=content)
    with open(os.path.join('docs', name), 'w') as file:
        file.write(html)
#destdir = sys.argv[2]
#path = os.path.join(destdir, name)
#print(template.format(title='Jerk', content=content))
#with open(path, 'w') as file:
#    file.write(html)
