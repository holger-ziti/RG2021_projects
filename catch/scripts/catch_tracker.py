#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import rogata_library as rgt
import numpy as np





def odom_callback( odom, (agent,rogata)):
    pos = np.array([odom.pose.pose.position.x,
                   -odom.pose.pose.position.y])*100+np.array([500,500])
    rogata.set_pos(agent,pos)





if __name__ == '__main__':
    rospy.init_node("agent_tracker")
    try:
        rogata1 = rgt.rogata_helper()
        rogata2 = rgt.rogata_helper()
        rospy.Subscriber("cat/odom"  , Odometry, odom_callback,("cat_obj",rogata1))
        rospy.Subscriber("mouse/odom", Odometry, odom_callback, ("mouse_obj",rogata2))

        rospy.spin()

    except rospy.ROSInterruptException:
        pass