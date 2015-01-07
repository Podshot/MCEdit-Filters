from pymclevel.nbt import *

displayName = "Enchanter"

Effects = {
	"*None": None,
	"Protection": 0,
	"Fire Protection": 1,
	"Feather Falling": 2,
	"Blast Protection": 3,
	"Projectile Protection": 4,
	"Respiration": 5,
	"Aqua Affinity": 6,
	"Thorns": 7,
	"Sharpness": 16,
	"Smite": 17,
	"Bane of Arthropods": 18,
	"Knockback": 19,
	"Fire Aspect": 20,
	"Looting": 21,
	"Efficiency": 32,
	"Silk Touch": 33,
	"Unbreaking": 34,
	"Fortune": 35,
	"Power": 48,
	"Punch": 49,
	"Flame": 50,
	"Infinity": 51,
	}

inputs = (
    ("Enchantment", tuple(sorted(Effects.keys()))),
    ("Enchantment Level", (1, 1, 127))
)

def perform(level, box, options):
    ent = options["Enchantment"]
    lvl = options["Enchantment Level"]

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Trap" or t["id"].value == "Dropper" or t["id"].value == "Chest":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value

                if (x,y,z) in box:
                    for item in t["Items"]:
                        if "tag" not in item:
                            item["tag"] = TAG_Compound()
                        if "ench" not in item["tag"]:
                            item["tag"]["ench"] = TAG_List()

                            bre = TAG_Compound()
                            bre["id"] = TAG_Short(ent)
                            bre["lvl"] = TAG_Short(lvl)
                            item["tag"]["ench"].append(bre)

                    chunk.dirty = True
