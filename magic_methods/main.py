class Kitty:
    def __init__(self, name, breed, color, age, mischievousness, heterochromia):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.mischievousness = mischievousness
        self.heterochromia = heterochromia

    def __str__(self):
        return f"{self.__class__.__name__}: {{\n\tname: {self.name}\n\tbreed: {self.breed}\n\tcolor: {self.color}\n\t" \
               f"age: {self.age}\n\tmischievousness: {self.mischievousness}\n\theterochromia: {self.heterochromia}\n}}"


class Wagon:
    def __init__(self, number, passenger: list):
        self.number = number
        self.sits = 5
        self.passenger = passenger

    def __str__(self):
        return f"[{self.number}]"

    def __len__(self):
        return len(self.passenger)

    def add(self, passenger):
        """
        add passanger to wagon. Wagon has only 5 sits
        :param passenger:recive list with new passengers
        :return: result with appeed list or message
        """
        if len(self.passenger) < self.sits and (len(passenger) < (self.sits - len(self.passenger) + 1)):
            self.passenger.extend(passenger)
        else:
            remain_sits = self.sits - (len(self.passenger))
            print(f"For this wagon remains {remain_sits} sits")


class Train:
    def __init__(self):
        self.locomotive = "HEAD"
        self.wagons = list()

    def __len__(self):
        """
        This method count wagons
        :return: how mutch wagons we have
        """
        return len(self.wagons)

    def len(self):
        """
        Alternative len for wagons list
        I create it because __len__ can't
        give me a list, only int
        :return: list
        """
        return print(self.wagons)

    def __str__(self):
        list_of_wagons = self.wagons
        result = [[item] for item in list_of_wagons]
        formatted_result = '-'.join(str(item) for item in result)
        return f"﻿<=[{self.locomotive}]-{formatted_result}"

    def addWagon(self, wagon: Wagon):
        self.wagons.append(wagon.number)
        wagon.number = len(self.wagons)


if __name__ == '__main__':
    kitty = Kitty('Murzik', "Siam", "Ash", 3, True, False)
    my_str = str(kitty)
    print(my_str)

    wagon_1 = Wagon(1, ["Tom", "George"])
    wagon_2 = Wagon(2, ["Ely", "Eva", "Candy"])
    wagon_3 = Wagon(3, ["Mysha", "Grysha", "Opanas"])
    wagon_4 = Wagon(4, ["Orest", "Saitama", "Tolik", "Vadik", "Petro Incognito", "Test"])

    wagon_3.add(["Mark", "Matviyy"])

    print(wagon_1, wagon_2, wagon_3)

    train = Train()
    train.addWagon(wagon_1)
    train.addWagon(wagon_2)
    train.addWagon(wagon_3)
    train.addWagon(wagon_4)

    print(len(train))
    train.len()

    print(train)
