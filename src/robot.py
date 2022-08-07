from enum import Enum
from typing import List
from controllers.base_controller import BaseController
from motions.simple_move import SimpleMove


class RobotStates(Enum):
    STAY = 1
    SL_FORWARD = 2
    SL_BACK = 3
    TROT_FORWARD = 4
    TROT_BACK = 5


class Robot():
    state: RobotStates
    angles: List[float]

    def __init__(self, controller: BaseController) -> None:
        self.state = RobotStates.STAY
        self.controller = controller
        self.motion = SimpleMove([(0, 0)] * 4, 5, [0] * 12)

    def control(self) -> None:
        '''
        Функция, считающая следующую позицию робота
        '''
        
        # Получение данных с контроллера (плойка, клава)
        print(self.controller.forward)
        self.controller.clear() # Очистка показаний контроллера для следующей итерации

        # Изменение состояния

        # Подсчёт позиции
        self.angles = self.motion(self.angles)

        # Отправка управляющих сигналов в космос (расп)
        pass
