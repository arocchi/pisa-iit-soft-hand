#!/usr/bin/env python
import rospy
from tf.msg import tfMessage
from pyExp.msg import messageFromQuat


if __name__ == '__main__':
    rospy.init_node('hand_lifter')
    # publish to cmd_vel
    p = rospy.Publisher('/tf_static', tfMessage,queue_size=10)

    x = -0.135
    y = -0.165
    z = 0.205
    qx = -0.3235158525735361
    qy = 0.6285744890169797
    qz = 0.323258330753712
    qw = 0.6290752391320014

    for i in xrange(196):  # to 0.4
        lifted_pos = messageFromQuat(x, y, z + i * 0.001, qx, qy, qz, qw)
        if i < 10:
            rospy.sleep(0.1)
        elif i > 190:
            rospy.sleep(0.2)
        else:
            rospy.sleep(0.05)
        p.publish(lifted_pos)
