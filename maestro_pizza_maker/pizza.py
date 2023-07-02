# class representing a pizza

from dataclasses import dataclass
from typing import List, Literal, Optional

from maestro_pizza_maker.ingredients import PizzaIngredients
import numpy as np
import random

@dataclass
class Pizza:
    dough: Literal[
        PizzaIngredients.CLASSIC_DOUGH,
        PizzaIngredients.THIN_DOUGH,
        PizzaIngredients.WHOLEMEAL_DOUGH,
    ]
    sauce: Literal[PizzaIngredients.TOMATO_SAUCE, PizzaIngredients.CREAM_SAUCE]
    cheese: Optional[
        List[
            Literal[
                PizzaIngredients.MOZZARELA,
                PizzaIngredients.CHEDDAR,
                PizzaIngredients.PARMESAN,
            ]
        ]
    ] = None
    fruits: Optional[
        List[Literal[PizzaIngredients.PINEAPPLE, PizzaIngredients.APPLE]]
    ] = None
    meat: Optional[
        List[
            Literal[
                PizzaIngredients.HAM, PizzaIngredients.BACON, PizzaIngredients.SAUSAGE
            ]
        ]
    ] = None
    vegetables: Optional[
        List[
            Literal[
                PizzaIngredients.MUSHROOMS,
                PizzaIngredients.ONIONS,
                PizzaIngredients.PEPPER,
            ]
        ]
    ] = None

    def __post_init__(self) -> None:
        if self.cheese is None:
            self.cheese = []
        if self.fruits is None:
            self.fruits = []
        if self.meat is None:
            self.meat = []
        if self.vegetables is None:
            self.vegetables = []
        self.ingredients = [
            self.dough,
            self.sauce,
            *self.cheese,
            *self.fruits,
            *self.meat,
            *self.vegetables,
        ]

    @property
    def price(self) -> float:
        return sum(ingredient.value.price for ingredient in self.ingredients)

    @property
    def protein(self) -> float:
        return sum(ingredient.value.protein for ingredient in self.ingredients)

    @property
    def fat(self) -> np.array:
        return np.sum(ingredient.value.fat for ingredient in self.ingredients)

    @property
    def average_fat(self) -> float:
        # TODO: implement average fat calculation
        # HINT: check the `PizzaIngredients` class properly, you will find a `fat` property there which is a numpy array representing the drawings from the fat distribution
        # since fat is a random variable, we will calculate the average fat of the pizza by averaging the fat vectors of the ingredients
        return np.average([ingredient.value.fat for ingredient in self.ingredients])

    @property
    def carbohydrates(self) -> float:
        return sum(ingredient.value.carbohydrates for ingredient in self.ingredients)

    @property
    def calories(self) -> float:
        return sum(ingredient.value.calories for ingredient in self.ingredients)

    @property
    def name(self) -> str:
        # TODO: implement name generation, it is purely up to you how you want to do it
        # (you can use random, you can use some kind of algorithm) - just make sure that
        # the name is unique.
        names = [PizzaIngredients.name for PizzaIngredients in self.ingredients]

        pizza_name = "Pizza"
        for name in names:
            pizza_name +=  " " + name

        return pizza_name

    @property
    def taste(self) -> np.array:
        # TODO: implement taste function
        # The famous fact that taste is subjective is not true in this case. We believe that fat is the most important factor, since fat carries the most flavor.
        # So we will use the fat vector to calculate the taste of the pizza with the following formula:
        # taste = 0.05 * fat_dough + 0.2 * fat_sauce + 0.3 * fat_cheese + 0.1 * fat_fruits + 0.3 * fat_meat + 0.05 * fat_vegetables
        fat_dough = self.dough.value.fat
        fat_sauce = self.sauce.value.fat
        fat_cheese = np.sum([cheese.value.fat for cheese in self.cheese])
        fat_fruits = np.sum([fruit.value.fat for fruit in self.fruits])
        fat_meat = np.sum([meat.value.fat for meat in self.meat])
        fat_vegetables = np.sum([vegetable.value.fat for vegetable in self.vegetables])

        taste = np.array([
                0.05 * fat_dough
                + 0.2 * fat_sauce
                + 0.3 * fat_cheese
                + 0.1 * fat_fruits
                + 0.3 * fat_meat
                + 0.05 * fat_vegetables
                ]
        )

        return taste


