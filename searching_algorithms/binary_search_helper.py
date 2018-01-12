def is_empty(arr):
    '''Checks if an array is empty'''
    return True if len(arr) < 1 else False

def are_items_equal(arr_item, item):
    '''Checks if array item is the same as item. Returns boolean'''
    return True if arr_item == item else False

def is_middle_value_bigger(middle_item, target):
    '''
    middle_item: string
    target: string
    Checks if first letter of the first item is bigger than, the second item first letter
    Returns boolean
    '''
    if middle_item[0] == target[0]:
        for middle_char, target_char in zip(middle_item, target):
            # Check each char until non duplicate is found
            if middle_char != target_char:
                return True if middle_char > target_char else False
        # if duplicate return true
        return True


    return True if middle_item[0] > target[0] else False

def get_start_position(middle_ind):
    '''Calculates the starting position. Returns Int'''
    return int(middle_ind + 1)

def get_middle_position(start_ind, end_ind):
    '''Calculates the middle position. Returns Int'''
    return int((end_ind + start_ind) / 2)

def get_end_position(middle_ind):
    '''Calculates the ending position. Returns Int'''
    return int(middle_ind - 1)