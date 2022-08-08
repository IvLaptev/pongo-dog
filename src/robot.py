from enum import Enum
import numpy as np
from controllers.base_controller import BaseController
from motions.simple_move import SimpleMove
from motions.stay import Stay


class RobotStates(Enum):
    UNDEFINED = -1
    STAY = 0
    SL_FORWARD = 1
    SL_BACK = 2
    TROT_FORWARD = 3
    TROT_BACK = 4


class Robot():
    state: RobotStates
    angles: np.ndarray

    def __init__(self, controller: BaseController) -> None:
        self.tick = 0
        self.state = RobotStates.UNDEFINED
        self.controller = controller
        self.angles = np.array([0, -1, 2] * 4)
        self.motion = SimpleMove([(0, 0)] * 4, 5, np.array([0] * 12)) # TODO: изменить начальную позицию, прописать её в README.md

    def control(self) -> None:
        '''
        Функция, считающая следующую позицию робота
        '''
        
        # Получение данных с контроллера (плойка, клава)
        self.controller.clear() # Очистка показаний контроллера для следующей итерации

        # Изменение состояния
        if (self.tick > 5):
            self.check_state()

        # Подсчёт позиции
        if self.motion:
            self.motion.print()
            self.angles = self.motion.next_tick(self.angles)

        # Отправка управляющих сигналов в космос (расп)
        self.tick += 1
        
    def check_state(self) -> None:
        if self.controller.is_empty() and self.state != RobotStates.STAY:
            self.state = RobotStates.STAY
            self.motion = Stay(self.angles)
