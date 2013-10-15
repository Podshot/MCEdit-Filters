from pymclevel import TAG_Byte

def perform(level, box, options):

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            
            if t["id"].value == "Trap" or t["id"].value = "Dropper":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value

                if (x,y,z) in box:
                    for item in t["Items"]:
                        count = item["Count"].value
                        new_count = count * -1
                        item["Count"] = TAG_Byte(new_count)
                        chunk.dirty = True
