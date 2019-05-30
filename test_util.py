#!/usr/bin/env python

import os

from util import get_test_dir, get_test_loci


def test_get_test_dir():
    td = get_test_dir()
    assert os.path.isdir(td)

    # second call should also succeed, even though td exists
    td = get_test_dir()
    assert os.path.isdir(td)
    os.rmdir(td)


def test_get_test_loci():
    assert len(list(get_test_loci(400))) == 400
