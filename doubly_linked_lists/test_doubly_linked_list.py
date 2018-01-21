from doubly_linked_list import *
import pytest

def test_append_empty_ll():
    ll = Linked_list()
    ll.append('A')
    assert ll.size == 1
    assert ll.head.data == 'A'
    assert ll.tail.data == 'A'

def test_append_ll_with_items():
    ll = Linked_list(['A'])
    assert ll.size == 1
    assert ll.head.data == 'A'
    assert ll.tail.data == 'A'
    ll.append('B')
    assert ll.head.data == 'A'
    assert ll.tail.data == 'B'
    assert ll.head.previous == None
    assert ll.tail.previous.data == 'A'
