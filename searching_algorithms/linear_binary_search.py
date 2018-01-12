from binary_search_helper import *

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if is_empty(array):
        return None

    if index == len(array):
        return None
    elif are_items_equal(array[index], item):
        return index
    # elif array[index] == item:
    #     return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, target):
    if is_empty(array):
        return None

    sorted_arr = sorted(array)

    start_position = 0
    end_position = len(sorted_arr) - 1
    middle_position = get_middle_position(start_position, end_position)

    while start_position < end_position:

        middle_item = sorted_arr[middle_position]

        if are_items_equal(middle_item, target):
            return middle_position

        if is_middle_value_bigger(middle_item, target):
            end_position = get_end_position(middle_position)

        else:
            start_position = get_start_position(middle_position)

        middle_position = get_middle_position(start_position, end_position)

    if are_items_equal(sorted_arr[start_position], target):
        return start_position
    return None

def binary_search_recursive(array, target, start_position=None, end_position=None, middle_position=None):
    sorted_arr = sorted(array)

    if middle_position == None:
        start_position = 0
        end_position = len(sorted_arr) - 1
        middle_position = get_middle_position(start_position, end_position)

    middle_item = sorted_arr[middle_position]

    if are_items_equal(middle_item, target):
        return middle_position

    if is_middle_value_bigger(middle_item, target):
        end_position = get_end_position(middle_position)
    else:
        start_position = get_start_position(middle_position)
    
    middle_position = get_middle_position(start_position, end_position)

    if start_position > end_position:
        # if are_items_equal(middle_item, target):
        #     return middle_position
        return None

    return binary_search_recursive(array, target, start_position, end_position, middle_position)