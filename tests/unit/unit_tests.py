import pytest
from SABR.SABRs.util import * #buggy line b/c cross-directory importing is janky, will fix later

test_out = [1, 2, 3, 4]
test_ct = 10
test_pdist = [[1, 2, 3, 4], [0.1, 0.2, 0.3, 0.4]]

def test_normlist():
    assert normlist(test_out, test_ct, True) == test_pdist[1]
    assert normlist(test_out, test_ct, False) == test_pdist[0]

def test_cumdist():
    assert cumdist(test_pdist[1]) == [0.1, 0.3, 0.6, 1.0]
    assert cumdist([0.1, 0.2, 0.7]) != [] 

def test_gencflip():
    assert isinstance(gencflip(0.4), int)

def test_gencnum():
    assert isinstance(gencnum(test_pdist), int)

def test_genpossouts():
    assert genpossouts(test_pdist, 5) == [*range(5, 21)]

def test_genposspdist():
    assert genposspdist(test_pdist, 3) == [[3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0.001, 0.006, 0.021, 0.056, 0.111, 0.174, 0.219, 0.204, 0.144, 0.064]]

