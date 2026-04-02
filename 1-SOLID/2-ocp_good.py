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

# Specification
class Specification:
    def is_satisfied(self, item):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs
    
    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.specs)

class OrSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs
    
    def is_satisfied(self, item):
        return any(spec.is_satisfied(item) for spec in self.specs)

# Filter
class Filter:
    def filter(self, items, spec):
        pass

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.RED, Size.SMALL)
    berry = Product("Blue berry", Color.BLUE, Size.MEDIUM)
    mango = Product("Mango", Color.GREEN, Size.LARGE)

    products = [apple, berry, mango]

    bf = BetterFilter()

    print("Green products: ")
    green = ColorSpecification(Color.GREEN)

    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print("Large products: ")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print("Medium and blue products: ")
    medium = SizeSpecification(Size.MEDIUM)
    blue = ColorSpecification(Color.BLUE)
    medium_and_blue = AndSpecification(medium, blue)
    for p in bf.filter(products, medium_and_blue):
        print(f' - {p.name} is medium and blue')
