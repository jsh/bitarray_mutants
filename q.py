#!/usr/bin/env python3

import os

from bitarray import bitarray


class Q:
    def __init__(self, seq = ''):
        self.bna = bitarray(seq)


    def __len__(self):
        return len(self.bna)


    def copy(self):
        copy = Q()
        copy.bna = self.bna.copy()
        return copy


    def empty(self):
        self.bna.setall(False)


    def fromfile(self, filename):
        with open(filename, 'br') as f:
            self.bna.fromfile(f)


    def tofile(self, filename):
        with open(filename, 'bw') as f:
            self.bna.tofile(f)
        os.chmod(filename, 0o775)


    def mutate(self, pos, mutation_type='point', **kwargs):
        mutant = self.copy()

        if mutation_type == 'none':
            pass
        elif mutation_type == 'point':
            mutant.bna[pos] = not mutant.bna[pos]
        elif mutation_type == 'frameshift':
            if kwargs['sense'] == '-':
                print('+ mutant')
            elif kwargs['sense'] == '+':
                print('- mutant')
            else:
                print('bad sense %s\n' % kwargs['sense'])
                raise ValueError
        else:
            print('bad mutation_type %s\n" % mutation_type')
            raise ValueError

        return mutant
