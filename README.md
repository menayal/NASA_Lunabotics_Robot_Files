# NASA Lunabotics Robot Minining Competition

This repository contains files for the NASA Lunabotics Robot Minining Competition.
This repository holds a single package named "my_robot_urdf". 
The repository has files on the robot's model, configuration, and navigation. 
## Getting Started

This robot uses ROS Melodic on Ubuntu 18.04 and is developed in Python. 
Please make sure to go through these instructions with a new virtual machine to properly configure ROS on your operating system to use Python3. 
Then make sure to start the ROS Tutorials. 

https://www.miguelalonsojr.com/blog/robotics/ros/python3/2019/08/20/ros-melodic-python-3-build.html
https://gist.github.com/drmaj/20b365ddd3c4d69e37c79b01ca17587a
http://wiki.ros.org/ROS/Tutorials
### Prerequisites
Create a GitHub account and install Git on your machine. 

Go through these instructions and follow the steps: 
https://www.miguelalonsojr.com/blog/robotics/ros/python3/2019/08/20/ros-melodic-python-3-build.html
https://gist.github.com/drmaj/20b365ddd3c4d69e37c79b01ca17587a

Not absolutely necessary, but highly recommmened so you can get foundation on what is going on. 
Go through the ROS URDF Tutorials.

http://wiki.ros.org/urdf/Tutorials



### Installing

You are now ready to get these files onto your machine. 

You should already have a catkin_ws on your machine from following the ROS Tutorials.

Change into that workspace (enter your worspace name where the quotations are):
```
cd "your_ws"
```
Make sure to source your workspace if you haven't already:
```
source devel/setup.bash
```
Move into src
```
cd src
```
This is where the robot's packages live. Now you need to get my package onto your machine. 

Run either one of the two choices based on your preference:

A) HTTPS: 
```
git clone https://github.com/menayal/NASA_Lunabotics_Robot_Files.git
```
B) SSH:
```
git clone git@github.com:menayal/NASA_Lunabotics_Robot_Files.git
```
You should now have my robot's package on your workspace. 

This repository's name is different from my packages actual name, so we will change the name to what the rest of my repository uses. 
```
mv NASA_Lunabotics_Robot_Files/ new_robot_urdf 
```
Now you need to move into the root of your workspace and build the package. 
```
cd ~/"your_ws"

catkin_make
```
My package is now on your machine. There are some folders and files that you will not need. For example the "old_robot_model_files" directory or the "README.md".

This is a visual representation of what your src should look like. 
```
├── CMakeLists.txt
└── new_robot_urdf
    ├── CMakeLists.txt
    ├── config
    ├── info
    ├── launch
    ├── meshes
    ├── old_robot_model_files
    ├── package.xml
    ├── README.md
    ├── rviz
    ├── scripts
    └── urdf

```
## View robot
To be continued..

## Acknowledgments

* Credit to https://github.com/ZBO-R8io/Roberto for the assisstance and robot's URDF model.

