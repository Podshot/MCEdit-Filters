# This filter removes the selected entity
# This was created by Podshot
# If you modify this filter, please give credit to Podshot
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
from math import sqrt
import random

displayName = "Purge Selected Entity"

Mobs = ("Creeper", "Skeleton", "WitherSkeleton", "Spider", "Giant", "Zombie", "Slime", "Ghast", "PigZombie", "Enderman", \
	"CaveSpider", "Silverfish", "Blaze", "LavaSlime" , "EnderDragon", "WitherBoss", "Witch", "Bat", "Pig", \
	"Sheep", "Cow", "Chicken", "Squid", "Wolf", "MushroomCow", "SnowMan", "Ozelot", "VillagerGolem", "Villager", "Horse")
inputs = (
        ("Mob", Mobs),
        ("Removes Selected Mob from Selection", "label"),
)

def perform(level, box, options):
    mob = options["Mob"]
    entitiesToRemove = []
    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            if e["id"].value == mob:
               # Finds any mob with the current id value
                x = e["Pos"][0].value
                y = e["Pos"][1].value
                z = e["Pos"][2].value

                if (x,y,z) in box:
                    entitiesToRemove.append((chunk, e))
                    chunk.dirty = True
    for (chunk, e) in entitiesToRemove:
        chunk.Entities.remove(e)
        # removes the entities
