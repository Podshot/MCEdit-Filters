from pymclevel import TAG_String
import time

inputs = (
    ("Command", "string"),
    )

def perform(level, box, options):
    command = options["Command"]
    method = "Commander"
    print '%s: Started at: %s' % (method, time.ctime())

    for (chunk, slices, point) in level.getChunkSlices(box):
        for te in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value

            if (x,y,z) in box:
               if te["id"].value == "Control":
                   te["Command"] = TAG_String(command)
                   print '%s' % (command)
                   print '%s: Ended at: %s' % (method, time.ctime())
                   chunk.dirty = True
