# Filter by SethBling
# Feel free to modify and reuse, but credit to SethBling would be nice.
# http://youtube.com/SethBling

from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from pymclevel import TAG_List
from pymclevel import TAG_Int
from numpy import zeros
import random

displayName = "Add Item to Container"

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

WeaponsArmor = {
	"*N/A": None,
	"Bow": 261,
	"Arrow": 262,
	"Wood Sword": 268,
	"Stone Sword": 272,
	"Iron Sword": 267,
	"Diamond Sword": 276,
	"Leather Boots": 301,
	"Leather Pants": 300,
	"Leather Tunic": 299,
	"Leather Helmet": 298,
	"Iron Boots": 309,
	"Iron Pants": 308,
	"Iron Chestplate": 307,
	"Iron Helmet": 306,
	"Diamond Boots": 313,
	"Diamond Pants": 312,
	"Diamond Chestplate": 311,
	"Diamond Helmet": 310,
	}
	
Consumables = {
	"*N/A": None,
	"Apple": 260,
	"Mushroom Stew": 202,
	"Bread": 297,
	"Raw Pork": 319,
	"Porkchop": 320,
	"Gold Apple": 322,
	"Raw Fish": 349,
	"Cooked Fish": 350,
	"Cake": 354,
	"Cookie": 257,
	"Raw Beef": 363,
	"Steak": 364,
	"Raw Chicken": 365,
	"Cooked Chicken": 366,
	"Zombie Flesh": 367,
	"Ender Pearl": 368,
	"Potion": 373,
	"Carrot": 391,
	"Potato": 392,
	"Baked Potato": 393,
	"Enchanted Book": 403,
	}

Tools = {
	"*N/A": None,
	"Iron Shovel": 256,
	"Iron Pickaxe": 257,
	"Iron Axe": 258,
	"Flint & Steel": 259,
	"Wood Shovel": 269,
	"Wood Pickaxe": 270,
	"Wood Axe": 271,
	"Stone Shovel": 273,
	"Stone Pickaxe": 274,
	"Stone Axe": 275,
	"Diamond Shovel": 277,
	"Diamond Pickaxe": 278,
	"Diamond Axe": 279,
	"Wood Hoe": 290,
	"Stone Hoe": 291,
	"Iron Hoe": 292,
	"Diamond Hoe": 293,
	"Gold Hoe": 294,
	"Gold Shovel": 284,
	"Gold Pickaxe": 285,
	"Gold Axe": 286,
	"Fishing Rod": 346,
	"Shears": 359,
	"Carrot on a Stick": 398,
}

Colors = {
	"*N/A": None,
	"Black": "0",
	"Dark Blue": "1",
	"Dark Green": "2",
	"Dark Aqua": "3",
	"Dark Red": "4",
	"Purple": "5",
	"Gold": "6",
	"Gray": "7",
	"Dark Gray": "8",
	"Indigo": "9",
	"Bright Green": "a",
	"Aqua": "b",
	"Red": "c",
	"Pink": "d",
	"Yellow": "e",
	"White": "f",
	}

inputs = (
	("Weapons & Armor", tuple(sorted(WeaponsArmor.keys()))),
	("Consumables", tuple(sorted(Consumables.keys()))),
	("Tools", tuple(sorted(Tools.keys()))),
	("Custom Id", 0),
	("Damage", 0),
	("Count", 1),
	("Name", ("string", "value=")),
	("Name Color", tuple(sorted(Colors.keys()))),
	("Name Bold", False),
	("Name Italic", False),
	("Lore", ("string", "value=")),
	("Lore Color", tuple(sorted(Colors.keys()))),
	("Lore Bold", False),
	("Lore Italic", False),
	("Enchantment", tuple(sorted(Effects.keys()))),
	("Enchant Lvl", 1),
	("Enchantment 2", tuple(sorted(Effects.keys()))),
	("Enchant 2 Lvl", 1),
	("Enchantment 3", tuple(sorted(Effects.keys()))),
	("Enchant 3 Lvl", 1),
	("Book Enchantment", tuple(sorted(Effects.keys()))),
	("Book Enchant Lvl", 1),
)

formatCode = unichr(167)

def perform(level, box, options):
	wa = WeaponsArmor[options["Weapons & Armor"]]
	if wa != None:
		id = wa
	else:
		consumable = Consumables[options["Consumables"]]
		if consumable != None:
			id = consumable
		else:
			tool = Tools[options["Tools"]]
			if tool != None:
				id = tool
			else:
				id = options["Custom Id"]
	
	dmg = options["Damage"]
	count = options["Count"]
	name = options["Name"]
	lore = options["Lore"]
	effect = Effects[options["Enchantment"]]
	effectlvl = options["Enchant Lvl"]
	effect2 = Effects[options["Enchantment 2"]]
	effect2lvl = options["Enchant 2 Lvl"]
	effect3 = Effects[options["Enchantment 3"]]
	effect3lvl = options["Enchant 3 Lvl"]
	bookeffect = Effects[options["Book Enchantment"]]
	bookeffectlvl = options["Book Enchant Lvl"]
	
	if name == "-":
		name = ""
	if lore == "-":
		lore = ""
	
	if name != "":
		if Colors[options["Name Color"]] != None:
			name = formatCode + Colors[options["Name Color"]] + name
		if options["Name Bold"]:
			name = formatCode + "l" + name
		if options["Name Italic"]:
			name = formatCode + "o" + name

	if lore != "":
		if Colors[options["Lore Color"]] != None:
			lore = formatCode + Colors[options["Lore Color"]] + lore
		if options["Lore Bold"]:
			lore = formatCode + "l" + lore
		if options["Lore Italic"]:
			lore = formatCode + "o" + lore
			
	if box.width == 1 and box.height == 1 and box.length == 1 and level.blockAt(box.minx, box.miny, box.minz) == 0:
		level.setBlockAt(box.minx, box.miny, box.minz, 54)
		chest = TAG_Compound()
		chest["Items"] = TAG_List()
		chest["id"] = TAG_String(u'Chest')
		chest["x"] = TAG_Int(box.minx)
		chest["y"] = TAG_Int(box.miny)
		chest["z"] = TAG_Int(box.minz)
		chunk = level.getChunk(box.minx/16, box.minz/16)
		chunk.TileEntities.append(chest)
		chunk.dirty = True
	
	for (chunk, slices, point) in level.getChunkSlices(box):
		for t in chunk.TileEntities:
			x = t["x"].value
			y = t["y"].value
			z = t["z"].value
			
			if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				slots = 0
				if t["id"].value == "Chest":
					slots = 27
				elif t["id"].value == "Trap" or t["id"].value == "Dropper":
					slots = 9
				else:
					continue
				
				taken = zeros(slots)
				for item in t["Items"]:
					taken[item["Slot"].value] = 1
				for slot in range(slots):
					if taken[slot] == 0:
						taken[slot] = 1
						item = TAG_Compound()
						item["id"] = TAG_Short(id)
						item["Damage"] = TAG_Short(dmg)
						item["Count"] = TAG_Byte(count)
						item["Slot"] = TAG_Byte(slot)
						if name != "":
							if "tag" not in item:
								item["tag"] = TAG_Compound()
							if "display" not in item["tag"]:
								item["tag"]["display"] = TAG_Compound()
							item["tag"]["display"]["Name"] = TAG_String(name)
							
						if lore != "":
							if "tag" not in item:
								item["tag"] = TAG_Compound()
							if "display" not in item["tag"]:
								item["tag"]["display"] = TAG_Compound()
							item["tag"]["display"]["Lore"] = TAG_List()
							item["tag"]["display"]["Lore"].append(TAG_String(lore))
						
						if effect != None:
							if "tag" not in item:
								item["tag"] = TAG_Compound()
							if "ench" not in item["tag"]:
								item["tag"]["ench"] = TAG_List()
							ef = TAG_Compound()
							ef["id"] = TAG_Short(effect)
							ef["lvl"] = TAG_Short(effectlvl)
							item["tag"]["ench"].append(ef)
							
						if effect2 != None:
							if "tag" not in item:
								item["tag"] = TAG_Compound()
							if "ench" not in item["tag"]:
								item["tag"]["ench"] = TAG_List()
							ef = TAG_Compound()
							ef["id"] = TAG_Short(effect2)
							ef["lvl"] = TAG_Short(effect2lvl)
							item["tag"]["ench"].append(ef)

						if effect3 != None:
							if "tag" not in item:
								item["tag"] = TAG_Compound()
							if "ench" not in item["tag"]:
								item["tag"]["ench"] = TAG_List()
							ef = TAG_Compound()
							ef["id"] = TAG_Short(effect3)
							ef["lvl"] = TAG_Short(effect3lvl)
							item["tag"]["ench"].append(ef)
							
						if bookeffect != None:
							if "tag" not in item:
								item["tag"] = TAG_Compound()
							if "StoredEnchantments" not in item["tag"]:
								item["tag"]["StoredEnchantments"] = TAG_List()
							ef = TAG_Compound()
							ef["id"] = TAG_Short(bookeffect)
							ef["lvl"] = TAG_Short(bookeffectlvl)
							item["tag"]["StoredEnchantments"].append(ef)
						
						t["Items"].append(item)
						chunk.dirty = True
							
						break
