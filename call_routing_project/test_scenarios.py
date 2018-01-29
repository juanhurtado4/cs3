from scenario1 import get_cost
import pytest

def test_scenario1_cost_is_0():
    assert get_cost('+15124156620', 'carrier_route1.txt') == 0

def test_scenario1_cost_is_001():
    assert get_cost('+1941613', 'carrier_route1.txt') == 0.05

