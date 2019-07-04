#!/usr/bin/env python3
'''Unit-test module.'''

from runner import run_one
from util import FALSE, TRUE, WILD_TYPE

nfiles = 100
lim = 2 * nfiles


def test_false():
    '''FALSE fails.'''
    outcome, returncode = run_one(FALSE)
    assert outcome == 'process'
    assert returncode == 1


def test_true():
    '''TRUE succeeds.'''
    outcome, returncode = run_one(TRUE)
    assert outcome == 'silent '
    assert returncode == 0


def test_WILD_TYPE():
    '''WILD_TYPE succeeds.'''
    outcome, returncode = run_one(WILD_TYPE)
    assert outcome == 'silent '
    assert returncode == 0


def test_empty():
    '''An empty file succeeds.'''
    open('empty', 'w').close()
    outcome, returncode = run_one('empty')
    assert outcome == 'silent '
    assert returncode == 0
