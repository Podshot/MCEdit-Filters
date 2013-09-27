from pymclevel.nbt import TAG_String
import re
import time

inputs = [
    (("Place Lines on signs", True),
    ("Filter Words", False),
    ("Note: Having both true will cause a error!", "label"),
    ("General","title"),),
    (("Sign Line #1:",("string","value=")),
    ("Sign Line #2:",("string","value=")),
    ("Sign Line #3:",("string","value=")),
    ("Sign Line #4:",("string","value=")),
    ("Sign Text","title"),),
    (("Filter Word #1:",("string","value=")),
    ("Replace Word #1:",("string","value=")),
    ("Replace Word #2:",("string","value=")),
    ("Filter Word #2:",("string","value=")),
    ("Replace Word #3:",("string","value=")),
    ("Filter Word #3:",("string","value=")),
    ("Replace Word #3:",("string","value=")),
    ("Filter Word #4:",("string","value=")),
    ("Replace Word #4:",("string","value=")),
    ("Word Filtering","title"),),
    ]

def replaceword(string, word1, word2, word3, word4, replace1, replace2, replace3, replace4):
    # Uses python's replace function and iterates for each keyword and replace word
    string = string.replace(word1, replace1)
    string = string.replace(word2, replace2)
    string = string.replace(word3, replace3)
    string = string.replace(word4, replace4)
    return string

def perform(level, box, options):
    # Start Input gathering
    PLOS = options["Place Lines on signs"]
    FL = options["Filter Words"]
    SL1 = options["Sign Line #1:"]
    SL2 = options["Sign Line #2:"]
    SL3 = options["Sign Line #3:"]
    SL4 = options["Sign Line #4:"]
    FW1 = options["Filter Word #1:"]
    FW2 = options["Filter Word #2:"]
    FW3 = options["Filter Word #3:"]
    FW4 = options["Filter Word #4:"]
    RW1 = options["Replace Word #1:"]
    RW2 = options["Replace Word #2:"]
    RW3 = options["Replace Word #3:"]
    RW4 = options["Replace Word #4:"]
    # End input gathering

    if PLOS and FL:
        raise Exception("Cannot Place Lines on sign and Filter Words \nIn the same filter run!")
        return
    if not PLOS and not FL:
        raise Exception("What do you want me to do then?!?!")
        return

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Sign":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value

                if (x,y,z) in box:
                    Line1 = t["Text1"].value
                    Line2 = t["Text2"].value
                    Line3 = t["Text3"].value
                    Line4 = t["Text4"].value
                    if PLOS:
                        t["Text1"] = TAG_String(SL1)
                        t["Text2"] = TAG_String(SL2)
                        t["Text3"] = TAG_String(SL3)
                        t["Text4"] = TAG_String(SL4)
                        chunk.dirty = True

                    if FL:
                        time.sleep(0.5)
                        t["Text1"] = TAG_String(replaceword(Line1, FW1, FW2, FW3, FW4, RW1, RW2, RW3, RW4))
                        t["Text2"] = TAG_String(replaceword(Line2, FW1, FW2, FW3, FW4, RW1, RW2, RW3, RW4))
                        t["Text3"] = TAG_String(replaceword(Line3, FW1, FW2, FW3, FW4, RW1, RW2, RW3, RW4))
                        t["Text4"] = TAG_String(replaceword(Line4, FW1, FW2, FW3, FW4, RW1, RW2, RW3, RW4))
                        chunk.dirty = True
                        
                        
                    
    
            
