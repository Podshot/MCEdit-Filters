from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
import time

displayName = "Example Entity Changer"

inputs = (
    ("Changes any Skeletons in the selection into Wither Skeletons.", "label"),
)

def perform(level, box, options):
    method = "Witherer"
    print '%s: Started at %s' % (method, time.ctime())
    # Logs in the MCEdit console when filter was started

    for (chunk, slices, point) in level.getChunkSlices(box):
        #Splits the box into Minecrafts Chunk data that is found in <World Folder>/region
        for e in chunk.Entities:
            #Looks for anything in the chunk that is a mob/entity
            if e["id"].value == "Skeleton":
                # Check to see if the mob/entity's Id tag matches "Skeleton"
                x = e["Pos"][0].value
                y = e["Pos"][1].value
                z = e["Pos"][2].value
                # If it does, its position is turned into variables

                if (x,y,z) in box:
                    # Checks to see if the Mob's position is in the box, so if it is not, the filter will not edit that entity
                    if "id" in e:
                        e["SkeletonType"] = TAG_Byte(1)
                        # Changes the Skeleton Type byte to 1 (Which is the Wither Seletons Byte value

                        print '%s: Ended at %s' % (method, time.ctime())
                        # Logs in the MCEdit console when the filter finishes
                        chunk.dirty = True
                        #Marks the chunks that have been edited as changed

                
