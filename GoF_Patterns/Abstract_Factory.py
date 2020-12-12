from abc import abstractmethod, ABC


###############
#               table
#       small_car   medium_car   big_car
# Lada  Lada-2110   Gazel        Kamaz
# Audi  A0          Q5           Q8
# Volvo C30         XC-40        VNX
###############

# classes interfaces
class SmallCar(ABC):

    @abstractmethod
    def get_car_model(self):
        pass

    @abstractmethod
    def get_car_category(self):
        pass


class MediumCar(ABC):

    @abstractmethod
    def get_car_model(self):
        pass

    @abstractmethod
    def get_car_category(self):
        pass

class BigCar(ABC):

    @abstractmethod
    def get_car_model(self):
        pass

    @abstractmethod
    def get_car_category(self):
        pass


#all variants of mixing models and category
class LadaSmallCar(SmallCar):

    def get_car_model(self):
        print('My car model is Lada')

    def get_car_category(self):
        print('Im a small car ')


class LadaMediumCar(MediumCar):

    def get_car_model(self):
        print('My car model is Lada')

    def get_car_category(self):
        print('Im a medium car ')


class LadaBigCar(BigCar):

    def get_car_model(self):
        print('My car model is Lada')

    def get_car_category(self):
        print('Im a big car ')


class AudiSmallCar(SmallCar):

    def get_car_model(self):
        print('My car model is Audi')

    def get_car_category(self):
        print('Im a small car ')


class AudiMediumCar(MediumCar):

    def get_car_model(self):
        print('My car model is Audi')

    def get_car_category(self):
        print('Im a medium car ')


class AudiBigCar(BigCar):

    def get_car_model(self):
        print('My car model is Audi')

    def get_car_category(self):
        print('Im a big car ')

class VolvoSmallCar(SmallCar):

    def get_car_model(self):
        print('My car model is Volvo')

    def get_car_category(self):
        print('Im a small car ')


class VolvoMediumCar(MediumCar):

    def get_car_model(self):
        print('My car model is Volvo')

    def get_car_category(self):
        print('Im a medium car ')


class VolvoBigCar(BigCar):

    def get_car_model(self):
        print('My car model is Volvo')

    def get_car_category(self):
        print('Im a big car ')


# Factory
class ModelFactory(ABC):

    @abstractmethod
    def create_small_car(self) -> SmallCar:
        pass

    @abstractmethod
    def create_medium_car(self) -> MediumCar:
        pass

    @abstractmethod
    def create_big_car(self) -> BigCar:
        pass

# versions of factory
class LadaModelFactory(ModelFactory):

    def create_small_car(self) -> SmallCar:
        return LadaSmallCar()

    def create_medium_car(self) -> MediumCar:
        return LadaMediumCar()

    def create_big_car(self) -> BigCar:
        return LadaBigCar()

class AudiModelFactory(ModelFactory):

    def create_small_car(self) -> SmallCar:
        return AudiSmallCar()

    def create_medium_car(self) -> MediumCar:
        return AudiMediumCar()

    def create_big_car(self) -> BigCar:
        return AudiBigCar()

class VolvoModelFactory(ModelFactory):

    def create_small_car(self) -> SmallCar:
        return VolvoSmallCar()

    def create_medium_car(self) -> MediumCar:
        return VolvoMediumCar()

    def create_big_car(self) -> BigCar:
        return VolvoBigCar()


def create_car(model_factory: ModelFactory):
    car1 = model_factory.create_small_car()
    car2 = model_factory.create_medium_car()
    car3 = model_factory.create_big_car()

    car1.get_car_category()
    car1.get_car_model()
    car2.get_car_category()
    car2.get_car_model()
    car3.get_car_category()
    car3.get_car_model()


def main():
    create_car(LadaModelFactory())
    create_car(AudiModelFactory())
    create_car(VolvoModelFactory())


if __name__ == '__main__':
    main()
