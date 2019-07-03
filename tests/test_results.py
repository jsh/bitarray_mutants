#!/usr/bin/env python3

import os
import shutil

import mutate
from make_mutants import make_mutants
from results import get_results
from runner import run_dir
from util import get_test_dir, wild_type

nfiles = 10


def run_empty():
    '''Create and run nfiles empty mutants.
    Save results in empty.results.
    '''
    outfile = 'empty.results'
    mutants = get_test_dir('empty.mutants')
    os.chdir(mutants)
    make_mutants(nfiles, wt=wild_type, mutagen=mutate.empty)
    os.chdir('..')
    run_dir(mutants, outfile)


def test_get_results():
    '''Check that there are nfiles results, all successful.'''
    run_empty()
    results = get_results('empty.mutants', 'empty.results')
    assert len(results) == nfiles
    positions = [result[0] for result in results]
    symptoms = [1 for result in results
                if result[1] == 'silent' and result[2] == '0']
    assert len(symptoms) == nfiles
    assert set(positions) == set(range(nfiles))
    shutil.rmtree('empty.mutants')
    os.remove('empty.results')
