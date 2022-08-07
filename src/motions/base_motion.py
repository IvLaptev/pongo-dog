from abc import ABCMeta, abstractmethod


class BaseMotion(metaclass=ABCMeta):
    duration: int

    def __init__(self) -> None:
        self.tick = 0

    @abstractmethod
    def next_tick(self) -> None:
        pass

    def is_finished(self) -> None:
        return self.tick >= self.duration
