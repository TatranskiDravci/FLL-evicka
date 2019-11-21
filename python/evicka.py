from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

left = Motor(Port.B)
right = Motor(Port.C)
sLeft = Motor(Port.D)
sRight = Motor(Port.A)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
robot = DriveBase(left, right, 44, 180)
watch = StopWatch()

def recal():
    gyro.speed()
    gyro.angle()
    time.sleep(1)

def reset():
    left.reset_angle(0)
    right.reset_angle(0)
    sLeft.reset_angle(0)
    sRight.reset_angle(0)
    gyro.reset_angle(0)

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
                gyro.reset_angle(0)
                break

def stick(spd=200, ang=0):
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sLeft.stop()

def claw(spd=200, ang=0):
    sRight.run_target(spd, ang, Stop.BRAKE)
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sRight.stop()
    sLeft.stop()

def mov(spd=40, tm=1, amm=20):
    watch.resume()
    watch.reset()
    while(1):
        robot.drive(spd, gyro.angle() * -1)
        if(watch.time() >= tm*1000):
            a = spd
            if(amm <= 0):
                break
            while(a != 0):
                a = a - amm
                if(a < 0):
                    break
                robot.drive(a, gyro.angle() * -1)
            break
    robot.stop()
    watch.pause()
    rot(20, 0)
    reset()
