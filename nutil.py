#!/usr/bin/env python3

import os
import shutil

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


def get_test_loci(n, start=0):
    '''Return list of n, evenly-spaced loci,
    beginning at start
    along the length of the wild-type,
    '''
    length = os.path.getsize(wild_type)
    spacing = length//n
    assert start in range(spacing), "start outside range({})".format(spacing)
    g = [i for i in range(length) if i % spacing == start]
    return g[:n]


def get_path(n, width):
    '''Make a filepath representing an int
    Convert the int to hex,
    Split the hex number into a filepath,
    return (directory, filename)
    If width > 2, use first two hex digits for subdirectory
    If width > 4, use first four hex digits for two levels
    so 0 -> 00000...0 -> ('00/00', '0...0')

    >>> get_path(10, 2)
    '0a'
    >>> get_path(0,3)
    '00/0'
    >>> get_path(15,10)
    '00/00/00000f'
    '''
    fmt = '0' + str(width) + 'x'
    s = format(n, fmt)
    assert len(s) <= width
    p = list(s)
    if width > 4:
        p.insert(4, '/')
    if width > 2:
        p.insert(2, '/')
    return ''.join(p)


def get_pos(path, root=''):
    '''Transform a path into a decimal position.

    >>> get_pos('0a')
    10
    >>> get_pos('00/0a')
    10
    >>> get_pos('00/00/00000f')
    15
    >>> get_pos('a/b/c/00/00/00000f', root='a/b/c')
    15
    '''
    relpath = os.path.relpath(path, root)
    relpath = relpath.replace('/', '')
    return int(relpath, 16)
