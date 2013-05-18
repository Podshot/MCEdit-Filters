''' SchematicToScript is a python script, that turns saved schematic file into a python script.
Of course, this is intended to be used with MCEdit filters :)
Created on May 17, 2013
@author: Tomsik68
'''
# Required dependency: pymclevel
import sys
from pymclevel import schematic

from pymclevel.schematic import MCSchematic
__version__ = "1.0"
print "================================================="
print "SchematicToScript v" + __version__
print "================================================="
if len(sys.argv) == 1:
    print "Help for SchematicToScript v" + __version__
    print "Usage: python SchematicToScript.py [options] [filename]"
    print "Options:"
    print "    --ignore-biomes      : Ignores biomes saved in schematic"
    print "    --ignore-tiles       : Ignores tile entities like furnaces, chests and so on"
    print "    --ignore-data        : Ignores block data like wool color"
    print "    --ignore-entities    : Ignores all entities in the schematic"
    
    exit(1)
def checkOption(option):
    if option in sys.argv:
        return True
    else:
        return False
def serializeArray(array):
    result = ""
    result += "["
    for x in array:
        result += "["
        for y in x:
            result += "["
            for z in y:
                result += str(z) + ","
            result += "]"
        result += "]"
    result += "]"
    result = result.replace(",]", "]")
    return result
# Load schematic using pymclevel
fileName = sys.argv[len(sys.argv) - 1]
schema = MCSchematic(filename=fileName)
ignoreTiles = checkOption("--ignore-tiles")
ignoreData = checkOption("--ignore-data")
ignoreEntities = checkOption("--ignore-entities")

lines = [""]
lines.append("from pymclevel import MCSchematic\n")
lines.append("# TODO: rename your class\n")
lines.append("class OutputSchematic(MCSchematic):\n")
lines.append("    def __init__(self):\n")
# copy blocks array
lines.append("        self._Blocks = \\" + "\n")
lines.append("        " + serializeArray(schema._Blocks) + "\n")
if not ignoreData:
    lines.append("        self.root_tag['Data'].value = \\" + "\n")
    lines.append("        " + serializeArray(schema.Data) + "\n")
with open("outSchematic.py", "w") as f:
    f.writelines(lines)
