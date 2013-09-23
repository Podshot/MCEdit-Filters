from pymclevel import *
import time

displayName = "Block to Command"
methods = {
        "replace": 1,
        "keep": 2,
        "destroy": 3,
}
inputs = (
        ("Method:" , tuple(sorted(methods.keys()))),
        )

def perform(level, box, options):
        met = options["Method:"]
	
        for x in xrange(box.minx, box.maxx):
                for y in xrange(box.miny, box.maxy):
                        for z in xrange(box.minz, box.maxz):
                                bid = int(level.blockAt(x, y, z))
                                bda = int(level.blockDataAt(x, y, z))
                                if bid != 0:
                                        if z <= 0:
                                                time.sleep(0.25)
                                                level.setBlockAt(x, y, z, 137)
                                                com = "/setblock " + str(x) + " " + str(y) + " " + str(z - 1) + " " + str(bid) + " " + str(bda) + " " + str(met)
                                                print com
                                                command = TAG_Compound()
                                                command["id"] = TAG_String("Control")
                                                command["Command"] = TAG_String(com)
                                                command["x"] = TAG_Int(x)
                                                command["y"] = TAG_Int(y)
                                                command["z"] = TAG_Int(z)
                                                command["CustomName"] = TAG_String("@")
                                                command["TrackOutput"] = TAG_Byte(1)
                                                command["SuccesCount"] = TAG_Int(0)
                                                chunk = level.getChunk(box.minx/16, box.minz/16)
                                                chunk.TileEntities.append(command)
                                                chunk.dirty = True
                                        if z >= 0:
                                                time.sleep(0.25)
                                                level.setBlockAt(x, y, z, 137)
                                                com = "/setblock " + str(x) + " " + str(y) + " " + str(z) + " " + str(bid) + " " + str(bda) + " " + str(met)
                                                print com
                                                command = TAG_Compound()
                                                command["id"] = TAG_String("Control")
                                                command["Command"] = TAG_String(com)
                                                command["x"] = TAG_Int(x)
                                                command["y"] = TAG_Int(y)
                                                command["z"] = TAG_Int(z)
                                                command["CustomName"] = TAG_String("@")
                                                command["TrackOutput"] = TAG_Byte(1)
                                                command["SuccesCount"] = TAG_Int(0)
                                                chunk = level.getChunk(box.minx/16, box.minz/16)
                                                chunk.TileEntities.append(command)
                                                chunk.dirty = True
