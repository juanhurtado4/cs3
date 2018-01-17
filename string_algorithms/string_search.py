from palindrome_helper import *

def contains(text, pattern):
    """
    Return a boolean indicating whether pattern occurs in text.
    Iterative solution
    Complexity: O(n) worst case
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return True

    (text, pattern_pos) = (text.lower(), 0)  # assign two vars
    match = False

    for char in text:
        pattern_char = pattern[pattern_pos]

        if pattern_found(pattern, pattern_pos, char):
            return True

        elif chars_match(char, pattern_char):
            match = True
            pattern_pos += 1

        else:
            if chars_overlap(char, pattern[0], pattern_pos):
                match = True
                pattern_pos = 1
                continue

            match = False
            pattern_pos = 0

    return match

# def contains(text, pattern, pattern_pos=None, text_pos=None):
#     """
#     Return a boolean indicating whether pattern occurs in text.
#     Recursive solution
#     """
#     if pattern_pos == None:
#         # TODO: Refactor helper assign_starting_vars func by if statement
#         # TODO: if contains do below, if palindrome execute default logic
#         (text, pattern_pos, text_pos) = (text.lower(), 0, 0) # assign two vars
    
#     if len(pattern) == 0: return True

#     if text_pos >= len(text):
#         return False

#     pattern_char = pattern[pattern_pos]
#     text_char = text[text_pos]
#     if chars_dont_match(text_char, pattern_char):
#         text_pos += 1
#         pattern_pos = 0
#     else:
#         if pattern_pos >= len(pattern) - 1:
#             return True
#         pattern_pos += 1
#         text_pos += 1

#     return contains(text, pattern, pattern_pos, text_pos)

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Complexity: O(n) worst case, O(1) best case"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return 0

    (text, pattern_pos) = (text.lower(), 0)  # assign two vars

    starting_index = None
    for char_ind, char in enumerate(text):

        pattern_char = pattern[pattern_pos]

        if pattern_found(pattern, pattern_pos, char):
            return log_index(char_ind, starting_index, pattern, True)

        elif chars_match(char, pattern_char):
            pattern_pos += 1

        else:
            if chars_overlap(char, pattern[0], pattern_pos):
                pattern_pos = 1
                continue

            pattern_pos = 0

    return starting_index

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Complexity: O(n) worst case, O(1) best case"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return get_all_indexes(text)

    (text, pattern_pos) = (text.lower(), 0)  # assign two vars

    index_arr = []
    for char_ind, char in enumerate(text):
        pattern_char = pattern[pattern_pos]

        if pattern_found(pattern, pattern_pos, char):
            index_arr = log_index(char_ind, index_arr, pattern)

        elif chars_match(char, pattern_char):
            pattern_pos += 1

        else:
            if chars_overlap(char, pattern[0], pattern_pos):
                pattern_pos = 1
                continue

            pattern_pos = 0

    return index_arr
    



def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
