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
brain=Brain()
controller_1 = Controller(PRIMARY)

# Robot configuration code
front_motor = Motor(Ports.PORT9, False)
left_back_motor = Motor(Ports.PORT1, False)
right_back_motor = Motor(Ports.PORT20, False)

# Begin project code
#
# Assume arms are 120* appart
# 
# Full forward should be 100 on the front wheel and 66.6 on the other wheels
#
# Transposing x,y into 3 motor values
#
# figuting out turning? 
# Axis1  <---> 
# Axis2 ^
while True:
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

    brain.screen.print("(X,Y):", controller_1.axis1.position(), controller_1.axis2.position())
    brain.screen.next_row()

    front_motor_value = controller_1.axis2.position()
    brain.screen.print("front motor", front_motor_value)
    front_motor.spin(FORWARD, front_motor_value,PERCENT)
    brain.screen.next_row()

    left_back_motor_value = controller_1.axis2.position() / 180 * -120
    brain.screen.print("Left motor", left_back_motor_value)
    left_back_motor.spin(FORWARD, left_back_motor_value,PERCENT)
    brain.screen.next_row()

    right_back_motor_value = controller_1.axis2.position() / 180 * -120
    brain.screen.print("Right motor", right_back_motor_value)
    right_back_motor.spin(FORWARD, right_back_motor_value,PERCENT)
    brain.screen.next_row()

    wait(10,MSEC)



# Print all Drivetrain sensing values to the screen in an infinite loop
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
    
