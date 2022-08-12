import numpy as np
from motions.base_motion import BaseMotion
from motions.simple_move import SimpleMove


class Stay(BaseMotion):
    '''
    Стояние на месте. Подразумевает фиксацию всех ног в точке (0, 0).
    '''
    
    name = 'STAY'

    def __init__(self, position: np.ndarray) -> None:
        super().__init__()

        self.target = [(0, 0)] * 4
        self.preparation = SimpleMove(self.target, 5, position)

    def next_tick(self, position: np.ndarray) -> np.ndarray:
        if not self.preparation.is_finished():
            self.target = self.preparation.next_tick(position)

        return self.target

