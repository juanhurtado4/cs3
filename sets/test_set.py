from sets import Set
import pytest

# TODO: Implement False test for each method
def test_union_sets_with_items():
    set1 = Set(['A', 'B', 'C'])
    set2 = Set(['B', 'C', 'D'])
    set3 = set1.union(set2)
    assert set3.contains('A')
    assert set3.contains('B')
    assert set3.contains('C')
    assert set3.contains('D')
    assert set3.size == 4

def test_is_subset_when_true():
    set1 = Set(['A', 'B', 'C', 'D'])
    set2 = Set(['B', 'C'])
    assert set1.is_subset(set2) == True

def test_difference_with_items():
    set1 = Set(['A', 'B', 'C', 'D'])
    set2 = Set(['A', 'B', 'C', 'D', 'E'])
    set3 = set1.difference(set2)
    assert set3.size == 1
    assert set3.contains('E') == True