from pymclevel.nbt import *
from pymclevel import TileEntity

displayName = "Mob to Summon"

inputs = (
    ("Use Exact Coordinates", True),
    ("Does not support extra tags yet!(Equipment, potion effects)", "label"),
    )

notNeededTags = ("OnGround", "Dimension", "UUIDMost", "UUIDLeast", "Health")


def stringifyTag(tag):
	rString=u''
	if tag.name and tag.name != None:
		rString += unicode(tag.name) + u':'
	rString += unicode(tag.value)
	return rString
	
def stringifyComLis(entity):
	rString=u''
	for tag in entity.value:
		if(not tag.name in notNeededTags):
			if(tag.tagID != 10 and tag.tagID != 9): #10 = TAG_Compound, 9 = TAG_List
				rString += stringifyTag(tag) + u','
			else:
				if tag.tagID == 10:
					if tag.name and tag.name != None:
						rString += unicode(tag.name) + u':{' + stringifyComLis(tag) + u'},'
					else:
						rString += u'{' + stringifyComLis(tag) + u'},'
				else:
					if tag.name and tag.name != None:
						rString += unicode(tag.name) + u':[' + stringifyComLis(tag) + u'],'
					else:
						rString += u'[' + stringifyComLis(tag) + u'],'
	return rString
	
def addBrackets(entity):
	tmpString = stringifyComLis(entity)
	rString = u'{' + tmpString + u'}'
	return rString
    
def perform(level, box, options):
    coords = options["Use Exact Coordinates"]
    entitiesToRemove = []

    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            x = e["Pos"][0].value
            y = e["Pos"][1].value
            z = e["Pos"][2].value
            print "x: %s" % (x)
            print "y: %s" % (y)
            print "z: %s" % (z)

            if (x,y,z) in box:
                if coords:
                    pos_1 = int(x)
                    pos_2 = int(y)
                    pos_3 = int(z)
                else:
                    pos_1 = "~"
                    pos_2 = "~"
                    pos_3 = "~"
                jsonfiy = addBrackets(e)
                entitiesToRemove.append((chunk, e))
                # Start gathering mob info
                mid = e["id"].value
                # End gathering mob info
                new_x = int(x)
                new_y = int(y)
                new_z = int(z)
                com = "/summon " + entity["id"].value + " " + pos_1 + " " + pos_2 + " " + pos_3 + " " + str(jsonfiy)
                print com
                level.setBlockAt(new_x, new_y, new_z, 137)
                level.setBlockDataAt(new_x, new_y, new_z, 0)

                control = TAG_Compound()
                control["id"] = TAG_String("Control")
                control["Command"] = TAG_String(com)
                control["x"] = TAG_Int(new_x)
                control["y"] = TAG_Int(new_y)
                control["z"] = TAG_Int(new_z
                control["CustomName"] = TAG_String("@")
                control["TrackOutput"] = TAG_Byte(1)
                control["SuccessCount"] = TAG_Int(0)
                chunk.TileEntities.append(control)
                chunk.dirty = True
                
    for (chunk, e) in entitiesToRemove:
        chunk.Entities.remove(e)
                
                
                
                
                
                
                
                
            
