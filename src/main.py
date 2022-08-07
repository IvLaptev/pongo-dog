from kinematics.robot import robot, init_robot
from utils.scheduler import Scheduler


init_robot(0, 1.75, 2.2, 2)

scheduler = Scheduler('print_data', robot, 0.2)
scheduler.start()

print('Laptev is the best)', robot.calf_link)
