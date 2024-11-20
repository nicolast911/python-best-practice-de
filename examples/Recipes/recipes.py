from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Recipe:
    name: str
    ingredients: list[str]
    instructions: str
    rating: Optional[int] = None


@dataclass
class RecipeBook:
    recipes: list[Recipe] = field(default_factory=list)

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def get_recipe_by_name(self, name: str) -> Recipe:
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        raise KeyError(f"recipe {name} not found!")

    def get_recipes_with_ingredient(self, ingredient: str) -> list[Recipe]:
        result = []
        for recipe in self.recipes:
            if ingredient in recipe.ingredients:
                result.append(recipe)
        return result

    def get_recipes_by_rating(self, rating: int) -> list[Recipe]:
        result = []
        for recipe in self.recipes:
            if recipe.rating == rating:
                result.append(recipe)
        return result

    def get_recipes_above_rating(self, min_rating: int) -> list[Recipe]:
        result = []
        for recipe in self.recipes:
            if recipe.rating is None or recipe.rating >= min_rating:
                result.append(recipe)
        return result