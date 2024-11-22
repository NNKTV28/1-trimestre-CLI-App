class Game:
    def __init__(self, name, genre, price, rating, available):
        self.name = name
        self.genre = genre
        self.price = price
        self.rating = rating
        self.available = available

    def __str__(self):
        return f"{self.name}|{self.genre}|{self.price}|{self.rating}|{self.available}"