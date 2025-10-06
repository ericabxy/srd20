#!/usr/bin/env python
import os
import sys

import markdown

path = sys.argv[1]
name = os.path.basename(path).lower().replace('_', '-')
print((name,))
