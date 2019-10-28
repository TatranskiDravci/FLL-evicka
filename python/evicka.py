from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left = Motor(Port.B)
right = Motor(Port.C)
sLeft = Motor(Port.D)
sRight = Motor(Port.A)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
robot = DriveBase(left, right, 43, 180)
watch = StopWatch()

def reset():
    left.reset_angle(0)
    right.reset_angle(0)
    sLeft.reset_angle(0)
    sRight.reset_angle(0)
    gyro.reset_angle(0)

def mov(spd=80, tm=1):
    watch.resume()
    watch.reset()
    while(1):
        robot.drive(spd, gyro.angle() * -1)
        if(watch.time() >= tm*1000):
            break
    robot.stop()
    watch.pause()

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
                        
def stick(spd=200, ang=0):
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sLeft.stop()

def claw(spd=200, ang=0):
    sRight.run_target(spd, ang, Stop.BRAKE)
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sRight.stop()
    sLeft.stop()
