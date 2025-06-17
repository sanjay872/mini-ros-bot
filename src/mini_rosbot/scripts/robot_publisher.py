#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('movement_command', String, queue_size=10)
    rospy.init_node('robot_publisher', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz
    commands = ["MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT", "STOP"]
    i = 0

    while not rospy.is_shutdown():
        msg = f"Command: {commands[i % len(commands)]}"
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
        i += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
