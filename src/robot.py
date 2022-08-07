from enum import Enum
from typing import List
from controllers.base_controller import BaseController


class RobotStates(Enum):
    STAY = 1
    SL_FORWARD = 2
    SL_BACK = 3
    TROT_FORWARD = 4
    TROT_BACK = 5


class Robot():
    state: RobotStates
    motors: List[int]

    def __init__(self, controller: BaseController) -> None:
        self.state = RobotStates.STAY
        self.controller = controller

    def control(self) -> None:
        '''
        Функция, считающая следующую позицию робота
        '''
        
        # Получение данных с контроллера (плойка)
        print(self.controller.forward)
        self.controller.clear() # Очистка показаний контроллера для следующей итерации

        # Подсчёт позиции


        # Отправка управляющих сигналов в космос (расп)
        pass
