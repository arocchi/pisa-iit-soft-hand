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
      x: -0.245
      y: -0.15
      z: 0.12
    rotation:
      x: 0.49999984146591736
      y: 0.4996018366446334
      z: 0.49999984146591736
      w: 0.5003981633553666"
