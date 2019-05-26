#!/usr/bin/env python

import os
import shutil

import mutate
from make_mutants import get_mutants, make_mutants
from util import get_test_dir, lim, loci, nfiles, wild_type


def test_make_empty_mutants_serial():
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim)
    os.chdir('..')

    assert sum(True for mutant in get_mutants(test_dir)) == nfiles
    shutil.rmtree(test_dir)


def test_make_empty_mutants_random():
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random')
    os.chdir('..')

    assert sum(True for mutant in get_mutants(test_dir)) == nfiles
    shutil.rmtree(test_dir)


def test_make_empty_mutants_list():
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='list', loci=loci)
    os.chdir('..')

    assert sum(True for mutant in get_mutants(test_dir)) == nfiles
    shutil.rmtree(test_dir)


def test_make_point_mutants_random():
    test_dir = get_test_dir()
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random',
                 wt=wild_type, mutation=mutate.point)
    os.chdir('..')

    assert sum(True for mutant in get_mutants(test_dir)) == nfiles
    shutil.rmtree(test_dir)
