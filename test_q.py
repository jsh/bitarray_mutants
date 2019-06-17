#!/usr/bin/env python3

import filecmp
import os
import sys

from bitarray import bitarray

from q import Q


def test_Q():
    for val in ['', '1'*8]:
        q = Q(val)
        q.bna = bitarray(val)


def test_len():
    size = 256
    q = Q('1'*size)
    assert len(q) == size


def test_empty():
    q0 = Q('0'*8)
    q1 = Q('1'*8)
    q1.empty()
    assert q0.bna == q1.bna


def test_copy():
    q1 = Q('11111111')
    q2 = q1.copy()
    assert q1 != q2
    assert q1.bna == q2.bna

   
def test_filops():
    copy = 'copy'
    q = Q()
    q.fromfile(sys.argv[0])
    q.tofile(copy)
    assert filecmp.cmp(sys.argv[0], copy, shallow=False)
    os.remove(copy)


def test_mutate():
    wt = Q('1'*8)
    mut = wt.copy()
    for i in range(len(wt)):
        mutant = mut.mutate(i)
    assert mutant == wt.empty()
