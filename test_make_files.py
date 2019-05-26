#!/usr/bin/env python

import os
import shutil

from make_files import make_files

test_dir = os.path.join(os.getcwd(), 'td')
nfiles = 100000


def test_make_files():
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)
    os.chdir(test_dir)
    make_files(nfiles)

    file_count = sum(len(files) for _, _, files in os.walk(test_dir))
    assert file_count == nfiles
    shutil.rmtree(test_dir)
