#!/usr/bin/env python

import os

from loci import get_loci
from util import get_dir, int_to_path
from q import Q


class screen:
    def __init__(self, wt, mutagen, nmutants):
        self.wt = wt
        self.mutagen = mutagen
        self.nmutants = nmutants
        self.q = Q()
        self.q.fromfile(wt)
        self.loci = get_loci(nmutants, len(self.q))
        self.maxpath = len(format(len(self.q), 'x'))

    def gen(self):
        for locus in self.loci: 
            mutant = self.q.copy()
            mutant.mutate(locus)
            mutant.tofile(int_to_path(locus, self.maxpath))

if __name__ == '__main__':
    get_dir('screen')
    os.chdir('screen')
    s = screen('/usr/local/bin/gtrue', 'point', 400)
    s.gen()
