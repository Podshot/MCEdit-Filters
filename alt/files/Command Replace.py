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
    ("Replace Word #5:",("string","value=")),
    )

def replacer(string, replaceWords):
    for (word,replacement) in replaceWords.items():
        string = string.replace(words,replacement)
    return string

def perform(level, box, options):
    replaceWords = {}

    for i in range(1,5):
        replaceWords[options["Filter Word #"+str(i)]] = options["Replace Word #"+str(i)]
        
    # Option Gathering
    #FW1 = options["Filter Word #1:"]
    #FW2 = options["Filter Word #2:"]
    #FW3 = options["Filter Word #3:"]
    #FW4 = options["Filter Word #4:"]
    #FW5 = options["Filter Word #5:"]
    #RW1 = options["Replace Word #1:"]
    #RW2 = options["Replace Word #2:"]
    #RW3 = options["Replace Word #3:"]
    #RW4 = options["Replace Word #4:"]
    #RW5 = options["Replace Word #5:"]
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
                    te["Command"] = TAG_String(replacer(command,replaceWords))
                    chunk.dirty = True
