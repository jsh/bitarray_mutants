#!/usr/bin/env python3
'''Unit-test module.'''

import os

from screen import Screen
from util import WILD_TYPE, create_dir


def test_generate_screen():
    '''Generate screen, check it's the right size.'''
    nloci = 400
    create_dir('screen')
    os.chdir('screen')
    s = Screen(WILD_TYPE, 'point', nloci)
    s.gen()
    files = [file for file in os.walk('.') if file[2]]
    assert len(files) == nloci
