from pymclevel import *
import time

displayName = "Block to Command"

def perform(level, box, options):
	
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
	 	 	for z in xrange(box.minz, box.maxz):
	 	 	 	bid = int(level.blockAt(x, y, z))
	 	 	 	bda = int(level.blockDataAt(x, y, z))
	 	 	 	time.sleep(0.5)
	 	 	 	level.setBlockAt(x, y, z, 137)
	 	 	 	com = "/setblock " + str(x) + " " + str(y) + " " + str(z - 1) + " " + str(bid) + " " + str(bda) + " replace"
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
	 	 	 	
