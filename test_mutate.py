#!/usr/bin/env python

import os

from bitarray import bitarray

from mutate import mutate

wild_type = 'wild_type'
mutant = 'mutant'
wt_bitcount = os.path.getsize(wild_type)*8
blank = bitarray(wt_bitcount)
blank.setall(0)


def test_mutate():
    pos = 10
    mutate(wild_type, mutant, 10)
    wt = bitarray()
    with open(wild_type, 'rb') as f:
        wt.fromfile(f)

    mut = bitarray()
    with open(mutant, 'rb') as f:
        mut.fromfile(f)

    mask = blank
    mask[pos] = 1
    assert wt ^ mut == mask
