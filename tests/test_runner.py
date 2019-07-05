#!/usr/bin/env python3
'''Unit-test module.'''

import os
from population import Population
from runner import run_all, run_one
from population import Population
from util import FALSE, TRUE, WILD_TYPE, create_dir

nfiles = 100
lim = 2 * nfiles


def test_false():
    '''FALSE fails.'''
    _, outcome, returncode = run_one(FALSE)
    assert outcome == 'process'
    assert returncode == 1


def test_true():
    '''TRUE succeeds.'''
    _, outcome, returncode = run_one(TRUE)
    assert outcome == 'silent '
    assert returncode == 0


def test_WILD_TYPE():
    '''WILD_TYPE succeeds.'''
    _, outcome, returncode = run_one(WILD_TYPE)
    assert outcome == 'silent '
    assert returncode == 0


def test_empty():
    '''An empty file succeeds.'''
    open('empty', 'w').close()
    _, outcome, returncode = run_one('empty')
    assert outcome == 'silent '
    assert returncode == 0


def test_run_all():
    '''Generate population, check it's the right size.'''
    nloci = 400
    create_dir('population')
    os.chdir('population')
    p = Population(TRUE, 'point', nloci)
    p.gen()
    assert len(run_all()) == p.size
