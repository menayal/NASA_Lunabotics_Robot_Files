#!/usr/bin/env python
import os

#Connect the controller with the joy package
#maybe check if the controller is conncted. 
def initializeController():
    print("The controller is being initialized...")
    os.system("bash runJoy.sh")


