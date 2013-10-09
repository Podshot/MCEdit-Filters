from pymclevel.nbt import *
from pymclevel import TileEntity

displayName = "Mob to Summon"

inputs = (
    ("Does not support extra tags yet!(Equipment, potion effects)", "label"),
    )

def perform(level, box, options):
    entitiesToRemove = []

    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
            y = e["Pos"][1].value
            z = e["Pos"][2].value
            print "x: %s" % (x)
            print "y: %s" % (y)
            print "z: %s" % (z)

            if (x,y,z) in box:
                entitiesToRemove.append((chunk, e))
                # Start gathering mob info
                mid = e["id"].value
                # End gathering mob info
                new_x = int(x)
                new_y = int(y)
                new_z = int(z)
                com = "/summon "+ mid +" ~ ~ ~"
                print com
                level.setBlockAt(new_x, new_y, new_z, 137)
                level.setBlockDataAt(new_x, new_y, new_z, 0)

                control = TAG_Compound()
                control["id"] = TAG_String("Control")
                control["Command"] = TAG_String(com)
                control["x"] = TAG_Int(new_x)
                control["y"] = TAG_Int(new_y)
                control["z"] = TAG_Int(new_z
                control["CustomName"] = TAG_String("@")
                control["TrackOutput"] = TAG_Byte(1)
                control["SuccessCount"] = TAG_Int(0)
                chunk.TileEntities.append(control)
                chunk.dirty = True
                
    for (chunk, e) in entitiesToRemove:
        chunk.Entities.remove(e)
                
                
                
                
                
                
                
                
            
