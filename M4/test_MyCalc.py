import pytest
from MyCalc import MyCalc


"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
"""This function tests the 'add' method of MyCalc with various number scenarios using parametrize test cases"""
test_data_add = [
    (2, 2, 4),    # Test positive integers
    (-2, 3, 1),   # Test negative and positive integers
    (10, 20, 30),    # Test adding zeros
]
@pytest.mark.parametrize("num1, num2, expected", test_data_add)
def test_add(num1, num2, expected):
    calc = MyCalc()
    result = calc.add(num1, num2)
    assert result == expected

"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
"""This function tests the 'subtract' method of MyCalc with various number scenarios using parametrize test cases"""
test_data_subtract = [
    (5, 3, 2),     # Test positive integers
    (-2, -3, 1),   # Test negative numbers
    (10, 20, -10),     # Test subtracting zeros
]
@pytest.mark.parametrize("num1, num2, expected", test_data_subtract)
def test_subtract(num1, num2, expected):
    calc = MyCalc()
    result = calc.sub(num1, num2)
    assert result == expected

"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
"""This function tests the 'mult' method of MyCalc with various number scenarios using parametrize test cases"""
test_data_multiply = [
    (3, 4, 12),    # Test positive integers
    (-2, 3, -6),   # Test a negative and a positive number
    (0, 5, 0),     # Test multiplying by zero
]
@pytest.mark.parametrize("num1, num2, expected", test_data_multiply)
def test_multiply(num1, num2, expected):
    calc = MyCalc()
    result = calc.mult(num1, num2)
    assert result == expected

"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
"""This function tests the 'div' method of MyCalc with various input scenarios using parametrize test cases"""
test_data_divide = [
    (6, 2, 3),     # Test positive integers
    (-10, 2, -5),  # Test a negative dividend and a positive divisor
    (0, 5, 0),     # Test dividing zero by a number
]
@pytest.mark.parametrize("num1, num2, expected", test_data_divide)
def test_divide(num1, num2, expected):
    calc = MyCalc()
    result = calc.div(num1, num2)
    assert result == expected

"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
"""This function tests the 'add' method of MyCalc using 'ans' from previous operations using parametize testing"""
calc = MyCalc()    #defining object outside so ans does nto get updated
test_ans_data_add = [
    (2, 2, 4),    # Test positive integers
    ("ans", 3, 7),   # Test negative and positive integers
    ("ans", 20, 27),    # Test adding zeros
]
@pytest.mark.parametrize("num1, num2, expected", test_ans_data_add)
def test_ans_add(num1, num2, expected):
    result = calc.add(num1, num2)
    assert result == expected

"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
""" This function tests the 'subtract' method of MyCalc using 'ans' from previous operations using parametize testing"""
calc = MyCalc()     #defining object outside so ans does nto get updated
test_ans_data_subtract = [
    (10, 5, 5),    # Test positive integers
    ("ans", 3, 2),   # Use "ans" from the previous operation
    ("ans", 20, -18),  # Use "ans" from the previous operation
]
@pytest.mark.parametrize("num1, num2, expected", test_ans_data_subtract)
def test_ans_subtract(num1, num2, expected):
    result = calc.sub(num1, num2)
    assert result == expected

"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
"""This function tests the 'mult' method of MyCalc using 'ans' from previous operations using fixtures"""
@pytest.fixture
def calc_with_answer_for_mult():
    calc = MyCalc()
    calc.ans = 20  # Set answer for testing
    return calc

def test_ans_mult_operation(calc_with_answer_for_mult):
    # The fixture supplies a calculator instance where the `ans` value is initialized to 18.
    calc_with_answer_for_mult.mult(calc_with_answer_for_mult.ans, 4)
    assert calc_with_answer_for_mult.ans == 80

"""Name: Bhavya Shah; UCID: bs635; Date: 15 October, 2023"""
"""This function tests the 'div' method of MyCalc using 'ans' from previous operations using fixtures"""
@pytest.fixture
def calc_with_answer_for_div():
    calc = MyCalc()
    calc.ans = 18  # Set answer for testing
    return calc

def test_ans_div_operation(calc_with_answer_for_div):
    # The fixture supplies a calculator instance where the `ans` value is initialized to 18.
    calc_with_answer_for_div.div(calc_with_answer_for_div.ans, 2)
    assert calc_with_answer_for_div.ans == 9
