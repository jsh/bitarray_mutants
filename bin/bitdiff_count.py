#!/usr/bin/env python

import os
import sys

from nutil import file_to_bitarray


if __name__ == '__main__':
    assert len(sys.argv) == 3, "usage %s <filename1> <filename2>" % sys.argv[0]
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    assert os.path.getsize(filename1) == os.path.getsize(filename2), \
		"files %s and %s must be the same size" % (filename1, filename2)
    diffs = file_to_bitarray(filename1) ^ file_to_bitarray(filename2)
    print(diffs.count())
