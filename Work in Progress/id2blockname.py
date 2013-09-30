from pymclevel.nbt import *

def num2str(string):
    popped = string.pop(4)
    popped2 = string.pop(4)
    popped3 = string.pop(4)
    if popped == '0':
        string.append('air')
        string.append(popped2)
        string.append(popped3)
    if popped == '1':
        string.append('stone')
        string.append(popped2)
        string.append(popped3)
    if popped == '2':
        string.append('grass_block')
        string.append(popped2)
        string.append(popped3)
    if popped == '3':
        string.append('dirt')
        string.append(popped2)
        string.append(popped3)
    if popped == '4':
        string.append('cobblestone')
        string.append(popped2)
        string.append(popped3)
    return string

def perform(level, box, options):

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Control":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value

                if (x,y,z) in box:
                    command = t["Command"]
                    command = command.split()
                    new_command = num2str(command)
                    t["Command"] = TAG_String(new_command)

                    
                    
