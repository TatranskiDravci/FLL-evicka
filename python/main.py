#!/usr/bin/env pybricks-micropython

from evicka import *

global switch
switch = 0

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
        reset()
        rot(40, -16)
        mov(140, 9)
        rot(30, -3)
        mov(125, 4.5)
        mov(-80, 1)
        rot(40, 15)
        mov(-80, 0.8)
        rot(40, 20)
        mov(-80, 1)
        rot(40, 40)
        mov(80, 1)
        rot(40, 170)
        mov(80, 2.8)
        claw(200, 200)
        mov(-80, 3)
        claw(200, 10)

    if(switch == 2):
        reset()
        pass
    if(switch == 3):
        reset()
        pass
    if(switch == 4):
        reset()
        pass
    switch = 0