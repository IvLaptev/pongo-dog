import threading
from kinematics.robot import init_robot
from robot import Robot
from controllers.keyboard_controller import KeyboardController
from utils.scheduler import Scheduler


controller = KeyboardController()

init_robot(0, 1.75, 2.2, 2)
robot = Robot(controller)

get_loop = threading.Thread(target=controller.listen)
ctrl_loop = Scheduler('control', robot, 0.2)

get_loop.start()
ctrl_loop.start()

print('Laptev is the best)')
