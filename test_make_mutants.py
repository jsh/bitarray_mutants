#!/usr/bin/env python

import os
import shutil

import mutate
from make_mutants import get_mutants, make_mutants

test_dir = os.path.join(os.getcwd(), 'td')
nfiles = 100
lim = 2 * nfiles

wild_type = os.path.join(os.getcwd(), 'wild_type')


def test_make_empty_mutants_serial():
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)

    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim)
    os.chdir('..')

    assert sum(True for mutant in get_mutants(test_dir)) == nfiles
    shutil.rmtree(test_dir)


def test_make_empty_mutants_random():
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)

    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random')
    os.chdir('..')

    assert sum(True for mutant in get_mutants(test_dir)) == nfiles
    shutil.rmtree(test_dir)


def test_make_point_mutants_random():
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)

    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random',
                 wt=wild_type, mutation=mutate.point)
    os.chdir('..')

    assert sum(True for mutant in get_mutants(test_dir)) == nfiles
    shutil.rmtree(test_dir)
