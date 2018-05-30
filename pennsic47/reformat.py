#!/usr/bin/env python

from __future__ import print_function

import sys

contents = ''
with open(sys.argv[1], 'r') as f:
    contents = f.read()

# there is exactly one table in this file

assert contents.count('<table ') == 1

contents = contents[contents.find('<table '):]
contents = contents[contents.find('<tbody>')+7:]
contents = contents[:contents.find('</table>')+8:]
contents = contents.replace('\n', ' ').replace('</tr>', '</tr>\n')

with open('classes-all', 'w') as f:
    print(contents, file=f)

