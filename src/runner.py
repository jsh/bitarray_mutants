#!/usr/bin/env python3
'''Run commands. Return outcomes and returncodes.'''

import hashlib
import os
import shlex
import subprocess


def _findfiles(directory='.'):
    leafnodes = []
    for (dirpath, _, filenames) in os.walk(directory):
        if filenames:
            for filename in filenames:
                leafnodes.append(os.path.join(dirpath, filename))
    return leafnodes


def run_one(file, output_type='sha1'):
    '''Run the file and report the result.'''
    timeout = 1  # second

    try:
        output = subprocess.check_output(
            shlex.split(file),
            timeout=timeout,
            stderr=subprocess.STDOUT)
        if output and output_type == 'sha1':
            h = hashlib.sha1(output)
            outcome = h.hexdigest() + ' '
        elif output:
            outcome = output
        else:
            outcome = 'silent '
        # expect 'silent ' but who knows?
        returncode = 0
    except subprocess.CalledProcessError as err:
        outcome = 'processerror'
        returncode = err.returncode
    except OSError:
        if os.path.getsize(file) == 0:
            outcome = 'silent '  # subprocess bug, success
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
