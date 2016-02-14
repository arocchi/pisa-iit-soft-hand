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
      x: -0.135
      y: -0.165
      z: 0.30
    rotation:
      x: -0.3235158525735361
      y: 0.6285744890169797
      z: 0.323258330753712
      w: 0.6290752391320014"
