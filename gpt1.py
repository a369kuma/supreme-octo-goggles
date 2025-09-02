class Book:
    def __init__(self, title = str, author = str, price = float):
        self.title = title
        self.author = author
        self.price = price

    def apply_coupon(self, discount):
        self.price -= discount

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, price: {self.price}")