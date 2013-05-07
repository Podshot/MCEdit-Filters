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
    # Start input finder
    if buil == "smith":
        print 'Choose Blacksmith'

    elif buil == "church":
        print 'Choose Church'

    elif buil == "lib":
        print 'Choose Library'

    elif buil == "h1":
        print 'Choose House #1'
        level.setBlockAt(x, y, z, 4)
        level.setBlockDataAt(x, y, z, 0)
        level.setBlockAt(x-1, y, z, 67)
        level.setBlockDataAt(x-1, y, z, 0x0)
        level.setBlockAt(x+1, y, z, 4)
        level.setBlockDataAt(x+1, y, z, 0)
        level.setBlockAt(x+2, y, z, 4)
        level.setBlockDataAt(x+2, y, z, 0)

    elif buil == "h2":
        print 'Choose House #2'

    elif buil == "h3":
        print 'Choose House #3'

    elif buil == "foun":
        print 'Choose Fountain'
        

    elif buil == "farm":
        print 'Choose Farm'
        
