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
    b = 0
    while(True):
        if(gyro.angle() > ang and b == 0): 
            right.run(spd)
            left.run(spd * -1)
        if(gyro.angle() < ang and b == 0):
            left.run(spd)
            right.run(spd * -1)
        if(gyro.angle() > ang and b == 1): 
            right.run(40)
            left.run(-40)
        if(gyro.angle() < ang and b == 1):
            left.run(40)
            right.run(-40)
        if(gyro.angle() == ang):
            left.stop(Stop.HOLD)
            right.stop(Stop.HOLD)
            time.sleep(0.5)
            if(gyro.angle() == ang):
                gyro.reset_angle(0)
                break
            if(gyro.angle() != ang):
                b = 1

def stickL(spd=200, ang=0):
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sLeft.stop()
    sLeft.reset_angle(0)

def stickR(spd=200, ang=0):
    sRight.run_target(spd, ang * -1, Stop.BRAKE)
    sRight.stop()
    sRight.reset_angle(0)

def claw(spd=200, ang=0):
    sRight.run_target(spd, ang, Stop.BRAKE)
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sRight.stop()
    sLeft.stop()
    sLeft.reset_angle(0)
    sRight.reset_angle(0)

def movf(spd=40, ang=360):
    while(1):
        if(((left.angle() + right.angle())/2) < ang and ((left.angle() + right.angle())/2) < (ang - 120)):
            robot.drive(spd, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) < ang and ((left.angle() + right.angle())/2) >= (ang - 120)):
            robot.drive(spd/2, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) >= ang):
            robot.stop(Stop.BRAKE)
            break
    robot.stop()
    rot(25, 0)
    reset()
        
def movb(spd=40, ang=360):
    while(1):
        if(((left.angle() + right.angle())/2) > -ang and ((left.angle() + right.angle())/2) > (-ang + 120)):
            robot.drive(-spd, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) > -ang and ((left.angle() + right.angle())/2) <= (-ang + 120)):
                robot.drive((spd/2)*-1, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) <= -ang):
            robot.stop(Stop.BRAKE)
            break
    robot.stop()
    rot(25, 0)
    reset()
