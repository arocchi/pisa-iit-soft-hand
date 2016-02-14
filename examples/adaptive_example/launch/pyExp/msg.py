import rospy
import PyKDL as kdl
from tf.msg import tfMessage
from geometry_msgs.msg import TransformStamped


def messageFromRot(x, y, z, roll, pitch, yaw):
    quat = kdl.Rotation.RPY(roll, pitch, yaw).GetQuaternion()
    return messageFromQuat(x, y, z, quat[0], quat[1], quat[2], quat[3])


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
