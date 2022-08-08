from abc import ABCMeta, abstractmethod
from typing import List, Tuple, Union
from numpy import ndarray


class BaseMotion(metaclass=ABCMeta):
    duration: int
    target: Union[List[Tuple[float, float]],  List[float], ndarray]
    name: str

    def __init__(self) -> None:
        self.tick = 0
        self.preparation = None

    @abstractmethod
    def next_tick(self) -> None:
        pass

    def is_finished(self) -> None:
        return self.tick >= self.duration

    def print(self) -> None:
        if self.preparation != None and not self.preparation.is_finished():
            self.preparation.print()
        else:
            print(self.name, self.target)
