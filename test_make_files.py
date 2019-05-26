#!/usr/bin/env python

import os
import shutil

from make_files import make_files

test_dir = os.path.join(os.getcwd(), 'td')
nfiles = 100
lim = 2 * nfiles


def test_make_files_serial():
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)
    os.chdir(test_dir)

    make_files(nfiles, lim=lim)
    file_count = sum(len(files) for _, _, files in os.walk(test_dir))
    assert file_count == nfiles
    os.chdir('..')
    shutil.rmtree(test_dir)


def test_make_files_random():
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)
    os.chdir(test_dir)
    make_files(nfiles, lim=lim, mode='random')
    file_count = sum(len(files) for _, _, files in os.walk(test_dir))
    assert file_count == nfiles
    os.chdir('..')
    shutil.rmtree(test_dir)
