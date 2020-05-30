#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# motors.py
#######

from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library
from time import sleep

robot = CamJamKitRobot()

# Set the relative speeds of the two motors, between 0.0 and 1.0
motorspeed = 1.0

motorforward = (motorspeed, motorspeed)
motorbackward = (-motorspeed, -motorspeed)
motorleft = (motorspeed, 0)
motorright = (0, motorspeed)

def forward():
    print("Going Forwards")
    robot.value = motorforward

    sleep(2)

def backward():
    print("Going Backwards")
    robot.value = motorbackward

    sleep(2)

def turnRight():
    print("Going Right")
    robot.value = motorright

    sleep(2)

def turnLeft():
    print("Going Left")
    robot.value = motorleft

    sleep(2)

def stop():
    print("Stopping")
    robot.stop()
