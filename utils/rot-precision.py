#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

left = Motor(Port.B)
right = Motor(Port.C)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
data = open("m_angle.data", "w")

def rot(spd=40, ang=0):
    while(True):
        if(gyro.angle() > ang):
            right.run(spd)
            left.run(spd * -1)
        if(gyro.angle() < ang):
            left.run(spd)
            right.run(spd * -1)
        if(gyro.angle() == ang):
            left.stop(Stop.HOLD)
            right.stop(Stop.HOLD)
            time.sleep(0.5)
            if(gyro.angle() == ang):
                data.write(str(gyro.angle()) + "\n")
                gyro.reset_angle(0)
                break
            else:
                pass

x = 2
n = 1
sp = 40
for i in range(x):
    n = 0 - n
    rot(sp, 0 * n)

n = 1
for i in range(x):
    n = 0 - n
    rot(sp, 10 * n)

n = 1
for i in range(x):
    n = 0 - n
    rot(sp, 20 * n)

n = 1
for i in range(x):
    n = 0 - n
    rot(sp, 40 * n)

n = 1
for i in range(x):
    n = 0 - n
    rot(sp, 80 * n)
