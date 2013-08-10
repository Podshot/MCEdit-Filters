# This is filter Generate Veins. It can create random veins of ores in your selection box. Supports several vein creation algorithms
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from random import randint, random
from math import pi, sin, cos

# minecraft's floor_double thing
def floor_double(d):
    i = int(d)
    if d < i:
        return (i - 1)
    else:
        return i
# block IDs of replaceable blocks
replaceableBlocks = [1, 3]
    
# this function is from WorldGenMinable, but it's rewritten in python  
def generateVeinMC(level, x, y, z, blockID, blockData, blockCount, respectRepl):
    f = random() * pi
    d0 = (x + 8.0) + sin(f) * blockCount / 8.0
    d1 = (x + 8.0) - sin(f) * blockCount / 8.0
    d2 = (z + 8.0) + cos(f) * blockCount / 8.0
    d3 = (z + 8.0) - cos(f) * blockCount / 8.0
    d4 = y + randint(0, 3) - 2.0
    d5 = y + randint(0, 3) - 2.0
    rang = range(blockCount)
    for __l in rang:
        l = __l * 1.0
        d6 = d0 + (d1 - d0) * l / (blockCount * 1.0)
        d7 = d4 + (d5 - d4) * l / (blockCount * 1.0)
        d8 = d2 + (d3 - d2) * l / (blockCount * 1.0)
        d9 = random() * (blockCount * 1.0) / 16.0
        d10 = sin(l * pi / (blockCount * 1.0) + 1.0) * d9 + 1.0
        d11 = sin(l * pi / (blockCount * 1.0) + 1.0) * d9 + 1.0
        i1 = floor_double(d6 - d10 / 2.0)
        j1 = floor_double(d7 - d11 / 2.0)
        k1 = floor_double(d8 - d10 / 2.0)
        l1 = floor_double(d6 + d10 / 2.0)
        i2 = floor_double(d7 + d11 / 2.0)
        j2 = floor_double(d8 + d10 / 2.0)
        rang2 = range(i1, l1)
        for __k2 in rang2:
            k2 = __k2 * 1.0
            d12 = (k2 + 0.5 - d6) / (d10 / 2.0)
            if (d12 ** 2) < 1.0:
                rang3 = range(j1, i2)
                for __l2 in rang3:
                    l2 = __l2 * 1.0
                    d13 = (l2 + 0.5 - d7) / (d11 / 2.0)
                    if d12 * d12 + d13 * d13 < 1.0:
                        rang4 = range(k1, j2)
                        for __i3 in rang4:
                            i3 = __i3 * 1.0
                            d14 = (i3 + 0.5 - d8) / (d10 / 2.0)
                            if d12 * d12 + d13 * d13 + d14 * d14 < 1.0 and (not respectRepl or level.blockAt(__k2, __l2, __i3) in replaceableBlocks):
                                level.setBlockAt(__k2, __l2, __i3, blockID)
                                level.setBlockDataAt(__k2, __l2, __i3, blockData)

# Cubic vein generator
def generateVeinCubic(level, x, y, z, blockID, blockData, blockCount, respectRepl):
    xRange = range(x,x+blockCount)
    yRange = range(y,y+blockCount)
    zRange = range(z,z+blockCount)
    for yy in yRange:
        for zz in zRange:
            for xx in xRange:
                if not respectRepl or level.blockAt(xx,yy,zz) in replaceableBlocks:
                    level.setBlockAt(xx,yy,zz,blockID)
                    level.setBlockDataAt(xx,yy,zz,blockData)     
# Randomized cubic vein generator
def generateVeinRandomizedCubic(level, x, y, z, blockID, blockData, blockCount, respectRepl):
    bcRange = range(blockCount)
    for bc in bcRange:
        xO = randint(-blockCount/2,blockCount/2)
        yO = randint(-blockCount/2,blockCount/2)
        zO = randint(-blockCount/2,blockCount/2)
        if not respectRepl or level.blockAt(x+xO,y+yO,z+zO) in replaceableBlocks:
            level.setBlockAt(x+xO,y+yO,z+zO,blockID)
            level.setBlockDataAt(x+xO,y+yO,z+zO,blockData)
        else:
            bc -= 1

veinGenerators = {"(~)Minecraft-like":generateVeinMC, "Cubic":generateVeinCubic, "(~)Randomized Cubic":generateVeinRandomizedCubic}
inputs = (
  ("Ore Block", "blocktype"),
  ("Vein count per slice", 4),
  ("Minimal iterations per vein", 0),
  ("Maximal iterations per vein", 5),
  ("Iteration count doesn't have to be the same as block count. Vein generators with different iteration and block count are marked by ~. If you tick 'respect replacable blocks', iteration count may be different than block count EVEN IN NON-MARKED GENERATORS.", "label"),
  ("Minimal vein layer", 20),
  ("Maximal vein layer", 50),
  ("Veins type", tuple(sorted(veinGenerators.keys()))),
  ("Respect replaceable blocks", False),
  ("Work strictly with selection box", False),
  ("The option above is useful if you didn't use 'Select Chunks'. This fits the ore generator to the selection box. It's useful if the box is small. In case you select to strictly work with box, the vein count per slice will be the vein count per whole box.","label")
)

displayName = "Generate Veins"

def perform(level, box, options):
    blockID = options["Ore Block"].ID
    blockData = options["Ore Block"].blockData
    veinsPerSlice = options["Vein count per slice"]
    minBlocksPerVein = options["Minimal iterations per vein"]
    maxBlocksPerVein = options["Maximal iterations per vein"]
    minLayer = options["Minimal vein layer"]
    maxLayer = options["Maximal vein layer"]
    veinGenerator = veinGenerators[options["Veins type"]]
    strictBox = False
    if strictBox:
        rang = range(veinsPerSlice)
        for i in rang:
                x = randint(box.minx,box.maxx)
                y = randint(box.miny,box.maxy)
                z = randint(box.minz,box.maxz)
                blockCount = randint(minBlocksPerVein, maxBlocksPerVein)
                if (x, y, z) in box:
                    veinGenerator.__call__(level, x, y, z, blockID, blockData, blockCount, options["Respect replaceable blocks"])
    else:
        for (chunk, slices, point) in level.getChunkSlices(box):
            chunkX, chunkZ = chunk.chunkPosition
            rang = range(veinsPerSlice)
            for i in rang:
                x = chunkX * 16 + randint(0, 15)
                y = randint(minLayer, maxLayer)
                z = chunkZ * 16 + randint(0, 15)
                blockCount = randint(minBlocksPerVein, maxBlocksPerVein)
                if (x, y, z) in box:
                    veinGenerator.__call__(level, x, y, z, blockID, blockData, blockCount, options["Respect replaceable blocks"])