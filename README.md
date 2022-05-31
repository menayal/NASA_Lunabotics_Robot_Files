# NASA Lunabotics Robot Mining Competition

This repository contains files for the [NASA Lunabotics Robot Mining Competition.](https://www.nasa.gov/content/lunabotics-information)
This repository holds a single package named "my_robot_urdf". 
The repository has files on the robot's model, configuration, and navigation. 
## Getting Started

This robot uses ROS Melodic on Ubuntu 18.04 and is developed in Python. If using Python3 head over to the [python3Version](https://github.com/menayal/NASA_Lunabotics_Robot_Files/tree/python3Version) branch to walkthrough how to use that. 

Please make sure to go through these instructions with a new virtual machine to properly configure ROS on your operating system. 
Then, start the ROS Tutorials. 

* [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)

### Prerequisites
Create a GitHub account and install Git on your machine. 

Go through the [ROS URDF Tutorials](http://wiki.ros.org/urdf/Tutorials). This is not absolutely necessary, but highly recommended so you can get a good foundation on what is actually going on. 

### Installing

You are now ready to get these files onto your machine. 

You should already have a catkin_ws on your machine from following the ROS Tutorials.

Change into that workspace (enter your workspace name where the quotations are):
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

This repository's name is **different** from my packages **actual name**, so we will change the name to what the rest of my repository uses. 
```
mv NASA_Lunabotics_Robot_Files/ new_robot_urdf 
```
Now you need to move into the root of your workspace and build the package. 
```
cd ~/"your_ws"

catkin_make
```
My package is now on your machine. There are some folders and files that you will not need. For example, the "old_robot_model_files" directory or the "README.md".

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
## View the robot in RVIZ and Gazebo

RVIZ and Gazebo allow you to view your robot's URDF model.

RVIZ is a 3D visualization tool that allows you to see what the robot is seeing and doing. 

### To view the robot in RVIZ:

Move into the workspace where you downloaded the previous package (enter your workspace name where the quotations are):
```
cd "your_ws"
```
Make sure to source your workspace if you haven't already:
```
source devel/setup.bash
```
Now run:
```
roslaunch new_robot_urdf launch_rviz.launch  
```
This launches the robot into just RVIZ. It also displays the joint state publishers node that has sliders to control some of the links(parts of the robot). It allows you to see how the links move in a very simplified motion. 

### To view the robot in Gazebo:
Gazebo is a simulation tool that allows you to simulate how your robot will move around in an environment. 

Move into the workspace where you downloaded the package (enter your workspace name where the quotations are):
```
cd "your_ws"
```
Make sure to source your workspace if you haven't already:
```
source devel/setup.bash
```
Now run:
```
roslaunch new_robot_urdf nasa_bot.launch  
```
This will launch the robot in Gazebo and will also launch RVIZ at the same time. As you can see the robot is now visible in RVIZ (may take a few seconds to fully load) and Gazebo (will also take a few seconds to load).

In addition to loading the robot, the launch files also launch rqt_robot_steering. This will let you control the robot with some sliders. 

<img width="1258" alt="Screen Shot 2022-02-09 at 10 27 46 PM" src="https://user-images.githubusercontent.com/43251979/153338117-f6ae7455-4933-4f18-a219-45882c9aa000.png">

Note that Gazebo will be very slow if your computer does not have a lot of ram or processing power. If you are running a VM and it is running slow, try allocating more ram or processors in the settings where the VM is managed. 


## Acknowledgments

* Credit to [ZBO-R8io](https://github.com/ZBO-R8io/Roberto) for the assistance and robot's URDF model.

## Resources
* https://www.nasa.gov/content/lunabotics-information
* https://www.miguelalonsojr.com/blog/robotics/ros/python3/2019/08/20/ros-melodic-python-3-build.html
* https://gist.github.com/drmaj/20b365ddd3c4d69e37c79b01ca17587a
* http://wiki.ros.org/ROS/Tutorials
* http://wiki.ros.org/urdf/Tutorials

