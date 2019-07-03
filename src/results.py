#!/usr/bin/env python3

import os
import sys

DEATHS = 'causes_of_death'

def _causes_of_death():
    reasons = {}
    with open(DEATHS, 'r') as deaths:
        for death in deaths:
            meaning, outcome, returncode, *comment = death.split()
            reasons[outcome, returncode] = meaning
        return reasons

class Result:
    causes_of_death = _causes_of_death()

    def __init__(self, s):
        self.data = s.split()

    def mutant(self):
        return self.data[0]

    def outcome(self):
        return self.data[1]

    def returncode(self):
        return self.data[2]

    def pos(self):
        '''Transform mutant path into a decimal position.
        '0a' -> 10
        '00/0a' -> 10
        '00/00/00000f' -> 15
        '''
        hexpos = self.mutant().replace('/', '')
        return int(hexpos, 16)

    def cause_of_death(self):
        try:
            return Result.causes_of_death[self.outcome(), self.returncode()]
        except:
            return 'unknown cause'

def get_results(mutation_type):
    results = get_results_file(mutation_type)
    mutants = {}
    with open(results, 'r') as f:
        for result in f:
            r = Result(result)
            mutants[r.pos()] = r
    return mutants

def put_results(mutation_type):
    pass
    

def main():
    for key, value in get_results('point').items():
        # print(key, value.outcome(), value.returncode())
        print(key, value.cause_of_death())

if __name__ == '__main__':
    main()
