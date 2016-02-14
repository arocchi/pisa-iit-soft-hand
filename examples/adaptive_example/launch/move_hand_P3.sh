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
      x: -0.28
      y: -0.085
      z: 0.13
    rotation:
      x: 0.49999984146591736
      y: 0.4996018366446334
      z: 0.49999984146591736
      w: 0.5003981633553666"