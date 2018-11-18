from mathematica.algebra.matrices import add_matrices, sub_matrices
import pytest

def test_add_matrices():

    m1 = [
        [1, 2, 3],
        [7, 8, 9]
    ]

    m2 = [
        [4, 5, 6],
        [10, 11, 12]
    ]



def test_add_matrices_diffrernt_size():

    with pytest.raises(ValueError):