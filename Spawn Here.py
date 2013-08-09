from pymclevel.nbt import TAG_List, TAG_Double

displayName = "Spawn Here"

inputs = (
    ("Spawners", True),
    ("Minecart Spawners", True),
)

def perform(level, box, options):
    spawner = options["Spawners"]
    mcspawner = options["Minecart Spawners"]

    for (chunk, slices, point) in level.getChunkSlices(box):
        if spawner:
            for te in chunk.TileEntities:
                if te["id"].value == "MobSpawner":
                    tex = te["x"].value
                    tey = te["y"].value
                    tez = te["z"].value

                    if (x,y,z) in box:
                        if "SpawnData" in e:
                            pos = te["Spawndata"]
                            pos["Pos"] = TAG_List()
                            pos["Pos"].append(TAG_Double(tex))
                            pos["Pos"].append(TAG_Double(tey))
                            pos["Pos"].append(TAG_Double(tez))
                            del te["SpawnPotentials"]
                            chunk.dirty = True

    for (chunk, slices, point) in level.getChunkSlices(box):
        if mcspawner:
            for e in chunk.Entities:
                if e["id"].value == "MinecartSpawner":
                    ex = e["Pos"][0].value
                    ey = e["Pos"][1].value
                    ez = e["Pos"][2].value

                    if (x,y,z) in box:
                        if "SpawnData" in e:
                            pos = e["Spawndata"]
                            pos["Pos"] = TAG_List()
                            pos["Pos"].append(TAG_Double(ex))
                            pos["Pos"].append(TAG_Double(ey))
                            pos["Pos"].append(TAG_Double(ez))
                            del te["SpawnPotentials"]
                            chunk.dirty = True
