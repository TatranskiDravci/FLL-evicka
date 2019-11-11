#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left = Motor(Port.B)
right = Motor(Port.C)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
data = open("m_angle.data", "w")

def rot(spd=40, ang=0):
    a = 1
    if(ang > 0):
        while(a == 1):
            if(gyro.angle == ang):
                left.stop(Stop.HOLD)
                right.stop(Stop.HOLD)
                gyro.reset_angle(0)
                a = 0
            left.run(spd)
            right.run(spd * -1)
            if(gyro.angle() > ang):
                while(1):
                    right.run(spd)
                    left.run(spd * -1)
                    if(gyro.angle() == ang):
                        right.stop(Stop.HOLD)
                        left.stop(Stop.HOLD)
                        gyro.reset_angle(0)
                        a = 0
                    if(gyro.angle() < ang):
                        break
                
    if(ang < 0):
        while(a == 1):
            if(gyro.angle == ang):
                left.stop(Stop.HOLD)
                right.stop(Stop.HOLD)
                gyro.reset_angle(0)
                a = 0
            left.run(spd * -1)
            right.run(spd)
            if(gyro.angle() < ang):
                while(1):
                    right.run(spd * -1)
                    left.run(spd)
                    if(gyro.angle() == ang):
                        right.stop(Stop.HOLD)
                        left.stop(Stop.HOLD)
                        gyro.reset_angle(0)
                        a = 0
                    if(gyro.angle() > ang):
                        break
    data.write(str(gyro.angle()) + "\n")

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 0 * n)

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 10 * n)

rot(40, -10)

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 20 * n)

rot(40, -20)

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 40 * n)

rot(40, -40)

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 80 * n)

rot(40, -80)

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 160 * n)

rot(40, -160)

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 320 * n)

rot(40, -320)

n = 1
for i in range(20):
    n = 0 - n
    rot(80, 640 * n)

rot(40, -640)



