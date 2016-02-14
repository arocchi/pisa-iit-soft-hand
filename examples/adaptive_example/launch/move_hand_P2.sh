#rosrun tf2_ros static_transform_publisher -.23 -.06 0.15 0.49 0.49 .49 0.5 world box_desired
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
      x: -0.095
      y: -0.165
      z: 0.19
    rotation:
      x: -0.3697428141890589
      y: 0.6025857997014756
      z: 0.3694484952503751
      w: 0.603065846082268"
