#!/usr/bin/env python

from util import get_pos


def get_results(mutant_dir, mutant_results):
    '''Read results, return array of (pos, symptom, code).'''

    rlist = []
    with open(mutant_results, 'r') as f:
        for result in f:
            res = result.split()  # mutant, symptom, code
            print("res[0] is {}".format(res[0]))
            res[0] = get_pos(res[0], root=mutant_dir)
            print("which turns into {}".format(res[0]))
            rlist.append(res)
    return rlist
