#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from robotics_lab1.msg import Turtlecontrol
import math

pos_msg = Turtlecontrol()

def pose_callback(data):
	pos_msg.kp = data.kp * 100
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_converter', anonymous = True)
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# add a publisher with a new topic using the Shortpos message
	pos_pub = rospy.Publisher('/turtle1/control_params', Turtlecontrol, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		pos_msg.xd = 500
		# publish the message
		pos_pub.publish(pos_msg)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
