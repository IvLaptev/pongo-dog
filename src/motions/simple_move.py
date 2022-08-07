from typing import List, Tuple
from kinematics.forward_kinematics import angles_to_points_2d
from kinematics.inverse_kinematics import position_to_angles_2d
from motions.base_motion import BaseMotion
import numpy as np 


class SimpleMove(BaseMotion):
    def __init__(self, target: List[Tuple[float, float]], duration: int, position: List[float]) -> None:
        super().__init__()
        self.target = target
        self.duration = duration
        self.steps = (np.concatenate([position_to_angles_2d(*i) for i in target]) - np.array(position)) / duration

    def next_tick(self, position: List[float]) -> List[int]:
        if self.is_finished():
            return self.target

        result = np.array(position) + self.steps

        self.tick += 1
        return list(result)
