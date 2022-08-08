import numpy as np
from motions.base_motion import BaseMotion
from motions.simple_move import SimpleMove


class Stay(BaseMotion):
    name = "STAY"

    def __init__(self, position: np.ndarray) -> None:
        super().__init__()

        self.target = [(0, 0)] * 4
        self.preparation = SimpleMove(self.target, 5, position)

    def next_tick(self, position: np.ndarray) -> np.ndarray:
        if self.preparation.is_finished():
            return self.target

        return self.preparation.next_tick(position)
