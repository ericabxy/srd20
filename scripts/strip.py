#!/usr/bin/env python
import re
import sys

def func(matchobj):
    return matchobj.group()[1:-13]

with open(sys.argv[1]) as file:
    text = file.read()
text2 = re.sub(
    r'\[[\s.]*\]\{\.underline\}',
    func,
    text
)
print(text2)
