# This is filter Fireworks Editor. It can edit fireworks rocket item in a container.
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel.nbt import TAG_Compound, TAG_Byte, TAG_List, TAG_Int_Array, TAG_Short, TAG_String, TAG_Int
from random import randint
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
  ("Flight", (0,-2,16))
)
class RGBColor():
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.rgb = 0
    def recalcRGB(self):
        self.rgb = self.r * 65536 + self.g * 256 + self.b
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
def getColor(options, num):
    color = RGBColor()
    if options["Randomize Colors"]:
        color.r = randint(0,256)
        color.g = randint(0,256)
        color.b = randint(0,256)
    else:
        color.r = options["Color #"+str(num)+" R"]
        color.g = options["Color #"+str(num)+" G"]
        color.b = options["Color #"+str(num)+" B"]
    color.recalcRGB()
    return color
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
    
    colors = []
    rang = range(1,4)
    for i in rang:
        color = getColor(options, i)
        colors.append(color.rgb)
    explosion["Colors"] = TAG_Int_Array(colors)
    return explosion
def perform(level, box, options):
    if box.width == 1 and box.height == 1 and box.length == 1 and level.blockAt(box.minx, box.miny, box.minz) == 0:
        level.setBlockAt(box.minx, box.miny, box.minz, 54)
        chest = TAG_Compound()
        chest["Items"] = TAG_List()
        chest["id"] = TAG_String(u'Chest')
        chest["x"] = TAG_Int(box.minx)
        chest["y"] = TAG_Int(box.miny)
        chest["z"] = TAG_Int(box.minz)
        chunk = level.getChunk(box.minx/16, box.minz/16)
        chunk.TileEntities.append(chest)
        chunk.dirty = True
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
                                item["tag"] = TAG_Compound()
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
                            chunk.dirty = True