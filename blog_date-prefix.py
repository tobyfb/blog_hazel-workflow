#!/usr/bin/env python3

import sys
import re

blog_file = sys.argv[1]

with open(blog_file, 'r', encoding="utf-8") as f: 
	find_date = f.readlines()

prefix = ''

for line in find_date:
	if line.startswith('date'):
		match = re.search(r'\d{4}-\d{2}-\d{2}', line)
		date = match.group()
		year = date[0:4]
		month = date[5:7]
		prefix = '![](/images/{}/{}/'.format(year, month)

with open(blog_file, 'r', encoding="utf-8") as f:
	full_content = f.read()
			
updated_content = full_content.replace('![](', prefix)

with open(blog_file, 'w', encoding='utf8') as f:
	f.write(updated_content)