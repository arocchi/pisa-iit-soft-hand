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
      z: 0.11
    rotation:
      x: 0.2886382139493777
      y: 0.6452296092959807
      z: 0.482248334565073
      w: 0.517497127088724"
