#!/usr/bin/env python3

import os

from src.util import get_dir


def test_get_dir():
    td = 'whatever'
    get_dir(td)
    assert os.path.isdir(td)

    # second call should also succeed, even though td exists
    get_dir(td)
    assert os.path.isdir(td)
    os.rmdir(td)
