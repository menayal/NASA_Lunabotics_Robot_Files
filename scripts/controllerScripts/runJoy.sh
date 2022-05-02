#!/bin/bash
gnome-terminal --tab -e "bash -c \"rosparam set joy_node/dev \"/dev/input/js0\"; 
rosrun joy joy_node; exec bash\""
