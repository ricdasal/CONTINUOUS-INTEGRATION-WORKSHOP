
import pytest
from dining_experience_manager import DiningExperienceManager

@pytest.fixture
def manager():
    return DiningExperienceManager()

def test_valid_quantity_input(manager, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")  # Mock user input to "3"
    quantity = manager.get_valid_quantity("Chinese Food")
    assert quantity == 3

# Prueba la función get_valid_quantity
# def test_get_valid_quantity_positive():
#     manager = DiningExperienceManager()
#     quantity = manager.get_valid_quantity("Chinese Food")
#     assert quantity >= 0

def test_get_valid_quantity_zero():
    manager = DiningExperienceManager()
    quantity = manager.get_valid_quantity("Italian Food")
    assert quantity == 0

def test_get_valid_quantity_negative_then_positive():
    manager = DiningExperienceManager()
    with pytest.raises(ValueError):
        manager.get_valid_quantity("Pastries")
    quantity = manager.get_valid_quantity("Pastries")
    assert quantity >= 0

def test_get_valid_quantity_out_of_range():
    manager = DiningExperienceManager()
    with pytest.raises(ValueError):
        manager.get_valid_quantity("Chef's Specials")
        
# Prueba la función calculate_total_cost
def test_calculate_total_cost_no_discount():
    manager = DiningExperienceManager()
    order = {'Chinese Food': 2, 'Italian Food': 1}
    total_cost = manager.calculate_total_cost(order)
    assert total_cost == 26  # 8*2 + 10*1

def test_calculate_total_cost_base_discount():
    manager = DiningExperienceManager()
    order = {'Chinese Food': 10, 'Pastries': 1}
    total_cost = manager.calculate_total_cost(order)
    assert total_cost == 82  # (8*10 + 5*1) - 10

def test_calculate_total_cost_large_order_discount():
    manager = DiningExperienceManager()
    order = {'Italian Food': 6, "Chef's Specials": 2}
    total_cost = manager.calculate_total_cost(order)
    assert total_cost == 94.5  # (10*6) + (12*2*1.05) - 25

def test_calculate_total_cost_quantity_discount():
    manager = DiningExperienceManager()
    order = {'Pastries': 7, 'Chef\'s Specials': 4}
    total_cost = manager.calculate_total_cost(order)
    assert total_cost == 38.25  # (5*7*0.9) + (12*4*1.05)

# Prueba la función run
def test_run_no_order():
    manager = DiningExperienceManager()
    manager.get_order = lambda: {}
    total_cost = manager.run()
    assert total_cost == -1

def test_run_with_order():
    manager = DiningExperienceManager()
    manager.get_order = lambda: {'Chinese Food': 2, 'Italian Food': 1}
    total_cost = manager.run()
    assert total_cost == 26

def test_run_order_confirmation():
    manager = DiningExperienceManager()
    manager.get_order = lambda: {'Chinese Food': 2, 'Italian Food': 1}
    assert manager.run() != -1