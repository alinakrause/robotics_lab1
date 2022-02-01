#!/usr/bin/env python3

import rospy
# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose
#importing the new message from our package
from robotics_lab1.msg import Turtlecontrol
# for radians to degrees conversions
import math

ROTATION_SCALE = 180.0/math.pi

pos_msg = Pose()
test = Turtlecontrol()

def pose_callback(data):
	global pos_msg
	global test
	# convert angular position to degrees
	#
	# convert x and y to cm
	pos_msg.x = data.x * 100
	pos_msg.y = data.y * 100
	#
	test.kp = 6.0
	test.xd = 1.0
	
def callback(data):
	global test
	test.xd = 8
	test.kp = 1
	
	
if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_converter', anonymous = True)
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	#rospy.Subscriber('/turtle1/params', Pose, callback)
	
	# add a publisher with a new topic using the Shortpos message
	pos_pub = rospy.Publisher('/turtle1/turtlecontrol',Pose, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		# publish the message
		pos_pub.publish(pos_msg)
		rospy.loginfo(test.xd)
		rospy.loginfo(test.xd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
