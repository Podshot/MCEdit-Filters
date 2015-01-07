displayName = "Get Block Data"

inputs = (
    ("Version: 1.1","label"),
    )

def perform(level, box, options):
    for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy):
                    di = int(level.blockAt(x, y, z))
                    da = int(level.blockDataAt(x, y, z))
                    raise Exception("Block ID: " + str(di) + "\nBlock Data " + str(da))
