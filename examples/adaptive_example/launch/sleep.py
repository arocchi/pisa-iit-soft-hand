#!/usr/bin/env python
import rospy
import sys


rospy.init_node('sleeper')
rospy.sleep(float(sys.argv[1]))
