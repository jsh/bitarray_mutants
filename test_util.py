#!/usr/bin/env python

import os

from util import get_test_dir


def test_get_test_dir():
    td = get_test_dir()
    assert os.path.isdir(td)

    # second call should also succeed, even though td exists
    td = get_test_dir()
    assert os.path.isdir(td)
    os.rmdir(td)
