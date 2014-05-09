from pymclevel.nbt import TAG_Byte, TAG_String

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/Tamer.json"

inputs = (
    ("Cats", True),
    ("Dogs", True),
    ("Horses", True),
    ("Owner Name", "string"),
    ("Version: 1.0","label"),
    )

def perform(level, box, options):
    cat = options["Cats"]
    dog = options["Dogs"]
    horse = options["Horses"]
    owner = options["Owner Name"]

    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
            y = e["Pos"][1].value
            z = e["Pos"][2].value

            if (x,y,z) in box:
               if e["id"].value == "Wolf" and dog:
                   e["Owner"] = TAG_String(owner)
                   chunk.dirty = True
               if e["id"].value == "Ozelot" and cat:
                   e["Owner"] = TAG_String(owner)
                   chunk.dirty = True
               if e["id"].value == "EntityHorse" and horse:
                   e["Tame"] = TAG_Byte(1)
                   e["OwnerName"] = TAG_String(owner)
                   chunk.dirty = True
    
