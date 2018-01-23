from stack import Stack
import pytest

def test_init():
    s = Stack()
    assert s.peek() is None
    assert s.length() == 0
    assert s.is_empty() is True

def test_init_with_list():
    s = Stack(['A', 'B', 'C'])
    assert s.peek() == 'C'
    assert s.length() == 3
    assert s.is_empty() is False

def test_length():
    s = Stack()
    assert s.length() == 0
    s.push('A')
    assert s.length() == 1
    s.push('B')
    assert s.length() == 2
    s.pop()
    assert s.length() == 1
    s.pop()
    assert s.length() == 0

def test_push():
    s = Stack()
    s.push('A')
    assert s.peek() == 'A'
    assert s.length() == 1
    s.push('B')
    assert s.peek() == 'B'
    assert s.length() == 2
    s.push('C')
    assert s.peek() == 'C'
    assert s.length() == 3
    assert s.is_empty() is False

def test_peek():
    s = Stack()
    assert s.peek() is None
    s.push('A')
    assert s.peek() == 'A'
    s.push('B')
    assert s.peek() == 'B'
    s.pop()
    assert s.peek() == 'A'
    s.pop()
    assert s.peek() is None

def test_pop():
    s = Stack(['A', 'B', 'C'])
    assert s.pop() == 'C'
    assert s.length() == 2
    assert s.pop() == 'B'
    assert s.length() == 1
    assert s.pop() == 'A'
    assert s.length() == 0
    assert s.is_empty() is True