#!/usr/bin/env python

import subprocess
from time import sleep

subprocess.call("./startMonitoring.sh")
print("started monitoring")
sleep(15)   
subprocess.call("./endMonitoring.sh")
print("ended monitoring")
