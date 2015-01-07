# This is filter SpawnerToCommandBlock. It converts all spawners in selection to command blocks, which will spawn entities with the same NBT data using the 1.7 /summon command.
# This filter was created by Tomsik68
# If you redistribute/modify, please give credit to Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel.nbt import *
inputs = (
  ("This filter converts all spawners in the selection box into command blocks with the /summon command." ,"label"),
  ("X",0),
  ("Y",2),
  ("Z",0),
  ("Coordinates are relative", True)
)

displayName = "Spawner2CommandBlock"
def nbt2json(nbt, forceNoName=False):
    result = ""
    if (nbt.name is not None and len(nbt.name) > 0) and not forceNoName:
        result = nbt.name+":"
    if nbt.tagID == 10: #TAG_COMPOUND
        result += "{"
        for tag in nbt:
            result += nbt2json(nbt[tag])
            result += ","
        result += "}"
    elif nbt.tagID == 9:#TAG_LIST
        result += "["
        for tag in nbt:
            result += nbt2json(tag, True)
            result += ","
        result += "]"
    elif nbt.tagID == 7 or nbt.tagID == 11 or nbt.tagID == 12:  # TAG_BYTE_ARRAY, TAG_INT_ARRAY, TAG_SHORT_ARRAY
        result += "["
        for v in nbt:
            result += str(v)
        result += "]"
    elif nbt.tagID == 8: # TAG_STRING
        result += "\""+nbt.value+"\""
    elif nbt.value is not None: # other TAGs like TAG_INT, TAG_SHORT etc.
        result += str(nbt.value)
    else:
        result += str(nbt)
    result = result.replace(",]", "]")
    result = result.replace(",}", "}")
    return result
def createCommandBlockTE(x,y,z):
    cmdBlock = TAG_Compound()
    cmdBlock["id"] = TAG_String("Control")
    cmdBlock["x"] = TAG_Int(x)
    cmdBlock["y"] = TAG_Int(y)
    cmdBlock["z"] = TAG_Int(z)
    cmdBlock["Command"] = TAG_String("")
    cmdBlock["SuccessCount"] = TAG_Int(0)
    return cmdBlock
def formatCoords(c,relative):
    ss = str(c)
    if relative:
        ss = "~"+ss
    return ss
def createSummonCommand(entityData,(x,y,z),relativeCoords):
    if "Pos" in entityData:
        del entityData["Pos"]
    if entityData.name is not None:
        entityData.name = None
    cmd = "/summon "+entityData["id"].value+" "+formatCoords(x,relativeCoords)+" "+formatCoords(y,relativeCoords)+" "+formatCoords(z,relativeCoords)+" "
    del entityData["id"]
    cmd += nbt2json(entityData,True)
    return cmd
def getEntityDataFromSpawner(spawner):
    if "SpawnData" in spawner:
        en = spawner["SpawnData"]
        en["id"] = TAG_String(spawner["EntityId"].value)
    elif "SpawnPotentials" in spawner and len(spawner["SpawnPotentials"]) > 0:
        en = spawner["SpawnPotentials"][0]["Properties"]
        en["id"] = TAG_String(spawner["SpawnPotentials"][0]["Type"].value)
    else:
        raise Exception("Spawner at "+str(spawner["Pos"])+" is invalid, as it doesn't contain SpawnData and SpawnPotentials, or SpawnPotentials is empty.")
    del en["UUIDMost"]
    del en["UUIDLeast"]
    return en
def perform(level, box, options):
    for (chunk, slices, point) in level.getChunkSlices(box):
        spawnersToRemove = []
        commandBlocksToAdd = []
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value
            if t["id"].value == "MobSpawner" and (x,y,z) in box:
                spawnersToRemove.append(t)
                commandBlock = createCommandBlockTE(x,y,z)
                commandBlock["Command"] = TAG_String(createSummonCommand(getEntityDataFromSpawner(t),(options["X"],options["Y"],options["Z"]),options["Coordinates are relative"]))
                commandBlocksToAdd.append(commandBlock)
        for t in spawnersToRemove:
            chunk.TileEntities.remove(t)
            level.setBlockAt(t["x"].value,t["y"].value,t["z"].value,0)
        for t in commandBlocksToAdd:
            chunk.TileEntities.append(t)
            level.setBlockAt(t["x"].value,t["y"].value,t["z"].value,137)
        chunk.dirty = len(spawnersToRemove) > 0 or len(commandBlocksToAdd) > 0