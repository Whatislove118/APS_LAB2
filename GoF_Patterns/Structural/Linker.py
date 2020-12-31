# Unit army ex.
from abc import ABC, ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta): # общий интерфейс
    """
        Базовый класс Компонент объявляет общие операции как для простых, так и для
        сложных объектов структуры.
    """

    @abstractmethod
    def print(self) -> None:
        pass

class Archer(Unit):
    """
        Класс Лист представляет собой конечные объекты структуры. Лист не может
        иметь вложенных компонентов.

        Обычно объекты Листьев выполняют фактическую работу, тогда как объекты
        Контейнера лишь делегируют работу своим подкомпонентам.
    """
    def print(self) -> None:
        print('Archer')

class Knight(Unit):

    def print(self) -> None:
        print('Knight')

class Swordsman(Unit):

    def print(self) -> None:
        print('Swordsman')

class Squad(Unit):
    """
        Компоновщик - отряд, состоящий более чем из одного человека. Также
        может включать в себя другие отряды-компоновщики.
    """

    def __init__(self):
        self._units = []

    def print(self) -> None:
        print('Отряд - {}'.format(self.__hash__()))
        for unit in self._units:
            unit.print()

    def add(self, unit: Unit) -> None:
        """
            Добавление нового отряда

            :param unit: отряд (может быть как базовым, так и компоновщиком)
        """
        self._units.append(unit)
        unit.print()
        print('Присоединился к отряду - {}'.format(unit.__hash__()))

    def remove(self, unit: Unit) -> None:
        """
            Удаление отряда из текущего компоновщика

            :param unit: объект отряда
        """
        try:
            self._units.remove(unit)
            unit.print()
            print('Отряд покинул - {}'.format(unit.__hash__()))
        except ValueError:
            unit.print()
            print('В отряде {} не найден'.format(unit.__hash__()))

def main():
    print('OUTPUT')
    squad = Squad()

    squad.add(Knight())
    squad.add(Archer())
    squad.add(Knight())
    swordsman = Swordsman()
    squad.add(swordsman)
    squad.remove(swordsman)

    squad.print()

    squad_big = Squad()

    squad_big.add(Knight())
    squad_big.add(squad)
    squad_big.add(Swordsman())

    squad_big.print()


if __name__ == '__main__':
    main()

