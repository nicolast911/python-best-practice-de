from recipes import Recipe, RecipeBook
import pytest


@pytest.fixture
def recipe1():
    return Recipe(
        "My Recipe",
        ["ingredient 1", "my ingredient 2"],
        "Instructions\n...",
        4
    )


@pytest.fixture
def recipe2():
    return Recipe(
        "Your Recipe",
        ["ingredient 1", "your ingredient 2"],
        "Instructions\n...",
        5
    )


@pytest.fixture
def recipe_book(recipe1, recipe2):
    return RecipeBook(
        [recipe1, recipe2],
    )


def test_add_recipe(recipe1):
    recipe_book = RecipeBook()
    recipe_book.add_recipe(recipe1)
    assert recipe_book.recipes == [recipe1]


def test_get_recipe_by_name(recipe1, recipe2, recipe_book):
    assert recipe_book.get_recipe_by_name("My Recipe") == recipe1
    assert recipe_book.get_recipe_by_name("Your Recipe") == recipe2

    with pytest.raises(KeyError):
        recipe_book.get_recipe_by_name("nonexistent")


def test_get_recipes_with_ingredient(recipe1, recipe2, recipe_book):
    assert recipe_book.get_recipes_with_ingredient("ingredient 1") == [recipe1, recipe2]
    assert recipe_book.get_recipes_with_ingredient("my ingredient 2") == [recipe1]
    assert recipe_book.get_recipes_with_ingredient("nonexistent") == []


def test_get_recipes_by_rating(recipe1, recipe2, recipe_book):
    assert recipe_book.get_recipes_by_rating(4) == [recipe1]
    assert recipe_book.get_recipes_by_rating(5) == [recipe2]
    assert recipe_book.get_recipes_by_rating(3) == []


def test_get_recipes_above_rating(recipe1, recipe2, recipe_book):
    assert recipe_book.get_recipes_above_rating(3) == [recipe1, recipe2]
    assert recipe_book.get_recipes_above_rating(4) == [recipe1, recipe2]
    assert recipe_book.get_recipes_above_rating(5) == [recipe2]
    assert recipe_book.get_recipes_above_rating(6) == []
