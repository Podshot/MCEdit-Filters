from pymclevel.nbt import TAG_Byte_Array
from pymclevel.box import Vector
from pymclevel.schematic import MCSchematic
import time

displayName = "Pyramid Maker"

inputs = (
    ("Levels", (2,2,10)),
    ("Box must be 1x1x1!","label"),
    )

def lvl1():
    e = MCSchematic(shape=(3,1,3),filename='')
    e._Blocks = [[[19,19,19],[19,19,19],[19,19,19]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0],[0,0,0],[0,0,0]]])
    return e

def lvl2():
    e = MCSchematic(shape=(5,1,5),filename='')
    e._Blocks = [[[19,19,19,19,19],[19,19,19,19,19],[19,19,19,19,19],[19,19,19,19,19],[19,19,19,19,19]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]])
    return e

def lvl3():
    e = MCSchematic(shape=(7,1,7),filename='')
    e._Blocks = [[[19,19,19,19,19,19,19],[19,19,19,19,19,19,19],[19,19,19,19,19,19,19],[19,19,19,19,19,19,19],[19,19,19,19,19,19,19],[19,19,19,19,19,19,19],[19,19,19,19,19,19,19]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]])
    return e

def lvl4():

def lvl5():

def lvl6():

def lvl7():

def lvl8():

def lvl9():

def lvl10():

l1 = lvl1()
l2 = lvl2()
l3 = lvl3()
l4 = lvl4()
l5 = lvl5()
l6 = lvl6()
l7 = lvl7()
l8 = lvl8()
l9 = lvl9()
l10 = lvl10()

def levelOne(level, dest):
    vec = Vector(0,0,0)
    level.copyBlocksFrom(l1,l1.bounds,vec + dest)

def levelTwo(level, dest, box):
    vec = Vector(0,0,0)
    level.copyBlocksFrom(l2,l2.bounds,vec + dest)
    level.markDirtyBox(box)
    levelOne(level, dest)

def levelThree(level, dest, box):
    vec = Vector(0,0,0)
    level.copyBlocksFrom(l3,l3.bounds,vec + dest)
    level.markDirtyBox(box)
    levelTwo(level, dest, box)











def perform(level, box, options):
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
    level.setBlockAt(box.minx, box.miny, box.minz, 19)
    level.setBlockDataAt(box.minx, box.miny, box.minz, 0)
    if levels == 2:
        levelOne(level,[box.minx,box.miny,box.minz])
        level.markDirtyBox(box)
    if levels == 3:
        levelTwo(level,[box.minx,box.miny,box.minz], box)
        level.markDirtyBox(box)
    if levels == 4:
        levelThree(level,[box.minx,box.miny,box.minz], box)
        level.markDirtyBox(box)
    if levels == 5:
        levelFour(level,[box.minx,box.miny,box.minz], box)
        level.markDirtyBox(box)
    
