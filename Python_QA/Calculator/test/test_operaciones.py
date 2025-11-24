import pytest
from Calculator.Main import add, divisions, multiplication, subtraction
@pytest.mark.parametrize("a,b,expected_results", [
   (2, 3, 5),          #1. Sum of positive numbers
   (-1, 1, 0),          #2. Sum of negative and positive numbers
    (0, 0, 0),          #3. Sum of zeros
   (-2, -3, -5)        #4. Sum of negative numbers
])
def test_add(a, b, expected_results):
    assert add(a, b) == expected_results   
@pytest.mark.parametrize("a,b,expected_results",[
    (6,3,2),         #1. division of positives
    (5,0, None),     #2. division by zero
    (10,5,2),        #3. exact division
    (7,2,3.5)        #4. division with decimals
])
def test_division(a,b,expected_results):
    if b== 0:
        with pytest.raises(ZeroDivisionError):
            divisions(a,b)
    else:
        assert divisions(a,b) == expected_results
@pytest.mark.parametrize("a,b,expected_results", [
    (5, 3, 2),        #1. subtraction of positives
    (2,-5, 7),       #2. subtraction resulting in negative
    (0, 0, 0),        #3. subtraction of zeros
    (-2,-3, 1)       #4. subtraction of negatives
])
def test_subtraction(a, b, expected_results):
    assert subtraction(a, b) == expected_results
@pytest.mark.parametrize("a,b,expected_results", [
    (2, 3, 6),        #1. multiplication of positives
    (-1, 1, -1),      #2. multiplication of negative and positive
    (0, 5, 0),        #3. multiplication by zero
    (-2, -3, 6)       #4. multiplication of negatives
])
def test_multiplication(a, b, expected_results):
    assert multiplication(a, b) == expected_results