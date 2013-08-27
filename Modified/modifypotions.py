# ColorArmor Filter by SethBling
# Feel free to modify and reuse, but credit to SethBling would be nice.
# http://youtube.com/SethBling
# Modified by Podshot

from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from pymclevel import TAG_Int
from pymclevel import TAG_List
from numpy import zeros

Effects = {
	"Strength": 5,
	"Jump Boost": 8,
	"Regeneration": 10,
	"Fire Resistance": 12,
	"Water Breathing": 13,
	"Resistance": 11,
	"Weakness": 18,
	"Poison": 19,
	"Speed": 1,
	"Slowness": 2,
	"Haste": 3,
	"Mining Fatigue": 4,
	"Nausea": 9,
	"Blindness": 15,
	"Hunger": 17,
	"Invisibility": 14,
	"Night Vision": 16,
	"Wither": 20,
	"Instant Damage": 7,
	"Instant Health": 6,
        "Health Boost": 21,
        "Absorption": 22,
        "Saturation": 23,  
	}

	
inputs = (
	("Effect", tuple(Effects.keys())),
	("Level", (1, -100, 127)),
	("Duration (seconds)", (0, 0, 100000000)),
)

def perform(level, box, options):
	effect = Effects[options["Effect"]]
	lvl = options["Level"]
	duration = options["Duration (seconds)"] * 20
	
	minx = int(box.minx/16)*16
	minz = int(box.minz/16)*16

	for x in xrange(minx, box.maxx, 16):
		for z in xrange(minz, box.maxz, 16):
			chunk = level.getChunk(x / 16, z / 16)

			for te in chunk.TileEntities:
				px = te["x"].value
				py = te["y"].value
				pz = te["z"].value

				if px < box.minx or px >= box.maxx:
					continue
				if py < box.miny or py >= box.maxy:
					continue
				if pz < box.minz or pz >= box.maxz:
					continue

					
				if te["id"].value == "Trap" or te["id"].value == "Chest" or te["id"].value == "Dropper":
					for item in te["Items"]:
						if item["id"].value == 373:
							if "tag" not in item:
								item["tag"] = TAG_Compound()
							if "CustomPotionEffects" not in item["tag"]:
								item["tag"]["CustomPotionEffects"] = TAG_List()
								
							ef = TAG_Compound()
							ef["Id"] = TAG_Byte(effect)
							ef["Amplifier"] = TAG_Byte(lvl-1)
							ef["Duration"] = TAG_Int(duration)
							item["tag"]["CustomPotionEffects"].append(ef)

							
					chunk.dirty = True
					
