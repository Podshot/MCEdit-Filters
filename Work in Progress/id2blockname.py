from pymclevel.nbt import *

def num2str(string):

    return string

def perform(level, box, options):

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Control":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value

                if (x,y,z) in box:
                    command = t["Command"]
                    new_command = num2str(command)
                    t["Command"] = TAG_String(new_command)

                    
                    
