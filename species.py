#!/usr/bin/env python3

from bitarray import bitarray

class Bug:
    def __init__(self, seq = ''):
        self.bna = bitarray(seq)


    def Bug.fromfile(self, filename):
        with open(filename, 'br') as f:
            self.bna.fromfile(f)


    def Bug.tofile(self, mutant):
        with open(filename, 'bw') as f:
            self.bna.tofile(f)
        os.chmod(mut, 0o775)


    def Bug.copy(self)
        copy = Bug()
        copy.bna = self.bna.copy()
        return copy


    def Bug.mutate(self, pos, mutation_type='point', **kwargs)
        mutant = self.copy()

        if mutation_type = 'none':
            pass
        elif mutation_type == 'point':
            mutant.bna[pos] = not bna[pos]
        elif mutation_type == 'frameshift'
            if kwargs['sense'] == '-':
                print('+ mutant')
            elif kwargs['sense'] == '+':
                print('- mutant')
            else:
                raise('bad sense %s\n' % kwargs['sense'])
        else:
            raise('bad mutation_type %s\n" % mutation_type)

        return mutant
        

