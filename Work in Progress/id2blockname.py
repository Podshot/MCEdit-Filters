from pymclevel.nbt import *

def num2str(string):
    print 'String: %s' % (string)
    popped = string.pop(4)
    print 'Pop #1: %s' % (string)
    popped2 = string.pop(4)
    print 'Pop #2: %s' % (string)
    popped3 = string.pop(4)
    print 'Pop #3: %s' % (string)
    if popped == '0':
        string.append('minecraft:air')
        string.append(popped2)
        string.append(popped3)
    if popped == '1':
        string.append('minecraft:stone')
        string.append(popped2)
        string.append(popped3)
    if popped == '2':
        string.append('minecraft:grass')
        string.append(popped2)
        string.append(popped3)
    if popped == '3':
        string.append('minecraft:dirt')
        string.append(popped2)
        string.append(popped3)
    if popped == '4':
        string.append('minecraft:cobblestone')
        string.append(popped2)
        string.append(popped3)
    if popped == '5':
        string.append('minecraft:planks')
        string.append(popped2)
        string.append(popped3)
    if popped == '6':
        string.append('minecraft:sapling')
        string.append(popped2)
        string.append(popped3)
    if popped == '7':
        string.append('minecraft:bedrock')
        string.append(popped2)
        string.append(popped3)
    if popped == '8':
        string.append('minecraft:flowing_water')
        string.append(popped2)
        string.append(popped3)
    if popped == '9':
        string.append('minecraft:water')
        string.append(popped2)
        string.append(popped3)
    if popped == '10':
        string.append('minecraft:flowing_lava')
        string.append(popped2)
        string.append(popped3)
    if popped == '11':
        string.append('minecraft:lava')
        string.append(popped2)
        string.append(popped3)
    if popped == '12':
        string.append('minecraft:sand')
        string.append(popped2)
        string.append(popped3)
    if popped == '13':
        string.append('minecraft:gravel')
        string.append(popped2)
        string.append(popped3)
    if popped == '14':
        string.append('minecraft:gold_ore')
        string.append(popped2)
        string.append(popped3)
    if popped == '15':
        string.append('minecraft:iron_ore')
        string.append(popped2)
        string.append(popped3)
    if popped == '16':
        string.append('minecraft:coal_ore')
        string.append(popped2)
        string.append(popped3)
    if popped == '17':
        string.append('minecraft:log')
        string.append(popped2)
        string.append(popped3)
    if popped == '18':
        string.append('minecraft:leaves')
        string.append(popped2)
        string.append(popped3)
    if popped == '19':
        string.append('minecraft:sponge')
        string.append(popped2)
        string.append(popped3)
    if popped == '20':
        string.append('minecraft:glass')
        string.append(popped2)
        string.append(popped3)
    if popped == '21':
        string.append('minecraft:lapis_ore')
        string.append(popped2)
        string.append(popped3)
    if popped == '22':
        string.append('minecraft:lapis_block')
        string.append(popped2)
        string.append(popped3)
    if popped == '23':
        string.append('minecraft:dispenser')
        string.append(popped2)
        string.append(popped3)
    if popped == '24':
        string.append('minecraft:sandstone')
        string.append(popped2)
        string.append(popped3)
    if popped == '25':
        string.append('minecraft:noteblock')
        string.append(popped2)
        string.append(popped3)
    if popped == '26':
        string.append('minecraft:bed')
        string.append(popped2)
        string.append(popped3)
    if popped == '27':
        string.append('minecraft:golden_rail')
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
                    command = t["Command"].value
                    if command.startswith('/setblock') or command.startwith('/testforblock'):
                        command = command.split()
                        new_command = num2str(command)
                        new_command = ' '.join(new_command)
                        t["Command"] = TAG_String(new_command)
                        chunk.dirty = True

                    
                    
