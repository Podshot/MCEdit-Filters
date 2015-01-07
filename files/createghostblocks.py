from pymclevel.nbt import *
import time

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/creatghostblocks.json"

displayName = "Ghost Block Creator"

def perform(level, box, options):

    for x in xrange(box.minx, box.maxx):
        for y in xrange(box.miny, box.maxy):
            for z in xrange(box.minz, box.maxz):
                bid = int(level.blockAt(x, y, z))
                bda = int(level.blockDataAt(x, y, z,))
                cmd = "/summon FallingSand " + x + " " + y + " " + z + " " + "{TileID:" + bid + ",Data:" + bda + ",Time:0,DropItem:0,Motion:[0.0,0.04,0.0]}
                time.sleep(0.25)
                level.setBlockAt(x, y, z, 0)
                level.setBlockDataAt(x, y, z, 0)
                command = TAG_Compund()
                command["x"] = TAG_Int(x)
                command["y"] = TAG_Int(y)
                command["z"] = TAG_Int(z)
                command["id"] = TAG_String("Control")
                command["Command"] = TAG_String(cmd)
                command["CustomName"] = TAG_String("@")
                command["TrackOutput"] = TAG_Byte(1)
                command["SuccessCount"] = TAG_Int(0)
                chunk = level.getChunk(box.minx/16, box.minz/16)
                chunk.TileEntities.append(block)
                chunk.Dirty = True
