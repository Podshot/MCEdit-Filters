from pymclevel.nbt import *

displayName = "Unbreakable"

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/Unbreakable.json"

def perform(level, box, options):

    for (chunk, slices, point) in leve.getChunkSlices(box):
        for te in chunk.TileEntities:
            if te["id"].value == "Chest" or te["id"].value == "Trap" or te["id"].value == "Dropper":
                x = te["x"].value
                y = te["y"].value
                z = te["z"].value

                if (x,y,z) in box:
                    if "Items" in te:
                        for item in te["Items"]:
                            if not "tag" in  item:
                                item["tag"] = TAG_Compound()
                            item["tag"]["Unbreakable"] = TAG_Int(1)
                            chunk.dirty = True
