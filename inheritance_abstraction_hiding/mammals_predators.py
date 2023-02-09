from inheritance_abstraction_hiding.mammals import Mammals


# це метод Predators він наслідується від метода Mammals
class Perdators(Mammals):
    def __init__(self, age: int, size: str, health: int, attack: int, speed: int, intelligence: int, blood: str):
        super().__init__(age, size, health, attack, speed, intelligence, blood)
        self.__talons = True

    def __str__(self):
        return f"Age: {self._age}\n Size: {self._size}\n health: {self._health}\n Attack: {self._attack}\n Speed: {self._speed}\n " \
               f"Intelligence: {self._intelligence}\n Blood: {self._blood}\n Wool: {self.wool}\n Feeding: {self.feeding}\n Wings: {self.__talons}\n"

    def my_type(self):
        print('Monkey created!')

    # це метод фід, цей метод є в батьківькому класі, тут ми його перевизначаємо та додаємо нових властивостей
    def feed(self):
        health = self._health + 20
        print(f"I eat meat and restore {health}")
