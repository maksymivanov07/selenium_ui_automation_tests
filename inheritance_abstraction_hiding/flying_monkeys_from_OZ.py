from inheritance_abstraction_hiding.mammals_bats import Bats
from inheritance_abstraction_hiding.mammals_primates import Primates


class FlyingMonkey(Primates, Bats):
    def __init__(self, age: int, size: str, health: int, attack: int, speed: int, intelligence: int, blood: str):
        Bats.__init__(self, age, size, health, attack, speed, intelligence, blood)
        Primates.__init__(self, age, size, health, attack, speed, intelligence, blood)

