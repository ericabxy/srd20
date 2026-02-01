#!/usr/bin/env python
import os
import sys

from bs4 import BeautifulSoup

masterlist = {}

def getentries(path):
  basename = '/' + os.path.basename(path)
  docname, _ = os.path.splitext(basename)
  with open(path) as file:
    html = file.read()
  soup = BeautifulSoup(html, 'html.parser')
  for tag in soup.find_all(['h2', 'h3']):
    if tag.has_attr('id'):
      name = tag.string.lower()
      url = docname + '#' + tag['id']
      masterlist[name] = url

path = sys.argv[1]
for path in sys.argv[1:]:
  getentries(path)
sorted_dict = dict(sorted(masterlist.items()))
for item in sorted_dict:
  print(item + ': ' + masterlist[item])
