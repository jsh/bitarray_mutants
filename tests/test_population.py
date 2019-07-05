#!/usr/bin/env python3
'''Unit-test module.'''

import os

from population import Population
from util import WILD_TYPE, create_dir


def test_generate_population():
    '''Generate population, check it's the right size.'''
    nloci = 400
    create_dir('population')
    os.chdir('population')
    p = Population(WILD_TYPE, 'point', nloci)
    p.gen()
    files = [file for file in os.walk('.') if file[2]]
    assert len(files) == nloci
    assert len(p.enum()) == nloci
    assert p.size == nloci
