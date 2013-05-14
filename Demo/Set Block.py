from pymclevel import MCSchematic
from pymclevel import alphaMaterials
import time

displayName = "Demo Filter: Block Gen"

inputs = (
        ("Material:", alphaMaterials),
        ("A filter version of the Fill Tool", "label"),
        ("However, It will only generate blocks in the very corners of the Selection Box.", "label"),
)
def setBlock(level, (block, data), x, y, z):
    level.setBlockAt(x, y, z, block)
    level.setBlockDataAt(x, y, z, data)
def perform(level, box, options):
    method = "Fill-ter"
    print '%s: Started: %s' % (method, time.ctime())
    mat = (options["Material:"].ID, options["Material:"].blockData)
    setBlock(level, mat, box.minx, box.miny, box.minz)
    setBlock(level, mat, box.maxx, box.maxy, box.maxz)
    level.markDirtyBox(box)

