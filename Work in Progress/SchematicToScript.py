# This is filter SchematicToScript. It can turn any selection into a python script. The scripts are saved in MCEdit/schematic2script/
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters

import os
from pymclevel.schematic import extractSchematicFrom

def serialize3DArray(array):
    result = ""
    result += "["
    for d1 in array:
        result += "["
        for d2 in d1:
            result += "["
            for elem in d2:
                result += str(elem) + ","
            result += "],"
        result += "],"
    result += "]"
    result = result.replace(",]", "]")
    return result
displayName = "Schematic2Script"
inputs = (
           ("Ignore Block Data", False),
           ("Filename", ("string","value=outSchematic"))
           )
def perform(level,box,options):
    try:
        os.mkdir("schematic2script")
    except OSError:
        pass
    # Get schematic from the level
    schema = extractSchematicFrom(level,box,False)
    ignoreData = options["Ignore Block Data"]
    # Create lines array for writing into file
    lines = [""]
    lines.append("from pymclevel import MCSchematic\n")
    lines.append("# TODO: rename your function\n")
    lines.append("def createSchematic():\n")
    lines.append("    e = MCSchematic(shape=("+str(schema.Width)+","+str(schema.Height)+","+str(schema.Length)+"),filename='')\n")
    # copy blocks array
    lines.append("    e._Blocks = " + serialize3DArray(schema._Blocks) + "\n")
    if not ignoreData:
        # copy data array if it's not ignored
        lines.append("    e.root_tag['Data'] = pymclevel.nbt.TAG_Byte_Array(" + serialize3DArray(schema.root_tag['Data'].value) + ")\n")
        lines.append("    return e")
    # save the file
    with open("schematic2script/"+options["Filename"]+".py", "w") as f:
        f.writelines(lines)
    raise Exception("Saved as schematic2script/"+options["Filename"]+".py")