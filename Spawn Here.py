from pymclevel.nbt import TAG_List, TAG_Double, TAG_Short, TAG_Compound

displayName = "Spawn Here"

inputs = (
    ("Spawners", True),
    ("Minecart Spawners", True),
    ("Change Spawn Radius?", True),
    ("Changes the Spawning Coordinates to the Spawner's current location", "label"),
)

def perform(level, box, options):
    spawner = options["Spawners"]
    mcspawner = options["Minecart Spawners"]
    radi = options["Change Spawn Radius?"]
    skipped = 0

    for (chunk, slices, point) in level.getChunkSlices(box):
        if spawner:
            for te in chunk.TileEntities:
                if te["id"].value == "MobSpawner":
                    tex = te["x"].value
                    tey = te["y"].value
                    tez = te["z"].value

                    if (tex,tey,tez) in box:
                        if "SpawnData" in te:
                            pos = te["SpawnData"]
                            pos["Pos"] = TAG_List()
                            pos["Pos"].append(TAG_Double(tex))
                            pos["Pos"].append(TAG_Double(tey))
                            pos["Pos"].append(TAG_Double(tez))
                            if "SpawnPotentials" in te:
                                del te["SpawnPotentials"]
                            if radi:
                                te["SpawnRange"] = TAG_Short(1)
                            chunk.dirty = True
                        if "SpawnData" not in te:
                            print "[Filter Message]Spawner at X:%s, Y:%s, Z:%s, was not modified!" % (tex, tey, tez)
                            print "Because it was missing the 'SpawnData' Tag"
                            skipped = skipped + 1

        if mcspawner:
            for e in chunk.Entities:
                if e["id"].value == "MinecartSpawner":
                    ex = e["Pos"][0].value
                    ey = e["Pos"][1].value
                    ez = e["Pos"][2].value

                    if (ex,ey,ez) in box:
                        if "SpawnData" in e:
                            pos = e["SpawnData"]
                            pos["Pos"] = TAG_List()
                            pos["Pos"].append(TAG_Double(ex))
                            pos["Pos"].append(TAG_Double(ey))
                            pos["Pos"].append(TAG_Double(ez))
                            if "SpawnPotentials" in e:
                                del e["SpawnPotentials"]
                            if radi:
                                e["SpawnRange"] = TAG_Short(1)
                            chunk.dirty = True
                        if "SpawnData" not in te:
                            print "[Filter Message]Minecart Spawner at X:%s, Y:%s, Z:%s, was not modified!" % (ex, ey, ez)
                            print "Because it was missing the 'SpawnData' Tag"
                            skipped = skipped + 1
        if skipped != 0:
            raise Exception("Check Console, some Spawners were skipped!")
                            
