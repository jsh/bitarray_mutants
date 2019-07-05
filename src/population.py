#!/usr/bin/env python3
'''Module for generating mutant populations.'''

from loci import get_loci
from q import Q
from util import int_to_path


class Population:
    '''Object representing directory hierarchy of mutants.'''

    def __init__(self, wt, mutagen, nmutants):
        '''Create the object, store input values.'''
        self.wt = wt
        self.mutagen = mutagen
        self.size = nmutants
        self.q = Q()
        self.q.fromfile(wt)
        self.loci = list(get_loci(nmutants, len(self.q)))
        self.maxpath = len(format(len(self.q), 'x'))

    def gen(self):
        '''Create all mutants.'''
        for locus in self.loci:
            mutant = self.q.copy()
            mutant.mutate(locus)
            mutant.tofile(int_to_path(locus, self.maxpath))

    def enum(self):
        '''List paths to all mutants.'''
        return [int_to_path(locus, self.maxpath) for locus in self.loci]
