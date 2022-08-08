from typing import List, Tuple
from kinematics.inverse_kinematics import position_to_angles_2d
from motions.base_motion import BaseMotion
import numpy as np 


class SimpleMove(BaseMotion):
    def __init__(self, target: List[Tuple[float, float]], duration: int, position: np.ndarray) -> None:
        super().__init__()
        self.target = target
        self.duration = duration
        self.steps = (np.concatenate([position_to_angles_2d(*i) for i in target]) - position) / duration

    def next_tick(self, position: np.ndarray) -> np.ndarray:
        if self.is_finished():
            return self.target

        result = position + self.steps

        self.tick += 1
        return result
