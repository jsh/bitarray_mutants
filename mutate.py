#!/usr/bin/env python

from bitarray import bitarray


def mutate(old_file, new_file, pos):
    ba = bitarray()
    with open(old_file, 'rb') as f:
        ba.fromfile(f)
    ba[pos] = not ba[pos]
    with open(new_file, 'wb') as f:
        ba.tofile(f)
