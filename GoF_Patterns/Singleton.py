
class BallMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Ball(metaclass=BallMeta):
    def hit(self):
        pass


def main():
    ball1 = Ball()
    ball2 = Ball()

    if id(ball1) == id(ball2):
        print('Same objects')
    else:
        print('Different objects')


if __name__ == '__main__':
    main()
