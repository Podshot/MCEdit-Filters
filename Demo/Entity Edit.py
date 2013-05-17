from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
import time

displayName = "Example Entity Changer"

inputs = (
    ("Changes any Skeletons in the selection into Wither Skeletons.", "label"),
)

def perform(level, box, options):
    method = "Witherer"
    print '%s: Started at %s' % (method, time.ctime())

    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            if e["id"].value == "Skeleton":
                x = e["x"].value
                y = e["y"].value
                z = e["z"].value

                if x >= box.minx and x < box.maxx and y >=box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
                    if "id" in e:
                        e["SkeletonType"] = TAG_Byte(1)

                        print '%s: Started at %s' % (method, time.ctime())
                        chunk.dirty = True

                
