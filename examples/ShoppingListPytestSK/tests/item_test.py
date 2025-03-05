from shopping_list_pytest_sk.shopping_list import ShoppingListItem, ShoppingList

def test_shopping_list():
    # Arrange
    item1 = ShoppingListItem("Brot", "1")  # Ensure amount is a string
    item2 = ShoppingListItem("Apfel", "4") 

    # Act
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")])  

    # Assert
    assert sl.items[0] == item1
    assert sl.items[1] == item2

def test_string_output():
    # Arrange & Act
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")]) 

    # Assert
    assert str(sl) == "Shopping List\n  Brot (1)\n  Apfel (4)\n"

def test_len():
    # Arrange & Act
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")]) 

    # Assert
    assert len(sl) == 2

def test_find_item():
    # Arrange & Act
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")]) 

    # Assert
    assert sl.find_by_product_name("Brot") == ShoppingListItem("Brot", "1")
    assert sl.find_by_product_name("Banane") == None

def test_add_item():
    # Arrange
    sl = ShoppingList.from_item_values([("Brot", "1"), ("Apfel", "4")]) 
    item3 = ShoppingListItem("Milch", "2") 

    # Act
    sl.add_item(item3)

    # Assert
    assert sl.find_by_product_name("Milch") == ShoppingListItem("Milch", "2")