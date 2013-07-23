# This is filter Fireworks Editor. It can edit fireworks rocket item in a chest.
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel.nbt import TAG_Compound, TAG_Byte, TAG_List, TAG_Int_Array, TAG_Short
fireworkTypes = {
    "Small Ball":0,
    "Large Ball":1,
    "Star":2,
    "Creeper":3,
    "Burst":4
}
inputs = (
  ("Each container in the selection box will be affected. If box is 1x1x1, chest will be created for you.", "label"),
  ("Overwrite Existing Explosions", False),
  ("Flicker", False),
  ("Trail", False),
  ("Type", tuple(sorted(fireworkTypes.keys()))),
  ("If you're too lazy to fill in colors, tick randomize colors below. It will override color menu below it.", "label"),
  ("Randomize Colors", False),
  ("Color #1 R", (0,0,256)),
  ("Color #1 G", (0,0,256)),
  ("Color #1 B", (0,0,256)),
  ("Color #2 R", (0,0,256)),
  ("Color #2 G", (0,0,256)),
  ("Color #2 B", (0,0,256)),
  ("Color #3 R", (0,0,256)),
  ("Color #3 G", (0,0,256)),
  ("Color #3 B", (0,0,256)),
  ("Flight", (0,0,16))
)
containerSlotCounts = {"Trap":9,"Dropper":9,"Chest":27,"Cauldron":4,"Furnace":3,"Hopper":5}
displayName = "Fireworks Editor"
def getFreeSlots(container):
    if not "Items" in container:
        raise Exception("Invalid Container")
    items = container["Items"]
    result = range(0,containerSlotCounts[container["id"].value])
    for item in items:
        if "Slot" in item:
            result.remove(item["Slot"].value)
    return result
def createExplosionFromOptions(options):
    explosion = TAG_Compound()
    
    if options["Flicker"]:
        flickerVal = 1
    else:
        flickerVal = 0
    explosion["Flicker"] = TAG_Byte(flickerVal)

    if options["Trail"]:
        trailVal = 1
    else:
        trailVal = 0
    explosion["Trail"] = TAG_Byte(trailVal)
    
    typeVal = fireworkTypes[options["Type"]]
    explosion["Type"] = TAG_Byte(typeVal)
    
    colors = [8073150]
    explosion["Colors"] = TAG_Int_Array(colors)
    return explosion
def perform(level, box, options):
    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value
            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
                if "Items" in t:
                    foundFirework = False
                    for item in t["Items"]:
                        if item["id"].value == 401:
                            foundFirework = True
                            if not "tag" in item:
                                item["tag"] = TAG_Compound("tag")
                            if not "Fireworks" in item["tag"]:
                                item["tag"]["Fireworks"] = TAG_Compound()
                            if not "Explosions" in item["tag"]["Fireworks"] or options["Overwrite Existing Explosions"]:
                                item["tag"]["Fireworks"]["Explosions"] = TAG_List()
                            item["tag"]["Fireworks"]["Flight"] = TAG_Byte(options["Flight"])
                            item["tag"]["Fireworks"]["Explosions"].append(createExplosionFromOptions(options))
                            chunk.dirty = True
                    if not foundFirework:
                        freeSlots = getFreeSlots(t)
                        if len(freeSlots) > 0:
                            fireworkItem = TAG_Compound()
                            fireworkItem["id"] = TAG_Short(401)
                            fireworkItem["Damage"] = TAG_Short(0)
                            fireworkItem["Slot"] = TAG_Byte(freeSlots[0])
                            fireworkItem["Count"] = TAG_Byte(64)
                            fireworkItem["tag"] = TAG_Compound()
                            fireworkItem["tag"]["Fireworks"] = TAG_Compound()
                            fireworkItem["tag"]["Fireworks"]["Explosions"] = TAG_List()
                            fireworkItem["tag"]["Fireworks"]["Flight"] = TAG_Byte(options["Flight"])
                            fireworkItem["tag"]["Fireworks"]["Explosions"].append(createExplosionFromOptions(options))
                            t["Items"].append(fireworkItem)