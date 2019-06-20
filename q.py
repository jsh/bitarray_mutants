#!/usr/bin/env python3

import os

from bitarray import bitarray


class Q(bitarray):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def empty(self):
        self.setall(False)

    def tofile(self, filename):
        with open(filename, 'bw') as f:
            super().tofile(f)
        os.chmod(filename, 0o775)

    def fromfile(self, filename):
        with open(filename, 'br') as f:
            super().fromfile(f)

    def mutate(self, pos, mutation_type='point', bit=False, **kwargs):
        if mutation_type == 'none':
            pass
        elif mutation_type == 'point':
            self[pos] = not self[pos]
        elif mutation_type == 'frameshift':
            if kwargs['sense'] == '-':
                self.pop(pos)
            elif kwargs['sense'] == '+':
                try:
                    self.insert(pos, bit)   # False (default) inserts 0, True inserts 1
                except:
                    print('cannot insert ', bit)
            else:
                print('bad sense %s\n' % kwargs['sense'])
                raise ValueError
        else:
            print('bad mutation_type %s\n" % mutation_type')
            raise ValueError
