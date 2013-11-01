from pymclevel.nbt import *
from pymclevel import MCSchematic
from pymclevel.box import Vector


displayName = "Create Class Tubes"

Boots = {
    "Leather Boots": 301,
    "Iron Boots": 309,
    "Diamond Boots": 313,
    }

Chestplate = {
    "Leather Tunic": 299,
    "Iron Chestplate": 307,
    "Diamond Chestplate": 311,
    }

Pants = {
    "Leather Pants": 300,
    "Iron Pants": 308,
    "Diamond Pants": 312,
    }

Helmet = {
	"Leather Helmet": 298,
	"Iron Pants": 308,
	"Diamond Helmet": 310,
	}
items = {
        "*N/A": None,
	"Apple": 260,
	"Mushroom Stew": 202,
	"Bread": 297,
	"Raw Pork": 319,
	"Porkchop": 320,
	"Gold Apple": 322,
	"Raw Fish": 349,
	"Cooked Fish": 350,
	"Cake": 354,
	"Cookie": 257,
	"Raw Beef": 363,
	"Steak": 364,
	"Raw Chicken": 365,
	"Cooked Chicken": 366,
	"Zombie Flesh": 367,
	"Ender Pearl": 368,
	"Potion": 373,
	"Carrot": 391,
	"Potato": 392,
	"Baked Potato": 393,
	"Enchanted Book": 403,
        "Iron Shovel": 256,
	"Iron Pickaxe": 257,
	"Iron Axe": 258,
	"Flint & Steel": 259,
	"Wood Shovel": 269,
	"Wood Pickaxe": 270,
	"Wood Axe": 271,
	"Stone Shovel": 273,
	"Stone Pickaxe": 274,
	"Stone Axe": 275,
	"Diamond Shovel": 277,
	"Diamond Pickaxe": 278,
	"Diamond Axe": 279,
	"Wood Hoe": 290,
	"Stone Hoe": 291,
	"Iron Hoe": 292,
	"Diamond Hoe": 293,
	"Gold Hoe": 294,
	"Gold Shovel": 284,
	"Gold Pickaxe": 285,
	"Gold Axe": 286,
	"Fishing Rod": 346,
	"Shears": 359,
	"Carrot on a Stick": 398,
        }

inputs = [
    (("Boots", tuple(sorted(Boots.keys()))),
    ("Boot Color (Red)", (0, 0, 255)),
    ("Boot Color (Green)", (0, 0, 255)),
    ("Boot Color (Blue)", (0, 0, 255)),
    ("Leggings", tuple(sorted(Pants.keys()))),
    ("Legging Color (Red)", (0, 0, 255)),
    ("Legging Color (Green)", (0, 0, 255)),
    ("Legging Color (Blue)", (0, 0, 255)),
    ("Chestplates", tuple(sorted(Chestplate.keys()))),
    ("Chestplate Color (Red)", (0, 0, 255)),
    ("Chestplate Color (Green)", (0, 0, 255)),
    ("Chestplate Color (Blue)", (0, 0, 255)),
    ("Helmets", tuple(sorted(Helmet.keys()))),
    ("Helmet Color (Red)", (0, 0, 255)),
    ("Helmet Color (Green)", (0, 0, 255)),
    ("Helmet Color (Blue)", (0, 0, 255)),
    ("Note: Armor coloring only works with Leather Armor","label"),
    ("Armor","title")),
    (("Item #1", tuple(sorted(items.keys()))),
    ("Item #1 Count", (0, -127, 64)),
    ("Item #2", tuple(sorted(items.keys()))),
    ("Item #2 Count", (0, -127, 64)),
    ("Item #3", tuple(sorted(items.keys()))),
    ("Item #3 Count", (0, -127, 64)),
    ("Item #4", tuple(sorted(items.keys()))),
    ("Item #4 Count", (0, -127, 64)),
    ("Items","title")),  
]

def createSchematic():
    e = MCSchematic(shape=(5,5,3),filename='')
    e._Blocks = [[[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,1,93,1,76],[0,0,0,1,0]],[[0,23,0,0,0],[23,70,23,0,1],[0,23,1,55,75]],[[1,158,1,0,0],[158,0,158,0,0],[1,158,55,0,0]],[[55,55,55,0,0],[55,0,55,0,0],[55,55,0,0,0]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,1,0,1],[0,0,0,0,0]],[[0,3,0,0,0],[5,0,4,0,0],[0,2,0,0,3]],[[0,3,0,0,0],[5,0,4,0,0],[0,2,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]])
    return e

createTubes = createSchematic()
def createclasstubes(level,dest):
    vec = Vector(-1,-2,-1)
    level.copyBlocksFrom(createTubes,createTubes.bounds,vec + dest)

def perform(level, box, options):
    # Start Gathering options
    helmid = Helmet[options["Helmets"]]
    chestid = Chestplate[options["Chestplates"]]
    pantid = Pants[options["Leggings"]]
    bootid = Boots[options["Boots"]]
    realitem1 = items[options["Item #1"]]
    realitem1count = options["Item #1 Count"]
    realitem2 = items[options["Item #2"]]
    realitem2count = options["Item #2 Count"]
    realitem3 = items[options["Item #3"]]
    realitem3count = options["Item #3 Count"]
    realitem4 = items[options["Item #4"]]
    realitem4count = options["Item #4 Count"]

    # End Gathering Options
    chunk = level.getChunk(box.minx/16, box.minz/16)
    the_x1 = box.minx - 1
    the_x2 = box.minx + 1
    the_z1 = box.minz - 1
    the_z2 = box.minz + 1
    the_y = box.miny + 1
    # Start Helmets
    dis1 = TAG_Compound()
    dis1["x"] = TAG_Int(the_x1)
    dis1["y"] = TAG_Int(box.miny)
    dis1["z"] = TAG_Int(box.minz)
    dis1["id"] = TAG_String("Trap")
    dis1["Items"] = TAG_List()
    item1 = TAG_Compound()
    item1["id"] = TAG_Short(helmid)
    item1["Damage"] = TAG_Short(0)
    item1["Count"] = TAG_Byte(-127)
    item1["Slot"] = TAG_Byte(0)
    if helmid == 298:
        item1["tag"] = TAG_Compound()
        item1["tag"]["display"] = TAG_Compound()
        helmcolor = (options["Helmet Color (Red)"] << 16) | (options["Helmet Color (Green)"] << 8) | options["Helmet Color (Blue)"]
        item1["tag"]["display"]["color"] = TAG_Int(helmcolor)
    dis1["Items"].append(item1)
    chunk.TileEntities.append(dis1)
    chunk.dirty = True
    # End Helmets
    # Start Chestplate
    dis2 = TAG_Compound()
    dis2["x"] = TAG_Int(the_x2)
    dis2["y"] = TAG_Int(box.miny)
    dis2["z"] = TAG_Int(box.minz)
    dis2["id"] = TAG_String("Trap")
    dis2["Items"] = TAG_List()
    item2 = TAG_Compound()
    item2["id"] = TAG_Short(chestid)
    item2["Damage"] = TAG_Short(0)
    item2["Count"] = TAG_Byte(-127)
    item2["Slot"] = TAG_Byte(0)
    if chestid == 299:
        item2["tag"] = TAG_Compound()
        item2["tag"]["display"] = TAG_Compound()
        chestcolor = (options["Chestplate Color (Red)"] << 16) | (options["Chestplate Color (Green)"] << 8) | options["Chestplate Color (Blue)"]
        item2["tag"]["display"]["color"] = TAG_Int(chestcolor)
    dis2["Items"].append(item2)
    chunk.TileEntities.append(dis2)
    chunk.dirty = True
    # End Chestplate
    # Start Leggings
    dis3 = TAG_Compound()
    dis3["x"] = TAG_Int(box.minx)
    dis3["y"] = TAG_Int(box.miny)
    dis3["z"] = TAG_Int(the_z1)
    dis3["id"] = TAG_String("Trap")
    dis3["Items"] = TAG_List()
    item3 = TAG_Compound()
    item3["id"] = TAG_Short(pantid)
    item3["Damage"] = TAG_Short(0)
    item3["Count"] = TAG_Byte(-127)
    item3["Slot"] = TAG_Byte(0)
    if pantid == 300:
        item3["tag"] = TAG_Compound()
        item3["tag"]["display"] = TAG_Compound()
        pantcolor = (options["Legging Color (Red)"] << 16) | (options["Legging Color (Green)"] << 8) | options["Legging Color (Blue)"]
        item3["tag"]["display"]["color"] = TAG_Int(pantcolor)
    dis3["Items"].append(item3)
    chunk.TileEntities.append(dis3)
    chunk.dirty = True
    # Stop Leggings
    # Start Boots
    dis4 = TAG_Compound()
    dis4["x"] = TAG_Int(box.minx)
    dis4["y"] = TAG_Int(box.miny)
    dis4["z"] = TAG_Int(the_z2)
    dis4["id"] = TAG_String("Trap")
    dis4["Items"] = TAG_List()
    item4 = TAG_Compound()
    item4["id"] = TAG_Short(bootid)
    item4["Damage"] = TAG_Short(0)
    item4["Count"] = TAG_Byte(-127)
    item4["Slot"] = TAG_Byte(0)
    if pantid == 301:
        item4["tag"] = TAG_Compound()
        item4["tag"]["display"] = TAG_Compound()
        bootcolor = (options["Boot Color (Red)"] << 16) | (options["Boot Color (Green)"] << 8) | options["Boot Color (Blue)"]
        item4["tag"]["display"]["color"] = TAG_Int(bootcolor)
    dis4["Items"].append(item4)
    chunk.TileEntities.append(dis4)
    chunk.dirty = True
    # Stop Dispensers
    # Start Droppers
    # Start Dropper 1
    drop1 = TAG_Compound()
    drop1["x"] = TAG_Int(the_x1)
    drop1["y"] = TAG_Int(the_y)
    drop1["z"] = TAG_Int(box.minz)
    drop1["id"] = TAG_String("Dropper")
    drop1["Items"] = TAG_List()
    if realitem1 != None:
        real1 = TAG_Compound()
        real1["id"] = TAG_Short(realitem1)
        real1["Damage"] = TAG_Short(0)
        real1["Count"] = TAG_Byte(realitem1count)
        real1["Slot"] = TAG_Byte(0)
    drop1["Items"].append(real1)    
    chunk.TileEntities.append(drop1)
    chunk.dirty = True
    # Stop Dropper 1
    # Start Dropper 2
    drop2 = TAG_Compound()
    drop2["x"] = TAG_Int(the_x2)
    drop2["y"] = TAG_Int(the_y)
    drop2["z"] = TAG_Int(box.minz)
    drop2["id"] = TAG_String("Dropper")
    drop2["Items"] = TAG_List()
    if realitem2 != None:
        real2 = TAG_Compound()
        real2["id"] = TAG_Short(realitem2)
        real2["Damage"] = TAG_Short(0)
        real2["Count"] = TAG_Byte(realitem2count)
        real2["Slot"] = TAG_Byte(0)
    drop2["Items"].append(real2)  
    chunk.TileEntities.append(drop2)
    chunk.dirty = True
    drop3 = TAG_Compound()
    drop3["x"] = TAG_Int(box.minx)
    drop3["y"] = TAG_Int(the_y)
    drop3["z"] = TAG_Int(the_z1)
    drop3["id"] = TAG_String("Dropper")
    drop3["Items"] = TAG_List()
    if realitem3 != None:
        real3 = TAG_Compound()
        real3["id"] = TAG_Short(realitem3)
        real3["Damage"] = TAG_Short(0)
        real3["Count"] = TAG_Byte(realitem3count)
        real3["Slot"] = TAG_Byte(0)
    drop3["Items"].append(real3) 
    chunk.TileEntities.append(drop3)
    chunk.dirty = True
    drop4 = TAG_Compound()
    drop4["x"] = TAG_Int(box.minx)
    drop4["y"] = TAG_Int(the_y)
    drop4["z"] = TAG_Int(the_z2)
    drop4["id"] = TAG_String("Dropper")
    drop4["Items"] = TAG_List()
    if realitem4 != None:
        real4 = TAG_Compound()
        real4["id"] = TAG_Short(realitem4)
        real4["Damage"] = TAG_Short(0)
        real4["Count"] = TAG_Byte(realitem4count)
        real4["Slot"] = TAG_Byte(0)
    drop4["Items"].append(real4) 
    chunk.TileEntities.append(drop4)
    chunk.dirty = True
    # Stop Droppers
    createclasstubes(level,[box.minx,box.miny,box.minz])
