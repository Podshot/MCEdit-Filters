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

displayName = "Make Mobs Persistent"

inputs = (
        ("Makes any mobs in the Selection Box Persistent", "label"),
)

def perform(level, box, options):
    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
            y = e["Pos"][1].value
            z = e["Pos"][2].value

            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >=box.minz and z < box.maxz:
                if "Health" in e:
                                        if "PersistenceRequired" not in e:
                                            e["PersistenceRequired"] = TAG_Byte()

                                        e["PersistenceRequired"] = TAG_Byte(1)
                                        chunk.dirty = True
