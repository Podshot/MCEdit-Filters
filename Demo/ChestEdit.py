from pymclevel.nbt import TAG_Compound, TAG_Short, TAG_Byte, TAG_List
# A demo filter on how to edit items in chest.
displayName = "Chest Edit"

def perform(level, box, options):
    # go through all chunk slices which our box is in
    for (chunk, slices, point) in level.getChunkSlices(box):
        # go through all Tile Entities in a chunk (Chest is Tile Entity)
        for tileEntity in chunk.TileEntities:
            # the slices are not precisely cut for our box, so we need to check if tile entity is in our box
            x = tileEntity["x"].value # it's important not to forget '.value' because tileEntity["x"] refers to NBT tag
            y = tileEntity["y"].value
            z = tileEntity["z"].value
            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
                # we're only looking for chests, so we need to check if this is a chest.
                # Tile Entity IDs can be found at minecraftwiki.net on page Chunk Format
                if tileEntity["id"] == "Chest":
                    # Now, we can do 3 things: add an item to the chest, edit the existing item, delete the existing item.
                    # ----------------------------------------------------------------------------------------------------
                    # 1.) Add an item
                    #     To add an item to the chest, we need to have its TAG_Compound first. I'll create the item here:
                    # ----------------------------------------------------------------------------------------------------
                    item = TAG_Compound()
                    item["id"] = TAG_Short(1) # here comes the item ID
                    item["Damage"] = TAG_Short(0) # here comes the damage/data
                    item["Count"] = TAG_Byte(1) # count (usually 0 - 64)
                    item["Slot"] = TAG_Byte(0) # this is ugly, because you may replace an existing item, but we'll assume our chest is empty for now.
                    #     We need to make sure there's already a TAG_List called "Items" so we can append our item safely
                    if not "Items" in tileEntity:
                        tileEntity["Items"] = TAG_List()
                    tileEntity["Items"].append(item)
                    # ----------------------------------------------------------------------------------------------------
                    # 2.) Edit an item
                    #     To edit an item in chest, we need to find the target item first, so we need to look through all items in the chest and see if it's what we're looking for.
                    #     In this example, I'll look for Diamond Pick(id 278) and change them to diamond hoes(293) >:)
                    # ----------------------------------------------------------------------------------------------------
                    if "Items" in tileEntity:
                        for item in tileEntity["Items"]:
                            if item["id"].value == 278:
                                item["id"].value = 293
                    # ----------------------------------------------------------------------------------------------------
                    # 3.) Delete an item
                    #     As in the previous example, we need to find the item to be deleted at first and then delete it.
                    #     In this example, I'll delete all music discs from the chest.
                    # ----------------------------------------------------------------------------------------------------
                    if "Items" in tileEntity:
                        index = 0
                        for item in tileEntity["Items"]:
                            if item["id"].value >= 2256 and item["id"].value <= 2267:
                                del tileEntity["Items"][index]
                            ++index
                    # Cleanup: After you edit a chest, you need to tell MCEdit that you changed it. It's done by flagging the current chunk as "dirty".
                    chunk.dirty = True