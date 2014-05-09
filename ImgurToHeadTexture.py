import base64, random, uuid
from pymclevel.nbt import *
from mcplatform import askOpenFile

#UUIDS = ["89e8ad73-b2e5-4502-8b74-dab92921c8c1", "9196230b-deac-46f2-8b86-ffb7cbc566c0", "d1d6fe65-6df9-422f-9e69-da2c694cc764", "9a891f3d-6573-45da-b42a-52293c37ff7c", "14878d90-01f3-4845-afda-97cce8df5771", "f352f7d9-f1f4-493f-9f87-699c28229191", "e031eda9-f6fb-43cf-a291-8d33fbed0ef6", "ff455523-909b-4bfe-85d6-62ba4ab72796", "8ab1deac-5e61-4911-aca1-3256e00d57dc", "6ec1592a-b14b-4446-a8e2-7678ff56b5ad", "d8c7efab-ffc4-42c3-b537-aae129e72863", "9620f7db-cee2-4b46-97d9-bc8b5ac81333", "fc290946-5c45-41a0-85c1-88a7c3283758", "41033658-d057-4e96-bbdc-b30475fac7da", "e1b2c6d0-d9fc-4ea3-9e95-8f09ded48ec9"]
CHUNKSIZE = 16
USEFILE = False

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/ImgurToHeadTexture.json"

inputs = (
    ("Imgur URL", ("string", "value=")),
    )

#def getRandomUUID():
#    slot = random.randint(0,len(UUIDS))
#    uuid = str(UUIDS[slot])
#    return uuid

def perform(level, box, options):
    url = str(options["Imgur URL"])
    external = options["Use external UUID text file"]

    toBase64 = '{textures:{SKIN:{url:"' + url + '"}}}'
    cLine = "/give @p minecraft:skull 1 3 {SkullOwner:{Id:" + str(uuid.uuid4()) + ",Properties:{textures:[{Value:" + str(base64.b64encode(toBase64)) + "}]}}}"
    command = TAG_Compound()
    command["x"] = TAG_Int(box.minx)
    command["y"] = TAG_Int(box.miny)
    command["z"] = TAG_Int(box.minz)
    command["id"] = TAG_String("Control")
    command["Command"] = TAG_String(cLine)
    command["CustomName"] = TAG_String("@")
    command["TrackOutput"] = TAG_Byte(1)


    level.setBlockAt(box.minx, box.miny, box.minz, 137)
    chunk = level.getChunk(int(box.minx/CHUNKSIZE), int(box.minz/CHUNKSIZE))
    chunk.TileEntities.append(command)
    chunk.dirty = True
    raise Exception("Used the UUID: " + uuidToUse + "\nKeep this UUID if you plan to use this filter more than once!\nSince it could use multiple textures for one UUID")
    
