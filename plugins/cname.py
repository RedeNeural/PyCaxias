# -*- coding: utf-8 -*-
'''
Cname
-------

generate cname in output directory.
'''

from __future__ import unicode_literals

import re
import collections
import os.path

from pelican import signals, contents

class CnameGenerator(object):

    def __init__(self, context, settings, path, theme, output_path, *null):
        self.output_path = output_path
        self.siteurl = settings.get('SITEURL')

    def generate_output(self, writer):
        path = os.path.join(self.output_path, 'CNAME')
        with open(path, 'w', encoding='utf-8') as fd:
            fd.write('pycaxias.org')

def get_generators(generators):
    return CnameGenerator


def register():
    signals.get_generators.connect(get_generators)
