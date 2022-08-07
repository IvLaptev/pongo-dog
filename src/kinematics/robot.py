from typing import Tuple


class Robot:
    def __init__(self):
        self.hip_link = 0
        self.thigh_link = 10
        self.calf_link = 13
        self.height = 11.4

    def print_data(self):
        print(self.hip_link)


robot = Robot()


def init_robot(hip: float, thigh: float, calf: float, height: float) -> None:
    robot.hip_link = hip
    robot.thigh_link = thigh
    robot.calf_link = calf
    robot.height = height


def change_height(height: float) -> None:
    robot.height = height
