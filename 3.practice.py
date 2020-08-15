"""
38  0-8 花
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()



















while True:
    x,y,z=mc.player.getPos()
    color=random.randrange(9)    
    mc.setBlock(x,y,z,38,color)
    time.sleep(1)


