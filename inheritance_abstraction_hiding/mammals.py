from inheritance_abstraction_hiding.animals import Animals


# це метод Mammals він наслідується від абстрактного метода Animals
class Mammals(Animals):

    def __init__(self, age: int, size: str, health: int, attack: int, speed: int, intelligence: int, blood: str):
        super().__init__(age, size, health, attack, speed, intelligence, blood)
        self.wool = True
        self.feeding = "Milk"

    def my_type(self):
        print('Animal created!')

    #це метод фід, чайлди його перевизначать і це буде прикладом поліморфізму
    def feed(self):
        print('Im eating')
