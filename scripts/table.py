#!/usr/bin/env python
import sys

columns = 4
widths = [0 for x in range(columns)]
with open(sys.argv[1]) as file:
    lines = []
    cells = []
    n = 0
    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip()
        if len(line) > widths[n]:
            widths[n] = len(line)
        cells.append(line)
        n = n + 1
        if n > columns - 1:
            n = 0
line = ''
n = 0
widths[columns - 1] = 0
for text in cells:
    line = line + '| ' + text.ljust(widths[n] + 1, ' ')
    n = n + 1
    if n > columns - 1:
        print(line)
        line = ''
        n = 0
