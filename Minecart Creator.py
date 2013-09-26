# This is filter that creates a custom minecart in the selection box
# This filter was created by Podshot
# If you redistribute/modify, please give credit to Podshot
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters

from pymclevel import TAG_Compound
from pymclevel import TAG_Int
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from pymclevel import TAG_Float
from pymclevel import TAG_Double
from pymclevel import TAG_List
from pymclevel import MCSchematic
from pymclevel import TileEntity


displayName = "Custom Minecart Creator"

carts = {
      "Ridable": 1,
      "Furnace": 2,
      "TNT": 3,
      "Chest": 4,
      "Hopper": 5,
      "Spawner": 6,
      "Command Block": 7,
}

inputs = (
    ("Block:", "blocktype"),
    ("Block Data:", (0,0,16)),
    ("Block Height from Cart:", 0),
    ("A Height of 16 will move the block up by exactly one multiple of its height.", "label"),
    ("Type of Cart:", tuple(sorted(carts.keys()))),
    ("Version: 1.7","label"),
)



def perform(level, box, options):
    block = options["Block:"].ID
    data = options["Block Data:"]
    height = options["Block Height from Cart:"]
    typ = options["Type of Cart:"]
    tileEntitiesToRemove = []

    if typ == "Ridable":
        mc = TAG_String("MinecartRideable")
    elif typ == "Furnace":
        mc = TAG_String("MinecartFurnace")
    elif typ == "TNT":
        mc = TAG_String("MinecartTNT")
    elif typ == "Chest":
        mc = TAG_String("MinecartChest")
    elif typ == "Hopper":
        mc = TAG_String("MinecartHopper")
    elif typ == "Spawner":
        mc = TAG_String("MinecartSpawner")
    elif typ == "Command Block":
        mc = TAG_String("MinecartCommandBlock")
        
    for (chunk, slices, point) in level.getChunkSlices(box):
            for t in chunk.TileEntities:
		x = t["x"].value
		y = t["y"].value
		z = t["z"].value

		tileEntitiesToRemove.append((chunk, t))

                level.setBlockAt(x, y, z, 0)

                cart = TAG_Compound()
                cart["Air"] = TAG_Short(300)
                cart["FallDistance"] = TAG_Float(0)
                cart["Fire"] = TAG_Short(-1)
                cart["id"] = mc
                cart["Invulnerable"] = TAG_Byte(0)
                cart["Motion"] = TAG_List()
                cart["Motion"].append(TAG_Double(0))
                cart["Motion"].append(TAG_Double(-0))
                cart["Motion"].append(TAG_Double(0))
                cart["OnGround"] = TAG_Byte(1)
                cart["Pos"] = TAG_List()
                cart["Pos"].append(TAG_Double(box.minx + 0.5))
                cart["Pos"].append(TAG_Double(box.miny + 1))
                cart["Pos"].append(TAG_Double(box.minz + 0.5))
                cart["Rotation"] = TAG_List()
                cart["Rotation"].append(TAG_Float(0))
                cart["Rotation"].append(TAG_Float(0))
                cart["CustomDisplayTile"] = TAG_Byte(1)
                cart["DisplayTile"] = TAG_Int(block)
                cart["DisplayData"] = TAG_Int(data)
                cart["DisplayOffset"] = TAG_Int(height)
                if typ == "Spawner":
                    for tag in t:
                        if tag not in ["id", "x", "y", "z"]:
                            cart[tag] = t[tag]
                if typ == "MinecartCommandBlock":
                    if level.blockAt(box.minx, box.miny, box.minz) == 137:
                        cart["Command"] = t["Command"]
                        cart["CustomName"] = t["CustomName"]
                        
                chunk.Entities.append(cart)
                chunk.dirty = True
				
    for (chunk, t) in tileEntitiesToRemove:
	    chunk.TileEntities.remove(t)
