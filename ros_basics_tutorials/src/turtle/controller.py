#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def controller():
    speed_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist ,queue_size=10)
    
    # To initialise the node under the master node
    rospy.init_node("controller", anonymous=True)
    
    # The rate at which the publisher transmit the data 
    # 1 = 1hz
    rate = rospy.Rate(1)
    
    count = 0
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 5.0
        twist.angular.y = 6.0
        speed_publisher.publish(twist)
        rate.sleep()
        count +=1
        rospy.loginfo("Command #{} - {}".format(count, str(twist)))
        
if __name__ == "__main__":
    try:
        controller()
    except rospy.ROSInterruptException:
        rospy.loginfo("Program stopped")
        