#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")

    try:
        return np.matmul(m_a, m_b).tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
