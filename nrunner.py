#!/usr/bin/env python3

import os
import subprocess

from make_mutants import get_mutants


def run_one(code):
    '''Run the code and report the result.'''
    returncode = 0
    timeout = 1  # second

    try:
        output = subprocess.check_output(
            code,
            timeout=timeout,
            stderr=subprocess.STDOUT)
        outcome = 'output ' if output else 'silent '
        # expect 'silent ' but who knows?
    except subprocess.CalledProcessError as err:
        outcome = 'process'
    except OSError as err:
        if os.path.getsize(code) == 0:
            outcome = 'silent '  # subprocess bug
        else:
            outcome = 'oserror'
    except subprocess.TimeoutExpired as err:
        outcome = 'timeout'
    except Exception as err:     # some other misfortune
        outcome = 'exception'

    returncode = err.returncode

    return (outcome, returncode)


def screen(mutation_type):
    '''Make a set of mutants and run them.'''
    make_mutants(wild_type, mutation_type, loci(len(wild_type), n, dist, start=0))
    with open(results, 'w') as f:
        for mutant in get_mutants(dir):
            outcome, returncode = run_one(mutant)
            f.write('{}\t{}\t{:>3d}\n'.format(mutant, outcome, returncode))
        return(get_results_file(mutation_type))
