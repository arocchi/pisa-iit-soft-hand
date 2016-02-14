#!/usr/bin/env python
import rospy
from tf.msg import tfMessage
from pyExp.msg import messageFromQuat


if __name__ == '__main__':
    rospy.init_node('hand_lifter')
    # publish to cmd_vel
    p = rospy.Publisher('/tf_static', tfMessage, queue_size=10)

    x = -0.24
    y = -0.17
    z = 0.11
    qx = 0.2886382139493777
    qy = 0.6452296092959807
    qz = 0.482248334565073
    qw = 0.517497127088724

    for i in xrange(146):  # to 0.4
        # setting up trapezoidal velocity profile
        d = 0.2
        d_max = 0.5
        lifted_pos = messageFromQuat(x, y, z + i * 0.001, qx, qy, qz, qw)
        if i < 5:
            n = 0
            m = 4
            d_real = d_max * (m - i) / (m - n) + d * (i - n) / (m - n)
            rospy.sleep(d_real)
        elif i > 140:
            n = 141
            m = 145
            d_real = d * (m - i) / (m - n) + d_max * (i - n) / (m - n)
            rospy.sleep(d_real)
        else:
            rospy.sleep(d)
        p.publish(lifted_pos)
