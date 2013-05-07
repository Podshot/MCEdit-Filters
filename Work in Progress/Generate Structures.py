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

displayName = "Generate Structure"

build = {
    "Blacksmith": smith,
    "Church": church,
    "Library": lib,
    "House #1": h1,
    "House #2": h2,
    "House #3": h3,
    "Fountain": foun,
    "Farm": farm,
    }

inputs = (
        ("Building", tuple(build.keys())),
        ("Note: This filter does not generate doors", "label"),
)

def end(level, box, options):
    method = "Generator"
    print '%s: Ended: %s' % (method, time.ctime())
    level.markDirtyBox(box)


def perform(level, box, options):
    buil = options["Building"]
    method = "Generator"
    print '%s: Started: %s' % (method, time.ctime())
    AIRBLOCK = 0
    bx = box.minx
    by = box.miny
    bz = box.minz
    # Start input finder
    if buil == "smith":
        print 'Choose Blacksmith'

    elif buil == "church":
        print 'Choose Church'

    elif buil == "lib":
        print 'Choose Library'

    elif buil == "h1":
        print 'Choose House #1'
        level.setBlockAt(bx, by, bz, 4)
        level.setBlockDataAt(bx, by, bz, 0)
        level.setBlockAt(bx-1, by, bz, 67)
        level.setBlockDataAt(bx-1, by, bz, 0x0)
        level.setBlockAt(bx+1, by, bz, 4)
        level.setBlockDataAt(bx+1, by, bz, 0)
        level.setBlockAt(bx+2, by, bz, 4)
        level.setBlockDataAt(bx+2, by, bz, 0)
        level.setBlockAt(bx+3, by, bz, 4)
        level.setBlockDataAt(bx+3, by, bz, 0)
        level.setBlockAt(bx+4, by, bz, 4)
        level.setBlockDataAt(bx+4, by, bz, 0)
        level.setBlockAt(bx+5, by, bz, 4)
        level.setBlockDataAt(bx+5, by, bz, 0)
        level.setBlockAt(bx, by, bz+1, 4)
        level.setBlockDataAt(bx, by, bz+1, 0)
        level.setBlockAt(bx+1, by, bz+1, 4)
        level.setBlockDataAt(bx+1, by, bz+1, 0)
        level.setBlockAt(bx+2, by, bz+1, 4)
        level.setBlockDataAt(bx+2, by, bz+1, 0)
        level.setBlockAt(bx+3, by, bz+1, 4)
        level.setBlockDataAt(bx+3, by, bz+1, 0)
        level.setBlockAt(bx+4, by, bz+1, 4)
        level.setBlockDataAt(bx+4, by, bz+1, 0)
        level.setBlockAt(bx+5, by, bz+1, 4)
        level.setBlockDataAt(bx+5, by, bz+1, 0)
        level.setBlockAt(bx, by, bz+2, 4)
        level.setBlockDataAt(bx, by, bz+2, 0)
        level.setBlockAt(bx+1, by, bz+2, 4)
        level.setBlockDataAt(bx+1, by, bz+2, 0)
        level.setBlockAt(bx+2, by, bz+2, 4)
        level.setBlockDataAt(bx+2, by, bz+2, 0)
        level.setBlockAt(bx+3, by, bz+2, 4)
        level.setBlockDataAt(bx+3, by, bz+2, 0)
        level.setBlockAt(bx+4, by, bz+2, 4)
        level.setBlockDataAt(bx+4, by, bz+2, 0)
        level.setBlockAt(bx+5, by, bz+2, 4)
        level.setBlockDataAt(bx+5, by, bz+2, 0)
        level.setBlockAt(bx, by, bz-1, 4)
        level.setBlockDataAt(bx, by, bz-1, 0)
        level.setBlockAt(bx+1, by, bz-1, 4)
        level.setBlockDataAt(bx+1, by, bz-1, 0)
        level.setBlockAt(bx+2, by, bz-1, 4)
        level.setBlockDataAt(bx+2, by, bz-1, 0)
        level.setBlockAt(bx+3, by, bz-1, 4)
        level.setBlockDataAt(bx+3, by, bz-1, 0)
        level.setBlockAt(bx+4, by, bz-1, 4)
        level.setBlockDataAt(bx+4, by, bz-1, 0)
        level.setBlockAt(bx+5, by, bz-1, 4)
        level.setBlockDataAt(bx+5, by, bz-1, 0)
        level.setBlockAt(bx, by, bz-2, 4)
        level.setBlockDataAt(bx, by, bz-2, 0)
        level.setBlockAt(bx+1, by, bz-2, 4)
        level.setBlockDataAt(bx+1, by, bz-2, 0)
        level.setBlockAt(bx+2, by, bz-2, 4)
        level.setBlockDataAt(bx+2, by, bz-2, 0)
        level.setBlockAt(bx+3, by, bz-2, 4)
        level.setBlockDataAt(bx+3, by, bz-2, 0)
        level.setBlockAt(bx+4, by, bz-2, 4)
        level.setBlockDataAt(bx+4, by, bz-2, 0)
        level.setBlockAt(bx+5, by, bz-2, 4)
        level.setBlockDataAt(bx+5, by, bz-2, 0)
        # Finish first row of generation
        
        

    elif buil == "h2":
        print 'Choose House #2'

    elif buil == "h3":
        print 'Choose House #3'

    elif buil == "foun":
        print 'Choose Fountain'
        

    elif buil == "farm":
        print 'Choose Farm'
        
