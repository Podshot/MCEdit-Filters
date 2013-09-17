from pymclevel.nbt import TAG_Byte_Array
from pymclevel.box import Vector
from pymclevel.schematic import MCSchematic
import time

displayName = "Pyramid Maker"

inputs = (
    ("Block:", "blockytpe"),
    ("Levels", (2,2,1data)),
    ("Box must be 1x1x1!","label"),
    )

def lvl1(block, data):
    e = MCSchematic(shape=(3,1,3),filename='')
    e._Blocks = [[[block,block,block],[block,block,block],[block,block,block]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[data,data,data],[data,data,data],[data,data,data]]])
    return e

def lvl2():
    e = MCSchematic(shape=(5,1,5),filename='')
    e._Blocks = [[[block,block,block,block,block],[block,block,block,block,block],[block,block,block,block,block],[block,block,block,block,block],[block,block,block,block,block]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[data,data,data,data,data],[data,data,data,data,data],[data,data,data,data,data],[data,data,data,data,data],[data,data,data,data,data]]])
    return e

def lvl3():
    e = MCSchematic(shape=(7,1,7),filename='')
    e._Blocks = [[[block,block,block,block,block,block,block],[block,block,block,block,block,block,block],[block,block,block,block,block,block,block],[block,block,block,block,block,block,block],[block,block,block,block,block,block,block],[block,block,block,block,block,block,block],[block,block,block,block,block,block,block]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[data,data,data,data,data,data,data],[data,data,data,data,data,data,data],[data,data,data,data,data,data,data],[data,data,data,data,data,data,data],[data,data,data,data,data,data,data],[data,data,data,data,data,data,data],[data,data,data,data,data,data,data]]])
    return e

def lvl4():
    e = MCSchematic(shape=(9,1,9),filename='')
    e._Blocks = [[[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data]]])
    return e

def lvl5():
    e = MCSchematic(shape=(9,1,9),filename='')
    e._Blocks = [[[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block],[block,block,block,block,block,block,block,block,block]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data],[data,data,data,data,data,data,data,data,data]]])
    return e

def lvl6():
    print "Not Used"

def lvl7():
    print "Not Used"

def lvl8():
    print "Not Used"

def lvl9():
    print "Not Used"

def lvl10():
    print "Not Used"

def levelOne(level, dest, block, data):
    vec = Vector(-1,-1,-1)
    level.copyBlocksFrom(lvl1(block),lvl1(data).bounds,vec + dest)

def levelTwo(level, dest, box):
    vec = Vector(-2,-2,-2)
    level.copyBlocksFrom(lvl2(block),lvl2(data).bounds,vec + dest)
    level.markDirtyBox(box)
    levelOne(level, dest, block, data)

def levelThree(level, dest, box, block, data):
    vec = Vector(-3,-3,-3)
    level.copyBlocksFrom(lvl3(block),lvl3(data).bounds,vec + dest)
    level.markDirtyBox(box)
    levelTwo(level, dest, box, block, data)

def levelFour(level, dest, box, block, data):
    vec = Vector(-4,-4,-4)
    level.copyBlocksFrom(lvl4(block),lvl4(data).bounds,vec + dest)
    level.markDirtyBox(box)
    levelThree(level, dest, box, block, data)

def levelFive(level, dest, box, block, data):
    vec = Vector(-5,-5,-5)
    level.copyBlocksFrom(lvl5(block),lvl5(data).bounds,vec + dest)
    level.markDirtyBox(box)
    levelFour(level, dest, box, block, data)











def perform(level, box, options):
    blid = options["Block:"].ID
    blda = optiond["Block:"].blockData
    levels = options["Levels"]
    boxx = box.maxx - box.minx
    boxy = box.maxy - box.miny
    boxz = box.maxz - box.minz
    if boxx != 1:
        raise Exception("Box must be 1x1x1!")
    if boxy != 1:
        raise Exception("Box must be 1x1x1!")
    if boxz != 1:
        raise Exception("Box must be 1x1x1!")
    level.setBlockAt(box.minx, box.miny, box.minz, blid)
    level.setBlockDataAt(box.minx, box.miny, box.minz, blda)
    if levels == 2:
        levelOne(level,[box.minx,box.miny,box.minz], blid, blda)
        level.markDirtyBox(box)
    if levels == 3:
        levelTwo(level,[box.minx,box.miny,box.minz], box, blid, blda )
        level.markDirtyBox(box)
    if levels == 4:
        levelThree(level,[box.minx,box.miny,box.minz], box, blid, blda)
        level.markDirtyBox(box)
    if levels == 5:
        levelFour(level,[box.minx,box.miny,box.minz], box, blid, blda)
        level.markDirtyBox(box)
    if levels == 6:
        levelFive(level,[box.minx,box.miny,box.minz], box, blid, blda)
        level.markDirtyBox(box)
    
