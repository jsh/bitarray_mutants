#!/usr/bin/env python

import os

from bitarray import bitarray

import mutate


def test_empty():
    mutate.empty(mut=mutate.mutant)
    assert os.path.isfile(mutate.mutant)
    assert os.path.getsize(mutate.mutant) == 0


def test_point():
    pos = 10
    mutate.point(wt=mutate.wild_type, mut=mutate.mutant, pos=10)
    wt_bna = bitarray()
    with open(mutate.wild_type, 'rb') as f:
        wt_bna.fromfile(f)

    mut_bna = bitarray()
    with open(mutate.mutant, 'rb') as f:
        mut_bna.fromfile(f)

    mask = mutate.blank
    mask[pos] = 1
    assert wt_bna ^ mut_bna == mask
    os.remove(mutate.mutant)
