from typing import List, Tuple
from kinematics.inverse_kinematics import position_to_angles_2d
from motions.base_motion import BaseMotion
import numpy as np 


class SimpleMove(BaseMotion):
    name = 'MOVE'
    
    def __init__(self, target: List[Tuple[float, float]], duration: int, position: np.ndarray) -> None:
        super().__init__()

        self.target = np.array([])
        for i in range(4):
            self.target[i * 3] = position[i * 3]
            self.target[i * 3 + 1], self.target[i * 3 + 2] = position_to_angles_2d(*target[i])

        self.duration = duration
        self.steps = (target - position) / duration

    def next_tick(self, position: np.ndarray) -> np.ndarray:
        if self.is_finished():
            return self.target

        result = position + self.steps

        self.tick += 1
        return result
