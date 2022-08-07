from kinematics.robot import robot, init_robot
from kinematics.inverse_kinematics import position_to_angles
from kinematics.forward_kinematics import angles_to_points

init_robot(0, 1.75, 2.2, 2)

angles = position_to_angles(0.5, 0)
print(angles)

positions = angles_to_points(*angles)
print(positions)

print('Laptev is the best)', robot.calf_link)
