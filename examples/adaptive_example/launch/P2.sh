./move_hand_P2_up.sh
./open_hand.sh
sleep 10
./move_hand_P2.sh
sleep 1
./close_hand.sh 0.5
sleep 4
echo "Finished closing"
rostopic echo -n 1 /clock > timing.txt
sleep 5
echo "Starting lift"
rostopic echo -n 1 /clock >> timing.txt
./move_hand_P2_up.sh
read
echo "Saving time"
rostopic echo -n 1 /clock >> timing.txt