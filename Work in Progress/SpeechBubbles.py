# This is filter SpeechBubbles. It can create command blocks for "Speech Bubbles" as seen in http://www.youtube.com/watch?v=2jYX526zgII
# This filter requires Minecraft 14w04b, because it uses the new /particle command
# This filter was created by Tomsik68, concept made by SimplySarc
# If you redistribute/modify, please give credit to SimplySarc & Tomsik68 :)
# ================================================================
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
from pymclevel.nbt import TAG_Compound, TAG_String, TAG_Int, TAG_Byte
particles = {
    "Water Dripping": "dripWater",
    "Lava Dripping": "dripLava",
    "Smoke": "smoke",
    "Large Smoke": "largeSmoke",
    "Fireworks":"fireworksSpark",
    "Tool Break": "iconcrack_",
    "Egg/Snowball Break": "snowballpoof",
    "Block break": "tilecrack_",
    "Portal": "portal",
    "Water Splash":"splash",
    "Water Bubbles":"bubble",
    "Void particles":"townaura",
    "Explosion": "hugeexplosion",
    "Flame":"flame",
    "Heart":"heart",
    "Cloud":"cloud",
    "Critical hit spark":"crit",
    "Magic weapon critical hit spark":"magicCrit",
    "Note":"note",
    "Magic Runes":"enchantmenttable",
    "Lava Spark": "lava",
    "Footsteps": "footstep",
    "Redstone Fumes": "reddust",
    "Happy Villager":"happyVillager",
    "Angry Villager":"angryVillager",
    "Witch": "witchMagic",
    "Slime Splatter": "slime",
    "Potion Effect":"spell",
    "Instant Potion Effect":"instantSpell"
}
displayName="Speech Bubbles"
inputs = (
  ("SimplySarc's Speech Bubbles, coded by Tomsik68", "label"),
# Uncomment following line for particle selection:
#  ("Particle type", tuple(particles.keys())),
  ("Entity selector", ("string", "value=@p")),
  ("Particle speed", 0),
  ("Particle count", 2),
  ("Delta X", 0),
  ("Delta Y", 0),
  ("Delta Z", 0),
  ("Build toward...", ("X", "Z")),
  ("How it works: You make a selection in MCEdit(can be 3D). Click filter to transform your selection into command blocks. At the moment, you need to wire up those command blocks yourself, order doesn't matter. When you trigger the command block chain, they'll display chosen particles above player's head.","label")
)

displayName = "SpeechBubbles"

def createParticleCommand(particle, x, y, z, dx, dy, dz, speed, count, selector):
    cmd = "particle %s ~%f ~%f ~%f %f %f %f %f %d %s" % (particle, x / 16.0 + dx, y / 16.0 + dy, z / 16.0 + dz, 0, 0, 0, speed, count, selector)
    return cmd
def createCommandBlock(x, y, z, command):
    commandBlock = TAG_Compound()
    commandBlock["id"] = TAG_String("Control")
    commandBlock["x"] = TAG_Int(x)
    commandBlock["y"] = TAG_Int(y)
    commandBlock["z"] = TAG_Int(z)
    commandBlock["Command"] = TAG_String(command)
    commandBlock["SuccessCount"] = TAG_Int(0)
    commandBlock["LastOutput"] = TAG_String("")
    commandBlock["TrackOutput"] = TAG_Byte(0)
    return commandBlock
def perform(level, box, options):
    generatedCommands = []
    dx = options["Delta X"]
    dy = options["Delta Y"]
    dz = options["Delta Z"]
    particle = "dripWater"
    if "Particle type" in options:
        particle = particles[options["Particle type"]]
    speed = options["Particle speed"]
    count = options["Particle count"]
    selector = options["Entity selector"]
    for x in xrange(box.minx, box.maxx):
        for y in xrange(box.miny, box.maxy):
            for z in xrange(box.minz, box.maxz):
                if level.blockAt(x, y, z) != 0:
                    generatedCommands.append(createParticleCommand(particle, x - box.minx, y - box.miny, z - box.minz, dx, dy, dz, speed, count, selector))
    x = box.maxx + 1
    y = box.maxy + 1
    z = box.maxz + 1
    towardX = (options["Build toward..."] == "X")
    for cmd in generatedCommands:
        level.setBlockAt(x, y, z, 137)
        level.getChunk(x / 16, z / 16).TileEntities.append(createCommandBlock(x, y, z, cmd))
        level.getChunk(x / 16, z / 16).dirty = True
        if towardX:
            x += 1
        else:
            z += 1
