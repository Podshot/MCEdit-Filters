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
        ("Building", tuple(Build.keys())),
        ("Note: This filter does not generate doors", "label"),
)

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
    level.setBlockAt(x+5, y, z, 4)
    level.setBlockDataAt(x+5, y, z, 0)
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
    level.setBlockAt(x+5, y, z+1, 4)
    level.setBlockDataAt(x+5, y, z+1, 0)
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
    level.setBlockAt(x+5, y, z+2, 4)
    level.setBlockDataAt(x+5, y, z+2, 0)
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
    level.setBlockAt(x+5, y, z-1, 4)
    level.setBlockDataAt(x+5, y, z-1, 0)
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
    level.setBlockAt(x+5, y, z-2, 4)
    level.setBlockDataAt(x+5, y, z-2, 0)
    # Finish first row of generation
    level.setBlockAt(x, y+1, z+1, 5)
    level.setBlockDataAt(x, y+1, z+1, 0)
    level.setBlockAt(x, y+1, z-1, 5)
    level.setBlockDataAt(x, y+1, z-1, 0)
    # Start Back Wall Generation
    level.setBlockAt(x+5, y+1, z, 5)
    level.setBlockDataAt(x+5, y+1, z, 0)
    level.setBlockAt(x+5, y+1, z+1, 5)
    level.setBlockDataAt(x+5, y+1, z+1, 0)
    level.setBlockAt(x+5, y+1, z-1, 5)
    level.setBlockDataAt(x+5, y+1, z-1, 0)
    level.setBlockAt(x+5, y+1, z+1, 5)
    level.setBlockDataAt(x+5, y+1, z+1, 0)
    # Back Wall Generated
    level.setBlockAt(x, y+1, z+2, 4)
    level.setBlockDataAt(x, y+1, z+2, 0)
    level.setBlockAt(x+1, y+1, z+2, 5)
    level.setBlockDataAt(x+1, y+1, z+2, 0)
    level.setBlockAt(x+2, y+1, z+2, 5)
    level.setBlockDataAt(x+2, y+1, z+2, 0)
    level.setBlockAt(x+3, y+1, z+2, 5)
    level.setBlockDataAt(x+3, y+1, z+2, 0)
    level.setBlockAt(x+4, y+1, z+2, 5)
    level.setBlockDataAt(x+4, y+1, z+2, 0)
    level.setBlockAt(x+5, y+1, z+2, 4)
    level.setBlockDataAt(x+5, y+1, z+2, 0)
    # Wall One Generated
    level.setBlockAt(x, y+1, z-2, 4)
    level.setBlockDataAt(x, y+1, z-2, 0)
    level.setBlockAt(x+1, y+1, z-2, 5)
    level.setBlockDataAt(x+1, y+1, z-2, 0)
    level.setBlockAt(x+2, y+1, z-2, 5)
    level.setBlockDataAt(x+2, y+1, z-2, 0)
    level.setBlockAt(x+3, y+1, z-2, 5)
    level.setBlockDataAt(x+3, y+1, z-2, 0)
    level.setBlockAt(x+4, y+1, z-2, 5)
    level.setBlockDataAt(x+4, y+1, z-2, 0)
    level.setBlockAt(x+5, y+1, z-2, 4)
    level.setBlockDataAt(x+5, y+1, z-2, 0)
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
    level.setBlockAt(x+4, y+2, z+2, 5)
    
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
        print 'Choose Blacksmith'

    elif build == "2":
        print 'Choose Church'

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
        

    elif build == "8":
        print 'Choose Farm'
    
