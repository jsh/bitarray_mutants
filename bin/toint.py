#!/usr/bin/env python

import sys

from util import path_to_int

if __name__ == '__main__':
    assert len(sys.argv) == 2, "usage: %s <path>" % sys.argv[0]
    # check that the arg is syntactically valid
    print(path_to_int(sys.argv[1]))
