import pytest


@pytest.mark.sanju
def test_first():
    print('Hi Guys')

def test_firstresult():
    print("first result without marker")

@pytest.mark.yash
def test_secondresultinfo():
    print('How are you??')


def test_calculation(value_return):
    assert value_return % 2


def test_addition():
    x = 1
    y = 2
    assert x + y == 3  # This will pass
    assert x + y == 4  # This will fail and show detailed output

def test_list():
    l = [1,2,3,4]
    assert len(l) == 4
    assert 5 in l


def test_multiplication_6():
    result = 3 * 3
    assert result == 6, f"Expected 6, but got {result}"



# @pytest.fixture
# def input_value():
#    input = 39
#    return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0, f"Expected 6, but got {input_value}"



