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
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2
from random import *
from numpy import *
from pymclevel import alphaMaterials
import time
from pymclevel import TileEntity

displayName = "Spawner Point v3"

inputs = (
    ("Keep Radius?", False),
)

def Findblock(level, box):
    targets = []
    for x in xrange(box.minx, box.maxx):
        for y in xrange(box.miny, box.maxy):
            for z in xrange(box.minz, box.maxz):
                block = level.blockAt(x, y, z)
                if block == 35:
                    data = level.blockDataAt(x, y, z)
                    if data == 4:
                        targets.append((x, y,z))

def perfom(level, box, options):
    radi = options["Keep Radius?"]

    targets = FindBlock(level, box)

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x1 = t["x"].value
            y1 = t["y"].value
            z1 = t["z"].value

            if x1 >= box.minx and x1 < box.maxx and y1 >= box.miny and y1 < box.maxy and z1 >= box.minz and z1 < box.maxz and t["id"].value == "MobSpawner":

               pos = e["Spawndata"]
               pos["Pos"] = TAG_List()
               print '%s %s %s' % (targets)
               chunk.dirty = True

    
