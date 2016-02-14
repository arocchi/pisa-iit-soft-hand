#!/usr/bin/env python
import numpy.random
import numpy.linalg
import rospy
import sys
from tf.msg import tfMessage
from pyExp.msg import messageFromQuat
from pyExp.rand import get_shake_perturbation


if __name__ == '__main__':
    rospy.init_node('hand_shaker')
    p = rospy.Publisher('/tf_static', tfMessage)

    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
    qx = float(sys.argv[4])
    qy = float(sys.argv[5])
    qz = float(sys.argv[6])
    qw = float(sys.argv[7])

    shake_disturbance = get_shake_perturbation()

    perturbed_pos = messageFromQuat(
        x + shake_disturbance[0],
        y + shake_disturbance[1],
        z + shake_disturbance[2],
        qx, qy, qz, qw)

    p.publish(perturbed_pos)
