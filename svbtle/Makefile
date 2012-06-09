# Install using:
#
#   pip install pygments
#
# built in styles: ['monokai', 'manni', 'rrt', 'perldoc', 'borland', 'colorful',
# 'default', 'murphy', 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs',
# 'vim', 'pastie', 'friendly', 'native']

STYLE = default

less:
	lessc -x static/css/style.less > static/css/style.css

pygments:
	pygmentize -S ${STYLE} -f html > ./static/css/pygments.css
