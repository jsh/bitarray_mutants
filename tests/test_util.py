#!/usr/bin/env python3

import os

from util import create_dir, file_to_bitarray, wild_type


def test_create_dir():
    td = 'whatever'
    create_dir(td)
    assert os.path.isdir(td)

    # second call should also succeed, even though td exists
    create_dir(td)
    assert os.path.isdir(td)
    os.rmdir(td)

def test_file_to_bitarray():
    assert os.path.getsize(wild_type)*8 == len(file_to_bitarray(wild_type))
