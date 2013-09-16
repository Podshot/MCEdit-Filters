from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
from pymclevel import TAG_Long

displayName = "Leasher"

inputs = (
    ("Note: Entities must be named with Name Tags before leashing", "label"),
    ("Entity #1 Name:", "string"),
    ("Entity #2 Name:", "string"),
    ("Remove Entity's Names", True),
    ("Version: 1.1", "label"),
    )

def perform(level, box, options):
    name1 = options["Entity #1 Name:"]
    name2 = options["Entity #2 Name:"]
    remove = options["Remove Entity's Names"]


    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
	    y = e["Pos"][1].value
	    z = e["Pos"][2].value

	    if (x,y,z) in box:
                if e["CustomName"].value != '':
                    if e["CustomName"].value == name1:
                        e["Leashed"] = TAG_Byte(1)
                        e["Leash"] = TAG_Compound()
                        e["Leash"]["UUIDMost"] = TAG_Long(UM)
                        e["Leash"]["UUIDLeast"] = TAG_Long(UL)
                        if remove:
                            e["CustomName"] = TAG_String()

                    elif e["CustomName"].value == name2:
                        UL = e["UUIDLeast"].value
                        UM = e["UUIDMost"].value
                        if remove:
                            e["CustomName"] = TAG_String()

                
        chunk.dirty = True         
