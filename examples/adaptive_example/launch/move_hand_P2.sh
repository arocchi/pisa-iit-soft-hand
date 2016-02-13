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
      x: -0.135
      y: -0.165
      z: 0.205
    rotation:
      x: -0.3235158525735361
      y: 0.6285744890169797
      z: 0.323258330753712
      w: 0.6290752391320014"
