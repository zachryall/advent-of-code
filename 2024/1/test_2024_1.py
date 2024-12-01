"""Advent of Code 2024 Day 1 Tests
"""

from a import answer_example as a_example, answer_input as a_input
from b import answer_example as b_example, answer_input as b_input

def test_part_a_example_is_correct():
    """Test to check that part A's example gets the correct answer
    """
    assert a_example == 11

def test_part_a_answer_is_correct():
    """Test to check that part A's input gets the correct answer
    """
    assert a_input == 1830478

def test_part_b_example_is_correct():
    """Test to check that part A's example gets the correct answer
    """
    assert b_example == 31

def test_part_b_answer_is_correct():
    """Test to check that part A's input gets the correct answer
    """
    assert b_input == 26674158

