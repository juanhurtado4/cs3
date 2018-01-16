def assign_starting_vars(text):
    return (text.lower(), 0, len(text) -1 )

def assign_chars(text, left, right):
    return (text[left], text[right])

def chars_not_alphabet(char, char2):
    return False if char.isalpha() and char2.isalpha() else True

def update_position(direction, old_pos, char):
    if direction == 'left':
        return old_pos if char.isalpha() else old_pos + 1
    else:
        return old_pos if char.isalpha() else old_pos - 1

def right_is_bigger(left, right):
    return True if left < right else False

def chars_dont_match(char, char2):
    return True if char != char2 else False
