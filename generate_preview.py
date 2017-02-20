#!/usr/bin/env python

import os
from glob import glob
from subprocess import call

# Cobble together markdown file
output = '''
<style>
body{
text-align:center
}
img{
padding: 20px 20px 20px 20px
}
</style>

# Theme Screenshots
'''

# Add a vertical line, a heading, and an image for each theme
for folder in os.listdir('.'):
	if os.path.isdir(os.path.join('.', folder)):
		output += "<hr>\n\n## %s\n\n" % folder
		imgs = glob(os.path.join('.', folder, '*.png'))
		for img in imgs:
			output += "\n\n![](%s)\n\n" % img
		if len(imgs) == 0:
			output += "\n\n>[NO PREVIEW]\n\n"
# Save to file
with open('preview.md', 'w') as f:
    f.write(output)
# Use pandoc to generate markdown from file.
call(['pandoc', 'preview.md', '-o', 'preview.html'])

