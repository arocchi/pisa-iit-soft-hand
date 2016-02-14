./move_hand_P3_up.sh
./open_hand.sh
./sleep.py 10
./move_hand_P3.sh
./sleep.py 2
./close_hand.sh 0.2
./sleep.py 1
./close_hand.sh 0.3
./sleep.py 1
./close_hand.sh 0.4
./sleep.py 3
echo "Finished closing"
rostopic echo -n 1 /clock > timing.txt
./sleep.py 5
echo "Starting lift"
rostopic echo -n 1 /clock >> timing.txt
./move_hand_P3_up.py
echo "Finished lift"
rostopic echo -n 1 /clock >> timing.txt
./sleep.py 5
echo "Saving time before opening"
rostopic echo -n 1 /clock >> timing.txt
./open_hand.sh