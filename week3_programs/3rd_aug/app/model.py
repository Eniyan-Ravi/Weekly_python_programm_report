#model

class Game:

    def __init__(self, id, name, genre, developer, description, rating, price):
        self.id = id
        self.name = name
        self.genre = genre
        self.developer = developer
        self.description = description
        self.rating = rating
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre,
            "developer": self.developer,
            "description": self.description,
            "rating": self.rating,
            "price": self.price
        }