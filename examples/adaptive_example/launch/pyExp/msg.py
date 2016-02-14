import rospy
import PyKDL as kdl
from tf.msg import tfMessage
from geometry_msgs.msg import TransformStamped


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
