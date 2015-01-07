# This is filter that changes a spawner's spawning coordinates to a sponge block in the selection
# This filter was created by Podshot
# If you redistribute/modify, please give credit to Podshot
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters

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
from pymclevel import MCSchematic
import time
from pymclevel import TileEntity

displayName = "Spawner Point v3"

VERSION = "1.5.0"
UPDATE_URL = "http://podshot.github.io/update/Spawner%20Point%20v3.json"

inputs = (
    ("Change Spawn Radius?", False),
    ("Replaces the Spawning Coordinates to a Sponge block in the Selection box.", "label"),
    ("Version: 1.5","label"),
)


def perform(level, box, options):
    method = "Spawner Pointer"
    xend = []
    yend = []
    zend = []
    radi = options["Change Spawn Radius?"]
    print '%s: Started at: %s' % (method, time.ctime())

    for x in xrange(box.minx, box.maxx):
        for y in xrange(box.miny, box.maxy):
            for z in xrange(box.minz, box.maxz):
                block = level.blockAt(x, y, z)
                if block == 19:
                    xend.append(x)
                    yend.append(y)
                    zend.append(z)

    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            if e["id"].value == "MinecartSpawner":
                x2 = e["Pos"][0].value
                y2 = e["Pos"][1].value
                z2 = e["Pos"][2].value

                if x2 >= box.minx and x2 < box.maxx and y2 >=box.miny and y2 < box.maxy and z2 >= box.minz and z2 < box.maxz:
                    if "SpawnData" in e:
                        pos = e["Spawndata"]
                        pos["Pos"] = TAG_List()
                        pos["Pos"].append(TAG_Double(xend+0.5))
                        pos["Pos"].append(TAG_Double(yend+0.5))
                        pos["Pos"].append(TAG_Double(zend+0.5))
                        del e["SpawnPotentials"]
                        if radi:
                            e["SpawnRange"] = TAG_Short(1)
                        print '%s %s %s' % (xend, yend, zend)
                        print '%s: Ended at: %s' % (method, time.ctime())
                        level.markDirtyBox(box)
                    
                    
        for t in chunk.TileEntities:
            x1 = t["x"].value
            y1 = t["y"].value
            z1 = t["z"].value

            if x1 >= box.minx and x1 < box.maxx and y1 >= box.miny and y1 < box.maxy and z1 >= box.minz and z1 < box.maxz and t["id"].value == "MobSpawner":
                if "SpawnData" in t:
                    pos = t["Spawndata"]
                    pos["Pos"] = TAG_List()
                    pos["Pos"].append(TAG_Double(xend+0.5))
                    pos["Pos"].append(TAG_Double(yend+0.5))
                    pos["Pos"].append(TAG_Double(zend+0.5))
                    del t["Spawnpotentials"]
                    if radi:
                        t["SpawnRange"] = TAG_Short(1)
                    print '%s %s %s' % (xend, yend, zend)
                    print '%s: Ended at: %s' % (method, time.ctime())
                    level.markDirtyBox(box) 
