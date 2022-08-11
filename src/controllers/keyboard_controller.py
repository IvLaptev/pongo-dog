from controllers.base_controller import BaseController
from utils.getch import getch


class KeyboardController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def listen(self):
        while True:
            c = getch()
            print(c)
            if (c[0] == '\x03'):
                raise KeyboardInterrupt

            self.process_key(c)

    def process_key(self, key: str):
        self.clear()
        if key == 'w':
            self.forward = True
        elif key == 's':
            self.back = True
        elif key == 'a':
            self.turn_left = True
        elif key == 'd':
            self.turn_right = True
