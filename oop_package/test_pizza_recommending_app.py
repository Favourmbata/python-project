import unittest
from oop_package.Pizza_recommending_app import Pizza_recommending_app
from oop_package.Pizza_recommending_app import pizza_app


class TestforLargepizzaBox(unittest.TestCase):
    def setUp(self):
        self.pizzaBox = Pizza_recommending_app
        self.pizza = pizza_app()

    def test_for_large_pizza_box(self):
        pizza = self.pizzaBox.large_pizza_app()
        self.assertEqual(5000, pizza.get_pizza_size_price())

    def test_for_medium_pizza(self):
        pizza = self.pizzaBox.medium_pizza_app()
        self.assertEqual(3000, pizza.get_pizza_size_price())

    def test_for_small_pizza(self):
        pizza = self.pizzaBox.small_pizza_app()
        self.assertEqual(1200, pizza.get_pizza_size_price())
