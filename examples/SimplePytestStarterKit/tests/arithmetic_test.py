from simple_pytest_sk.arithmetic import sign, lerp, negate, my_abs

def test_sign_for_positive_number():
    assert sign(2) == 1

def test_sign_for_negative_number():
    assert sign(-1) == -1

def test_sign_for_zeros():
    assert sign(0) == 0

class TestLerp:
    def test_for_t_eq_0(self):
        assert lerp(1, 3, 0) == 1

    def test_for_t_eq_1(self):
        assert lerp(1, 3, 1) == 3

    def test_for_intermediate_t(self):
        assert lerp(1, 3, 0.5) == 2.0
    

class TestNegate:
    def test_positive(self):
        assert negate(1) == -1

    def test_negative(self):
        assert negate(-1) == 1

    def test_zero(self):
        assert negate(0) == 0

    def test_zero02(self):
        assert negate(0) == -0

class TestMyAbs:
    def test_positive(self):
        assert my_abs(2) == 2

    def test_positive(self):
        assert my_abs(-2) == 2

    def test_zero(self):
        assert my_abs(0) == 0

    