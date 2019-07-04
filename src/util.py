#!/usr/bin/env python3
'''Utility functions.

>>> print(TRUE)
/usr/bin/true
>>> print(FALSE)
/usr/bin/false
>>> print(WILD_TYPE)
/Users/jsh/Desktop/Python/bitarray_mutants/src/wild_type
'''

import os
import shutil

from bitarray import bitarray

FALSE = shutil.which('false')
TRUE = shutil.which('true')
WILD_TYPE = os.path.join(os.getcwd(), 'wild_type')


def create_dir(dirname):
    '''Mkdir, first removing older versions if needed.'''
    try:
        os.mkdir(dirname)
    except FileExistsError:
        shutil.rmtree(dirname)
        os.mkdir(dirname)


def results_file(dirname):
    '''Return results name of results file.
    Does not create the file or require the file exist.
    >>> print(results_file('whatever'))
    whatever/results
    '''
    return os.path.join(dirname, 'results')


def path_to_int(path):
    '''Transform a path into a decimal position.

    >>> path_to_int('0a')
    10
    >>> path_to_int('00/0a')
    10
    >>> path_to_int('00/a')
    10
    >>> path_to_int('00/00/00/00/0f')
    15
    '''
    return int(path.replace('/', ''), 16)


def int_to_path(n, width):
    '''Make a filepath representing an int.
    Convert the int to hex,
    Split the hex number into a filepath,
    return (directory, filename)
    If width > 2, use first two hex digits for subdirectory
    If width > 4, use first four hex digits for two levels
    so 0 -> 00000...0 -> ('00/00', '0...0')

    >>> int_to_path(10, 2)
    '0a'
    >>> int_to_path(0, 3)
    '00/0'
    >>> int_to_path(15, 10)
    '00/00/00/00/0f'
    '''
    fmt = '0' + str(width) + 'x'
    s = format(n, fmt)
    assert len(s) <= width
    return '/'.join([s[i:i+2] for i in range(0, len(s), 2)])


def file_to_bitarray(file):
    '''Read a file into a bitarray.
    '''
    with open(file, 'rb') as f:
        b = bitarray()
        b.fromfile(f)
    return b
