#!/usr/bin/env python

from runner import run_one


def test_true():
    outcome, returncode = run_one('/usr/bin/true')
    assert outcome == '-'
    assert returncode == 0


def test_false():
    outcome, returncode = run_one('/usr/bin/false')
    assert outcome == 'c'
    assert returncode == 1
