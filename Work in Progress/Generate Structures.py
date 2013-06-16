# This is filter that generates buildings that can be found in a NPC Village
# This filter was created by Podshot
# If you redistribute/modify, please give credit to Podshot
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters

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
from numpy import *
import random
import time

displayName = "Generate Structures"

Build = {
    "Blacksmith": 1,
    "Church": 2,
    "Library": 3,
    "House #1": 4,
    "House #2": 5,
    "House #3": 6,
    "Fountain": 7,
    "Farm": 8,
    }

inputs = (
        ("Building", tuple(sorted(Build.keys()))),
        ("Note: This filter does not generate doors", "label"),
)

def farm(level, x, y, z):
    level.setBlockAt(x, y, z, 17)
    level.setBlockDataAt(x, y, z, 0)
    level.setBlockAt(x, y, z+1, 17)
    level.setBlockDataAt(x, y, z+1, 0)
    level.setBlockAt(x, y, z-1, 17)
    level.setBlockDataAt(x, y, z-1, 0)
    level.setBlockAt(x, y, z+2, 17)
    level.setBlockDataAt(x, y, z+2, 0)
    level.setBlockAt(x, y, z-2, 17)
    level.setBlockDataAt(x, y, z-2, 0)
    level.setBlockAt(x, y, z+3, 17)
    level.setBlockDataAt(x, y, z+3, 0)
    level.setBlockAt(x, y, z-3, 17)
    level.setBlockDataAt(x, y, z-3, 0)
    # First row generated
    level.setBlockAt(x+1, y, z+3, 17)
    level.setBlockDataAt(x+1, y, z+3, 0)
    level.setBlockAt(x+1, y, z+2, 60)
    level.setBlockDataAt(x+1, y, z+2, 0)
    level.setBlockAt(x+1, y, z+1, 60)
    level.setBlockDataAt(x+1, y, z+1, 0)
    level.setBlockAt(x+1, y, z, 9)
    level.setBlockDataAt(x+1, y, z, 0)
    level.setBlockAt(x+1, y, z-1, 60)
    level.setBlockDataAt(x+1, y, z-1, 0)
    level.setBlockAt(x+1, y, z-2, 60)
    level.setBlockDataAt(x+1, y, z-2, 0)
    level.setBlockAt(x+1, y, z-3, 17)
    level.setBlockDataAt(x+1, y, z-3, 0)
    # Second row generated
    level.setBlockAt(x+2, y, z+3, 17)
    level.setBlockDataAt(x+2, y, z+3, 0)
    level.setBlockAt(x+2, y, z+2, 60)
    level.setBlockDataAt(x+2, y, z+2, 0)
    level.setBlockAt(x+2, y, z+1, 60)
    level.setBlockDataAt(x+2, y, z+1, 0)
    level.setBlockAt(x+2, y, z, 9)
    level.setBlockDataAt(x+2, y, z, 0)
    level.setBlockAt(x+2, y, z-1, 60)
    level.setBlockDataAt(x+2, y, z-1, 0)
    level.setBlockAt(x+2, y, z-2, 60)
    level.setBlockDataAt(x+2, y, z-2, 0)
    level.setBlockAt(x+2, y, z-3, 17)
    level.setBlockDataAt(x+2, y, z-3, 0)
    # Third row generated
    level.setBlockAt(x+3, y, z+3, 17)
    level.setBlockDataAt(x+3, y, z+3, 0)
    level.setBlockAt(x+3, y, z+2, 60)
    level.setBlockDataAt(x+3, y, z+2, 0)
    level.setBlockAt(x+3, y, z+1, 60)
    level.setBlockDataAt(x+3, y, z+1, 0)
    level.setBlockAt(x+3, y, z, 9)
    level.setBlockDataAt(x+3, y, z, 0)
    level.setBlockAt(x+3, y, z-1, 60)
    level.setBlockDataAt(x+3, y, z-1, 0)
    level.setBlockAt(x+3, y, z-2, 60)
    level.setBlockDataAt(x+3, y, z-2, 0)
    level.setBlockAt(x+3, y, z-3, 17)
    level.setBlockDataAt(x+3, y, z-3, 0)
    # Fourth row generated
    level.setBlockAt(x+4, y, z+3, 17)
    level.setBlockDataAt(x+4, y, z+3, 0)
    level.setBlockAt(x+4, y, z+2, 60)
    level.setBlockDataAt(x+4, y, z+2, 0)
    level.setBlockAt(x+4, y, z+1, 60)
    level.setBlockDataAt(x+4, y, z+1, 0)
    level.setBlockAt(x+4, y, z, 9)
    level.setBlockDataAt(x+4, y, z, 0)
    level.setBlockAt(x+4, y, z-1, 60)
    level.setBlockDataAt(x+4, y, z-1, 0)
    level.setBlockAt(x+4, y, z-2, 60)
    level.setBlockDataAt(x+4, y, z-2, 0)
    level.setBlockAt(x+4, y, z-3, 17)
    level.setBlockDataAt(x+4, y, z-3, 0)
    # Fifth row generated
    level.setBlockAt(x+5, y, z+3, 17)
    level.setBlockDataAt(x+5, y, z+3, 0)
    level.setBlockAt(x+5, y, z+2, 60)
    level.setBlockDataAt(x+5, y, z+2, 0)
    level.setBlockAt(x+5, y, z+1, 60)
    level.setBlockDataAt(x+5, y, z+1, 0)
    level.setBlockAt(x+5, y, z, 9)
    level.setBlockDataAt(x+5, y, z, 0)
    level.setBlockAt(x+5, y, z-1, 60)
    level.setBlockDataAt(x+5, y, z-1, 0)
    level.setBlockAt(x+5, y, z-2, 60)
    level.setBlockDataAt(x+5, y, z-2, 0)
    level.setBlockAt(x+5, y, z-3, 17)
    level.setBlockDataAt(x+5, y, z-3, 0)
    # Sixth row generated
    level.setBlockAt(x+6, y, z+3, 17)
    level.setBlockDataAt(x+6, y, z+3, 0)
    level.setBlockAt(x+6, y, z+2, 60)
    level.setBlockDataAt(x+6, y, z+2, 0)
    level.setBlockAt(x+6, y, z+1, 60)
    level.setBlockDataAt(x+6, y, z+1, 0)
    level.setBlockAt(x+6, y, z, 9)
    level.setBlockDataAt(x+6, y, z, 0)
    level.setBlockAt(x+6, y, z-1, 60)
    level.setBlockDataAt(x+6, y, z-1, 0)
    level.setBlockAt(x+6, y, z-2, 60)
    level.setBlockDataAt(x+6, y, z-2, 0)
    level.setBlockAt(x+6, y, z-3, 17)
    level.setBlockDataAt(x+6, y, z-3, 0)
    # Seventh row generated
    level.setBlockAt(x+7, y, z+3, 17)
    level.setBlockDataAt(x+7, y, z+3, 0)
    level.setBlockAt(x+7, y, z+2, 60)
    level.setBlockDataAt(x+7, y, z+2, 0)
    level.setBlockAt(x+7, y, z+1, 60)
    level.setBlockDataAt(x+7, y, z+1, 0)
    level.setBlockAt(x+7, y, z, 9)
    level.setBlockDataAt(x+7, y, z, 0)
    level.setBlockAt(x+7, y, z-1, 60)
    level.setBlockDataAt(x+7, y, z-1, 0)
    level.setBlockAt(x+7, y, z-2, 60)
    level.setBlockDataAt(x+7, y, z-2, 0)
    level.setBlockAt(x+7, y, z-3, 17)
    level.setBlockDataAt(x+7, y, z-3, 0)
    # Eigth row generated
    level.setBlockAt(x+8, y, z, 17)
    level.setBlockDataAt(x+8, y, z, 0)
    level.setBlockAt(x+8, y, z+1, 17)
    level.setBlockDataAt(x+8, y, z+1, 0)
    level.setBlockAt(x+8, y, z-1, 17)
    level.setBlockDataAt(x+8, y, z-1, 0)
    level.setBlockAt(x+8, y, z+2, 17)
    level.setBlockDataAt(x+8, y, z+2, 0)
    level.setBlockAt(x+8, y, z-2, 17)
    level.setBlockDataAt(x+8, y, z-2, 0)
    level.setBlockAt(x+8, y, z+3, 17)
    level.setBlockDataAt(x+8, y, z+3, 0)
    level.setBlockAt(x+8, y, z-3, 17)
    level.setBlockDataAt(x+8, y, z-3, 0)

def houseOne(level, x, y, z):
    level.setBlockAt(x, y, z, 4)
    level.setBlockDataAt(x, y, z, 0)
    level.setBlockAt(x-1, y, z, 67)
    level.setBlockDataAt(x-1, y, z, 0x0)
    level.setBlockAt(x+1, y, z, 4)
    level.setBlockDataAt(x+1, y, z, 0)
    level.setBlockAt(x+2, y, z, 4)
    level.setBlockDataAt(x+2, y, z, 0)
    level.setBlockAt(x+3, y, z, 4)
    level.setBlockDataAt(x+3, y, z, 0)
    level.setBlockAt(x+4, y, z, 4)
    level.setBlockDataAt(x+4, y, z, 0)
    level.setBlockAt(x+4, y, z, 4)
    level.setBlockDataAt(x+4, y, z, 0)
    level.setBlockAt(x, y, z+1, 4)
    level.setBlockDataAt(x, y, z+1, 0)
    level.setBlockAt(x+1, y, z+1, 4)
    level.setBlockDataAt(x+1, y, z+1, 0)
    level.setBlockAt(x+2, y, z+1, 4)
    level.setBlockDataAt(x+2, y, z+1, 0)
    level.setBlockAt(x+3, y, z+1, 4)
    level.setBlockDataAt(x+3, y, z+1, 0)
    level.setBlockAt(x+4, y, z+1, 4)
    level.setBlockDataAt(x+4, y, z+1, 0)
    level.setBlockAt(x+4, y, z+1, 4)
    level.setBlockDataAt(x+4, y, z+1, 0)
    level.setBlockAt(x, y, z+2, 4)
    level.setBlockDataAt(x, y, z+2, 0)
    level.setBlockAt(x+1, y, z+2, 4)
    level.setBlockDataAt(x+1, y, z+2, 0)
    level.setBlockAt(x+2, y, z+2, 4)
    level.setBlockDataAt(x+2, y, z+2, 0)
    level.setBlockAt(x+3, y, z+2, 4)
    level.setBlockDataAt(x+3, y, z+2, 0)
    level.setBlockAt(x+4, y, z+2, 4)
    level.setBlockDataAt(x+4, y, z+2, 0)
    level.setBlockAt(x+4, y, z+2, 4)
    level.setBlockDataAt(x+4, y, z+2, 0)
    level.setBlockAt(x, y, z-1, 4)
    level.setBlockDataAt(x, y, z-1, 0)
    level.setBlockAt(x+1, y, z-1, 4)
    level.setBlockDataAt(x+1, y, z-1, 0)
    level.setBlockAt(x+2, y, z-1, 4)
    level.setBlockDataAt(x+2, y, z-1, 0)
    level.setBlockAt(x+3, y, z-1, 4)
    level.setBlockDataAt(x+3, y, z-1, 0)
    level.setBlockAt(x+4, y, z-1, 4)
    level.setBlockDataAt(x+4, y, z-1, 0)
    level.setBlockAt(x, y, z-2, 4)
    level.setBlockDataAt(x, y, z-2, 0)
    level.setBlockAt(x+1, y, z-2, 4)
    level.setBlockDataAt(x+1, y, z-2, 0)
    level.setBlockAt(x+2, y, z-2, 4)
    level.setBlockDataAt(x+2, y, z-2, 0)
    level.setBlockAt(x+3, y, z-2, 4)
    level.setBlockDataAt(x+3, y, z-2, 0)
    level.setBlockAt(x+4, y, z-2, 4)
    level.setBlockDataAt(x+4, y, z-2, 0)
    # Finish first row of generation
    level.setBlockAt(x, y+1, z+1, 5)
    level.setBlockDataAt(x, y+1, z+1, 0)
    level.setBlockAt(x, y+1, z-1, 5)
    level.setBlockDataAt(x, y+1, z-1, 0)
    # Start Back Wall Generation
    level.setBlockAt(x+4, y+1, z, 5)
    level.setBlockDataAt(x+4, y+1, z, 0)
    level.setBlockAt(x+4, y+1, z+1, 5)
    level.setBlockDataAt(x+4, y+1, z+1, 0)
    level.setBlockAt(x+4, y+1, z-1, 5)
    level.setBlockDataAt(x+4, y+1, z-1, 0)
    level.setBlockAt(x+4, y+1, z+1, 5)
    level.setBlockDataAt(x+4, y+1, z+1, 0)
    # Back Wall Generated
    level.setBlockAt(x, y+1, z+2, 4)
    level.setBlockDataAt(x, y+1, z+2, 0)
    level.setBlockAt(x+1, y+1, z+2, 5)
    level.setBlockDataAt(x+1, y+1, z+2, 0)
    level.setBlockAt(x+2, y+1, z+2, 5)
    level.setBlockDataAt(x+2, y+1, z+2, 0)
    level.setBlockAt(x+3, y+1, z+2, 5)
    level.setBlockDataAt(x+3, y+1, z+2, 0)
    level.setBlockAt(x+4, y+1, z+2, 4)
    level.setBlockDataAt(x+4, y+1, z+2, 0)
    # Wall One Generated
    level.setBlockAt(x, y+1, z-2, 4)
    level.setBlockDataAt(x, y+1, z-2, 0)
    level.setBlockAt(x+1, y+1, z-2, 5)
    level.setBlockDataAt(x+1, y+1, z-2, 0)
    level.setBlockAt(x+2, y+1, z-2, 5)
    level.setBlockDataAt(x+2, y+1, z-2, 0)
    level.setBlockAt(x+3, y+1, z-2, 5)
    level.setBlockDataAt(x+3, y+1, z-2, 0)
    level.setBlockAt(x+4, y+1, z-2, 4)
    level.setBlockDataAt(x+4, y+1, z-2, 0)
    # Second Row Generated
    # Layer #2 Generated
    level.setBlockAt(x, y+2, z+1, 5)
    level.setBlockDataAt(x, y+2, z+1, 0)
    level.setBlockAt(x, y+2, z-1, 5)
    level.setBlockDataAt(x, y+2, z-1, 0)
    level.setBlockAt(x, y+2, z+2, 4)
    level.setBlockDataAt(x, y+2, z+2, 0)
    level.setBlockAt(x, y+2, z-2, 4)
    level.setBlockDataAt(x, y+2, z-2, 0)
    # Front Wall Generated
    level.setBlockAt(x+1, y+2, z+2, 5)
    level.setBlockDataAt(x+1, y+2, z+2, 0)
    level.setBlockAt(x+2, y+2, z+2, 102)
    level.setBlockDataAt(x+2, y+2, z+2, 0)
    level.setBlockAt(x+3, y+2, z+2, 5)
    level.setBlockDataAt(x+3, y+2, z+2, 0)
    level.setBlockAt(x+4, y+2, z+2, 4)
    level.setBlockDataAt(x+4, y+2, z+2, 0)
    # Right wall generated
    level.setBlockAt(x+4, y+2, z+1, 5)
    level.setBlockDataAt(x+4, y+2, z+1, 0)
    level.setBlockAt(x+4, y+2, z, 102)
    level.setBlockDataAt(x+5, y+2, z, 0)
    level.setBlockAt(x+4, y+2, z-1, 5)
    level.setBlockDataAt(x+4, y+2, z-1, 0)
    level.setBlockAt(x+4, y+2, z-2, 4)
    level.setBlockDataAt(x+4, y+2, z-2, 0)
    # Back Wall Generated
    level.setBlockAt(x+2, y+2, z-2, 102)
    level.setBlockDataAt(x+2, y+2, z-2, 0)
    level.setBlockAt(x+1, y+2, z-2, 5)
    level.setBlockDataAt(x+1, y+2, z-2, 0)
    level.setBlockAt(x+3, y+2, z-2, 5)
    level.setBlockDataAt(x+3, y+2, z-2, 0)
    # 3rd layer generated
    level.setBlockAt(x, y+3, z, 5)
    level.setBlockDataAt(x, y+3, z, 0)
    level.setBlockAt(x, y+3, z+1, 5)
    level.setBlockDataAt(x, y+3, z+1, 0)
    level.setBlockAt(x, y+3, z-1, 5)
    level.setBlockDataAt(x, y+3, z-1, 0)
    level.setBlockAt(x, y+3, z+2, 4)
    level.setBlockDataAt(x, y+3, z+2, 0)
    level.setBlockAt(x, y+3, z-2, 4)
    level.setBlockDataAt(x, y+3, z-2, 0)
    # Front Wall generated
    level.setBlockAt(x+1, y+3, z+2, 5)
    level.setBlockDataAt(x+1, y+3, z+2, 0)
    level.setBlockAt(x+2, y+3, z+2, 5)
    level.setBlockDataAt(x+2, y+3, z+2, 0)
    level.setBlockAt(x+3, y+3, z+2, 5)
    level.setBlockDataAt(x+3, y+3, z+2, 0)
    level.setBlockAt(x+4, y+3, z+2, 4)
    level.setBlockDataAt(x+4, y+3, z+2, 0)
    # Left Wall generated
    level.setBlockAt(x+1, y+3, z-2, 5)
    level.setBlockDataAt(x+1, y+3, z-2, 0)
    level.setBlockAt(x+2, y+3, z-2, 5)
    level.setBlockDataAt(x+2, y+3, z-2, 0)
    level.setBlockAt(x+3, y+3, z-2, 5)
    level.setBlockDataAt(x+3, y+3, z-2, 0)
    level.setBlockAt(x+4, y+3, z-2, 4)
    level.setBlockDataAt(x+4, y+3, z-2, 0)
    # Right Wall generated
    level.setBlockAt(x+4, y+3, z-1, 5)
    level.setBlockDataAt(x+4, y+3, z-1, 0)
    level.setBlockAt(x+4, y+3, z, 5)
    level.setBlockDataAt(x+4, y+3, z, 0)
    level.setBlockAt(x+4, y+3, z+1, 5)
    level.setBlockDataAt(x+4, y+3, z+1, 0)
    # Back Wall generated
    # Start roof generation
    level.setBlockAt(x, y+4, z, 17)
    level.setBlockDataAt(x, y+4, z, 0)
    level.setBlockAt(x, y+4, z-1, 17)
    level.setBlockDataAt(x, y+4, z-1, 0)
    level.setBlockAt(x, y+4, z+1, 17)
    level.setBlockDataAt(x, y+4, z+1, 0)
    level.setBlockAt(x, y+4, z-2, 17)
    level.setBlockDataAt(x, y+4, z-2, 0)
    level.setBlockAt(x, y+4, z+2, 17)
    level.setBlockDataAt(x, y+4, z+2, 0)
    # First roof row
    level.setBlockAt(x+1, y+4, z+2, 17)
    level.setBlockDataAt(x+1, y+4, z+2, 0)
    level.setBlockAt(x+1, y+4, z+1, 5)
    level.setBlockDataAt(x+1, y+4, z+1, 0)
    level.setBlockAt(x+1, y+4, z, 5)
    level.setBlockDataAt(x+1, y+4, z, 0)
    level.setBlockAt(x+1, y+4, z-1, 5)
    level.setBlockDataAt(x+1, y+4, z-1, 0)
    level.setBlockAt(x+1, y+4, z-2, 17)
    level.setBlockDataAt(x+1, y+4, z-2, 0)
    # Second roof row
    level.setBlockAt(x+2, y+4, z+2, 17)
    level.setBlockDataAt(x+2, y+4, z+2, 0)
    level.setBlockAt(x+2, y+4, z+1, 5)
    level.setBlockDataAt(x+2, y+4, z+1, 0)
    level.setBlockAt(x+2, y+4, z, 5)
    level.setBlockDataAt(x+2, y+4, z, 0)
    level.setBlockAt(x+2, y+4, z-1, 5)
    level.setBlockDataAt(x+2, y+4, z-1, 0)
    level.setBlockAt(x+2, y+4, z-2, 17)
    level.setBlockDataAt(x+2, y+4, z-2, 0)
    # Third roof row
    level.setBlockAt(x+3, y+4, z+2, 17)
    level.setBlockDataAt(x+3, y+4, z+2, 0)
    level.setBlockAt(x+3, y+4, z+1, 5)
    level.setBlockDataAt(x+3, y+4, z+1, 0)
    level.setBlockAt(x+3, y+4, z, 5)
    level.setBlockDataAt(x+3, y+4, z, 0)
    level.setBlockAt(x+3, y+4, z-1, 5)
    level.setBlockDataAt(x+3, y+4, z-1, 0)
    level.setBlockAt(x+3, y+4, z-2, 17)
    level.setBlockDataAt(x+3, y+4, z-2, 0)
    # Fourth roof row
    level.setBlockAt(x+4, y+4, z+2, 17)
    level.setBlockDataAt(x+4, y+4, z+2, 0)
    level.setBlockAt(x+4, y+4, z+1, 5)
    level.setBlockDataAt(x+4, y+4, z+1, 0)
    level.setBlockAt(x+4, y+4, z, 5)
    level.setBlockDataAt(x+4, y+4, z, 0)
    level.setBlockAt(x+4, y+4, z-1, 5)
    level.setBlockDataAt(x+4, y+4, z-1, 0)
    level.setBlockAt(x+4, y+4, z-2, 17)
    level.setBlockDataAt(x+4, y+4, z-2, 0)
    # Last roof row
    level.setBlockAt(x+4, y+4, z, 17)
    level.setBlockDataAt(x+4, y+4, z, 0)
    level.setBlockAt(x+4, y+4, z-1, 17)
    level.setBlockDataAt(x+4, y+4, z-1, 0)
    level.setBlockAt(x+4, y+4, z+1, 17)
    level.setBlockDataAt(x+4, y+4, z+1, 0)
    level.setBlockAt(x+4, y+4, z-2, 17)
    level.setBlockDataAt(x+4, y+4, z-2, 0)
    level.setBlockAt(x+4, y+4, z+2, 17)
    level.setBlockDataAt(x+4, y+4, z+2, 0)
    
def perform(level, box, options):
    method = "Generator"
    findIn(level, box, options)
    print '%s: Ended: %s' % (method, time.ctime())
    level.markDirtyBox(box)
        
def findIn(level, box, options):
    build = options["Building"]
    method = "Generator"
    print '%s: Started: %s' % (method, time.ctime())
    print '%s: Choose building: %s' % (method, build)
    # Start input finder
    if build == "1":
        print 'Test'
    elif build == "2":
        print 'Choose'
    elif build == "3":
        print 'Choose Library'
    elif build == "House #1":
        houseOne(level, box.minx, box.miny, box.minz)
    elif build == "5":
        print 'Choose House #2'
    elif build == "6":
        print 'Choose House #3'
    elif build == "7":
        print 'Choose Fountain'
    elif build == "Farm":
        farm(level, box.minx, box.miny, box.minz)
