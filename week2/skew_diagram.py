import sys

def test_skew_diagram(s, r):
    assert skew_diagram('CATGGGCATCGGCCATACGCC') == '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'

def skew_diagram(s):
    i = 0
    skew = '0'
    for c in s:
        if c == 'G':
            i += 1
        elif c == 'C':
            i -= 1
        skew += ' ' + str(i)
    return skew
