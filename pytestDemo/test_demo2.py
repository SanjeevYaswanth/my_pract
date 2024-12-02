import pytest

@pytest.fixture
def input_data():
    return 'bad'

def test_thirdresultinfo(input_data):
    # msg = 'Good'
    assert input_data == 'bad', "string doesn't match"

def test_firstpgm():
    print("hello pytest")



@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output

# def test_divisible_by_13(num, input_value):
#    assert input_value % 13 == 0


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected


@pytest.mark.xfail
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    assert x+2 == y, f"expected is {y}, but got {x}"


@pytest.mark.skip
def test_great():
    num = 100
    assert num >= 100