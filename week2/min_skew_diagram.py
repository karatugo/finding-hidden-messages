from skew_diagram import *
import sys

def test_min_skew_diagram(s, r):
    assert min_skew_diagram('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT') == '11 24'

def min_skew_diagram(s):
    skew = skew_diagram(s)
    skew = skew.split(' ')
    min_skew = min([int(s) for s in skew])
    return ' '.join([str(i) for i, s in enumerate(skew) if int(s) == min_skew])
