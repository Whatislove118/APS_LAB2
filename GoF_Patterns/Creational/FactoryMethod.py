from abc import ABC, abstractmethod


class Soldier(ABC):

    @abstractmethod
    def get_type(self) -> str:
        pass


class SoldierCreator(ABC):

    @abstractmethod
    def factory_method(self) -> Soldier:
        pass

    def get_type_of_soldier(self) -> None:
        soldier = self.factory_method()
        print(soldier.get_type())

class Ninja(Soldier):

    def get_type(self) -> str:
        return 'I\'m Ninja'

class Bower(Soldier):

    def get_type(self) -> str:
        return 'I\'m Bower'

class NinjaCreator(SoldierCreator):

    def factory_method(self) -> Soldier:
        return Ninja()

    def get_type_of_soldier(self) -> None:
        soldier = self.factory_method()
        print(soldier.get_type() + '1')


class BowerCreator(SoldierCreator):

    def factory_method(self) -> Soldier:
        return Bower()

class Witcher(Soldier):

    def get_type(self) -> str:
        return 'I\'m Witcher'

class WitcherCreator(SoldierCreator):
    def factory_method(self) -> Soldier:
        return Witcher()

def client_code(soldier_creator: SoldierCreator):

    soldier_creator.get_type_of_soldier()

def main():

    client_code(NinjaCreator())

    client_code(BowerCreator())

    client_code(WitcherCreator())

if __name__ == '__main__':
    main()

