from inheritance_abstraction_hiding.flying_monkeys_from_OZ import FlyingMonkey
from inheritance_abstraction_hiding.mammals_primates import Primates
from inheritance_abstraction_hiding.mammals_predators import Perdators
from inheritance_abstraction_hiding.mammals_bats import Bats

if __name__ == '__main__':
    monkey = Primates(age=12, size="Medium", health=5, attack=5, speed=5, intelligence=10, blood="hot")
    monkey.my_type()

    puma = Perdators(age=5, size="Big", health=8, attack=9, speed=8, intelligence=7, blood="hot")

    bat = Bats(age=1, size="Small", health=1, attack=2, speed=9, intelligence=3, blood="hot")
    bat.feed()

    print(bat)

    bat.fight(puma)
    puma.fight(bat)
    bat.avoid(puma)

    hybrid = FlyingMonkey(age=100, size="Big", health=99, attack=99, speed=100, intelligence=25, blood="hot")
    hybrid.screaming()
    hybrid.flying()



