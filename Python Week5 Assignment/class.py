class ShoeBrand:
    pass

class Sneaker(ShoeBrand):
    def __init__(self, brand, style):
        self.brand = brand
        self.style = style

    def display_info(self):
        return f"{self.brand} - {self.style}"
    

shoe1 = Sneaker("Nike", "Airmax")
print(shoe1.display_info())

shoe2 = Sneaker("Adidas", "Yeezy")
print(shoe2.display_info())
