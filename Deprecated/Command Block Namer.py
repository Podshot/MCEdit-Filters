# This filter renames command blocks
# This was created by Podshot
# If you modify this filter, please give credit to Podshot
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from numpy import zeros
import random

displayName = "Renames Command Blocks"

inputs = (
        ("Custom Name:", "string"),
)
# Asks for user input
def perform(level, box, options):
    name = options["Custom Name:"]
    
    for (chunk, slices, point) in level.getChunkSlices(box):
        # Looks for Tile Entities in the Selection Box
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value

            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz and t["id"].value == "Control":
                if "Command" in t:
                                        if "CustomName" not in t:
                                            t["CustomName"] = TAG_String()
                                        # Checks to see if specified tag exists

                                        t["CustomName"] = TAG_Byte(name)
                                        chunk.dirty = True
                                        # Ends filter and marks chunk as changed
