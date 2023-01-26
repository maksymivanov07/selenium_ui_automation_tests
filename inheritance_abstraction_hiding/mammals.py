from inheritance_abstraction_hiding.animals import Animals


class Mammals(Animals):

    def __init__(self, age: int, size: str, health: int, attack: int, speed: int, intelligence: int, blood: str):
        super().__init__(age, size, health, attack, speed, intelligence, blood)
        self.wool = True
        self.feeding = "Milk"

    def my_type(self):
        print('Animal created!')

    def feed(self):
        print('Im eating')
