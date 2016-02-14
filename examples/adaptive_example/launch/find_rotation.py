#!/usr/bin/env python
import rospy
import sys
from tf.msg import tfMessage
from pyExp.msg import messageFromRot


if __name__ == '__main__':
    rospy.init_node('rotate_node')
    # publish to cmd_vel
    p = rospy.Publisher('/tf_static', tfMessage, queue_size=2)

    x = 0
    y = 0
    z = 0.3
    roll = float(sys.argv[1])
    pitch = float(sys.argv[2])
    yaw = float(sys.argv[3])
    rospy.sleep(0.01)
    pose = messageFromRot(x, y, z, roll, pitch, yaw)
    p.publish(pose)
    p.publish(pose)
    p.publish(pose)
