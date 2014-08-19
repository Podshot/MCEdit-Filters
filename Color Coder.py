# -*- coding: cp1252 -*-
from pymclevel.nbt import TAG_String

formatChar = "§"

inputs = (
    ("Character to Replace", ("string","value=&")),
    ("Blocks to Skip", ("string", "value=")),
    ("Use \"^\" to seperate different block ids","label"),
    ("Chests", True),
    ("Dispensers", True),
    ("Droppers", True),
    ("Command Blocks", True),
    ("Operate on Lore", True),
    ("Operate on Names", True),
    )
    

VERSION = "2.0.0"
UPDATE_URL = "http://podshot.github.io/update/Color%20Coder.json"

def perform(level, box, options):
    char2Replace = options["Character to Replace"]
    chests = options["Chests"]
    disp = options["Dispensers"]
    drop = options["Droppers"]
    cmds = options["Command Blocks"]
    name = options["Operate on Names"]
    lore = options["Operate on Lore"]

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value

            if (x,y,z) in box:
                if t["id"].value == "Control" and cmds:
                    command = t["Command"].value
                    new = command.replace(char2Replace, formatChar)
                    t["Command"] = TAG_String(new)
                if t["id"].value == "Chest" and chests:
                    for itemStack in t["Items"]:
                        if "tag" in item:
                            if "display" in item["tag"]:
                                if "Name" in item["tag"]["display"] and name:
                                    itemName = item["tag"]["display"]["Name"].value
                                    newItemName = itemName.replace(char2Replace, formatChar)
                                    item["tag"]["display"]["Name"] = TAG_String(newItemName)
                                if "Lore" in item["tag"]["display"] and lore:
                                    loreLines = item["tag"]["display"]["Lore"]
                                    for line in loreLines:
                                        line.replace(char2Replace, formatChar)
                                    item["tag"]["display"]["Lore"] = TAG_List()
                                    for aLine in loreLines:
                                        item["tag"]["display"]["Lore"].append(aLine)
                if t["id"].value == "Trap" and disp:
                    for itemStack in t["Items"]:
                        if "tag" in item:
                            if "display" in item["tag"]:
                                if "Name" in item["tag"]["display"] and name:
                                    itemName = item["tag"]["display"]["Name"].value
                                    newItemName = itemName.replace(char2Replace, formatChar)
                                    item["tag"]["display"]["Name"] = TAG_String(newItemName)
                                if "Lore" in item["tag"]["display"] and lore:
                                    loreLines = item["tag"]["display"]["Lore"]
                                    for line in loreLines:
                                        line.replace(char2Replace, formatChar)
                                    item["tag"]["display"]["Lore"] = TAG_List()
                                    for aLine in loreLines:
                                        item["tag"]["display"]["Lore"].append(aLine)
                if t["id"].value == "Dropper" and drop:
                    for itemStack in t["Items"]:
                        if "tag" in item:
                            if "display" in item["tag"]:
                                if "Name" in item["tag"]["display"] and name:
                                    itemName = item["tag"]["display"]["Name"].value
                                    newItemName = itemName.replace(char2Replace, formatChar)
                                    item["tag"]["display"]["Name"] = TAG_String(newItemName)
                                if "Lore" in item["tag"]["display"] and lore:
                                    loreLines = item["tag"]["display"]["Lore"]
                                    for line in loreLines:
                                        line.replace(char2Replace, formatChar)
                                    item["tag"]["display"]["Lore"] = TAG_List()
                                    for aLine in loreLines:
                                        item["tag"]["display"]["Lore"].append(aLine)
        chunk.dirty = True
                    
