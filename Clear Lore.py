from pymclevel.nbt import TAG_Byte, TAG_Short, TAG_String, TAG_Compound, TAG_Int, TAG_List

displayName = "Clear Lore"
		
def perform(level, box, options):
	item = options["Item"]
	
	for (chunk, slices, point) in level.getChunkSlices(box):
		for te in chunk.TileEntities:
			if te["id"].value == "Chest":
				x = te["x"].value
                y = te["y"].value
                z = te["z"].value
				
				if (x,y,z) in box:
					for item in te:
						if "tag" in item:
							if "display" in item["tag"]:
								if "Lore" in item["tag"]["display"]:
									del item["tag"]["display"]["Lore"]
							
									chunk.dirty = True