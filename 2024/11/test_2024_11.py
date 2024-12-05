"""Advent of Code 2024 Day 11 Tests
"""

from d11 import (
    ANSWER_EXAMPLE_A as a_example,
    ANSWER_INPUT_A as a_input,
    ANSWER_INPUT_B as b_input
)

def test_part_a_example_is_correct():
    """Test to check that part A's example gets the correct answer
    """
    assert a_example == 22

def test_part_a_answer_is_correct():
    """Test to check that part A's input gets the correct answer
    """
    assert a_input == 188902

def test_part_b_answer_is_correct():
    """Test to check that part A's input gets the correct answer
    """
    assert b_input == 223894720281135
