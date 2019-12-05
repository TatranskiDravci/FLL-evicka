#!/usr/bin/env pybricks-micropython

from evicka import *

global switch
switch = 0

recal()
brick.sound.beep(1500, 500, 100)

while(1):
    if(Button.UP in brick.buttons()):
        switch = 1
    if(Button.LEFT in brick.buttons()):
        switch = 2
    if(Button.DOWN in brick.buttons()):
        switch = 3
    if(Button.RIGHT in brick.buttons()):
        switch = 4
    
    if(switch == 1):
        #Path 2
        reset()
        recal()
        # H --> acc1 (p1)
        rot(130, -16)
        movf(200, 2726)
        # acc1 --> p2
        rot(100, -7)
        movf(200, 1923)
        # p2 --> out
        movb(100, 660)
        rot(80, -110)
        movf(100, 480)
        claw(200, 150)
        movb(100, 500)
        claw(200, -150)
        rot(120, -65)
        movf(300, 3500)

    if(switch == 2):
        reset()
        movf(320, 1200)
        wait(1000)
        movb(150, 1000)

    if(switch == 3):
        pass

    if(switch == 4):
        pass
    
    switch = 0