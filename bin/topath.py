#!/usr/bin/env python

import sys
from nutil import int_to_path

if __name__ == '__main__':
    assert len(sys.argv) == 3, "usage: %s <N (in decimal)> <path_width>" % sys.argv[0]
    print(int_to_path(int(sys.argv[1]), int(sys.argv[2])))


