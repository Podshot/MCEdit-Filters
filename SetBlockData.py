# This is filter Set Block Data. This filter is intended to be used for experimenting with minecraft bugs
# & other exploits while setting block data to non-vanilla values.
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters

inputs = (
  ("Set data of blocks in box to selected value. Only blocks with same ID as chosen block will be affected.","label"),
  ("Block", "blocktype"),
  ("Data",(0,0,16))
)

displayName = "Set Block Data"

def perform(level, box, options):
    blockId = options["Block"].ID
    data = options["Data"]
    for x in range(box.minx,box.maxx):
        for y in range(box.miny,box.maxy):
            for z in range(box.minz,box.maxz):
                # Look for blocks with the same ID
                if level.blockAt(x,y,z) == blockId:
                    # Set their data to chosen value
                    level.setBlockDataAt(x,y,z,data)