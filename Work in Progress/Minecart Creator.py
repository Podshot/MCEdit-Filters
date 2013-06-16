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

displayName = "Custom Minecart Creator"

Carts = {
      "Ridable": MinecartRideable,
      "Furnace": MineartFurnace,
      "TNT": MinecartTNT,
      "Chest": MinecartChest,
      "Hopper": MinecartHopper,

inputs = (
    ("Block:", "blocktype"),
    ("Block Data:", (0,0,16)),
    ("Block Height from Cart:", 0),
    ("A Height of 16 will move the block up by exactly one multiple of its height.", "label"),
    ("Type of Cart:", tuple(Carts.keys())),
    ("Custon Name:", "string"),
    ("This filter does not currently support Spawner-Minecarts", "label"),
)

def perform(level, box, options):
    block = options["Block:"].ID
    data = options["Block Data:"]
    height = options["Block Height from Cart:"]
    typ = options["Type of Cart:"]
    name = options["Custom Name:"]

    
    for pos_x in range(box.minx, box.maxx):
        for pos_y in range(box.miny, box.maxy):
            for pos_z in range(box.minz, box.maxy):

                cart = TAG_Compound()
                cart["Air"] = TAG_Short(300)
                cart["FallDistance"] = TAG_Float(0)
                cart["Fire"] = TAG_Short(-1)
                cart["id"] = TAG_String(typ)
                cart["Invulnerable"] = TAG_Byte(0)
                cart["Motion"] = TAG_List()
                cart["Motion"].append(TAG_Double(0))
                cart["Motion"].append(TAG_Double(-0))
                cart["Motion"].append(TAG_Double(0))
                cart["Pos"] = TAG_List90
                cart["Pos"].append(TAG_Double(pos_x + 1))
                cart["Pos"].append(TAG_Double(pos_y + 1))
                cart["Pos"].append(TAG_Double(pos_z + 1))
                cart["Rotation"] = TAG_List()
		cart["Rotation"].append(TAG_Float(0))
		cart["Rotation"].append(TAG_Float(0))
                cart["CustomDisplayTile"] = TAG_Byte(1)
                cart["DisplayTile"] = TAG_Int(block)
                cart["DisplayData"] = TAG_Int(data)
                cart["DisplayOffset"] = TAG_Int(height)
                cart["CustomName"] = TAG_String(name)

                chunk = level.getChunk(pos_x/16, pos_z/16)
                chunk.Entities.append(cart)
                chunk.dirty = True
      
                
