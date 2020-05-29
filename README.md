# Raspberry Pi Web Controlled Robot With Video Stream #

Raspberry Pi Robot that can be controlled via a website with a live streaming webcam

Adapted from [James Poole's project](http://jamespoole.me/2016/04/29/web-controlled-robot-with-video-stream/) with changes as follows:

* [Adafruit motor shield v1](https://learn.adafruit.com/adafruit-motor-shield) instead of LD293 IC + proto-board
* New Python module to drive the motors through the motor shield, taking C source code this [post](https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=16118) as guideline
* [MJPG-streamer](https://sourceforge.net/projects/mjpg-streamer) streaming application instead of motion. Since it's less resource intensive, video responsiveness and quality icmproved noticeably
* Updated index.html page:
    * Removed fixed IP for streaming server (based on [Quintin Balsdon's improvement)](https://github.com/qbalsdon/WebControlledRobot)
    * Rearranged control buttons to mimic layout of most remote controls (stop button moved into center of motion arrows)