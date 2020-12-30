import copy  # this pattern realized in Python
class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Ball:

    def __init__(self, radius: int, bar: int, type: str) -> None:
        self.radius = radius
        self.bar = bar
        self.type = type

    def __copy__(self):
        new_copy = self.__class__(self.radius, self.bar, self.type)
        new_copy.__dict__.update(self.__dict__)
        return new_copy

    def __deepcopy__(self, memodict={}):
        new_copy = self.__class__(self.radius, self.bar, self.type)
        new_copy.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new_copy


def main():
    ball = Ball(1, 3, 'footbal')
    copy_ball = copy.copy(ball)

    print('b', ball.radius)
    print('copy_ball', copy_ball.radius)

    ball.radius += 1

    print('b', ball.radius)
    print('copy_ball', copy_ball.radius)

    deep_copy_ball = copy.deepcopy(copy_ball)

    #simple example difference between copy and deepcopy
    a = [1, 2, 3]
    b = [1, 4, 6]
    c = [a, b]

    d = copy.copy(c)
    print(id(c) == id(d))  # False - d is now a new object
    print(id(c[0]) == id(d[0]))  # True - d[0] is the same object as c[0]

    d = copy.deepcopy(c)
    print(id(c) == id(d))  # False - d is now a new object
    print(id(c[0]) == id(d[0]))  # False - d[0] is now a new object


if __name__ == '__main__':
    main()





