from pymclevel.nbt import *
import urllib2, json, time

URL = "http://api.goender.net/api/profiles/"

inputs = (
     ("Player Name:", ("string", "value=")),
     )

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
                         site = urllib2.urlopen(URL + player)
                         response = site.read()
                         jsonRaw = json.loads(response)
                         te["Owner"] = TAG_Compound()
                         te["Owner"]["Id"] = TAG_String(jsonRaw[player])
                         te["Owner"]["Name"] = TAG_String(player)
                         chunk.dirty = True
                    else:
                         name = te["ExtraType"].value
                         site = urllib2.urlopen(URL + name)
                         response = site.read()
                         jsonRaw = json.loads(response)
                         te["Owner"] = TAG_Compound()
                         te["Owner"]["Id"] = TAG_String(jsonRaw[player])
                         te["Owner"]["Name"] = TAG_String(player)
                         chunk.dirty = True
                         
                         
