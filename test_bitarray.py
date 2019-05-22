#!/usr/bin/env python
import os

from bitarray import bitarray

kba = bitarray()
bytes_1k = 8*2**10
kba.extend(bytes_1k*[False])


def test_construction():
    ba = bitarray()
    ba.append(True)
    ba.extend([False, True, True])
    assert ba == bitarray('1011')
    ba[0] = 0b0
    assert ba == bitarray('0011')
    ba[-1] = 0b0
    assert ba == bitarray('0010')


def test_write():
    with open('new', 'wb') as filehandle:
        kba.tofile(filehandle)
    assert os.path.getsize('new') == len(kba)/8
    os.remove('new')


def test_read():
    with open('new', 'wb') as filehandle:
        kba.tofile(filehandle)

    ba = bitarray()
    with open('new', 'rb') as filehandle:
        ba.fromfile(filehandle)
    assert ba == kba
    os.remove('new')


def test_bitops():
    # single-bit
    zero = bitarray('0')
    one = bitarray('1')
    assert zero & one == zero
    assert zero | one == one

    # multi-bit
    two = bitarray('010')
    three = bitarray('011')
    five = bitarray('101')
    six = bitarray('110')
    seven = bitarray('111')
    assert three | six == seven
    assert three & six == two
    assert three ^ six == five
