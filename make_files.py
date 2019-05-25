#!/usr/bin/env python

import os


def get_filepath(n, width):
    '''Make a filepath representing an int
    Convert the int to hex,
    Split the hex number into a three-level filepath,
    return (directory, filename)
    ('xx/yy', 'zzz..z')
    where xx and yy are the first four hex digits
    so 0 -> 00000...0 -> ('00/00', '0...0')

    >>> get_filepath(15,10)
    ('00/00', '00000f')
    '''
    assert width > 4
    fmt = '{0:0{1}x}'
    s = fmt.format(n, width)
    return s[0:2] + '/' + s[2:4],  s[4:]


def make_files(n):
    '''Make files with names from 0..n-1'''
    width = len(format(n-1, 'x'))  # length of hex representation of largest
    for i in range(n):
        directory, file = get_filepath(i, width)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        f = open(os.path.join(directory, file), 'w')
        f.close()
