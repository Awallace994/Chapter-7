import random
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y, pos.z, 16)
count = 0
while count < 100:
    x = random.randint(63, 73 + 1)
    y = random.randint(10, 12+ 3)
    z = random.randint(112, 112 + 3)
    
    count += 1
    mc.setBlock = 10
    time.sleep(0.1)
    mc.player.setTilePos(x, y, z)
    print(count)
    
continueAnswer = 
    
