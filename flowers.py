import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 10)
    print(True)
    time.sleep(.00001)
