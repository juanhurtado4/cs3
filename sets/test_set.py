from sets import Set
import pytest

def test_union_sets_with_items():
    set1 = Set(['A'])
    set2 = Set(['B'])
    set3 = set1.union(set2)
    assert set3.contains('A')
    assert set3.contains('B')

def test_is_subset_when_true():
    set1 = Set(['A', 'B', 'C', 'D'])
    set2 = Set(['B', 'C'])
    assert set1.is_subset(set2) == True