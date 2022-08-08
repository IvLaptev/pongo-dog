from abc import ABCMeta, abstractmethod
from typing import List, Tuple


class BaseMotion(metaclass=ABCMeta):
    duration: int
    target: List[Tuple[float, float]]

    def __init__(self) -> None:
        self.tick = 0
        self.preparation = None

    @abstractmethod
    def next_tick(self) -> None:
        pass

    def is_finished(self) -> None:
        return self.tick >= self.duration
