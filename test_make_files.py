#!/usr/bin/env python

import os

from make_files import make_files

'''
import shutil
'''


test_dir = 'td'
nfiles = 100000


def test_make_files():
    os.mkdir(test_dir)
    os.chdir(test_dir)
    make_files(nfiles)
    os.chdir('..')

    tot = 0
    for subdir in os.listdir(test_dir):
        tot += len(os.listdir(os.path.join(test_dir, subdir)))

    assert tot == nfiles
    '''
    shutil.rmtree(test_dir)
    '''
