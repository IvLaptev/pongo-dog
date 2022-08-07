from math import cos, sin
from kinematics.robot import robot

def angles_to_points_2d(q1: float, q2: float):
    x1 = sin(q1) * robot.thigh_link
    y1 = -cos(q1) * robot.thigh_link

    x2 = x1 + sin(q1 + q2) * robot.calf_link
    y2 = y1 - cos(q1 + q2) * robot.calf_link

    # Приведеение к базису
    y1 = y1 + robot.height
    y2 = y2 + robot.height

    return (x1, y1), (x2, y2)
