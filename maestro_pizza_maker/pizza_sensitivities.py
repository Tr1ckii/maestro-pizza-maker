# The maestro pizza maker wants to fully understand of the properties of his pizza menu.
# Therefore he defines the follwing variables in the pizza industry known as "pizza sensitivities":
# 1. menu_sensitivity_protein - represents the rate of change between the price of the pizza and the amount of protein in the pizza
# 2. menu_sensitivity_carbs - represents the rate of change between the price of the pizza and the amount of carbohydrates in the pizza
# 3. menu_sensitivity_fat - represents the rate of change between the price of the pizza and the amount of average_fat in the pizza

# TODO: implement above mentioned sensitivities
# hint: simple linear regression might be helpful

from maestro_pizza_maker.pizza_menu import PizzaMenu
import numpy as np


def menu_sensitivity_protein(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    df_menu = menu.to_dataframe(sort_by="price",descendent=True)

    cov = df_menu[["protein","price"]].cov()["protein"].iloc[0]
    var = df_menu["protein"].var(ddof = 0)
    sensitivty = cov / var



    return sensitivty


def menu_sensitivity_carbs(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    df_menu = menu.to_dataframe(sort_by="price",descendent=True)

    cov = df_menu[["carbohydrates","price"]].cov()["carbohydrates"].iloc[0]
    var = df_menu["carbohydrates"].var(ddof = 0)
    sensitivty = cov / var



    return sensitivty


def menu_sensitivity_fat(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    df_menu = menu.to_dataframe(sort_by="price",descendent=True)

    cov = df_menu[["average_fat","price"]].cov()["average_fat"].iloc[0]
    var = df_menu["average_fat"].var(ddof = 0)
    sensitivty = cov / var



    return sensitivty

