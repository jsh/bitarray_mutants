#!/usr/bin/env python3
'''Classify run results by type.'''
# pylint: disable=C0413


import os

import mutate
from make_mutants import make_mutants
from runner import run_dir
from util import get_test_dir, get_test_loci, wild_type

lim = os.path.getsize(wild_type)
nfiles = 400
test_loci = get_test_loci(nfiles)


def run_screen(mutation='point', mutagen=mutate.point):
    '''generate mutants, record results'''
    results = mutation + '.results'
    test_dir = get_test_dir(mutation + '.mutants')
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='list',
                 loci=test_loci, wt=wild_type,
                 mutagen=mutagen)
    os.chdir('..')
    run_dir(test_dir, results)
    assert os.path.isfile(results)
    with open(results, 'r') as f:
        assert len(list(f)) == nfiles


def is_neutral(symptom):
    '''Is a neutral mutation.'''
    return symptom == 'silent'


def main():
    '''The driver.'''
    run_screen('neutral')
    with open('neutral.results', 'r') as f:
        for line in f:
            mutant, symptom, _ = line.split()
            if not is_neutral(symptom):
                os.remove(mutant)


if __name__ == '__main__':
    main()
