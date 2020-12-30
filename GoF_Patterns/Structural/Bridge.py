from abc import ABC, abstractmethod


class Color(ABC): # Implementation

    @abstractmethod
    def get_type_color(self) -> str:
        pass

class RedColor(Color): # Concrete Implementation
    def get_type_color(self) -> str:
        return 'Red'

class BlueColor(Color): # Concrete Implementation
    def get_type_color(self) -> str:
        return 'Blue'

class Figure(ABC): # Abstraction

    def __init__(self, color: Color) -> None:
        self.color = color
        self.type = self.__class__.__name__

    def get_info(self) -> None:
        print('Type: ' + self.type)
        print('Color: ' + self.color.get_type_color())

class Square(Figure): # Extended Abstraction
    pass

class Circle(Figure): # Extended Abstraction
    pass

def client_code(abstraction: Figure) -> None:

    abstraction.get_info()


if __name__ == '__main__':
    # 1 ex.
    implementation = RedColor()
    abstraction = Figure(implementation)
    client_code(abstraction)

    print('\n')

    # 2 ex.
    implementation = RedColor()
    abstraction = Square(implementation)
    client_code(abstraction)

    print('\n')

    #3 ex.
    implementation = BlueColor()
    abstraction = Circle(implementation)
    client_code(abstraction)




