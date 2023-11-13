from oop_package.Pizza_app import pizza_app
from oop_package import Pizza_prediction

class pizza_prediction:
    def __init__(self):
        pass


class Pizza_recommending_app:
    def __init__(self):
        self.pizza = pizza_app()
        self.hungry_people = 2
        self.super_hungry_people = 4
        self.classic_people = 1

    def medium_pizza_app(self):
        self.pizza.set_pizza_slices(6)
        self.pizza.set_pizza_size_price(3000)
        self.pizza.set_pizza_size("medium")
        return self.pizza

    def large_pizza_app(self):
        self.pizza.set_pizza_slices(10)
        self.pizza.set_pizza_size_price(5000)
        self.pizza.set_pizza_size("large")
        return self.pizza

    def small_pizza_app(self):
        self.pizza.set_pizza_slices(2)
        self.pizza.set_pizza_size_price(1200)
        self.pizza.set_pizza_size("small")
        return self.pizza

    def pizza_prediction_hungry_people_pizza_box_calculator(self):
        Pizza_prediction.pizza_prediction
