from pymclevel.nbt import TAG_String

displayName = "Custom Heads"

VERSION = "1.0.0"
UPDATE_URL = "http://podshot.github.io/update/Custom%20Heads.json"

safeheads = {
    "Note Block": "C418",
    "Old Radio": "uioz",
    "Dark Wood": "bendablob2",
    "Eye of Ender": "Edna_I",
    "Chest": "MHF_Chest",
    "Camera": "FHG_Cam",
    "Jukebox": "stgiga",
    "Puffer Fish": "luci999",
    "Redstone Lamp": "AutoSoup",
    "Crafting Table": "Russellgoo97",
    "Podzol": "PhasePvP",
    "BookShelf": "BowAimbot",
    "Villager": "MHF_Villager",
    "Monster Spawner": "GAMEZENMASTER",
    "Cactus": "MHF_Cactus",
    "Cake": "MHF_Cake",
    "Melon": "MHF_Melon",
    "Oak Log": "MHF_OakLog",
    "Pumpkin": "MHF_Pumpkin",
    "TNT Version 1": "MHF_TNT",
    "TNT Version 2": "MHF_TNT2",
    "Glowstone": "samstine11",
    "Dispenser": "scemm",
    "Leaves": "rsfx",
    }

inputs = (
    ("Premade Heads", tuple(sorted(safeheads.keys()))),
    ("Custom Head:",("string","value=")),
    ("Override all existing custom heads", False),
    ("NOTE: The Custom Head option will overwrite the Premade Head Option", "label"),
    )

def perform(level, box, options):
    premadehead = safeheads[options["Premade Heads"]]
    customhead = options["Custom Head:"]
    override = options["Override all existing custom heads"]
    empty = ""

    for (chunk, slices, point) in level.getChunkSlices(box):
        for te in chunk.TileEntities:
            x = te["x"].value
            y = te["y"].value
            z = te["z"].value

            if (x,y,z) in box:
                if override:
                    if customhead != empty:
                        te["ExtraType"] = TAG_String(customhead)
                        
                    if customhead == empty:
                        te["ExtraType"] = TAG_String(premadehead)
                        
                if not override:
                    if customhead != empty:
                        if te["ExtraType"].value == "":
                            te["ExtraType"] = TAG_String(customhead)
                        
                    if customhead == empty:
                        if te["ExtraType"].value == "":
                            te["ExtraType"] = TAG_String(premadehead)

                chunk.dirty = True
                    
