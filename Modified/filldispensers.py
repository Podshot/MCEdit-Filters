# FillDispensers Filter by SethBling
# Feel free to modify and reuse, but credit to SethBling would be nice.
# Dropper compatiblity added by Podshot

from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from numpy import zeros
import random


inputs = (
    ("Quantity", (127, 0, 127)),
    ("Fill empty slots", False),
    ("Fill item id", (0, 0, 2266)),
    ("Fill item damage", 0),
)

def perform(level, box, options):
    qty = options["Quantity"]
    fill = options["Fill empty slots"]
    fillid = options["Fill item id"]
    filldmg = options["Fill item damage"]

    minx = int(box.minx/16)*16
    minz = int(box.minz/16)*16

    for x in xrange(minx, box.maxx, 16):
        for z in xrange(minz, box.maxz, 16):
            chunk = level.getChunk(x / 16, z / 16)

            for te in chunk.TileEntities:
                px = te["x"].value
                py = te["y"].value
                pz = te["z"].value

                if px < box.minx or px >= box.maxx:
                    continue
                if py < box.miny or py >= box.maxy:
                    continue
                if pz < box.minz or pz >= box.maxz:
                    continue

                if te["id"].value == "Dropper":
                    slots = zeros(9)
                    for item in te["Items"]:
                        item["Count"] = TAG_Byte(qty)
                        slot = item["Slot"].value
                        if slot >= 0 and slot < 9:
                            slots[slot] = 1

                    if fill:
                        for i in range(9):
                            if slots[i] == 0:
                                item = TAG_Compound()
                                item["id"] = TAG_Short(fillid)
                                item["Damage"] = TAG_Short(filldmg)
                                item["Count"] = TAG_Byte(qty)
                                item["Slot"] = TAG_Byte(i)
                                te["Items"].append(item)
                    chunk.dirty = True
                                     

                    
                if te["id"].value == "Trap":
                    slots = zeros(9)
                    for item in te["Items"]:
                        item["Count"] = TAG_Byte(qty)
                        slot = item["Slot"].value
                        if slot >= 0 and slot < 9:
                            slots[slot] = 1

                    if fill:
                        for i in range(9):
                            if slots[i] == 0:
                                item = TAG_Compound()
                                item["id"] = TAG_Short(fillid)
                                item["Damage"] = TAG_Short(filldmg)
                                item["Count"] = TAG_Byte(qty)
                                item["Slot"] = TAG_Byte(i)
                                te["Items"].append(item)

                    chunk.dirty = True
                    
