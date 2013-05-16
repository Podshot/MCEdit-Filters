import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel
from mcplatform import *

displayName = "Schematic Maker"

def perform(level, box, options):
    method = "Schematic-er"
    print '%s: Started at %s' % (method, time.ctime())

    filename = askOpenFile("Select Schematic...", False)
    level.copyBlocksFrom(filename, filename, (box.minx, box.miny, box.minz))
    print 's%: Started at %s' % (method, time.ctime())
    level.markDirtyBox(box)
