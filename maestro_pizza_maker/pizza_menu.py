# class representing the pizza menu

from dataclasses import dataclass
from typing import List

import numpy as np
import pandas as pd

from maestro_pizza_maker.pizza import Pizza


@dataclass
class PizzaMenu:
    pizzas: List[Pizza]

    def to_dataframe(self, sort_by: str, descendent: bool) -> pd.DataFrame:
        # TODO: transform the list of pizzas into a pandas dataframe, where each row represents a pizza
        # and it contains the following columns: name, price, protein, average_fat, carbohydrates, calories and ingredients
        # where ingredients is a list of ingredients.
        # The dataframe should be sorted by the column specified by the sort_by parameter
        # and the order of sorting should be specified by the descendent parameter
        # (descendent=True means that the dataframe should be sorted in a descendent order)
        #
        # Example:
        #
        # pizza_menu = PizzaMenu(pizzas=[Pizza(sauce=PizzaIngredients.CREAM_SAUCE, dough=PizzaIngredients.CLASSIC_DOUGH)])
        # pizza_menu.to_dataframe(sort_by="price", descendent=True)
        #
        # should return a dataframe with a single row and the following columns:
        # name, price, protein, average_fat, carbohydrates, calories, ingredients
        # where the name column contains the name of the pizza, price contains the price of the pizza,
        # protein contains the protein content of the pizza, average_fat contains the average_fat content of the pizza,
        # carbohydrates contains the carbohydrates content of the pizza, calories contains the calories content of the pizza
        # and ingredients contains a list of ingredients that the pizza contains
        #
        # The dataframe should be sorted by the price column in a descendent order

        data = []
        for pizza in self.pizzas:
            data.append([
                pizza.name,
                pizza.price,
                pizza.protein,
                pizza.average_fat,
                pizza.carbohydrates,
                pizza.calories,
                pizza.ingredients
            ])
        columns = [
            "name",
            "price",
            "protein",
            "average_fat",
            "carbohydrates",
            "calories",
            "ingredients"
        ]
        df = pd.DataFrame(data, columns=columns)

        # Sort the dataframe by the specified column in the specified order
        df = df.sort_values(by=sort_by, ascending=descendent)

        return df

    @property
    def cheapest_pizza(self) -> Pizza:
        # TODO: return the cheapest pizza from the menu
        df = self.to_dataframe(sort_by="price", descendent=True)
        name = df["name"].iloc[0]
        for pizza in self.pizzas:
            if name == pizza.name:
                cheapest_pizza_ = pizza

        return cheapest_pizza_
    @property
    def most_caloric_pizza(self) -> Pizza:
        # TODO: return the most caloric pizza from the menu
        df = self.to_dataframe(sort_by="calories", descendent=False)
        name = df["name"].iloc[0]
        for pizza in self.pizzas:
            if name == pizza.name:
                fattest_pizza_ = pizza

        return fattest_pizza_



    def get_most_fat_pizza(self, quantile: float = 0.5) -> Pizza:
        # TODO: return the most fat pizza from the menu
        # consider the fact that fat is random and it is not always the same, so you should return the pizza that has the most fat in the quantile of cases specified by the quantile parameter
        fat_data = []
        columns = [
            "pizza",
            "fat"
        ]
        for pizza in self.pizzas:
           fat_data.append([
               pizza,
               np.quantile(pizza.fat,quantile)
           ])

        fat_df = pd.DataFrame(fat_data,columns=columns).sort_values(by="fat", ascending=True)

        fattest_pizza = fat_df["pizza"].iloc[0]
        for pizza in self.pizzas:
            if fattest_pizza == pizza:
                fattest_pizza_ = pizza

        return fattest_pizza_



    def add_pizza(self, pizza: Pizza) -> None:
        # TODO: code a function that adds a pizza to the menu
        self.pizzas.append(pizza)

    def remove_pizza(self, pizza: Pizza) -> None:
        # TODO: code a function that removes a pizza from the menu
        # do not forget to check if the pizza is actually in the menu
        # if it is not in the menu, raise a ValueError
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        else:
            raise ValueError("Hey, we don't have that Pizza in the menu")


    def __len__(self) -> int:
        # TODO: return the number of pizzas in the menu
        return len(self.pizzas)

