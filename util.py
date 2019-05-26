#!/usr/bin/env python

import os
import shutil

nfiles = 100
lim = 2 * nfiles
loci = [2 * pos for pos in range(nfiles)]

test_dir = os.path.join(os.getcwd(), 'td')
wild_type = os.path.join(os.getcwd(), 'wild_type')


def get_test_dir():
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        shutil.rmtree(test_dir)
        os.mkdir(test_dir)

    return test_dir
