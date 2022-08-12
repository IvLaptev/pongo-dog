from math import sqrt, pi, acos, asin
from typing import Tuple
from kinematics.robot import robot

def position_to_angles_2d(x: float, y: float) -> Tuple[float, float]:
    '''
    Превращает точку из двумерного конфигурационного пространства двух
    последних частей ноги в углы поворота, которые позволяют поставить
    ногу в заданную точку

        Параметры:
            x (float):  смещение по горизонтали от положения стоя
            y (float):  смещение по вертикали от положения стоя
    '''
    
    # Приведение к базису
    y = y - robot.height

    # Расчёт углов
    distance_to_point = sqrt(x**2 + y**2)
    q1 = -acos((distance_to_point**2 + robot.thigh_link**2 - robot.calf_link**2) / (2 * robot.thigh_link * distance_to_point)) \
        + asin(x / distance_to_point)
    q2 = pi - acos((robot.thigh_link**2 + robot.calf_link**2 - distance_to_point**2) / (2 * robot.calf_link * robot.thigh_link))

    return (q1, q2)
