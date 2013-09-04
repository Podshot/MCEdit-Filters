from pymclevel.nbt import TAG_Byte_Array
from pymclevel.box import Vector
from pymclevel.schematic import MCSchematic
import time

displayName = "Pyramid Maker"

inputs = (
    ("Levels", (1,1,10)),
    )

def lvl1():
    e = MCSchematic(shape=(3,1,3),filename='')
    e._Blocks = [[[19,19,19],[19,19,19],[19,19,19]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0],[0,0,0],[0,0,0]]])
    return e

def lvl2():

def lvl3():

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

def levelTwo(level, dest):
    vec = Vector(0,0,0)
    level.copyBlocksFrom(l2,l2.bounds,vec + dest)
    levelOne(level, dest)











def perform(level, box, options):
    level.setBlockAt(box.minx, box.miny, box.minz, 19)
    level.setBlockDataAt(box.minx, box.miny, box.minz, 0)
    
