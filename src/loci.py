def get_loci(n, length, start=0, dist='uniform'):
    '''Return list of n loci from 0 to n-1
    Distributions available include

    uniform: a constant distance apart
    extent: approximately a constant distance apart, covering the entire length
    random: what it says
    all: every position in the range


    >>> list(get_loci(3,9))
    [0, 3, 6]
    >>> list(get_loci(3,9,1))
    [1, 4, 7]
    >>> list(get_loci(3,9,2))
    [2, 5, 8]
    >>> list(get_loci(3, 11))
    [0, 3, 6]
    >>> list(get_loci(3, 11, dist='extent'))
    [0, 4, 8]
    >>> list(get_loci(3, 11, dist='extent', start=1))
    [1, 5, 9]
    >>> list(get_loci(3, 11, dist='extent', start=2))
    [2, 6, 10]
    >>> list(get_loci(3, 11, dist='extent', start=3))
    [3, 7, 11]
    >>> len(get_loci(3, 11, dist='random'))
    3
    >>> list(get_loci(3, 11, dist='all'))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
    if dist == 'uniform':
        spacing = length//n
        assert start <= spacing, "start [{}] > spacing [{}]".format(start, spacing)

        return (start + spacing*i for i in range(n))
    if dist == 'extent':
        err_msg = "start [{}] > spacing [{}]".format(start, spacing)
        assert round(start + (length/n)*(n-1)) < length, err_msg
        return(start + round((length/n))*i for i in range(n))
    if dist == 'random':
        import random
        return sorted(random.sample(range(length), n))
    if dist == 'all':
        return range(length)
    print("Unknown dist type: %s" % dist)
    raise ValueError
