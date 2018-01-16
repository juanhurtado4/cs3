from palindrome_helper import *

def contains(text, pattern):
    """
    Return a boolean indicating whether pattern occurs in text.
    Iterative solution
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if len(pattern) == 0: return True
    (text, pattern_pos) = (text.lower(), 0) # assign two vars
    for char_pos, char in enumerate(text):
        if pattern_pos >= len(pattern):
            pattern_pos = 0
        pattern_char = pattern[pattern_pos]
        if chars_dont_match(char, pattern_char):

            first_pattern_char = pattern[0] # refactor
            if chars_dont_match(char, first_pattern_char):
                pattern_pos = 0
            else:
                pattern_pos = 1

        else:
            if pattern_pos >= len(pattern) - 1:
                return True
            pattern_pos += 1
    return False

# def contains(text, pattern, pattern_pos=None, text_pos=None):
#     """
#     Return a boolean indicating whether pattern occurs in text.
#     Recursive solution
#     """
#     if pattern_pos == None:
#         # TODO: Refactor helper assign_starting_vars func by if statement
#         # TODO: if contains do below, if palindrome execute default logic
#         (text, pattern_pos, text_pos) = (text.lower(), 0, 0) # assign two vars
    
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
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # # TODO: Uncomment these lines after you implement find_index
    # index = find_index(text, pattern)
    # print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # # TODO: Uncomment these lines after you implement find_all_indexes
    # indexes = find_all_indexes(text, pattern)
    # print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


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