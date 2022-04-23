import random
from abc import ABC, abstractmethod


class NotThisSexError(Exception):
    """ If Woman goes to barber"""
    pass


class NotImplementedMethod(Exception):
    """ If some method doesn't implement"""
    pass


class Human:

    def __init__(self, name: str, year_of_birth: int, sex: str, hair_length: int, nail_length: int,
                 color_nail="Uncolored", ):
        if sex not in ['M', 'F']:
            raise NotThisSexError("You must used values only from ['M','W']")
        self.name = name
        self.year_of_birth = year_of_birth
        self.sex = sex
        self.hair_length = hair_length
        self.nail_length = nail_length
        self.color_nail = color_nail

    def __str__(self):
        return f"My name is {self.name}, My hair length is {self.hair_length}, " \
               f"My nail length and color is {self.nail_length} {self.color_nail} and my sex is {self.sex}"


class Worker(ABC):
    def __init__(self, name, year_of_birth, sex):
        self.name = name
        self.year_of_birth = year_of_birth
        self.sex = sex

    @abstractmethod
    def do_job(self, human):
        raise NotImplementedMethod("Please implement this method")


class Manicurist(Worker):
    def __init__(self, name, year_of_birth, sex):
        super().__init__(name, year_of_birth, sex)

    def do_job(self, human):
        nail_color = ['Blue', 'Red', 'Purple', 'Orange', 'Green', 'Black']

        if human.nail_length > 0:
            human.nail_length = human.nail_length - 1
        else:
            print("Too short Nails")
        human.color_nail = random.choice(nail_color)


class Hairdresser(Worker):
    def __init__(self, name, year_of_birth, sex):
        super().__init__(name, year_of_birth, sex)

    def do_job(self, human):
        if human.hair_length > 0:
            human.hair_length = human.hair_length - 1
        else:
            print("Too short Hair")


class Barber(Worker):
    def __init__(self, name, year_of_birth, sex):
        super().__init__(name, year_of_birth, sex)

    def do_job(self, human):
        if human.sex != 'M':
            raise NotThisSexError("NotThisSexError : Woman tried go to barber ")
        if human.hair_length > 0:
            human.hair_length = human.hair_length - 1
        else:
            print("Волосы нельзя подстричь")


def main():
    neo = Human(
        name="Neo", sex="M", year_of_birth=1964,
        hair_length=10, nail_length=2
    )
    trinity = Human(
        name="Trinity", sex="F", year_of_birth=1967,
        hair_length=30, nail_length=5
    )

    manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
    barber = Barber(name="Bob", sex="M", year_of_birth=1987)

    print(neo)
    manicurist.do_job(neo)
    print(neo)
    # Теперь у Нео ногти длины 1 и, например, фиолетовые

    barber.do_job(neo)
    print(neo)
    # Теперь у Нео волосы длины 9

    barber.do_job(trinity)
    print(trinity)
    # А тут программа падает с исключением ValueError...


if __name__ == '__main__':
    try:
        main()
    except NotThisSexError as nte:
        print(nte)
    except NotImplementedMethod as nim:
        print(nim)
