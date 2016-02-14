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
      y: -0.2
      z: 0.13
    rotation:
      x: 0.4111482550562382
      y: 0.5749425614866617
      z: 0.5754005860467192
      w: 0.41147579385968597"
