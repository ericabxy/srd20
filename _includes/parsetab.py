#!/usr/bin/env python
import sys

with open(sys.argv[1]) as file:
    line = file.readline()
    print("<table>")
    while line:
        print("  <tr>")
        for text in line.split('\t'):
            print("    <td>{text}</td>".format(text = text.strip()))
        print("  </tr>")
        line = file.readline()
    print("</table>")
