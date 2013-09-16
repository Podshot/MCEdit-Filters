from pymclevel.nbt import TAG_List

displayName = "Clear Items"

inputs = (
    ("Chest", True),
    ("Brewing Stand", True),
    ("Furnace", True),
    ("Hopper", True),
    ("Dispenser", True),
    ("Dropper", True),
    ("Version: 1.0","label"),
)

def perform(level, box, options):
    chest = options["Chest"]
    brewing = options["Brewing Stand"]
    furnace = options["Furnace"]
    hoppers = options["Hopper"]
    dispenser = options["Dispenser"]
    dropper = options["Dropper"]

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value

            if (x,y,z) in box:
                if t["id"].value == "Chest" and chest:
                    del t["Items"]
                    t["Items"] = TAG_List()
                    chunk.dirty = True
                if t["id"].value == "Furnace" and furnace:
                    del t["Items"]
                    t["Items"] = TAG_List()
                    chunk.dirty = True
                if t['id'].value == "Dropper" and dropper:
                    del t["Items"]
                    t["Items"] = TAG_List()
                    chunk.dirty = True
                if t['id'].value == "Trap" and dispenser:
                    del t["Items"]
                    t["Items"] = TAG_List()
                    chunk.dirty = True
                if t['id'].value == "Cauldron" and brewing:
                    del t["Items"]
                    t["Items"] = TAG_List()
                    chunk.dirty = True
                if t['id'].value == "Hopper" and hoppers:
                    del t["Items"]
                    t["Items"] = TAG_List()
                    chunk.dirty = True
    
