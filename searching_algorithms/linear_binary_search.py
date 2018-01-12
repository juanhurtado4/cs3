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
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    if is_empty(array):
        return None

    sorted_arr = sorted(array)

    subarr_start_position = 0
    subarr_end_position = len(sorted_arr) - 1
    subarr_middle_position = get_middle_position(
                                subarr_start_position, 
                                subarr_end_position
                                )

    while subarr_start_position < subarr_end_position:

        middle_item = sorted_arr[subarr_middle_position]

        if are_items_equal(middle_item, item):
            return subarr_middle_position

        if is_middle_value_bigger(middle_item, item):
            subarr_end_position = get_end_position(subarr_middle_position)

        else:
            subarr_start_position = get_start_position(subarr_middle_position)

        subarr_middle_position = get_middle_position(
                                    subarr_start_position, 
                                    subarr_end_position
                                    )

    if are_items_equal(sorted_arr[subarr_start_position], item):
        return subarr_start_position
    return None

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests