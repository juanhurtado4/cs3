def is_empty(arr):
    '''
    Arr: Array
    Checks if an array is empty
    Returns Boolean
    '''
    return True if len(arr) < 1 else False

def are_items_equal(arr_item, item):
    '''
    Arr_item: any
    Item: any
    Checks if array item is the same as item
    Returns boolean
    '''
    return True if arr_item == item else False

def is_first_value_bigger(first_item, second_item):
    return True if first_item[0] > second_item[0] else False

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
    elif items_are_equal(array[index], item):
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
    elif len(array) == 1:
        if are_items_are_equal(array[0], item):
            return 0
        else:
            return None

    sorted_arr = sorted(array)
    middle_ind = len(sorted_arr / 2)

    while len(sorted_arr) > 1:
        if is_first_value_bigger(sorted_arr[middle_ind], item):

        ord(sorted_arr[middle_ind])


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
