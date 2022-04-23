from datetime import datetime


class CostException(Exception):
    """ Raised when Human haven't enough money """
    pass


class AllowedException(Exception):
    """Raised when Human not enough years"""
    pass


class Movie:

    def __init__(self, name, director, year, country, duration, age_rating, cost):
        self._name = name
        self.director = director
        self.year = year
        self.country = country
        self.duration = duration
        self.age_rating = age_rating
        self.cost = cost

    @property
    def name(self):
        """
        getter
        """
        return self._name

    @name.setter
    def set_name(self, value):
        """
        setter
        """
        self._name = value

    def __add__(self, other):
        """
        :return: Sum of films of one director and here characteristics
        """
        if not isinstance(other, self.__class__):
            return TypeError
        if not self.director == other.director:
            return ValueError
        return Movie(name=f"{self.name} and {other._name}", cost=self.cost + other.cost, director=self.director,
                     year=[self.year, other.year],
                     country=self.country, duration=f"{self.duration + other.duration} min.",
                     age_rating=[self.age_rating, other.age_rating])

    def __str__(self):
        """
        :return: The info about __add__ method
        """
        return f'The films : {self.name} \nTheir sum cost : {self.cost} \nDirector : {self.director} \n' \
               f'Release dates :  {self.year} \nCountry = {self.country}\n' \
               f'Sum duration : {self.duration}\nAge rating : {self.age_rating}'

    @staticmethod
    def convert(cost, rate):
        """
        :return: convert price of film
        """
        return cost * rate

    # @staticmethod
    # def price_converter(name, director, year, country, duration, age_rating, cost, rate):
    #     """
    #     :return: retrun Movie object with converted price of film
    #     """
    #     return Movie(name, director, year, country, duration, age_rating, cost * rate)

    @classmethod
    def price_converter(cls, name, director, year, country, duration, age_rating, cost, rate):
        """
        :return: retrun Class object  with converted price of film
        """
        return cls(name, director, year, country, duration, age_rating, cls.convert(cost, rate))

    def is_allowed(self, human):
        """
        :param human: object from Human class
        :return: Possibility of Human to watch a film
        """
        if (datetime.now().year - human.year_of_birth) < self.age_rating:
            raise AllowedException
        return print(f"{human.name} is allow to watch {self._name}")


class Cartoon(Movie):

    def __init__(self, name, director, year, country, duration, age_rating, technique, cost):
        super().__init__(name, director, year, country, duration, age_rating, cost)
        self.technique = technique


class Anime(Cartoon):

    def __init__(self, name, director, year, duration, age_rating, cost, country="Japan", technique="Drawn"):
        super().__init__(name, director, year, country, duration, age_rating, technique, cost)


class Human:
    def __init__(self, name, sex, year_of_birth, money):
        self._name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
        self.money = money

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, value):
        self._name = value

    def possibility_to_buy(self, movie):
        """
        :param movie: object from Movie classes and his babies
        :return: Possibility to pay for a film
        """
        if self.money < movie.cost:
            raise CostException
        return print(f"{self._name} can buy a ticket on {movie.name}")


class Basket:
    def __init__(self):
        self._items = {}

    @property
    def items(self):
        """
        :return: all info about Basket
        """
        return self._items

    def __getitem__(self, item):
        """
        :return: Info about tickets on film by Name
        """
        return self._items[item.name]

    def __setitem__(self, key, value):
        """
        :param key.name - Name of Film , key.cost - price of film
        :param value - quantity of tickets
        :return: items in Basket
        """
        self._items[key.name] = value

    def __len__(self):
        """
        :return: size of Basket (How much items here)
        """
        return sum(self._items.values())

    def __contains__(self, item):
        """
        :return: True - if movie in basket , False - if movie doesn't in basket
        """
        return item.name in self._items


def main():
    movie = Movie(name="Dune", director="Denis Villeneuve", year=2021, country="USA", duration=155, age_rating=13,
                  cost=200)

    movie_2 = Movie(name="Arrival", director="Denis Villeneuve", year=2011, country="USA", duration=100, age_rating=18,
                    cost=300)
    #
    #
    # movie_3 = Movie.price_converter(name="Dune", director="Denis Villeneuve", year=2021, country="USA", duration=155,
    #                                 age_rating=13,cost=200, rate=10)

    human_1 = Human(name="Neo", sex="M", year_of_birth=1964, money=200)
    # human_2 = Human(name="Leo", sex="M", year_of_birth=2019, money=99)

    # anime = Anime.price_converter(name="The Castle of Cagliostro", director="Hayao Miyazaki", year=1979,
    #                               country="Japan", duration=100,
    #                               age_rating=13, technique="Drawn", cost=50, rate=3)
    # anime_2 = Anime(name="The Castle of Cagliostro", director="Hayao Miyazaki", year=1979, country="Japan",
    #                 duration=100,
    #                 age_rating=13, technique="Drawn", cost=70)

    ### Try to work with methods
    # print(movie_3)
    # human_2.possibility_to_buy(movie)
    # movie.is_allowed(human_2)

    ### Try to use dunder methods
    # basket = Basket()
    # basket[movie] = 2
    # basket[movie_2] = 3
    # print(basket[movie])
    # print(len(basket))
    # print(movie in basket)
    # print(basket[movie])
    final_list_of_films = movie + movie_2
    print(final_list_of_films)


# Здесь исключения работают как просто отличие от выполнения условия но не как обработка ошибок - это плохо

if __name__ == '__main__':
    try:
        main()
    except CostException:
        print("Mot enough money")
        exit(1)
    except AllowedException:
        print("Not enough years")
        exit(2)
    except (TypeError, ValueError) as e:
        print(e)
        exit(2)
    except Exception as e:
        print(e)
        exit(3)
    else:
        print("-- Successfully Compiled")


else:
    print("-- Error")
