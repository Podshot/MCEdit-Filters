from pymclevel.nbt import *
import urllib2

def perform(level, box, options):
     
     for (chunk, point, slices) in level.getChunkSlices(box):
         for te in chunk.TileEntities:
             if te["id"].value == "Skull":
                 x = te["x"].value
                 y = te["y"].value
                 z = te["z"].value

                 if (x,y,z) in box:
                     if "ExtraType" not in te:
                         # Assuming user has already converted world to a 1.8 Snapshot
                         player = str(options["Player Name:"])
                         response = urllib2.urlopen("http://connorlinfoot.com/uuid/api/?user=" + player + "&get=uuid")
                         source = response.read()
                         print source
                         #ownerTag = TAG_Compound()
                         #ownerTag["Id"] = TAG_String()
                         
                         
