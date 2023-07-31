import pytest


class Test_001:

    def test_sum_001(self):
        a = 10
        b = 20
        c = a + b
        print("sum of a and b is ", c)
        if c == 30:
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_sum_002(self):
        a = 50
        b = 20
        c = a - b
        print("sub of a and b is ", c)
        if c == 30:
            assert True
        else:
            assert False










