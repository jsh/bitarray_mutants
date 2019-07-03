#!/usr/bin/env python

import os

from loci import get_loci
from runner import run_one
from q import Q
from util import get_dir, int_to_path, path_to_int


class screen:
    def __init__(self, wt, mutagen, nmutants):
        self.wt = wt
        self.mutagen = mutagen
        self.nmutants = nmutants
        self.q = Q()
        self.q.fromfile(wt)
        self.loci = list(get_loci(nmutants, len(self.q)))
        self.maxpath = len(format(len(self.q), 'x'))

    def gen(self):
        for locus in self.loci: 
            mutant = self.q.copy()
            mutant.mutate(locus)
            mutant.tofile(int_to_path(locus, self.maxpath))

    def enum(self):
        return [int_to_path(locus, self.maxpath) for locus in self.loci]

if __name__ == '__main__':
    nloci = 400
    get_dir('screen')
    os.chdir('screen')
    s = screen('/usr/local/bin/gtrue', 'point', nloci)
    s.gen()

    for mpath in s.enum():
        outcome, returncode = run_one(mpath)
        print(path_to_int(mpath), mpath, outcome, returncode)
