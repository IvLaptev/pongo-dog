class BaseController():
    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.forward = False
        self.back = False
        self.turn_left = False
        self.turn_right = False
