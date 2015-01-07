from pymclevel.nbt import *
import urllib2, json, time

URL = "http://api.goender.net/api/profiles/"

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/Head%20to%20UUID.json"

def perform(level, box, options):
     
     for (chunk, point, slices) in level.getChunkSlices(box):
         for te in chunk.TileEntities:
             if te["id"].value == "Skull":
                 x = te["x"].value
                 y = te["y"].value
                 z = te["z"].value

                 if (x,y,z) in box:
                    name = te["ExtraType"].value
                    site = urllib2.urlopen(URL + name)
                    response = site.read()
                    jsonRaw = json.loads(response)
                    te["Owner"] = TAG_Compound()
                    te["Owner"]["Id"] = TAG_String(jsonRaw[player])
                    te["Owner"]["Name"] = TAG_String(player)
                    chunk.dirty = True
                         
                         
