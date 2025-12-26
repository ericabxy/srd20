#!/usr/bin/env python
import sys

with open(sys.argv[1]) as file:
    line = file.readline()
    while line:
        print("<tr>")
        for text in line.split('|'):
            print("  <td>{text}</td>".format(text = text.strip()))
        print("</tr>")
        line = file.readline()
