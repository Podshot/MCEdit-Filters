from pymclevel.nbt import *
from pymclevel import TileEntity

displayName = "Mob to Summon"

inputs = (
    ("Does not support extra tags yet.!/n(Equipment, potion effects)", "label"),
    )

def perform(level, box, options):
    entitiesToRemove = []

    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
            y = e["Pos"][1].value
            z = e["Pos"][2].value

            if (x,y,z) in box:
                entitiesToRemove.append((chunk, e))
                # Start gathering mob info
                mid = e["id"].value
                # End gathering mob info
                com = "/summon "+ mid +" ~ ~ ~"
                print com
                level.setBlockAt(x, y+0.5, z, 137)

                control = TAG_Compound()
                control["id"] = TAG_String("Control"]
                control["Command"] = TAG_String(com)
                control["x"] = TAG_Int(x)
                control["y"] = TAG_Int(y+0.5)
                control["z"] = TAG_Int(z)
                
                
                
                
                
                
                
            
