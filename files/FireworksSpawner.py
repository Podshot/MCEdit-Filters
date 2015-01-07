# This is filter Fireworks Spawner. It can create a spawner from any container that contains fireworks rocket.
# It's designed to work with FireworksEdit filter.
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel.nbt import *
from pymclevel.entity import TileEntity
inputs = (
  ("Every container in selection box which contains firework rocket will change to mob spawner that spawns firework rocket it finds in the container.", "label"),
  ("Min Spawn Delay", 600),
  ("Max Spawn Delay", 1200),
  ("Spawn Count", 1),
  ("Entity Cap", 6),
  ("Detection Range", 16),
  ("Spawn Radius", 4),
  ("Spawn X", 0),
  ("Spawn Y", 0),
  ("Spawn Z", 0)
)

displayName = "Fireworks Spawner"
def createRocketEntity(fireworksItem):
    rocket = TAG_Compound()
    rocket["id"] = TAG_String("FireworksRocketEntity")
    rocket["Invulnerable"] = TAG_Byte(0)
    rocket["OnGround"] = TAG_Byte(0)
    rocket["Air"] = TAG_Short(300)
    rocket["Fire"] = TAG_Short(-1)
    rocket["Dimension"] = TAG_Int(0)
    rocket["PortalCooldown"] = TAG_Int(0)
    rocket["FallDistance"] = TAG_Float(0.0)
    rocket["Rotation"] = TAG_List()
    rocket["Rotation"].append(TAG_Float(0.0))
    rocket["Rotation"].append(TAG_Float(0.0))
    rocket["Motion"] = TAG_List()
    rocket["Motion"].append(TAG_Double(0.0))
    rocket["Motion"].append(TAG_Double(0.0))
    rocket["Motion"].append(TAG_Double(0.0))
    rocket["FireworksItem"] = fireworksItem
    '''rocket["Pos"] = TAG_List()
    rocket["Pos"].append(TAG_Int(x))
    rocket["Pos"].append(TAG_Int(y))
    rocket["Pos"].append(TAG_Int(z))'''
    return rocket
def createMobSpawnerWithOptions(x,y,z, options):
    spawner = TileEntity.Create("MobSpawner")
    TileEntity.setpos(spawner, (x,y,z))
    spawner["Delay"] = TAG_Short(0)
    spawner["MaxSpawnDelay"] = TAG_Short(options["Max Spawn Delay"])
    spawner["MinSpawnDelay"] = TAG_Short(options["Min Spawn Delay"])
    spawner["SpawnCount"] = TAG_Short(options["Spawn Count"])
    spawner["SpawnRange"] = TAG_Short(options["Spawn Radius"])
    spawner["MaxNearbyEntities"] = TAG_Short(options["Entity Cap"])
    spawner["RequiredPlayerRange"] = TAG_Short(options["Detection Range"])
    return spawner
def perform(level, box, options):
    for (chunk, slices, point) in level.getChunkSlices(box):
        tileEntitiesToRemove = []
        tileEntitiesToAdd = []
        rocket = None
        for t in chunk.TileEntities:
            removeThisTE = False
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value
            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
                if "Items" in t:
                    for item in t["Items"]:
                        if item["id"].value == 401:
                            # found rocket
                            # validate the rocket
                            if "tag" in item and "Fireworks" in item["tag"]:
                                rocket = item
                                removeThisTE = True
            if removeThisTE and rocket is not None:
                tileEntitiesToRemove.append(t)
                spawner = createMobSpawnerWithOptions(x, y, z, options)
                spawner["EntityId"] = "FireworksRocketEntity"
                entity = createRocketEntity(rocket)
                spawner["SpawnData"] = entity
                tileEntitiesToAdd.append(spawner)
        for t in tileEntitiesToRemove:
            chunk.TileEntities.remove(t)
        for t in tileEntitiesToAdd:
            level.setBlockAt(t["x"].value, t["y"].value, t["z"].value, 52)
            chunk.TileEntities.append(t)