#!/usr/bin/env python

import shutil

import mutate
from make_mutants import make_mutants

def make_test_dir():
    test_dir = os.path.join(os.getcwd(), 'td')
    nfiles = 100
    lim = 2 * nfiles
    wild_type = os.path.join(os.getcwd(), 'wild_type')

    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)

    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='random',
                 wt=wild_type, mutation=mutate.point)
    os.chdir('..')
    return test_dir


