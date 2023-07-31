import pytest


class Test_004:
    @pytest.mark.xfail
    def test_mul_001(self):
        a = 10
        b = 20
        c = a * b
        print("mul of a and b is ", c)
        if c == 20:
            assert True
        else:
            assert False
