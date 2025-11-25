#!/usr/bin/env python
import sys

def print_table_data(line, colspan=None):
    if line:
        if colspan:
            print('    <td colspan="' + colspan + '">', end='')
        else:
            print('    <td>', end='')
        if line[0] == '"':
            print(line[1:-2] + '</td>')
        else:
            print(line[:-1] + '</td>')

def print_table_header(line, colspan=None):
    if line:
        if colspan:
            print('      <th colspan="' + colspan + '">', end='')
        else:
            print('      <th>', end='')
        if line[0] == '"':
            print(line[1:-2] + '</th>')
        else:
            print(line[:-1] + '</th>')

def parse_row(file, span):
    for x in range(span):
        line = file.readline()
        if line:
            if line[:-1] == '[colspan]':
                colspan = file.readline()[:-1]
                line = file.readline()
                print_table_data(line, colspan)
            else:
                print_table_data(line)

def parse_head_row(file, span):
    for x in range(span):
        line = file.readline()
        if line:
            if line[:-1] == '[colspan]':
                colspan = file.readline()[:-1]
                line = file.readline()
                print_table_header(line, colspan)
            else:
                print_table_header(line)

def parse_table_header(file, rowspan):
    print('  <thead>')
    row = 0
    while(row < rowspan):
        line = file.readline()
        if line[:-1] == '[span]':
            span = int(file.readline( ))
        elif line[:-1] == '[row]':
            print('    <tr>')
            parse_head_row(file, span)
            print('    </tr>')  
            row = row + 1
    print('  </thead>')

with open(sys.argv[1]) as file:
    global span
    span = 10
    print('<table>')
    while(True):
        line = file.readline()
        if not line:
            break
        if line[:-1] == '[caption]':
            caption = file.readline()
            print('  <caption>' + caption[1:-2] + '</caption>')
        elif line[:-1] == '[span]':
            span = int(file.readline( ))
        elif line[:-1] == '[thead]':
            rowspan = int(file.readline( ))
            parse_table_header(file, rowspan)
        elif line[:-1] == '[row]':
            print('  <tr>')
            parse_row(file, span)
            print('  </tr>')
    print('</table>')
