#!/usr/bin/env python3

import os
import shutil

from bitarray import bitarray

wild_type = os.path.join(os.getcwd(), 'wild_type')


def get_mutant_dir(mutation_type):
    '''Return name of directory of mutants.

    Make it if it doesn't already exist.
    '''
    if mutants_dir is None:
        mutants_dir = os.path.join(os.getcwd(), mutation_type)
    try:
        os.mkdir(mutants_dir)
    except FileExistsError:
        shutil.rmtree(mutants_dir)
        os.mkdir(mutants_dir)
    return mutants_dir


def get_results_file(mutation_type):
    '''Return results name of results file.'''
    return os.path.join(get_mutants_dir(mutation_type), 'results')


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
    '''Make a filepath representing an int
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
    with open(file, 'rb') as f:
        b = bitarray()
        b.fromfile(f)
        
    return b
