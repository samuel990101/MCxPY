# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:55:19 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getPos()
    color=random.randrange(0,8)
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.5)
    
    
time.sleep(5)
x,y,z=mc.player.getTilePos()
    
