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
        reset()
        recal()
        rot(50, -15)
        mov(300, 4)
        rot(40, -13)
        mov(300, 1.7)
        mov(-80, 1)
        rot(50, 15)
        mov(-80, 1)
        rot(50, 20)
        mov(-80, 1)
        rot(50, 40)
        mov(80, 1)
        rot(60, 170)
        mov(80, 2.8)
        claw(200, 200)
        mov(-80, 3)
        claw(200, 10)
        rot(80, 75)
        mov(300, 4)

    if(switch == 2):
        reset()
        mov_n(200, 1.5)
        rot(80, 90)
        mov_n(200, 1.5)

    if(switch == 3):
        reset()
        pass
    if(switch == 4):
        reset()
        pass
    switch = 0