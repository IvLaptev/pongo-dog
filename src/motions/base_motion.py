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
