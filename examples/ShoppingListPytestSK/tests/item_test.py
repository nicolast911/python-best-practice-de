from shopping_list_pytest_sk.shopping_list import ShoppingListItem, ShoppingList

import pytest

@pytest.fixture
def shopping_list():
    return ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")])  


def test_shopping_list(shopping_list):
    # Arrange
    item1 = ShoppingListItem("Brot", "1")  # Ensure amount is a string
    item2 = ShoppingListItem("Apfel", "4") 

    # Act

    # Assert
    assert shopping_list.items[0] == item1
    assert shopping_list.items[1] == item2

def test_string_output(shopping_list):
    # Arrange


    # Act & Assert
    assert str(shopping_list) == "Shopping List\n  Brot (1)\n  Apfel (4)\n"

def test_len():
    # Arrange
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")]) 

    # Act & Assert
    assert len(sl) == 2

def test_find_item():
    # Arrange
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")]) 

    # Assert
    assert sl.find_by_product_name("Brot") == ShoppingListItem("Brot", "1")
    assert sl.find_by_product_name("Banane") == None  #  Eher auslagern, da 2x Act

def test_add_item():
    # Arrange
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")]) 
    item3 = ShoppingListItem("Milch", "2") 

    # Act
    sl.add_item(item3)

    # Assert
    assert sl.find_by_product_name("Milch") == ShoppingListItem("Milch", "2")