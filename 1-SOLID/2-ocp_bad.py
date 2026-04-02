# Open close principle
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p
    
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p
    
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p

if __name__ == "__main__":
    apple = Product("Apple", Color.RED, Size.SMALL)
    berry = Product("Blue berry", Color.BLUE, Size.MEDIUM)
    mango = Product("Mango", Color.GREEN, Size.LARGE)

    products = [apple, berry, mango]

    filter = ProductFilter()
    
    print("Small products: ")
    for p in filter.filter_by_size(products, Size.SMALL):
        print(f' - {p.name}')
