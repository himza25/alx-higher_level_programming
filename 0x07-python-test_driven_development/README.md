# Python Test-Driven Development

This repository is dedicated to practicing test-driven development in Python. Below are the task descriptions and requirements.

## Tasks

### 0. Integers addition

- Prototype: `def add_integer(a, b=98):`
- Requirements:
  - `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`.
  - `a` and `b` must be first casted to integers if they are float.
  - Returns an integer: the addition of `a` and `b`.
  - You are not allowed to import any module.

### 1. Divide a matrix

- Prototype: `def matrix_divided(matrix, div):`
- Requirements:
  - `matrix` must be a list of lists of integers or floats.
  - Each row of the matrix must be of the same size.
  - `div` must be a number (integer or float).
  - All elements of the matrix should be divided by `div`, rounded to 2 decimal places.
  - Returns a new matrix.
  - You are not allowed to import any module.

### 2. Say my name

- Prototype: `def say_my_name(first_name, last_name=""):`
- Requirements:
  - `first_name` and `last_name` must be strings.
  - You are not allowed to import any module.

### 3. Print square

- Prototype: `def print_square(size):`
- Requirements:
  - `size` is the size length of the square.
  - `size` must be an integer.
  - if `size` is a float and is less than 0, raise a TypeError exception with the message `size must be an integer`.
  - You are not allowed to import any module.

### 4. Text indentation

- Prototype: `def text_indentation(text):`
- Requirements:
  - `text` must be a string.
  - There should be no space at the beginning or at the end of each printed line.
  - You are not allowed to import any module.

### 5. Max integer - Unittest

- Prototype: `def max_integer(list=[]):`
- Requirements:
  - Your test file should be inside a folder `tests`.
  - You have to use the `unittest` module.

### 6. Matrix multiplication (Advanced)

- Prototype: `def matrix_mul(m_a, m_b):`
- Requirements:
  - `m_a` and `m_b` must be validated with specific requirements.
  - `m_a` and `m_b` must be an list of lists of integers or floats.

## Repo:

GitHub repository: `alx-higher_level_programming`
Directory: `0x07-python-test_driven_development`
