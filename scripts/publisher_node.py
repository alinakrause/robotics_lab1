#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from robotics_lab1.msg import Turtlecontrol
from geometry_msgs.msg import Twist
import math

pos_msg = Turtlecontrol()
vel_cmd = Twist()


def pose_callback(data):
	global vel_cmd
	vel_cmd.linear.x = data.x * 100
	#rospy.loginfo(vel_cmd.linear.x)

def controller(data):
	global pos_mag
	pos_msg.kp = 1
	pos_msg.xd = 8


if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_converter', anonymous = True)
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol,controller)
	
	# add a publisher with a new topic using the Shortpos message
	pos_pub = rospy.Publisher('/turtle1/turtlecontrol', Twist, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	

	while not rospy.is_shutdown():
		vel_cmd.linear.x = (pos_msg.kp*((pos_msg.xd)-(vel_cmd.linear.x)))
		#rospy.loginfo(vel_cmd.linear.x)
		# publish the message
		pos_pub.publish(vel_cmd)
		
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
