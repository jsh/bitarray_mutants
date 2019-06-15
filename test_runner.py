#!/usr/bin/env python

import os

import mutate
from make_mutants import make_mutants
from runner import run_dir, run_one
from util import get_test_dir, wild_type

nfiles = 100
lim = 2 * nfiles


def test_true():
    outcome, returncode = run_one('true')
    assert outcome == 'silent '
    assert returncode == 0


def test_false():
    outcome, returncode = run_one('false')
    assert outcome == 'process'
    assert returncode == 1


def test_empty():
    open('empty', 'w').close()
    outcome, returncode = run_one('empty')
    assert outcome == 'silent '
    assert returncode == 0


def test_run_dir():
    results = 'results'
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random',
                 wt=wild_type, mutagen=mutate.point)
    os.chdir('..')
    run_dir(test_dir, results)
    assert os.path.isfile(results)
    with open(results, 'r') as f:
        assert len(list(f)) == nfiles
    os.remove(results)
