#!/usr/bin/env python
import os

#Connect the controller with the joy package
#maybe check if the controller is conncted. 
def initializeController():
    print("The controller is being initialized...")
    #os.system("bash runJoy.sh") #needed to be in dir to run

    #runs file from root dir
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "runJoy.sh")
    os.system("bash " + str(DATA_PATH))