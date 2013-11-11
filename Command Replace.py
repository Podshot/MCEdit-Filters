from pymclevel.nbt import *

displayName = "Command Replace"

inputs = (
    ("Filter Word #1:",("string","value=")),
    ("Replace Word #1:",("string","value=")),
    ("Replace Word #2:",("string","value=")),
    ("Filter Word #2:",("string","value=")),
    ("Replace Word #3:",("string","value=")),
    ("Filter Word #3:",("string","value=")),
    ("Replace Word #3:",("string","value=")),
    ("Filter Word #4:",("string","value=")),
    ("Replace Word #4:",("string","value=")),
    ("Filter Word #5:",("string","value=")),
    ("Replace Word #6:",("string","value=")),
    )

def replacer(string, word1, word2, word3, word4, word5, filter1, filter2, filter3, filter4, filer5):
    string = string.replace(word1, filter1)
    string = string.replace(word2, filter2)
    string = string.replace(word3, filter3)
    string = string.replace(word4, filter4)
    string = string.replace(word5, filter5)
    return string

def perform(level, box, options):
    # Option Gathering
    FW1 = options["Filter Word #1:"]
    FW2 = options["Filter Word #2:"]
    FW3 = options["Filter Word #3:"]
    FW4 = options["Filter Word #4:"]
    FW5 = options["Filter Word #5:"]
    RW1 = options["Replace Word #1:"]
    RW2 = options["Replace Word #2:"]
    RW3 = options["Replace Word #3:"]
    RW4 = options["Replace Word #4:"]
    RW5 = options["Replace Word #5:"]
    # End

    for (chunk, slices, point) in level.getChunkSlices(box):
        for te in chunk.TileEntities:
            if te["id"].value == "Control":
                x = te["x"].value
                y = te["y"].value
                z = te["z"].value

                if (x,y,z) in box:
                    command = te["Command"].value
                    # Replace stuff
                    t["Command"] = TAG_String(replacer(Line1, FW1, FW2, FW3, FW4, FW5, RW1, RW2, RW3, RW4, RW4)))
                    chunk.dirty = True
