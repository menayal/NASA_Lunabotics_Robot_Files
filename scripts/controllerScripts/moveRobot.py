#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import os #from initialize controller script
from initializeController import initializeController

# Receives joystick messages (subscribed to Joy topic)
    # then converts the joysick inputs into Twist commands
    # axis 1 aka left stick vertical controls linear speed
    # axis 0 aka left stick horizonal controls angular speed

def callback(data):
    twist = Twist()
    twist.linear.x = 4*data.axes[1]
    twist.angular.z = 4*data.axes[0]
    pub.publish(twist)

    #now lets see what happens when i click a button:
    #if x(0) is clicked: do something
    #if button is clicked:
    if (data.buttons[0]):
        print("X(Playstation)        or A(Xbox) is pressed")
    if (data.buttons[1]):
        print("Circle(Playstation    or B(Xbox) is pressed")
    if (data.buttons[2]):
        print("Square(Playstation)   or X(Xbox) is pressed")
        os.system("roslaunch roberto_hw_interface api_tests.launch")
    if (data.buttons[3]):
        print("Triangle(Playstation) or Y(Xbox) is pressed")

    


# Intializes everything
def start():
    global pub
    pub = rospy.Publisher('/new_robot_urdf_diff_drive_controller/cmd_vel', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2RobotControl')
    rospy.spin()

if __name__ == '__main__':
        #start the initialize controller script
        initializeController()
        start()
