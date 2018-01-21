from doubly_linked_list import *
import pytest

ll = Linked_list()
full_ll = Linked_list(['A', 'B', 'C', 'D'])

def test_append_empty_ll():
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
    assert ll.size == 2

def test_find_item_exist():
    assert full_ll.size == 4
    assert full_ll.find(lambda item: item == 'A').data == 'A'
    assert full_ll.find(lambda item: item == 'B').data == 'B'
    assert full_ll.find(lambda item: item == 'C').data == 'C'
    assert full_ll.find(lambda item: item == 'D').data == 'D'
    full_ll.append('E')
    assert full_ll.size == 5
    assert full_ll.find(lambda item: item == 'E').data == 'E'

def test_find_item_does_not_exist():
    assert full_ll.find(lambda item: item == 'z') == None

def test_delete_with_items():
    full_ll_2 = Linked_list(['A', 'B', 'C', 'D'])
    assert full_ll_2.size == 4
    full_ll_2.delete('A')
    assert full_ll_2.size == 3
    assert full_ll_2.head.data == 'B'
    assert full_ll_2.head.next.data == 'C'
    assert full_ll_2.tail.data == 'D'