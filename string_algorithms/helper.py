def assign_starting_vars(text):
    return (text.lower(), 0, len(text) -1 )

def assign_chars(text, left, right):
    return (text[left], text[right])

def check_in_alphabet(char, char2):
    char_result = True if char.isalpha() else False
    char2_result = True if char2.isalpha() else False
    return (char_result, char2_result)

# def left_is_bigger(left, right):
#     return True if left > right else False
def right_is_bigger(left, right):
    return True if left < right else False

def chars_dont_match(char, char2):
    return True if char != char2 else False
