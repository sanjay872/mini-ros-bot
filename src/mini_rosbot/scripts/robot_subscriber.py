#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f"Received command: {data.data}")

def listener():
    rospy.init_node('robot_subscriber', anonymous=True)
    rospy.Subscriber('movement_command', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
