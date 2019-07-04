#!/usr/bin/env python3

import os
import subprocess


def run_one(code):
    '''Run the code and report the result.'''
    timeout = 1  # second

    try:
        output = subprocess.check_output(
            code,
            timeout=timeout,
            stderr=subprocess.STDOUT)
        outcome = 'output ' if output else 'silent '
        # expect 'silent ' but who knows?
        returncode = 0
    except subprocess.CalledProcessError as err:
        outcome = 'process'
        returncode = err.returncode
    except OSError as err:
        if os.path.getsize(code) == 0:
            outcome = 'silent '  # subprocess bug
        else:
            outcome = 'oserror'
        returncode = None
    except subprocess.TimeoutExpired as err:
        outcome = 'timeout'
        returncode = err.returncode
    except Exception as err:     # some other misfortune
        outcome = 'exception'
        returncode = err.returncode

    return (outcome, returncode)
