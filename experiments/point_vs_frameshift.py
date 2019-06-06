#!/usr/bin/env python

import os

import mutate
from make_mutants import make_mutants
from runner import run_dir
from util import get_test_dir, get_test_loci, wild_type

lim = os.path.getsize(wild_type)
nfiles = 400
test_loci = get_test_loci(nfiles)


def run_screen(mutation='point', mutagen=mutate.point, direction='+'):
    '''generate mutants, record results'''
    results = mutation + '.results'
    test_dir = get_test_dir(mutation + '.mutants')
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='list',
                 loci=test_loci, wt=wild_type,
                 mutagen=mutagen, direction=direction)
    os.chdir('..')
    run_dir(test_dir, results)
    assert os.path.isfile(results)
    with open(results, 'r') as f:
        assert len(list(f)) == nfiles


def main():
    run_screen(mutation='point', mutagen=mutate.point)
    run_screen(mutation='frameshift', mutagen=mutate.frameshift, direction='-')


if __name__ == '__main__':
    main()
