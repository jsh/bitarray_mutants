#!/usr/bin/env python

import os

import mutate
from make_mutants import make_mutants
from runner import run_dir
from util import get_test_dir, lim, nfiles, wild_type

lim = os.path.getsize(wild_type)
nfiles = 400


def run_empty():
    results = 'results.empty'
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random',
                 wt=wild_type, mutation=mutate.empty)
    os.chdir('..')
    run_dir(test_dir, results)
    assert os.path.isfile(results)
    with open(results, 'r') as f:
        assert len(list(f)) == nfiles


def run_frameshift():
    results = 'results.frameshift'
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random',
                 wt=wild_type, mutation=mutate.frameshift)
    os.chdir('..')
    run_dir(test_dir, results)
    assert os.path.isfile(results)
    with open(results, 'r') as f:
        assert len(list(f)) == nfiles


def run_point():
    results = 'results.point'
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random',
                 wt=wild_type, mutation=mutate.point)
    os.chdir('..')
    run_dir(test_dir, results)
    assert os.path.isfile(results)
    with open(results, 'r') as f:
        assert len(list(f)) == nfiles


if __name__ == '__main__':
    run_empty()
    run_frameshift()
    run_point()
