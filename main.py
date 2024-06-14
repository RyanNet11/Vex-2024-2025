# ----------------------------------------------------------------------------- #
#                                                                               #             
# 	Project:        Drivetrain Sensing                                          #
#   Module:         main.py                                                     #
#   Author:         VEX                                                         #
#   Created:        Fri Aug 05 2022                                             #
#	Description:    This example will show all of the available commands        #
#                   for using the Drivetrain                                    #
#                                                                               #                                                                          
#   Configuration:  V5 Speedbot (Drivetrain 2-motor, No Gyro)                   #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain = Brain()
controller_1 = Controller(PRIMARY)

# Robot configuration code
# positive motor value = to the outside
# negative motor value = to the inside 
#  \ L1     / R1
#  o\     o/
#   /o     \o
#  / L2     \ R2
#
#
L1 = Motor(Ports.PORT9, False)
L2 = Motor(Ports.PORT8, False)
R1 = Motor(Ports.PORT7, False)
R2 = Motor(Ports.PORT6, False)

xvalues = [0, 0, 0, 0]  # Placeholder values for L1, R1, L2, R2
yvalues = [0, 0, 0, 0]  # Placeholder values for L1, R1, L2, R2

def wheel_vector_maker_x(x):
    xvalues[0] = -x  # L1
    xvalues[1] = x   # R1
    xvalues[2] = -x  # L2
    xvalues[3] = x   # R2

def wheel_vector_maker_y(y):
    yvalues[0] = y   # L1
    yvalues[1] = y   # R1
    yvalues[2] = -y  # L2
    yvalues[3] = -y  # R2

while True:
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    x_pos = controller_1.axis1.position()
    y_pos = controller_1.axis2.position()
    brain.screen.print("(X,Y):", x_pos, y_pos)
    brain.screen.next_row()

    wheel_vector_maker_x(x_pos)
    brain.screen.print("X", xvalues)
    brain.screen.next_row()

    wheel_vector_maker_y(y_pos)
    brain.screen.print("Y", yvalues)
    brain.screen.next_row()

    wait(10, MSEC)

# while True:
#     brain.screen.clear_screen()
#     brain.screen.set_cursor(1,1)

#     brain.screen.print("(X,Y):", controller_1.axis1.position(), controller_1.axis2.position())
#     brain.screen.next_row()
#     if controller_1.axis1.position() + controller_1.axis2.position() > added:
#         added = controller_1.axis1.position() + controller_1.axis2.position()
#     brain.screen.print("Added:",added)
#     brain.screen.next_row()

#     L1_v1 = controller_1.axis1.position() * -1
#     L1_v2 = controller_1.axis2.position() * -1
#     brain.screen.print("Left 1", L1_v1, L1_v2)
#     brain.screen.next_row()

#     L2_v1 = controller_1.axis1.position()
#     L2_v2 = controller_1.axis2.position()
#     brain.screen.print("left 2", L2_v1, L2_v2)
#     brain.screen.next_row()

#     R1_v1 = controller_1.axis1.position()
#     R1_v2 = controller_1.axis2.position()
#     brain.screen.print("right 1", R1_v1, R1_v2)
#     brain.screen.next_row()

#     R2_v1 = controller_1.axis1.position() * -1
#     R2_v2 = controller_1.axis2.position() * -1
#     brain.screen.print("right 2", R2_v1, R2_v2)
#     brain.screen.next_row()
#     wait(10,MSEC)

# Begin project code
# Three wheels forward and back
# Assume arms are 120* appart
# 
# Full forward should be 100 on the front wheel and 66.6 on the other wheels
#
# Transposing x,y into 3 motor values
#
# figuting out turning? 
# Axis1  <---> 
# Axis2 ^
# while True:
#     brain.screen.clear_screen()
#     brain.screen.set_cursor(1,1)

#     brain.screen.print("(X,Y):", controller_1.axis1.position(), controller_1.axis2.position())
#     brain.screen.next_row()

#     front_motor_value = controller_1.axis2.position()
#     brain.screen.print("front motor", front_motor_value)
#     front_motor.spin(FORWARD, front_motor_value,PERCENT)
#     brain.screen.next_row()

#     left_back_motor_value = controller_1.axis2.position() / 180 * -120
#     brain.screen.print("Left motor", left_back_motor_value)
#     left_back_motor.spin(FORWARD, left_back_motor_value,PERCENT)
#     brain.screen.next_row()

#     right_back_motor_value = controller_1.axis2.position() / 180 * -120
#     brain.screen.print("Right motor", right_back_motor_value)
#     right_back_motor.spin(FORWARD, right_back_motor_value,PERCENT)
#     brain.screen.next_row()

#     wait(10,MSEC)



# Print all Drivetrain sensing values 
#
# while True:
#     # Clear the screen and set the cursor to top left corner on each loop
#     while i < 80: 
#         brain.screen.clear_screen()
#         brain.screen.set_cursor(1,1)

#         brain.screen.print("Velocity:", right_drive_smart.velocity(PERCENT))
#         brain.screen.next_row()

#         brain.screen.print("Current:", right_drive_smart.current(CurrentUnits.AMP))
#         brain.screen.next_row()

#         brain.screen.print("Power:", right_drive_smart.power(PowerUnits.WATT))
#         brain.screen.next_row()

#         brain.screen.print("Torque:", right_drive_smart.torque(TorqueUnits.NM))
#         brain.screen.next_row()

#         brain.screen.print("Efficiency:", right_drive_smart.efficiency(PERCENT))
#         brain.screen.next_row()

#         brain.screen.print("Temperature:", right_drive_smart.temperature(PERCENT))
#         brain.screen.next_row()
#         i = i + 1
#         wait(10,MSEC)
#     i = 0
#     while i < 1:
#         right_drive_smart.spin_to_position(100)
#         while True:
#             if right_drive_smart.is_done:
#                 break
#             else:
#                 continue
#         right_drive_smart.stop()
#         i= i + 1
#     # A brief delay to allow text to be printed without distortion or tearing
    
