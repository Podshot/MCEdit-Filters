# This is filter that renames existing mobs, requested by VideoGameMaster on The Minecraft Forums
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
displayName = "Rename Mobs"

inputs = (
    ("Name",("string","value=")),
    ("Name Color",tuple(sorted(colors.keys()))),
    ("Name Bold",False),
    ("Name Itallics",False),
    ("Name Strikethrough",False),
    ("Name Underline",False)
)

formatChar = unichr(167)

def perform(level, box, options):
    formatCode = formatChar + colors[options["Name Color"]]
    if options["Name Bold"]:
        formatCode += formatChar + formatting["Bold"]
    if options["Name Itallics"]:
        formatCode += formatChar + formatting["Itallics"]
    if options["Name Strikethrough"]:
        formatCode += formatChar + formatting["Strikethrough"]
    if options["Name Underline"]:
        formatCode += formatChar + formatting["Underline"]
    name = TAG_String(formatCode + options["Name"] + formatChar + "r")


    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
            y = e["Pos"][1].value
            z = e["Pos"][2].value
            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
                e["CustomNameVisible"] = TAG_Byte(1)
                e["CustomName"] = TAG_String(name)
                chunk.dirty = True
    
