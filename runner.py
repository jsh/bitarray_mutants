#!/usr/bin/env python

import subprocess


def run_one(code):
    '''Run the code and report the result.'''
    returncode = 0
    timeout = 1  # second

    try:
        output = subprocess.check_output(
            code,
            timeout=timeout,
            stderr=subprocess.STDOUT)
        outcome = '+' if output else '-'  # expect '-', but who knows?
    except subprocess.CalledProcessError as err:
        outcome = 'c'
        returncode = err.returncode
    except OSError:
        outcome = 'o'
    except subprocess.TimeoutExpired:
        outcome = 't'
    except Exception:              # some other misfortune
        outcome = 'e'

    return (outcome, returncode)

