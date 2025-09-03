class Book:
    def __init__(self, title = str, author = str, price = float):
        self.title = title
        self.author = author
        self.price = price

    def apply_coupon(self, discount):
        self.price -= discount

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, price: {self.price}")

class EBook:
    def __init__(self, title = str, author = str, price = float, file_size = float):
        self.title = title
        self.author = author
        self.price = price
        self.file_size = file_size

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, price: {self.price}, File Size: {self.file_size}MB")

class AudioBook:
    def __init__(self, title = str, author = str, price = float, duration = float):
        self.title = title
        self.author = author
        self.price = price
        self.duration = duration

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, price: {self.price}, Duration: {self.duration} hours")