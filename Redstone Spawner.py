import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2
from random import *
from numpy import *
from pymclevel import alphaMaterials
from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
from math import sqrt
import random

# Some imports are not used, but you can never have too many imports :D
displayName = "Red-Spawner"

inputs = (
        ("Material:", alphaMaterials.YellowWool),
        ("Made by Podshot, huehuehue", "label"),
)

def setBlock(level, (block, data), x, y, z):
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

    

def platform(level, box, options):
    method = "Red-Spawner"
    print '%s: Started: %s' % (method, time.ctime())
    AIRBLOCK = 0
    AIR = (AIRBLOCK,0)
    mat = (options["Material:"].ID, options["Material:"].blockData)
    setBlock(level, mat, box.minx, box.miny, box.minz)
    print '%s: Ended: %s' % (method, time.ctime())
    
