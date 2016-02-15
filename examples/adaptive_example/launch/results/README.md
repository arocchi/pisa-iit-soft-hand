Timing for P1_blem,P1_blem_t{1,2,3,4} and P1_opcode, P1_opcode_t{1,2,3,4} contains the time when the grasp ends, when the lifting begins vs when the object starts to drop.
For P2_blem* it contains the time when the grasp ends, when the lifting begins, when the lifting ends, and when the object starts to drop. P2_blem_t1 uses easing while lifting, which is smoother and a necessity for the P2 grasps, which are more fragile and thus can drop the object while lifting. The same code is the used for all P3 and for P1_{blem,opcode}_t5

All data recording are stopped after the object has dropped, except of P2_blem and P2_blem_t1 (even though the object could fall)

P2_opcode_t1 and P2_opcode_t3 drop during lift (like for the P1_opcode, there is a lot of variability).

P2_blem_t2 and  P2_opcode_t2 are all recorded with automatic object dropping routine.
Same for P1_{blem,opcode}_t5, and P3_blem, P3_opcode
P3_* drop during lift
