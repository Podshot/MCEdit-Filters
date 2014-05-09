from pymclevel.nbt import *
import time

METHOD = "[Executify]"
BASECOMMAND = "/execute {} {} {}"

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/Executify.json"

displayName = "Executify"

inputs = (
	("Execute Entity Arguments", ("string", "value=")),
	("Relative Coordinates", ("string", "value=~ ~ ~")),
	)

def perform(level, box, options):
	print '%s: Started at %s' % (METHOD, time.ctime())
	eea = str(options["Execute Entity Arguments"])
	rc = str(options["Relative Coordinates"])
	
    for (chunk, point, slices) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Control":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value
            
                if (x,y,z) in box:
                    command = t["Command"].value
                    newC = BASECOMMAND.format(eea, rc, command)
		    time.sleep(1)
		    t["Command"] = TAG_String(newC)
		    chunk.dirty = True
	print '%s: Ended at %s' % (METHOD, time.ctime())
