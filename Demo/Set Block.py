from pymclevel import MCSchematic
from pymclevel import alphaMaterials
import time

displayName = "Demo Filter: Block Gen"

inputs = (
        ("Material:", "blocktype"),
        ("A filter version of the Fill Tool", "label"),
)
def setBlock(level, (block, data), box):
    for x in xrange(box.minx, box.maxx):
        for y in xrange(box.miny, box.maxy):
            for z in xrange(box.minz, box.maxz):
                level.setBlockAt(x, y, z, block)
                level.setBlockDataAt(x, y, z, data)
def perform(level, box, options):
    method = "Fill-ter"
    print '%s: Started: %s' % (method, time.ctime())
    mat = (options["Material:"].ID, options["Material:"].blockData)
    setBlock(level, mat, box)
    print '%s: Ended: %s' % (method, time.ctime())
    level.markDirtyBox(box)

