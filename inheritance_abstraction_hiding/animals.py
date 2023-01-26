from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, age: int, size: str, health: int, attack: int, speed: int, intelligence: int, blood: str):
        self._age = age
        self._size = size
        self._health = health
        self._attack = attack
        self._speed = speed
        self._intelligence = intelligence
        self._blood = blood

    @abstractmethod
    def feed(self):
        pass

    def fight(self, cls):
        """
        This class moddiling battle via compare class attributes
        :param cls: class to compare
        :return: result of the battle
        """
        if cls._health < self._attack > cls._attack:  # своя більше атаки ворога, але менже ніж здоров‘я ворога
            print(f"You deal {self._attack} damage")
        elif self._attack > cls._attack and cls._health:  # cвоя атака більше за атаку ворога + здоров‘є ворога
            print(f"Target is dead!")
        elif self._attack and self._health < cls._attack:  # cвоя атака та здоров‘я менше за атаку ворога
            print(f"You are dead!")
        else:
            damage = self._health and self._attack > cls._attack  # своя атака та здоров‘я менше за атаку ворога
            print(f"You get: {damage} damage")

    def avoid(self, cls):
        """
        This class moddiling avoiding via compare class attributes
        :param cls: class to compare
        :return: result of hiding or call method fight
        """
        if self._speed > cls._speed:
            print("Sucsess avoid battle!")
        else:
            self.fight(cls)
