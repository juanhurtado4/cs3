from palindrome import is_palindrome
import unittest
import pytest

def test_is_palindrome_with_mirrored_strings():
    # palindromes that are perfectly mirrored strings
    assert is_palindrome('') is True  # base case
    assert is_palindrome('A') is True  # base case
    assert is_palindrome('BB') is True  # even length
    assert is_palindrome('LOL') is True  # odd length
    assert is_palindrome('noon') is True
    assert is_palindrome('radar') is True
    assert is_palindrome('doggod') is True
    assert is_palindrome('racecar') is True

def test_is_palindrome_with_mixed_casing():
    # palindromes with mixed letter casing
    assert is_palindrome('Bb') is True
    assert is_palindrome('Lol') is True
    assert is_palindrome('NoOn') is True
    assert is_palindrome('Radar') is True
    assert is_palindrome('DogGod') is True
    assert is_palindrome('RaceCar') is True

def test_is_palindrome_with_whitespace():
    # palindromes with whitespace
    assert is_palindrome('B B') is True
    assert is_palindrome('no on') is True
    assert is_palindrome('dog god') is True
    assert is_palindrome('taco cat') is True
    assert is_palindrome('race car') is True
    assert is_palindrome('race fast safe car') is True

def test_is_palindrome_with_whitespace_and_mixed_casing():
    # palindromes with whitespace and mixed letter casing
    assert is_palindrome('B b') is True
    assert is_palindrome('No On') is True
    assert is_palindrome('Dog God') is True
    assert is_palindrome('Taco Cat') is True
    assert is_palindrome('Race Car') is True
    assert is_palindrome('Race Fast Safe Car') is True

def test_is_palindrome_with_whitespace_and_punctuation():
    # palindromes with whitespace and punctuation
    assert is_palindrome('B-B') is True
    assert is_palindrome('no, on!') is True
    assert is_palindrome('dog god?') is True
    assert is_palindrome('taco? cat.') is True
    assert is_palindrome('race-car!!!') is True
    assert is_palindrome('race fast, safe car...') is True

def test_is_palindrome_with_mixed_casing_and_punctuation():
    # palindromes with whitespace, punctuation and mixed letter casing
    assert is_palindrome('No, On!') is True
    assert is_palindrome('Dog God?') is True
    assert is_palindrome('Taco? Cat.') is True
    assert is_palindrome('Taco!!!!!!!!!!Cat.') is True
    assert is_palindrome('Race-Car!!!') is True
    assert is_palindrome('Race Fast, Safe Car...') is True
    assert is_palindrome('Was it a car or a cat I saw?') is True
    assert is_palindrome("Go hang a salami, I'm a lasagna hog.") is True
    assert is_palindrome('A man, a plan, a canal - Panama!') is True

def test_is_palindrome_with_non_palindromic_strings():
    # examples of non-palindromic strings that should be rejected
    assert is_palindrome('AB') is False  # even length
    assert is_palindrome('ABC') is False  # odd length
    assert is_palindrome('AAB') is False
    assert is_palindrome('AABB') is False
    assert is_palindrome('AAABB') is False
    assert is_palindrome('AAABBB') is False
    assert is_palindrome('ABCZBA') is False
    assert is_palindrome('ABCCZA') is False
    assert is_palindrome('ABCCBZ') is False
    assert is_palindrome('ABCDZCBA') is False
    assert is_palindrome('ABCDDZBA') is False
    assert is_palindrome('ABCDDCZA') is False
    assert is_palindrome('ABCDDCBZ') is False
    assert is_palindrome('AAAAZAAA') is False
    assert is_palindrome('AAAAAAAZ') is False