from math import cos, pi, sin
from kinematics.robot import robot
from motions.base_motion import BaseMotion
import numpy as np
from motions.simple_move import SimpleMove


def get_single_leg_position(step_height: float, step_duration: int, leg_number: int, tick: int):
    step_part_duration = step_duration / 4
    tick = (tick + step_part_duration * leg_number) % step_duration

    if tick < step_part_duration:
        rotation = pi * (tick / step_part_duration - 1)
        return (step_height * cos(rotation), step_height * sin(rotation))
    else:
        tick = tick - step_part_duration
        return (step_height * (1 - 2 * tick / (3 * step_part_duration)), 0) 


class SingleLegMove(BaseMotion):
    '''
    Перемещение при помощи поочерёдного переставления ног.

    Очерёдность (TODO поверить):
    1. FR
    2. FL
    3. RR
    4. RL
    '''

    name = 'SL'

    def __init__(self, step_duration: int, position: np.ndarray) -> None:
        super().__init__()

        self.duration = step_duration

        # Начальное положение для движения робота вперёд
        self.target = [(get_single_leg_position(robot.step_height, self.duration, i, 0)) for i in range(4)]
        self.preparation = SimpleMove(self.target, 5, position)

    def next_tick(self, position: np.ndarray) -> None:
        if self.preparation.is_finished():
            self.target = [(get_single_leg_position(robot.step_height, self.duration, i, self.tick)) for i in range(4)]
            move = SimpleMove(self.target, 1, position)
            
            self.tick += 1
            return move.next_tick(position)

        return self.preparation.next_tick(position)
