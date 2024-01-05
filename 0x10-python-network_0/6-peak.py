#!/usr/bin/python3
"""Module to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    :param list_of_integers: List of integers
    :return: A peak element, or None if not found
    """
    if not list_of_integers:
        return None

    def binary_search(nums, low, high):
        if low == high:
            return nums[low]

        mid = low + (high - low) // 2
        if nums[mid] < nums[mid + 1]:
            return binary_search(nums, mid + 1, high)
        return binary_search(nums, low, mid)

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
