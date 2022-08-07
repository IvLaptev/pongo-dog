from abc import ABCMeta, abstractmethod


class BaseController(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.clear()

    @abstractmethod
    def listen(self) -> None:
        pass

    def clear(self) -> None:
        self.forward = False
        self.back = False
        self.turn_left = False
        self.turn_right = False
