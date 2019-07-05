#!/usr/bin/env python3
'''Run commands. Return outcomes and returncodes.'''

import os
import subprocess


def _findfiles(directory='.'):
    leafnodes = []
    for (dirpath, _, filenames) in os.walk(directory):
        if filenames:
            for filename in filenames:
                leafnodes.append(os.path.join(dirpath, filename))
    return leafnodes


def run_one(file):
    '''Run the file and report the result.'''
    timeout = 1  # second

    try:
        output = subprocess.check_output(
            file,
            timeout=timeout,
            stderr=subprocess.STDOUT)
        outcome = 'output ' if output else 'silent '
        # expect 'silent ' but who knows?
        returncode = 0
    except subprocess.CalledProcessError as err:
        outcome = 'process'
        returncode = err.returncode
    except OSError:
        if os.path.getsize(file) == 0:
            outcome = 'silent '  # subprocess bug
            returncode = 0
        else:
            outcome = 'oserror'
            returncode = None
    except subprocess.TimeoutExpired:
        outcome = 'timeout'
        returncode = None
    except Exception:     # some other misfortune
        outcome = 'exception'
        returncode = None

    return (file, outcome, returncode)

def run_all(directory='.'):
    '''Run all files in the directory.'''
    results = []
    for file in _findfiles(directory):
        results.append(run_one(file))

    return results
