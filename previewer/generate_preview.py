#!/usr/bin/env python

import os
import codecs
import sys

from glob import glob

from jinja2 import Environment, FileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))


def get_theme_previews(root_path='..'):
    themes = {}
    missing = []
    for folder in os.listdir(root_path):
        if os.path.isdir(os.path.join(root_path, folder)):
            imgs = glob(os.path.join(root_path, folder, '*.png'))
            if imgs:
                themes[folder] = imgs
            else:
                missing.append(folder)

    return themes, missing


def render_theme_previews(output_path, themes, missing):
    env = Environment(loader=FileSystemLoader(HERE))
    template = env.get_template('template.html')
    output = template.render({
        'themes': themes,
        'missing': missing
    })

    full_path = os.path.join(output_path, "index.html")

    with codecs.open(full_path, 'w+', encoding='utf-8') as f:
        f.write(output)


def main():
    output_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    root_path = sys.argv[2] if len(sys.argv) > 2 else '..'

    themes, missing = get_theme_previews(root_path)
    render_theme_previews(output_path, themes, missing)


if __name__ == '__main__':
    main()
