#rosrun tf2_ros static_transform_publisher -.24 .0 0.30 0.0 0.7068 0.0 0.7074 world box_desired
rostopic pub --once /tf_static tf/tfMessage "transforms:
- header:
    seq: 0
    stamp:
      secs: 0
      nsecs: 0
    frame_id: 'world'
  child_frame_id: 'box_desired'
  transform:
    translation:
      x: -0.1
      y: -0.18
      z: 0.30
    rotation:
      x: -0.3697428141890589
      y: 0.6025857997014756
      z: 0.3694484952503751
      w: 0.603065846082268"
