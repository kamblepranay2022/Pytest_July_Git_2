import pytest


class Test_002:
    # @pytest.mark.skipif
    @pytest.mark.pranay   # user defined marker  pytest  command  -m=pranay
    def test_mul_001(self):
        a = 10
        b = 20
        c = a * b
        print("mul of a and b is ", c)
        if c == 200:
            assert True
        else:
            assert False















