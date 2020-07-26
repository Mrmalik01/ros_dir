#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def new_data_refresh(message):
    linear_data = "Linear\n - x : {}\n- y : {}\n - z : {}\n".format(message.linear.x, message.linear.y, message.linear.z)
    angular_data = "Angular\n - x : {}\n - y : {}\n - z : {}".format(message.angular.x, message.angular.y, message.angular.z)
    rospy.loginfo(rospy.get_caller_id(), " ||||| ",linear_data+angular_data)

def analyser():
    
    rospy.init_node("analyser", anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel", Twist, new_data_refresh)
    rospy.spin()
    
if __name__ == "__main__":
    try:
        analyser()
    except rospy.ROSInterruptException:
        rospy.loginfo("Program stopped")