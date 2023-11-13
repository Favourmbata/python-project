
class pizza_prediction:
    def __init__(self):
        self.number_of_boxes_to_get = 0
        self.number_of_slices_remaining = 0
        self.total_price = 0

    def __set__number_of_boxes_to_get(self, number_of_boxes_to_get):
        self.number_of_boxes_to_get = number_of_boxes_to_get

    def __get__number_of_boxes_to_get(self):
        return self.number_of_boxes_to_get

    def __set__number_of_slices_remaining(self, number_of_slices_remaining):
        self.number_of_slices_remaining = number_of_slices_remaining

    def __get__number_of_slices_remaining(self):
        return self.number_of_slices_remaining

    def __set__total_price(self, total_price):
        self.total_price = total_price

    def __get__total_price(self):
        return self.total_price
