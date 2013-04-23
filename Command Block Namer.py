from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from numpy import zeros
import random

displayName = "Renames Command Blocks"

inputs = (
        ("Custom Name:", "string"),
)

def perform(level, box, options):
    name = options["Custom Name:"]

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value

            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz and t["id"].value == "Control":
                if "Command" in t:
                                        if "CustomName" not in t:
                                            t["CustomName"] = TAG_String()

                                        t["CustomName"] = TAG_Byte(name)
                                        chunk.dirty = True
