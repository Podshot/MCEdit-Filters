# This filter renames command blocks
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

Mobs = {
     "Bat": Bat,
     "Blaze": Blaze,
     "Cave Spider": CaveSpider,
     "Chicken": Chicken,
     "Cow": Cow,
     "Creeper": Creeper,
     "Ender Dragon": EnderDragon,
     "Enderman": Enderman,
     "Ghast": Ghast,
     "Giant": Giant,
     "Magma Cube": LavaSlime,
     "Mooshroom": MushroomCow,
     "Ocelot": Ozelot,
     "Pig": Pig,
     "Zombie Pigman": PigZombie,
     "Sheep": Sheep,
     "Silverfish": Silverfish,
     "Skeleton": Skeleton,
     "Slime": Slime,
     "Snow Golem": SnowMan,
     "Spider": Spider,
     "Squid": Squid,
     "Villager": Villager,
     "Iron Golem": VillagerGolem,
     "Witch": Witch,
     "Wither": WitherBoss,
     "Wolf": Wolf,
     "Zombie": Zombie,
     }
inputs = (
        ("Mob", tuple(Mobs.keys())),
        ("Removes Selected Mob from Selection", "label"),
)

def perform(level, box, options):
    mob = options["Mob"]
    entitiesToRemove = []
    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.Entities:
            if e["id"].value == "mob":
               # Finds any mob with the current id value
                x = e["x"].value
                y = e["y"].value
                z = e["z"].value

                if x >= box.minx and x < box.maxx and y >=box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
                    entitiesToRemove.append((chunk, e))
                    chunk.dirty = True
    for (chunk, e) in entitiesToRemove:
        chunk.Entities.remove(e)
        # removes the entities
