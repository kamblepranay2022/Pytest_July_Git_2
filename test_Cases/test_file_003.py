import pytest


class Test_003:
    @pytest.mark.xfail
    def test_div_001(self):
        a = 200
        b = 20
        c = a / b
        print("mul of a and b is ", c)
        if c == 10:
            assert True
        else:
            assert False
