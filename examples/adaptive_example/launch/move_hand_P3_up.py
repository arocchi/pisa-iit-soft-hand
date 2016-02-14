#!/usr/bin/env python
import rospy
from tf.msg import tfMessage
from pyExp.msg import messageFromQuat


if __name__ == '__main__':
    rospy.init_node('hand_lifter')
    # publish to cmd_vel
    p = rospy.Publisher('/tf_static', tfMessage, queue_size=10)

    x = -0.28
    y = -0.085
    z = 0.13
    qx = 0.49999984146591736
    qy = 0.4996018366446334
    qz = 0.323258330753712
    qw = 0.5003981633553666

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
