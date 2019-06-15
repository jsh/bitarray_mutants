#!/usr/bin/env python3
'''Classify run results by type.'''
# pylint: disable=C0413


import os
import sys

import plotly.graph_objs as go
import plotly.offline as po

import mutate
from make_mutants import make_mutants
from results import get_results
from runner import run_dir
from util import get_test_dir, get_test_loci, wild_type

lim = os.path.getsize(wild_type)
nfiles = 400
test_loci = get_test_loci(nfiles)


def run_screen(mutation='frameshift', mutagen=mutate.frameshift,
               direction='+'):
    '''generate mutants, record results'''
    results = mutation + '.results'
    test_dir = get_test_dir(mutation + '.mutants')
    os.chdir(test_dir)
    make_mutants(nfiles, lim=lim, mode='list',
                 loci=test_loci, wt=wild_type,
                 mutagen=mutagen, direction=direction)
    os.chdir('..')
    run_dir(test_dir, results)
    assert os.path.isfile(results)
    with open(results, 'r') as f:
        assert len(list(f)) == nfiles


def results_to_list(mutation='frameshift', direction='+'):
    '''return results as list'''
    run_screen(mutation, direction=direction)
    rlist = get_results(mutation + '.mutants', mutation + '.results')
    return rlist


def is_silent(r):
    '''Is a silent mutation.'''
    return r[1] == 'silent'


def is_process(r):
    '''Is a process mutation.'''
    return r[1] == 'process'


def is_oserror(r):
    '''Is an oserror mutation.'''
    return r[1] == 'oserror'


def is_nonsense(r):
    '''Illegal instruction.'''
    return r[2] == '-4'


def is_killed(r):
    '''kill -9.'''
    return r[2] == '-9'


def is_library(r):
    '''Can't load dynamic library.'''
    return r[2] == '-6'


def graph_it(rlist, title='Causes of Death'):
    killed_mutants = [r for r in rlist if (is_process(r) and is_killed(r))]
    nonsense_mutants = [r for r in rlist if (is_process(r) and is_nonsense(r))]
    stillborn_mutants = [r for r in rlist if is_oserror(r)]
    starved_mutants = [r for r in rlist if is_library(r)]
    killed = go.Bar(
        name='Suicide',
        x=[r[0] for r in killed_mutants],
        y=[1 for r in killed_mutants]
    )
    starved = go.Bar(
        name='Starved',
        x=[r[0] for r in starved_mutants],
        y=[1 for r in starved_mutants]
    )
    nonsense = go.Bar(
        name='Nonsense',
        x=[r[0] for r in nonsense_mutants],
        y=[1 for r in nonsense_mutants]
    )
    stillborn = go.Bar(
        name='Stillborn',
        x=[r[0] for r in stillborn_mutants],
        y=[1 for r in stillborn_mutants]
    )
    data = [killed, nonsense, stillborn, starved]
    layout = go.Layout(
        barmode='group',
        title=title
    )
    fig = go.Figure(data=data, layout=layout)
    po.plot(fig, filename=sys.argv[0].replace('.py', '.html'), auto_open=False)


def main():
    '''The driver.'''
    rlist = results_to_list('frameshift', '+')
    graph_it(rlist,
             title='Causes of Death for Frameshift Mutants ("+")')
    rlist = results_to_list('frameshift', '-')
    graph_it(rlist,
             title='Causes of Death for Frameshift Mutants ("-")')


if __name__ == '__main__':
    main()
