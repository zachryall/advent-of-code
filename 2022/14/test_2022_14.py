"""Advent of Code 2024 Day 1 Tests
"""

from a import ANSWER_EXAMPLE as a_example, ANSWER_INPUT as a_input
from b import ANSWER_EXAMPLE as b_example, ANSWER_INPUT as b_input

def test_part_a_example_is_correct():
    """Test to check that part A's example gets the correct answer
    """
    assert a_example == 24

def test_part_a_answer_is_correct():
    """Test to check that part A's input gets the correct answer
    """
    assert a_input == 1133

def test_part_b_example_is_correct():
    """Test to check that part A's example gets the correct answer
    """
    assert b_example == 93

def test_part_b_answer_is_correct():
    """Test to check that part A's input gets the correct answer
    """
    assert b_input == 27566
