#!/usr/bin/env python3

import rospy
# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
#importing the new message from our package
from robotics_lab1.msg import Turtlecontrol
# for radians to degrees conversions
import math

ROTATION_SCALE = 180.0/math.pi

pos_msg = Pose()
vel_cmd = Twist()
test = Turtlecontrol()

def pose_callback(data):
	global pos_msg
	# convert angular position to degrees
	#
	# convert x and y to cm
	pos_msg.x = data.x * 100
	pos_msg.y = data.y * 100
	
	
def callback(data):
	global test
	test.xd = data.xd
	test.kp = data.kp
	
	
	
if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_converter', anonymous = True)
	# add a subscriber to it to read the position information
	
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	

	rospy.Subscriber('/turtle1/params', Turtlecontrol, callback)
	# add a publisher with a new topic using the Shortpos message
	pos_pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	
	
	while not rospy.is_shutdown():
		# publish the message
		vel_cmd.linear.x = test.kp*(test.xd - pos_msg.x)
		
		pos_pub.publish(vel_cmd)
		
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
