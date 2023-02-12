from inheritance_abstraction_hiding.mammals import Mammals


# це метод Bats він наслідується від метода Mammals
class Bats(Mammals):
    def __init__(self, age: int, size: str, health: int, attack: int, speed: int, intelligence: int, blood: str):
        super().__init__(age, size, health, attack, speed, intelligence, blood)
        self.__wings = True

    def __str__(self):
        return f"Age: {self._age}\n Size: {self._size}\n health: {self._health}\n Attack: {self._attack}\n Speed: {self._speed}\n " \
               f"Intelligence: {self._intelligence}\n Blood: {self._blood}\n Wool: {self.wool}\n Feeding: {self.feeding}\n Wings: {self.__wings}\n"

    # цей метод буде використовуватись в якосьі приклада множинного наслідування
    def flying(self):
        print('I am flying')

    # це метод фід, цей метод є в батьківькому класі, тут ми його перевизначаємо та додаємо нових властивостей
    def feed(self):
        health = self._health + 10
        print(f"I eat bugs and restore {health}")
