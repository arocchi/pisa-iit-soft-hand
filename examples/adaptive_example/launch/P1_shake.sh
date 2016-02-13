./move_hand_P1_up.sh
./open_hand.sh
./move_hand_P1.sh
sleep 4
./close_hand.sh 0.9
sleep 5
echo "Finished closing"
rostopic echo -n 1 /clock > P1_timing.txt
sleep 5
echo "Starting lift"
rostopic echo -n 1 /clock >> P1_timing.txt
./move_hand_P1_up.sh
sleep 3
echo "Starting shake"
rostopic echo -n 1 /clock >> P1_timing.txt
python ./perturb.py -0.24 0.0 0.18 0.0 0.6816387600233341 0.0 0.7316888688738209
sleep 3
python ./perturb.py -0.24 0.0 0.18 0.0 0.6816387600233341 0.0 0.7316888688738209
sleep 3
python ./perturb.py -0.24 0.0 0.18 0.0 0.6816387600233341 0.0 0.7316888688738209
sleep 3
python ./perturb.py -0.24 0.0 0.18 0.0 0.6816387600233341 0.0 0.7316888688738209
sleep 3
echo "Finishing shake"
python ./perturb.py -0.24 0.0 0.18 0.0 0.6816387600233341 0.0 0.7316888688738209
sleep 3
echo "Saving time"
rostopic echo -n 1 /clock >> P1_timing.txt