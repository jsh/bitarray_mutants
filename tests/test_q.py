#!/usr/bin/env python3

import filecmp
import os
import sys

from bitarray import bitarray

from src.q import Q


def test_Q():
    for val in ['', '1'*8, False*2]:
        q = Q(val)
        assert q == bitarray(val)

def test_len():
    size = 256
    q = Q('1'*size)
    assert len(q) == size


def test_empty():
    q0 = Q('0'*8)
    q1 = Q('1'*8)
    q1.empty()
    assert q0 == q1


def test_copy():
    q1 = Q('11111111')
    q2 = q1.copy()
    assert q1 == q2

   
def test_filops():
    orig = __file__
    copy = 'copy'
    q = Q()
    try:
        q.fromfile(orig)
        q.tofile(copy)
    except Exception as err:
        sys.exit(err)

    assert filecmp.cmp(orig, copy, shallow=False)
    os.remove(copy)


def test_mutate():
    size = 8
    wt = Q('1'*size)
    mut = wt.copy()
    empty = Q('0'*size)

    for i in range(len(wt)):
        mut.mutate(i)
    assert mut == empty
    assert len(mut) == size

    mut.mutate(2, mutation_type='frameshift', sense='+', bit=True)
    print(mut)
    assert len(mut) == size + 1
    assert mut == Q('001000000')
    mut.mutate(2, mutation_type='frameshift', sense='-')
    assert mut == empty
