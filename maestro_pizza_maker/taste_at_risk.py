# The maestro pizza maker is aware of the fact that the fat content of the ingredients is random and it is not always the same.
# Since fat is the most important factor in taste, the maestro pizza maker wants to know how risky his pizza menu is.

# TODO: define 2 risk measures for the pizza menu and implement them (1 - Taste at Risk (TaR), 2 - Conditional Taste at Risk (CTaR), also known as Expected Shorttaste (ES)

from maestro_pizza_maker.pizza import Pizza
from maestro_pizza_maker.pizza_menu import PizzaMenu
import numpy as np
import statistics as st


def taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    # TODO: implement the taste at risk measure for a pizza
    # quantile is the quantile that we want to consider
    # Hint: Similarity between the Taste at Risk and the Value at Risk is not a coincidence or is it?
    # Hint: Use function taste from Pizza class, but be aware that the higher the taste, the better -> the lower the taste, the worse
    taste_values = pizza.taste
    reversed_taste_values =  - np.sort(-taste_values)# Reverse the taste values
    mean = np.mean(reversed_taste_values)  # Estimate the mean of taste values
    std_dev = np.std(reversed_taste_values)  # Estimate the standard deviation of taste values

    quantile_ = np.quantile(reversed_taste_values,quantile)#Calculate the z-score corresponding to the quantile

    z_score = quantile = (quantile_-mean)/std_dev

    var = mean - (z_score * std_dev)

    return var


def taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    # TODO: implement the taste at risk measure for a menu
    # quantile is the quantile that we want to consider
    # Hint: the taste of the whole menu is the sum of the taste of all pizzas in the menu, or? ;)

    # Calculate the tastes of all pizzas in the menu

    # Extract taste values of the pizzas in the menu

    taste_values = np.zeros(shape=(menu.__len__(),len(menu.pizzas[0].fat)))
    lst = [pizza.taste for pizza in menu.pizzas]
    for lst_i in lst:
        lst_i.sort()

    for i in range(0,menu.__len__()):
        taste_values[i]= lst[i]
    # Compute the covariance matrix of taste values
    taste_values_sum =np.sum(np.mean(taste_values,axis=1))

    covariance_matrix = np.cov(taste_values, rowvar=False)

    # Calculate the variance of taste values for each pizza
    taste_values_var = np.sum(np.diagonal(covariance_matrix))

    # Calculate the covariance of taste values between pizzas
    covariance_sum = np.sum(covariance_matrix) - taste_values_var

    # Calculate the standard deviation of the menu
    menu_std_dev = np.sqrt(taste_values_var + 2 * covariance_sum)

    # Sort the taste values in ascending order
    sorted_taste = np.sort(taste_values)

    # Calculate the Taste at Risk at the desired quantile
    confidence = np.quantile(sorted_taste, quantile)

    z_score = (confidence-taste_values_sum)/menu_std_dev

    menu_tar = taste_values_sum -z_score * menu_std_dev

    return menu_tar




def conditional_taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    # TODO: implement the conditional taste at risk measure for a pizza
    # quantile is the quantile that we want to consider
    # Hint: Simmilarity between the Conditional Taste at Risk and the Conditional Value at Risk is not a coincidence or is it?
    taste = pizza.taste

    # Sort the taste values in descending order (higher taste is better)
    sorted_taste = np.sort(taste)[::-1]

    # Determine the index corresponding to the quantile
    index = int(quantile * len(sorted_taste[0]))

    # Calculate the conditional taste at risk
    conditional_taste_at_risk = np.mean(sorted_taste[0:index])

    return conditional_taste_at_risk


def conditional_taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    # TODO: implement the conditional taste at risk measure for a menu
    # Hint: the taste of the whole menu is the sum of the taste of all pizzas in the menu, or? ;) (same as for the taste at risk)
    # Calculate the tastes of all pizzas in the menu

    # Extract taste values of the pizzas in the menu

    taste_values = np.zeros(shape=(menu.__len__(), len(menu.pizzas[0].fat)))
    lst = [pizza.taste for pizza in menu.pizzas]
    for lst_i in lst:
        lst_i.sort()
    for i in range(0, menu.__len__()):
        taste_values[i] = lst[i]

    quantile_arr = np.linspace(0,quantile,num=100)
    tvar_arr = []
    for alpha in quantile_arr:
        tvar_arr.append(taste_at_risk_menu(menu,alpha))

    tvar = np.mean(tvar_arr)


    return tvar