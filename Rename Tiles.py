# This is filter Rename Tiles. It can rename command blocks, furnaces, chests, brewing stands, and more tiles!
# you can also use colors & formatting in the name
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters

from pymclevel import TAG_String

formatting = {
    "Bold":"l",
    "Strikethrough":"m",
    "Underline":"n",
    "Itallics":"o"
    }

colors = {
	"White": "f",
	"Black": "0",
	"Dark Blue": "1",
	"Dark Green": "2",
	"Dark Aqua": "3",
	"Dark Red": "4",
	"Purple": "5",
	"Gold": "6",
	"Gray": "7",
	"Dark Gray": "8",
	"Indigo": "9",
	"Bright Green": "a",
	"Aqua": "b",
	"Red": "c",
	"Pink": "d",
	"Yellow": "e",
	}

inputs = (
  ("Chests", False),
  ("Furnaces", False),
  ("Dispensers", False),
  ("Droppers", False),
  ("Command Blocks", False),
  ("Enchantment Tables", False),
  ("Hoppers", False),
  ("Brewing Stands", False),
  ("Name",("string","value=")),
  ("Name Color",tuple(sorted(colors.keys()))),
  ("Name Bold",False),
  ("Name Itallics",False),
  ("Name Strikethrough",False),
  ("Name Underline",False)
)

displayName = "Rename Tiles"
formatChar = unichr(167)

def perform(level, box, options):
    # Check options
    chest = options["Chests"]
    furnace = options["Furnaces"]
    dispenser = options["Dispensers"]
    dropper = options["Droppers"]
    commands = options["Command Blocks"]
    tables = options["Enchantment Tables"]
    hoppers = options["Hoppers"]
    brewing = options["Brewing Stands"]
    formatCode = formatChar + colors[options["Name Color"]]
    if options["Name Bold"]:
        formatCode += formatChar + formatting["Bold"]
    if options["Name Itallics"]:
        formatCode += formatChar + formatting["Itallics"]
    if options["Name Strikethrough"]:
        formatCode += formatChar + formatting["Strikethrough"]
    if options["Name Underline"]:
        formatCode += formatChar + formatting["Underline"]
    nameTag = TAG_String(formatCode + options["Name"] + formatChar + "r")
    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value
            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
                if t["id"].value == "Chest" and chest:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
                if t["id"].value == "Furnace" and furnace:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
                if t['id'].value == "Control" and commands:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
                if t['id'].value == "EnchantTable" and tables:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
                if t['id'].value == "Dropper" and dropper:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
                if t['id'].value == "Trap" and dispenser:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
                if t['id'].value == "Cauldron" and brewing:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
                if t['id'].value == "Hopper" and hoppers:
                    t["CustomName"] = nameTag
                    chunk.dirty = True
