# This filter creates Traz-Landers Redstone Controlled Spawner Layout
# This was created by Podshot
# If you modify this filter, please give credit to Podshot
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
import time # for timing
from numpy import *
from pymclevel import alphaMaterials
from pymclevel.schematic import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
from pymclevel.nbt import TAG_Byte_Array
from pymclevel.box import Vector
from math import sqrt
import random

# Some imports are not used, but you can never have too many imports :D
displayName = "Red-Spawner"

inputs = (
        ("Extend amount", (0,0,10)),
        ("Made by Podshot", "label"),
        ("Change the sponge that is generated", "label"),
        ("To a spawner that spawns a spawner minecart between", "label"),
        ("The sponge and the dispenser", "label"),
        ("Make sure to add a lava bucket to the dispenser before use!", "label"),
        ("", "label"),
        ("It will generate the layout towards the west, put the selection box", "label"),
        ("were the inupt is. Make sure the selection box is 1x1x1!", "label"),
)


def createSchematic():
    e = MCSchematic(shape=(9,6,3),filename='')
    e._Blocks = [[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,20,0],[0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,19,0],[0,0,0,0,0,0,20,0,20],[1,0,1,0,0,1,1,23,1]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[93,1,93,1,75,55,55,93,55]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,76,1,55,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,1,55,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,55,0,0,0,0,0,0,0]]]
    e.root_tag['Data'] = pymclevel.nbt.TAG_Byte_Array([[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,2,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[1,0,9,0,1,0,0,9,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,5,0,14,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,15,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,15,0,0,0,0,0,0,0]]])
    return e

def repeat(level, (block, data), x, y, z, count):
    rep = count + 1
    cur = 1
    while cur != rep:
        x = x + 9
        level.setBlockAt(x, y, z, block)
        level.setBlockDataAt(x, y, z, data)
        level.setBlockAt(x+1, y, z, 23)
        level.setBlockDataAt(x+1, y, z, 2)
        level.setBlockAt(x+2, y, z, block)
        level.setBlockDataAt(x+2, y, z, data)
        level.setBlockAt(x, y+1, z, 55)
        level.setBlockDataAt(x, y+1, z, 0)
        level.setBlockAt(x+1, y+1, z, 93)
        level.setBlockDataAt(x+1, y+1, z, 9)
        level.setBlockAt(x+2, y+1, z, 55)
        level.setBlockDataAt(x+2, y+1, z, 0)
        level.setBlockAt(x, y, z-1, 1)
        level.setBlockDataAt(x, y, z-1, 0)
        level.setBlockAt(x, y, z+1, 2)
        level.setBlockDataAt(x, y, z+1, 0)
        
        
    
def setBlock(level, (block, data), x, y, z):
    # Credit to Abrightmoore for helping me with repeater directions
    counter = 9
    con = 1
    # Start Generation
    level.setBlockAt(x, y, z, block)
    level.setBlockDataAt(x, y, z, data)
    level.setBlockAt(x+2, y, z, block)
    level.setBlockDataAt(x+2, y, z, data)
    # First Row generated
    level.setBlockAt(x, y+1, z, 93)
    level.setBlockDataAt(x, y+0, z, con%16)
    level.setBlockAt(x+2, y+1, z, 93)
    level.setBlockDataAt(x+2, y+1, z, counter%16)
    # First Repeater level generated
    level.setBlockAt(x+1, y+1, z, block)
    level.setBlockDataAt(x+1, y+1, z, data)
    level.setBlockAt(x+3, y+1, z, block)
    level.setBlockDataAt(x+3, y+1, z, data)
    # Second Row Generated
    level.setBlockAt(x+4, y+1, z, 75)
    level.setBlockDataAt(x+4, y+1, z, 0x1)
    # Redstone Torch Generated
    level.setBlockAt(x+1, y+2, z, 76)
    level.setBlockDataAt(x+1, y+2, z, 0)
    level.setBlockAt(x+2, y+2, z, block)
    level.setBlockDataAt(x+2, y+2, z, data)
    level.setBlockAt(x+3, y+2, z, 55)
    level.setBlockDataAt(x+3, y+2, z, 0)
    # Third Line Generated
    level.setBlockAt(x+1, y+3, z, block)
    level.setBlockDataAt(x+1, y+3, z, data)
    level.setBlockAt(x+2, y+3, z, 55)
    level.setBlockDataAt(x+2, y+3, z, 0)
    # Fourth Line generated
    level.setBlockAt(x+1, y+4, z, 55)
    level.setBlockDataAt(x+1, y+4, z, 0)
    # Last line generated
    # Start Generation of the next section
    level.setBlockAt(x+5, y, z, block)
    level.setBlockDataAt(x+5, y, z, data)
    level.setBlockAt(x+6, y, z, block)
    level.setBlockDataAt(x+6, y, z, data)
    level.setBlockAt(x+7, y, z, 23)
    level.setBlockDataAt(x+7, y, z, 0x3)
    # Generates blocks next to spawner location
    level.setBlockAt(x+6, y, z+1, block)
    level.setBlockDataAt(x+6, y, z+1, data)
    level.setBlockAt(x+6, y, z+2, block)
    level.setBlockDataAt(x+6, y, z+2, data)
    level.setBlockAt(x+7, y, z+2, 19)
    level.setBlockDataAt(x+7, y, z+2, 0)
    level.setBlockAt(x+8, y, z, block)
    level.setBlockDataAt(x+8, y, z, data)
    level.setBlockAt(x+8, y, z+1, block)
    level.setBlockDataAt(x+8, y, z+1, data)
    level.setBlockAt(x+7, y-1, z+1, block)
    level.setBlockDataAt(x+7, y-1, z+1, data)
    level.setBlockAt(x+8, y, z+2, block)
    level.setBlockDataAt(x+8, y, z+2, data)
    # Starts generating blocks under the redstone wire
    level.setBlockAt(x+9, y, z, block)
    level.setBlockDataAt(x+9, y, z, data)
    level.setBlockAt(x+9, y, z-1, block)
    level.setBlockDataAt(x+9, y, z-1, data)
    level.setBlockAt(x+8, y-1, z-1, block)
    level.setBlockDataAt(x+8, y-1, z-1, data)
    level.setBlockAt(x+7, y, z-1, block)
    level.setBlockDataAt(x+7, y, z-1, data)
    # Starts generating the last of the redstone
    level.setBlockAt(x+5, y+1, z, 55)
    level.setBlockDataAt(x+5, y+1, z, 0)
    level.setBlockAt(x+6, y+1, z, 55)
    level.setBlockDataAt(x+6, y+1, z, 0)
    level.setBlockAt(x+7, y+1, z, 55)
    level.setBlockDataAt(x+7, y+1, z, 0)
    level.setBlockAt(x+8, y+1, z, 93)
    level.setBlockDataAt(x+8, y+1, z, 0x1)
    level.setBlockAt(x+9, y+1, z, 55)
    level.setBlockDataAt(x+9, y+1, z, 0)
    level.setBlockAt(x+9, y+1, z-1, 55)
    level.setBlockDataAt(x+9, y+1, z-1, 0)
    level.setBlockAt(x+8, y, z-1, 93)
    level.setBlockDataAt(x+8, y, z-1, 0x7)
    # End of generation


def perform(level, box, options):
    platform(level, box, options)
    level.markDirtyBox(box)

red = createSchematic()

def place(level,dest):
    vec = Vector(0,1,-2)
    level.copyBlocksFrom(red,red.bounds,vec + dest)

def platform(level, box, options):
    method = "Red-Spawner"
    print '%s: Started: %s' % (method, time.ctime())
    AIRBLOCK = 0
    AIR = (AIRBLOCK,0)
    times = options["Extend amount"]
    place(level,[box.minx,box.miny,box.minz])
    # Calls the function "setBlock" and provides it with its required arguments"
    #setBlock(level, mat, box.minx, box.miny, box.minz)
    #if times != 0:
        #repeat(level, mat, box.minx, box.miny, box.minz, times)
    print '%s: Ended: %s' % (method, time.ctime())
