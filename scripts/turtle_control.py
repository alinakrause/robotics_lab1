#!/usr/bin/env python3

import rospy
# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose
# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist
#importing the new message from our package
from robotics_lab1.msg import Turtlecontrol


pos_msg = Pose()
vel_cmd = Twist()
control = Turtlecontrol()

def pose_callback(data):
	global pos_msg
	# stores x position of the turtle
	pos_msg.x = data.x
	
	
	
def control_callback(data):
	global control
	# stores desired position and control gain
	control.xd = data.xd
	control.kp = data.kp 
	
	
	
if __name__ == '__main__':
	# initialize the node
	rospy.init_node('turtle_control', anonymous = True)
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# add a subscriber to it to read the desired position and control gain
	rospy.Subscriber('/turtle1/params', Turtlecontrol, control_callback)
	# declare a publisher to publish in the velocity command topic
	pos_pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	
	# run this control loop regularly
	while not rospy.is_shutdown():
		# if the position is not the desired position
		if(not(vel_cmd.linear == control.xd)):
			# proportional controller equation
			vel_cmd.linear.x = (control.kp*(control.xd - pos_msg.x))
			# publish the message
			pos_pub.publish(vel_cmd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
