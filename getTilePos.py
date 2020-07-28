# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:14:48 2020

@author: 李俊毅
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

print(mc.player.getTilePos())