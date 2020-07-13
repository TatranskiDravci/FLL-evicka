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
robot = DriveBase(left, right, 44, 180)
watch = StopWatch()

def recal():
    gyro.speed()
    gyro.angle()
    time.sleep(1)

def reset():
    left.reset_angle(0)
    gyro.reset_angle(0)

def rot(max=40, ang=0):
    # drive backwards
    backwards = False
    # base speed
    base = 20
    # start with base speed
    spd = base
    diff = max / base

    # rotation loop
    while(True):
        # gradual speedup and slowdown
        if(ang - 3 < gyro.angle() > 3 and spd < max):
            spd = spd + diff
        elif(ang - 3 > gyro.angle() or gyro.angle() < 3 and spd > base):
            spd = spd - diff

        # check if measured angle equals desired angle
        if(gyro.angle() != ang):
            if(backwards == False):
                if(gyro.angle() > ang):
                    right.run(spd)
                    left.run(spd * -1)
                else:
                    left.run(spd)
                    right.run(spd * -1)
            else:
                if(gyro.angle() > ang):
                    right.run(spd)
                    left.run(spd * -1)
                else:
                    left.run(spd)
                    right.run(spd * -1)
        # stop robot and do a final angle check
        else:
            left.stop(Stop.HOLD)
            right.stop(Stop.HOLD)
            time.sleep(0.5)
            if(gyro.angle() == ang):
                gyro.reset_angle(0)
                break
            else:
                backwards = True

def movf(spd=40, ang=360):
    while(1):
        if(((left.angle() + right.angle())/2) < ang and ((left.angle() + right.angle())/2) < (ang - 120)):
            robot.drive(spd, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) < ang and ((left.angle() + right.angle())/2) >= (ang - 120)):
            if(((left.angle() + right.angle())/2) >= (ang - 60)):
                robot.drive(spd/2, gyro.angle() * -1)
            else:
                robot.drive(spd/(3/2), gyro.angle() * -1)
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
            if(((left.angle() + right.angle())/2) <= (-ang + 60)):
                robot.drive((spd/2)*-1, gyro.angle() * -1)
            else:
                robot.drive((spd/(3/2))*-1, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) <= -ang):
            robot.stop(Stop.BRAKE)
            break
    robot.stop()
    rot(25, 0)
    reset()
