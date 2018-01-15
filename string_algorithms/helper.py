def left_is_bigger(left, right):
    return True if left > right else False

def chars_dont_match(char, char2):
    return True if char != char2 else False

def assign_variables(text):
    return (text.lower(), 0, len(text) -1 )