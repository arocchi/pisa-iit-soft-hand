#!/usr/bin/env python
import numpy.random
import numpy.linalg
import PyKDL as kdl
import rospy
#import roslib
#import sys
from tf.msg import tfMessage
from geometry_msgs.msg import TransformStamped
rospy.init_node('hand_shaker')

# create a twist message, fill in the details


def messageFromRot(x, y, z, roll, pitch, yaw):
    tf_pose = TransformStamped()
    tf_pose.header.frame_id = "world"
    tf_pose.header.stamp = rospy.Time.now()
    tf_pose.child_frame_id = "box_desired"
    tf_pose.transform.translation.x = x
    tf_pose.transform.translation.y = y
    tf_pose.transform.translation.z = z
    quat = kdl.Rotation.EulerZYX(0, 1.57, -1.1).GetQuaternion()
    tf_pose.transform.rotation.x = quat[0]
    tf_pose.transform.rotation.y = quat[1]
    tf_pose.transform.rotation.z = quat[2]
    tf_pose.transform.rotation.w = quat[3]
    tf_msg = tfMessage([tf_pose])
    return tf_msg


def messageFromQuat(x, y, z, qx, qy, qz, qw):
    tf_pose = TransformStamped()
    tf_pose.header.frame_id = "world"
    tf_pose.header.stamp = rospy.Time.now()
    tf_pose.child_frame_id = "box_desired"
    tf_pose.transform.translation.x = x
    tf_pose.transform.translation.y = y
    tf_pose.transform.translation.z = z
    tf_pose.transform.rotation.x = qx
    tf_pose.transform.rotation.y = qy
    tf_pose.transform.rotation.z = qz
    tf_pose.transform.rotation.w = qw
    tf_msg = tfMessage([tf_pose])
    return tf_msg


# by default, move the hand by 0.05m in a random direction. If the
# experiment is in the custom_pert dict, use that value
DEFAULT_SHAKING_PERT = 0.05
custom_pert = {}


def get_shake_perturbation():
    print "shaking object"
    shake_pert = DEFAULT_SHAKING_PERT

    random_dist = (numpy.random.random_sample(3) - 0.5)
    random_dist /= numpy.linalg.norm(random_dist)
    random_dist *= shake_pert

    return random_dist


if __name__ == '__main__':
    # publish to cmd_vel
    p = rospy.Publisher('/tf_static', tfMessage)

    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
    qx = float(sys.argv[4])
    qy = float(sys.argv[5])
    qz = float(sys.argv[6])
    qx = float(sys.argv[7])

    shake_disturbance = get_shake_perturbation()

    #nominal_pos = messageFromQuat(x, y, z, qx, qy, qz, qw)
    perturbed_pos = messageFromQuat(x + random_dist[0],
                                    y + random_dist[1],
                                    z + random_dist[2],
                                    qx, qy, qz, qw)

    #p.publish(nominal_pos)
    p.publish(perturbed_pos)
