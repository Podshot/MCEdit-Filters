from pymclevel.nbt import *
import time

METHOD = "[Item NBT Changer]"
CHUNKSIZE = 16
ENUM = 1
AMNUM = 2
UNUM = 4
CDNUM = 8
CPONUM = 16
ETNUM = 32

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/Item%20NBT%20Changer.json"

displayName = "Item NBT Changer"

inputs = (
    ("Name", ("string", "value=")),
    ("Unbreakable", False),
    ("Hide Enchantments", False),
    ("Hide Attribute Modifiers", False),
    ("Hide Unbreakable", False),
    ("Hide Can Destroy", False),
    ("Hide Can Place On", False),
    ("Hide Extra Tags", False),
    ("Add Lore", ("string", "value=")),
    ("Separate Lines of lore with \"::\"", "label"),
    )
    
def perform(level, box, options):
    print '%s: Started at %s' % (METHOD, time.ctime())
    name = str(options["Name"])
    unbreakable = options["Unbreakable"]
    hideE = options["Hide Enchantments"]
    hideAM = options["Hide Attribute Modifiers"]
    hideU = options["Hide Attribute Modifiers"]
    hideCD = options["Hide Can Destroy"]
    hideCPO = options["Hide Can Place On"]
    hideET = options["Hide Extra Tags"]
    total = 0
    
    lore = options["Add Lore"]
    splitLore = lore.split("::")
    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Chest":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value
            
                if (x,y,z) in box:
                    if "Items" in t:
                        for item in t["Items"]:
                            if "tag" not in item:
                                item["tag"] = TAG_Compound()
                            if name != "":
                                if "display" not in item["tag"]:
                                    item["tag"]["display"] = TAG_Compound()
                                item["tag"]["display"]["Name"] = TAG_String(name)
                            if lore != "":
                                if "display" not in item["tag"]:
                                    item["tag"]["display"] = TAG_Compound()
                                item["tag"]["display"]["Lore"] = TAG_List()
                                for LoLore in splitLore:
                                    item["tag"]["display"]["Lore"].append(TAG_String(str(LoLore)))
                            if unbreakable:
                                item["tag"]["Unbreakable"] = TAG_Byte(1)
                            if hideE:
                                total = total + ENUM
                            if hideAM:
                                total = total + AMNUM
                            if hideU:
                                total = total + UNUM
                            if hideCD:
                                total = total + CDNUM
                            if hideCPO:
                                total = total + CPONUM
                            if hideET:
                                total = total = ETNUM
                            if "display" not in item["tag"]:
                                item["tag"]["display"] = TAG_Compound()
                            item["tag"]["display"]["HideFlags"] = TAG_Int(total)
                            
                            chunk.dirty = True
                            
    print '%s: Ended at %s' % (METHOD, time.ctime())
