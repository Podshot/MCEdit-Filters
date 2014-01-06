from pymclevel.nbt import *
from pymclevel import MCSchematic
from pymclevel.box import Vector
import random

direction = {
        "North": 90,
        "South": -90,
        "East": 180,
        "West": 0,
                   
            
            }

inputs = (
        ("Display Offset", (0, -127, 127)),
        ("Chest Direction", tuple(sorted(direction.keys()))),
        )

item_id = []
item_damage = []
item_count = []
tileEntitiesToRemove = []

def createRandom():
    base = random.randint(0, 2)
    dec = random.randint(1, 1000)
    returnable = str(base) + "." + str(dec)
    return returnable

def createBlocks():
    e = MCSchematic(shape=(21,4,6),filename='')
    e._Blocks = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,137,137,137,137,137,137,137,137,137,137,137,137,137],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,137,137,137,137,137,137,137,137,137,137,137,137,137],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,137,0,0,0,0,0,0,0,0,0,0,0]],[[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,0,1,0,1,1,75,55,55,55,55,55,55,55,55,55,55,55,55],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,93],[0,0,0,0,0,0,0,0,55,55,55,55,55,55,55,55,55,55,55,55,55],[0,0,0,0,0,0,0,0,93,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,55,55,0,0,0,0,0,0,0,0,0,0,0]],[[75,94,55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,94,55,137,149,1,76,55,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],[[4,1,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,14,1,1,0,1,15,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]])
    return e

def createTheBlocks(level, dest):
    vec = Vector(0,0,0)
    level.copyBlocksFrom(createBlocks(),createBlocks().bounds,vec + dest)


def clearChests(level, box):
    for (chunk, t) in tileEntitiesToRemove:
	chunk.TileEntities.remove(t)
    

def perform(level, box, options):
    height = options["Display Offset"]
    face = direction[options["Chest Direction"]]
    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value
            
            if (x,y,z) in box:
                if t["id"].value == "Chest":
                    tileEntitiesToRemove.append((chunk, t))
                    level.setBlockAt(x, y, z, 36)
                    for i in t["Items"]:
                        item_id.append(i["id"].value)
                        item_damage.append(i["Damage"].value)
                        item_count.append(i["Count"].value)

                    cart = TAG_Compound()
                    cart["Air"] = TAG_Short(300)
                    cart["FallDistance"] = TAG_Float(0)
                    cart["Fire"] = TAG_Short(-1)
                    cart["id"] = TAG_String("MinecartRideable")
                    cart["Invulnerable"] = TAG_Byte(0)
                    cart["Motion"] = TAG_List()
                    cart["OnGround"] = TAG_Byte(1)
                    cart["Pos"] = TAG_List()
                    cart["Pos"].append(TAG_Double(box.minx + 0.5))
                    cart["Pos"].append(TAG_Double(box.miny - 2))
                    cart["Pos"].append(TAG_Double(box.minz + 0.5))
                    cart["Rotation"] = TAG_List()
                    cart["Rotation"].append(TAG_Float(0))
                    cart["Rotation"].append(TAG_Float(0))
                    cart["CustomDisplayTile"] = TAG_Byte(1)
                    cart["DisplayTile"] = TAG_Int(54)
                    cart["DisplayData"] = TAG_Int(0)
                    cart["DisplayOffset"] = TAG_Int(height)
                    #cart["Riding"] = TAG_Compound()
                    #cart["Riding"]["id"] = TAG_String("MinecartRideable")
                    #pos = TAG_List()
                    #pos.append(TAG_Double(1000000))
                    #pos.append(TAG_Double(200))
                    #pos.append(TAG_Double(1000000))
                    #cart["Riding"]["Pos"] = pos
                    mot = TAG_List()
                    mot.append(TAG_Double(float("NaN")))
                    mot.append(TAG_Double(float("NaN")))
                    mot.append(TAG_Double(float("NaN")))
                    #cart["Riding"]["Motion"] = mot
                    cart["Motion"] = mot
                    chunk.Entities.append(cart)
                    chunk.dirty = True

                        
    #createCart(level, box, height, face)
    print 'Ids: %s' % (item_id)
    print 'Damage: %s' % (item_damage)
    print 'Count: %s' % (item_count)
    print createRandom()
    #createTheBlocks(level,[box.minx,box.miny,box.minz])
    
    
    
