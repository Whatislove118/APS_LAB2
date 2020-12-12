# пример из игры:
# персонаж может обеими руками либо атаковать мечом, либо двумя руками держать щит и блокировать урон.
# Опишем эти действия словом State.
from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def info(self) -> str:
        pass

class Context:

    prop = property()
    def __init__(self, state: State) -> None:

        self._state = state

    @prop.getter
    def state(self) -> State:
        return self._state

    @prop.setter
    def state(self, state: State) -> None:
        self._state = state

    def print_state_status(self):
        print('State status: {}'.format(self._state.info()))


class AttackState(State):

    def info(self) -> str:
        return 'Attack'

class DefenseState(State):

    def info(self) -> str:
        return 'Block'

def main():

    context = Context(AttackState())
    context.print_state_status()

    context = Context(DefenseState())
    context.print_state_status()



if __name__ == '__main__':
    main()