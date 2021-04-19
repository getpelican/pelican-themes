import os
import sys
from pelican import signals

THEME_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(THEME_DIR)
import jinja_filters


def pelican_init(pelicanobj):
    pelicanobj.settings['JINJA_FILTERS'].update(pagination=jinja_filters.pagination)

def register():
    signals.initialized.connect(pelican_init)
