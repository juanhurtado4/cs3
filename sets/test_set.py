from sets import Set
import pytest

def test_union_sets_with_items():
    set1 = Set(['A'])
    set2 = Set(['B'])
    set3 = set1.union(set2)
    assert set3.contains('A')
    assert set3.contains('B')

