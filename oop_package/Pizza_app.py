class pizza_app:
    def __init__(self):
        self.pizza_size = ""
        self.pizza_slices = 0
        self.pizza_size_price = 0

    def get_pizza_size(self):
        return self.pizza_size

    def set_pizza_slices(self, pizza_slices):
        self.pizza_slices = pizza_slices

    def get_pizza_slices(self):
        return self.pizza_slices

    def set_pizza_size_price(self, pizza_size_price):
        self.pizza_size_price = pizza_size_price

    def get_pizza_size_price(self):
        return self.pizza_size_price

    def set_pizza_size(self, pizza_size):
        self.pizza_size = pizza_size
