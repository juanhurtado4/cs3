import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    '''
    text: str
    running time: o(n)
    checks if text is a palindrome
    returns boolean
    '''
    text = text.lower()
    left_pos = 0
    right_pos = len(text) - 1
    while left_pos < right_pos:
        if text[left_pos] != text[right_pos]: return False
        else:
            left_pos += 1
            right_pos -= 1
    return True

def is_palindrome_recursive(text, left=None, right=None):
    '''
    text: str
    running time: o(n)
    checks if text is a palindrome recursively
    returns boolean
    '''
    if left == None and right == None:
        # assign multiple variables
        (text, left, right) = (text.lower(), 0, len(text) - 1)
    if left > right: return True
    if text[left] != text[right]: return False
    return is_palindrome_recursive(text, left+1, right-1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
