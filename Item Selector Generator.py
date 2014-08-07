# -*- coding: cp1252 -*-

from pymclevel.nbt import *
from pymclevel import MCSchematic
from pymclevel.box import Vector
import mcplatform
import os

displayName = "Item Selector Generator"

VERSION = "0.0.3"
UPDATE_URL = "http://podshot.github.io/update/Item%20Selector%20Generator.json"

colorCode = "§"

ARROWBLOCK = 19
SIGNBLOCK = 63
LEVEL = None

signIdentifierDICT = {}

Operations = {
    "Generate Arrows": 0,
    "Test": 1,
    }

inputs = [
    (("Operation", tuple(sorted(Operations.keys()))),
    #("Schematic Filename", ("string","value=outSchematic")),
    ("Arrow Format", ("string","value=%8<%7<::%7>%8>")),
    ("Fine Tune X", ("string","value=0.5")),
    ("Fine Tune Y", ("string","value=0.75")),
    ("Fine Tune Z", ("string","value=0.5")),
    ("General", "title")),
    ]

def arrowSchematic():
    e = MCSchematic((5,3,3),filename='', mats=)
    e._Blocks = [[[0,0,0,0,0],[0,0,0,0,137],[137,1,1,1,0]],[[0,0,0,0,137],[0,0,0,0,0],[137,93,137,149,137]],[[0,0,0,0,0],[0,0,0,0,137],[0,0,0,0,0]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,3,0,3,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]])
    e.root_tag['TileEntities'] = TAG_List()
    return e

def CommandBlock(x,y,z,command):
    commandBlock = TAG_Compound()
    commandBlock["id"] = TAG_String("Control")
    commandBlock["x"] = TAG_Int(x)
    commandBlock["y"] = TAG_Int(y)
    commandBlock["z"] = TAG_Int(z)
    commandBlock["CustomName"] = TAG_String("@")
    commandBlock["TrackOutput"] = TAG_Byte(1)
    commandBlock["Command"] = TAG_String(command)
    return commandBlock

def generateArrows(level, box, options):
    arrows = options["Arrow Format"]
    fineX = float(options["Fine Tune X"])
    fineY = float(options["Fine Tune Y"])
    fineZ = float(options["Fine Tune Z"])
    leftArrow = str(str(arrows.split("::")[0]).replace("%", colorCode))
    rightArrow = str(str(arrows.split("::")[1]).replace("%", colorCode))
    for x in xrange(box.minx, box.maxx):
        for y in xrange(box.miny, box.maxy):
            for z in xrange(box.minz, box.maxz):
                if level.blockAt(x, y, z) == ARROWBLOCK:
                    if level.blockAt(x, y+1, z) == SIGNBLOCK:
                        tileEntity = level.tileEntityAt(x, y+1, z)
                        if tileEntity["id"].value == "Sign":
                            identifier = tileEntity["Text1"].value
                            arrowType = tileEntity["Text2"].value
                            value = str(float(x) + fineX) + ":" + str(float(y) + fineY) + ":" + str(float(z) + fineZ) + ":" + arrowType
                            signIdentifierDICT[identifier] = value

    for identify in signIdentifierDICT.keys():
        value = signIdentifierDICT[identify]
        data = value.split(":")
        x = data[0]
        y = data[1]
        z = data[2]
        arrowType = data[3]
        arrowName = ""
        if arrowType == "LEFT":
            arrowName = leftArrow
        elif arrowType == "RIGHT":
            arrowName = rightArrow
            
        testforCommand = "/testfor @e[x={},y={},z={},r=0,type=Slime]".format(str(round(float(x))), str(round(float(y))), str(round(float(z))))
        summonCommand = "/summon Slime "+x+" "+y+" "+z+" {ActiveEffects:[{Id:14,Amplifier:-1,Duration:1000000000}],Riding:{id:WitherSkull,direction:[0.0,0.0,0.0],CustomName:"+arrowName+",CustomNameVisible:1b},PersistenceRequired:1b}"
        teleportCommand = "/tp @e[x={},y={},z={},r=0,type=WitherSkull] ~ ~-1000000 ~".format(str(round(float(x))), str(round(float(y))), str(round(float(z))))
        schematic = arrowSchematic()
        
        TEL = schematic.root_tag["TileEntities"]
        TEL.append(CommandBlock(4,2,1,testforCommand))

        TEL.append(CommandBlock(0,1,2,summonCommand))

        TEL.append(CommandBlock(2,1,2,teleportCommand))

        TEL.append(CommandBlock(4,1,0,"/setblock ~ ~ ~1 air"))

        TEL.append(CommandBlock(4,0,1,"/setblock ~ ~1 ~ redstone_block 0 destroy"))

        TEL.append(CommandBlock(4,1,2,"/testforblock ~ ~1 ~-1 command_block 0 {SuccessCount:0}"))

        schematicFile = mcplatform.askSaveFile(mcplatform.lastSchematicsDir or mcplatform.schematicsDir, "Save Schematic As...", "", "Schematic\0*.schematic\0\0", ".schematic")

        if schematicFile == None:
		print "ERROR: No schematic filename provided!"
		return
	schematic.saveToFile(schematicFile)
	
        #schematic.saveToFile(filename="SchematicOutput/"+options["Schematic Filename"]);
                                
        
        
        

                            
def perform(level, box, options):
    LEVEL = level
    operation = options["Operation"]
    if operation == "Generate Arrows":
        generateArrows(level, box, options)
    if operation == "Test":
        #vec = Vector(-4,-1,-1)
        vec = Vector(0,0,0)

        level.copyBlocksFrom(arrowSchematic(),arrowSchematic().bounds,vec + [box.minx,box.miny,box.minz])
