#!/usr/bin/env python

import os
import random


def get_path(n, width):
    '''Make a filepath representing an int
    Convert the int to hex,
    Split the hex number into a filepath,
    return (directory, filename)
    If width > 2, use first two hex digits for subdirectory
    If width > 4, use first four hex digits for two levels
    so 0 -> 00000...0 -> ('00/00', '0...0')

    >>> get_path(10, 2)
    './a'
    >>> get_path(0,3)
    '00/0'
    >>> get_path(15,10)
    '00/00/00000f'
    '''
    fmt = '0' + width + 'x'
    s = format(n, fmt)
    assert len(s) <= width
    p = list(s)
    if width > 4:
        p.insert(4, '/')
    if width > 2:
        p.insert(2, '/')
    if width <= 2:
        p = ['.', '/'] + p
    return ''.join(p)


def make_files(n, lim=None, mode='serial'):
    '''Make n files with names in the range [0,lim-1]'''
    if lim is None:
        lim = n
    assert n <= lim

    if mode == 'random':
        nums = random.sample(range(lim), n)
    else:
        nums = range(n)

    width = len(format(lim - 1, 'x'))  # length of hex representation of largest
    for i in nums:
        directory, file = get_path(i, width)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        f = open(os.path.join(directory, file), 'w')
        f.close()
