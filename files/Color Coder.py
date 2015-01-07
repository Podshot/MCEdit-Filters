# -*- coding: cp1252 -*-
from pymclevel.nbt import TAG_String

char = unicode("§")

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/Color%20Coder.json"

def perform(level, box, options):

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value

            if (x,y,z) in box and t["id"].value == "Control":
                command = t["Command"].value
                new = command.replace("%", str(char))
                t["Command"] = TAG_String(new)
                chunk.dirty = True
                        
    
