./move_hand_P2_up.sh
./open_hand.sh
./sleep.py 5
./move_hand_P2.sh
./sleep.py 1
./close_hand.sh 0.47
./sleep.py 3
echo "Finished closing"
rostopic echo -n 1 /clock > timing.txt
./sleep.py 3
echo "Starting lift"
rostopic echo -n 1 /clock >> timing.txt
./move_hand_P2_up.py
echo "Finished lift"
rostopic echo -n 1 /clock >> timing.txt
./sleep.py 5
echo "Saving time before opening"
rostopic echo -n 1 /clock >> timing.txt
./open_hand.sh