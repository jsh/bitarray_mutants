#!/usr/bin/env python

import os
import random

import mutate
from util import get_path


def make_mutants(
                 n=0,
                 lim=None,
                 mode='serial',
                 mutagen=mutate.empty,
                 wt=mutate.wild_type,
                 loci=None
                 ):

    '''Make n files with names in the range [0,lim-1]'''
    if lim is None:
        lim = n
    assert n <= lim

    if mode == 'random':
        nums = random.sample(range(lim), n)
    elif mode == 'list':
        assert len(loci) <= lim
        nums = loci             # n is irrelevant
    else:
        nums = range(n)  # all

    width = len(format(lim - 1, 'x'))  # hex of largest
    for i in nums:
        path = get_path(i, width)
        directory = os.path.dirname(path) or '.'
        if not os.path.isdir(directory):
            os.makedirs(directory)
        mutagen(wt=wt, mut=path, pos=i)


def get_mutants(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.join(dirpath, f)
