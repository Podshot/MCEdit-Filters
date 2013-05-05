# This filter creates a spawner minecart
# Then creates a spawner that spawns the Spawner Minecart
# This was created by Podshot
# If you modify this filter, please give credit to Podshot
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel import TAG_Compound
from pymclevel import TAG_Int
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from pymclevel import TAG_Float
from pymclevel import TAG_Double
from pymclevel import TAG_List
from pymclevel import TileEntity
from math import sqrt
import random
import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2
from random import *
from numpy import *
from pymclevel import alphaMaterials
from pymclevel import MCSchematic

displayName = "Minecart Spawner"

inputs = (
    ("Make sure to select a Spawner", "label"),
    ("", "label"),
    ("This filter will create a Spawner-Minecart Spawner of the current Spawner", "label"),
    # Hey, we heard you liked spawners so we put a spawner in a spawner so you can spawn when you spawn
)

def dat(level, box, options):
    tileEntitiesToRemove = []

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x1 = t["x"].value
            y1 = t["y"].value
            z1 = t["z"].value

            if x1 >= box.minx and x1 < box.maxx and y1 >= box.miny and y1 < box.maxy and z1 >= box.minz and z1 < box.maxz and t["id"].value == "MobSpawner":
                tileEntitiesToRemove.append((chunk, t))

                level.setBlockAt(x1, y1, z1, 0)

                cart = TAG_Compound()
                cart["id"] = TAG_String("MinecartSpawner")
                cart["Pos"] = TAG_List([TAG_Double(x1+0.5), TAG_Double(y1+0.35), TAG_Double(z1+0.5)])
                cart["PortalCooldown"] = TAG_Int(0)
                cart["Motion"] = TAG_List([TAG_Double(0), TAG_Double(0), TAG_Double(0)])
                cart["OnGround"] = TAG_Byte(0)
                cart["Type"] = TAG_Int(0)
                cart["Fire"] = TAG_Short(-1)
                cart["Dimension"] = TAG_Int(0)
                cart["FallDistance"] = TAG_Float(0)
                cart["Air"] = TAG_Short(300)
                cart["Rotation"] = TAG_List([TAG_Float(0), TAG_Float(0)])
                cart["Invunerable"] = TAG_Byte(0)
                for tag in t:
                        if tag not in ["id", "x", "y", "z"]:
                            cart[tag] = t[tag]

                chunk.Entities.append(cart)

    for (chunk, t) in tileEntitiesToRemove:
        chunk.TileEntities.remove(t)


def spawn(level, box, options):
    entitiesToRemove = []

    for (chunk, slices, point) in level.getChunkSlices(box):

        for entity in chunk.Entities:
            x2 = int(entity["Pos"][0].value-0.5)
            y2 = int(entity["Pos"][1].value)
            z2 = int(entity["Pos"][2].value-0.5)

            if x2 >= box.minx and x2 < box.maxx and y2 >= box.miny and y2 < box.maxy and z2 >= box.minz and z2 < box.maxz and entity["id"].value == "MinecartSpawner":
                entitiesToRemove.append((chunk, entity))

                level.setBlockAt(x2, y2, z2, 52)
                # Sets the block at the coordinates to 52, the spawner block
                spawner = TileEntity.Create("MobSpawner")
                TileEntity.setpos(spawner, (x2, y2, z2))
                # Makes the block at the coordinates a Tile Entity with the value of Spawner
                spawner["Delay"] = TAG_Short(120)
                spawner["SpawnData"] = entity
                spawner["EntityId"] = entity["id"]

                chunk.TileEntities.append(spawner)

    for (chunk, entity) in entitiesToRemove:
        chunk.Entities.remove(entity)
        # Removes the spawner-minecart entity


def perform(level, box, option):
    dat(level, box, options)
    spawn(level, box, options)

    level.markDirtyBox(box)
    
                
