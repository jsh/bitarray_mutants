#!/usr/bin/env python

import os

from bitarray import bitarray

wild_type = 'wild_type'
mutant = 'mutant'
wt_bitcount = os.path.getsize(wild_type)*8
blank = bitarray(wt_bitcount)
blank.setall(0)


def point(wt=wild_type, mut=mutant, pos=None):
    bna = bitarray()
    with open(wt, 'rb') as f:
        bna.fromfile(f)
    if pos is not None:
        bna[pos] = not bna[pos]
    with open(mut, 'wb') as f:
        bna.tofile(f)


def empty(wt=None, mut=None, pos=None):
    f = open(mut, 'w')
    f.close()
