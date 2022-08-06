from typing import Tuple


class Robot:
    hip_link: float
    thigh_link: float
    calf_link: float

    def __init__(self):
        self.hip_link = 0
        self.thigh_link = 22
        self.calf_link = 26


robot = Robot()


def init_robot(hip: float, thigh: float, calf: float) -> None:
    robot.hip_link = hip
    robot.thigh_link = thigh
    robot.calf_link = calf
