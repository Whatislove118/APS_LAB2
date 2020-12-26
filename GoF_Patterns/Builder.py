from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class DoshirakBuilder(ABC):

    @property
    def get_doshirak(self) -> None:
        pass

    @abstractmethod
    def doshirak_taste(self) -> None:
        pass

    @abstractmethod
    def doshirak_species(self) -> None:
        pass

    @abstractmethod
    def doshirak_type_of_meat(self) -> None:
        pass

class ChickenDoshirak():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class ChickenDoshirakBuilder(DoshirakBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._doshirak = ChickenDoshirak()

    def get_doshirak(self) -> ChickenDoshirak:
        doshirak = self._doshirak
        self.reset()
        return doshirak

    def doshirak_taste(self) -> None:
        self._doshirak.add('Chicken')

    def doshirak_type_of_meat(self) -> None:
        self._doshirak.add('Chicken balls')

    def doshirak_species(self) -> None:
        self._doshirak.add('Chicken species')


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def doshirak_builder(self) -> DoshirakBuilder:
        return self._builder

    @doshirak_builder.setter
    def doshirak_builder(self, builder: DoshirakBuilder) -> None:
        self._builder = builder


    def bild_doshirak_without_meat(self) -> None:
        self._builder.doshirak_taste()
        self._builder.doshirak_species()

    def bild_full_doshirak(self) -> None:
        self._builder.doshirak_species()
        self._builder.doshirak_taste()
        self._builder.doshirak_type_of_meat()


if __name__ == '__main__':

    director = Director()
    builder = ChickenDoshirakBuilder()
    director.doshirak_builder = builder

    print('without meat')
    director.bild_doshirak_without_meat()
    builder._doshirak.list_parts()

    print('\n')
    print('full doshirak')
    director.bild_full_doshirak()
    builder._doshirak.list_parts()

