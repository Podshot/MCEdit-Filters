# This is filter Add Vines. It can randomly attach vines on the leaves blocks and also grow them as you wish.
# It's good with MCEdit Forester filter.
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters

import random
inputs = (
  ("Vines", "blocktype"),
  ("Leaves", "blocktype"),
  ("Length", (10,1,30)),
  ("Length Variability", (5,1,30)),
  ("Chance",(50,0,100))
)
displayName = "Add Vines"
# Vine data constants
BIT_SOUTH = 1
BIT_WEST = 2
BIT_NORTH = 4
BIT_EAST = 8

# Returns collections of X/Z coordinates of leaves around specified block in level
def findLeaves(level,x,y,z,leaveType,leaveData):
    result = []
    rangeX = range(x-1,x+1)
    rangeZ = range(z-1,z+1)
    for rX in rangeX:
        if(level.blockAt(rX,y,z) == leaveType and level.blockDataAt(rX,y,z) == leaveData):
            result.append([rX,z])
    for rZ in rangeZ:
        if(level.blockAt(x,y,rZ) == leaveType and level.blockDataAt(x,y,rZ) == leaveData):
            result.append([x,rZ])
    return result
def perform(level, box, options):
    
    vineType = options["Vines"].ID
    if(vineType != 106):
        vineData = options["Vines"].blockData
        
    leaveType = options["Leaves"].ID
    leaveData = options["Leaves"].blockData

    chance = options["Chance"]
    
    length = options["Length"]
    len_diversity = options["Length Diversity"]
    for x in xrange(box.minx, box.maxx):
        for z in xrange(box.minz, box.maxz):
            for y in xrange(box.miny, box.maxy):
                if(level.blockAt(x,y,z) == 0):
                    level.getChunk(x/16,z/16).dirty = True
                    if(vineType == 106):
                        vineData = 0
                        # find leaves attached to the block
                        leaves = findLeaves(level,x,y,z,leaveType,leaveData)
                        for leaf in leaves:
                            if(leaf[0] > x):
                                #EAST
                                vineData = vineData + BIT_EAST
                            if(leaf[0] < x):
                                #WEST
                                vineData = vineData + BIT_WEST
                            if(leaf[1] > z):
                                #SOUTH
                                vineData = vineData + BIT_SOUTH
                            if(leaf[1] < z):
                                #NORTH
                                vineData = vineData + BIT_NORTH
                        # if there are leaves, we can randomly choose, if we want to grow vines here
                        if(len(leaves) > 0 and random.randint(0,99) < chance):
                            yrange = range(y-length-random.randint(1,len_diversity),y)
                            for yR in yrange:
                                if(level.blockAt(x,yR,z) == 0):
                                    level.setBlockAt(x,yR,z,vineType)
                                    level.setBlockDataAt(x,yR,z,vineData)
                                else:
                                    break
                    else:
                        level.setBlockAt(x,y,z,vineType)
                        level.setBlockDataAt(x,y,z,vineData)
