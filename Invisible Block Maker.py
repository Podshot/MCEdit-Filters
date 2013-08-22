from pymclevel import TAG_Byte, TAG_Int, TAG_Float, TAG_Compound, TAG_String
import time

displayName = "Invisible Wall"

inputs = (
    ("These invisible blocks are full blocks, and they are un-breakable in survival", "label"),
    )

def perform(level, box, options):

    for x in xrange(box.minx, box.maxx):
      for y in xrange(box.miny, box.maxy):
       for z in xrange(box.minz, box.maxz):
           level.setBlockAt(x, y, z, 36)
           level.setBlockDataAt(x, y, z, 0)
           block = TAG_Compound()
           block["extending"] = TAG_Byte(0)
           block["blockData"] = TAG_Int(0)
           block["blockId"] = TAG_Int(7)
           block["facing"] = TAG_Int(0)
           block["x"] = TAG_Int(x)
           block["y"] = TAG_Int(y)
           block["z"] = TAG_Int(z)
           block["progress"] = TAG_Float(-1.001638E+07)
           block["id"] = TAG_String("Piston")
           chunk = level.getChunk(box.minx/16, box.minz/16)
           chunk.TileEntities.append(block)
           chunk.Dirty = True
