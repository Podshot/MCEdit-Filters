from pymclevel.nbt import TAG_String
import re

inputs = [
    (("Place Lines on signs", True),
    ("Filter Words", False),
    ("Note: Having both true will cause a error!", "label"),
    ("General","title"),),
    (("Sign Line #1:", "string"),
    ("Sign Line #2:", "string"),
    ("Sign Line #3:", "string"),
    ("Sign Line #4:", "string"),
    ("Sign Text","title"),),
    (("Filter Word #1:", "string"),
    ("Replace Word #2:", "string"),
    ("Filter Word #2:", "string"),
    ("Replace Word #3:", "string"),
    ("Filter Word #3:", "string"),
    ("Replace Word #3:", "string"),
    ("Filter Word #4:", "string"),
    ("Replace Word #4:", "string"),
    ("Word Filtering","title"),),
    ]

def perform(level, box, options):
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

    if PLOS and FL:
        raise Exception("Cannot Place Lines on sign and Filter Words \nIn the same filter run!")
        return
    if not PLOS and not FL:
        raise Exception("What do you want me to do then?!?!")
        return

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.Entities:
            if t["id"].value = "Sign":
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
                        SignLine1 = t["Text1"].value
                        SignLine2 = t["Text2"].value
                        SignLine3 = t["Text3"].value
                        SignLine4 = t["Text4"].value
                        SignLine1.replace(FW1, RW1)
                        SignLine1.replace(FW2, RW2)
                        SignLine1.replace(FW3, RW3)
                        SignLine1.replace(FW4, RW4)
                        SignLine2.replace(FW1, RW1)
                        SignLine2.replace(FW2, RW2)
                        SignLine2.replace(FW3, RW3)
                        SignLine2.replace(FW4, RW4)
                        SignLine3.replace(FW1, RW1)
                        SignLine3.replace(FW2, RW2)
                        SignLine3.replace(FW3, RW3)
                        SignLine3.replace(FW4, RW4)
                        SignLine4.replace(FW1, RW1)
                        SignLine4.replace(FW2, RW2)
                        SignLine4.replace(FW3, RW3)
                        SignLine4.replace(FW4, RW4)
                        t["Text1"] = TAG_String(SignLine1)
                        t["Text2"] = TAG_String(SignLine2)
                        t["Text3"] = TAG_String(SignLine3)
                        t["Text4"] = TAG_String(SignLine4)
                        chunk.dirty = True
                        
                        
                    
    
            
