#!/usr/bin/env python

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
        returncode = err.returncode
    except OSError:
        outcome = 'oserror'
    except subprocess.TimeoutExpired:
        outcome = 'timeout'
    except Exception:              # some other misfortune
        outcome = 'exceptn'

    return (outcome, returncode)


def run_dir(directory, results):
    with open(results, 'w') as f:
        for mutant in get_mutants(directory):
            outcome, returncode = run_one(mutant)
            f.write('{}\t{}\t{:>3d}\n'.format(mutant, outcome, returncode))
