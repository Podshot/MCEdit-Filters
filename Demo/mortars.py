# coding unicode-escape
# Feel free to modify and use this filter however you wish. If you do,
# please give credit to SethBling.
# http://youtube.com/SethBling
# Comments by Podshot

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

displayName = "Mortars"

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
	"Instant Damage": 7,
	"Instant Health": 6,
	"Wither": 20,
	}
        # Creates a drop-down list with the words in the "s and combining them with their following numbers

Colors = {
	"Regeneration (Pink)": 16385,
	"Swiftness (Light Blue)": 16386,
	"Fire Resistance (Orange)": 16419,
	"Poison (Green)": 16388,
	"Healing (Red)": 16453,
	"Night Vision (Blue)": 16422,
	"Weakness (Gray)": 16424,
	"Strength (Magenta)": 16393,
	"Slowness (Gray-Blue)": 16426,
	"Harming (Purple)": 16460,
	"Invisibility (Light Gray-Blue)": 16430,
}

inputs = (
	("Max Height Gain", 5),
	("Random Max Height Gain", False),
	("Spawner Detection Radius", 50),
	("Spawn Ticks", 5),
	("Projectile", ("Splash Potion", "Arrow", "Snowball", "TNT")),
	("Potion Effect", tuple(Effects.keys())),
	("Potion Amplifier", 0),
	("Potion Duration (Seconds)", 60),
	("Potion Color", tuple(Colors.keys())),
	("TNT Fuse", 80),
)

def perform(level, box, options):
	peakGain = options["Max Height Gain"]
	spawnerRadius = options["Spawner Detection Radius"]
	spawnTicks = options["Spawn Ticks"]
	projectile = options["Projectile"]
	effect = options["Potion Effect"]
	amp = options["Potion Amplifier"]
	duration = options["Potion Duration (Seconds)"] * 20
	color = Colors[options["Potion Color"]]
	fuse = options["TNT Fuse"]
	# Binds the options to variables
	
	targets = FindSpawnerLocationsAndTargets(level, box)
	
	if projectile == "Splash Potion" or projectile == "Arrow" or projectile == "TNT":
		G = 0.115 #Gravitational constant
	elif projectile == "Snowball":
		G = 0.075
	# Sets the gravatational constants for the projectiles
	
	for loc in targets:
		target = targets[loc]
		lx, ly, lz = loc
		tx, ty, tz = target
		
		endGain = ty-ly
		horizDist = sqrt(dist2((lx, 0, lz), (tx, 0, tz)))
	
		if options["Random Max Height Gain"]:
			gain = random.randint(1, peakGain)
		else:
			gain = peakGain
		
		maxGain = max(gain, endGain + gain)
		
		# solve quadratic equation for velocity
		a = -horizDist*horizDist / (4*maxGain)
		b = horizDist
		c = -endGain
		
		slope = -b/(2*a) - sqrt(b*b-4*a*c)/(2*a)
		
		# vertical velocity
		vy = sqrt(maxGain*G)
		
		# horizontal velocity
		vh = vy/slope
		
		# calculate horizontal direction
		dx = tx-lx
		dz = tz-lz
		mag = sqrt(dx*dx + dz*dz)
		dirx = dx/mag
		dirz = dz/mag
		
		# horizontal velocity components
		vx = vh * dirx
		vz = vh * dirz

		spawner = createSpawner(loc, 0, spawnTicks, spawnerRadius)

		if projectile == "Splash Potion":
			potion = createPotion((lx+0.5, ly+1.0, lz+0.5), (vx, vy, vz), Effects[effect], duration, amp, color)
			spawner["SpawnData"] = potion
		elif projectile == "Snowball":
			snowball = createSnowball((lx+0.5, ly+1.0, lz+0.5), (vx, vy, vz))
			spawner["SpawnData"] = snowball
		elif projectile == "Arrow":
			arrow = createArrow((lx+0.5, ly+1.0, lz+0.5), (vx, vy, vz))
			spawner["SpawnData"] = arrow
		elif projectile == "TNT":
			tnt = createTNT((lx+0.5, ly+1.0, lz+0.5), (vx, vy, vz), fuse)
			spawner["SpawnData"] = tnt
		# Creates the projectiles and puts their data into the Spawner's "SpawnData" Tag Compound
		
		spawner["EntityId"] = spawner["SpawnData"]["id"]
		level.setBlockAt(lx, ly, lz, 52)
		level.setBlockDataAt(lx, ly, lz, 0)
		level.setBlockAt(tx, ty, tz, 0)
		level.setBlockDataAt(tx, ty, tz, 0)
		chunk = level.getChunk(lx/16, lz/16)
		chunk.TileEntities.append(spawner)
		chunk.dirty = True
		# Finish the filters execution
	
def FindSpawnerLocationsAndTargets(level, box):
	locations = []
	targets = []
	# Sets local variables
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				block = level.blockAt(x, y, z)
				if block == 35:
                                        # Looks for a block with the ID of 35
					data = level.blockDataAt(x, y, z)
					if data == 5:
                                                # Looks for a block with the ID of 35 and Data of 5
						locations.append((x, y, z))
						# Adds the location of the lime wool to the local variable of locations
					elif data == 14:
						targets.append((x, y, z))
	
	if len(targets) == 0:
		raise Exception("No valid targets (red wool)")
                # Notifies the user if the Red Wool block is not found
	if len(locations) == 0:
		raise Exception("No valid spawner locations (lime wool)")
	
	ret = {}
	for loc in locations:
		minDist = -1
		bestTarget = None
		for target in targets:
			d2 = dist2(loc, target)
			if minDist == -1 or d2 < minDist:
				minDist = d2
				bestTarget = target
		ret[loc] = bestTarget
	# This will find the closest Target and set it as the only target
	return ret

def dist2((x1, y1, z1), (x2, y2, z2)):
	dx = x2-x1
	dy = y2-y1
	dz = z2-z1
	
	return dx*dx + dy*dy + dz*dz

def createSpawner((x, y, z), delay, loopTicks, range):
	spawner = TAG_Compound()
	spawner["id"] = TAG_String("MobSpawner")
	spawner["Items"] = TAG_List()
	spawner["x"] = TAG_Int(x)
	spawner["y"] = TAG_Int(y)
	spawner["z"] = TAG_Int(z)
	spawner["Delay"] = TAG_Short(delay)
	spawner["MinSpawnDelay"] = TAG_Short(loopTicks)
	spawner["MaxSpawnDelay"] = TAG_Short(loopTicks)
	spawner["SpawnCount"] = TAG_Short(1)
	spawner["MaxNearbyEntities"] = TAG_Short(10000)
	spawner["RequiredPlayerRange"] = TAG_Short(range)
	# Creates a spawner with certain aspects

	return spawner

def createPotion((x, y, z), (vx, vy, vz), effect, duration, amp, potionId):
	thrownPotion = TAG_Compound()
	thrownPotion["yTile"] = TAG_Short(-1)

	motion = TAG_List()
	motion.append(TAG_Double(vx))
	motion.append(TAG_Double(vy))
	motion.append(TAG_Double(vz))
	thrownPotion["Motion"] = motion
	
	thrownPotion["OnGround"] = TAG_Byte(0)
	thrownPotion["inGround"] = TAG_Byte(0)
	thrownPotion["shake"] = TAG_Byte(0)
	thrownPotion["Dimension"] = TAG_Int(0)
	thrownPotion["inTile"] = TAG_Byte(0)
	thrownPotion["Air"] = TAG_Short(300)
	thrownPotion["id"] = TAG_String(u'ThrownPotion')
	
	pos = TAG_List()
	pos.append(TAG_Double(x))
	pos.append(TAG_Double(y))
	pos.append(TAG_Double(z))
	thrownPotion["Pos"] = pos
	
	thrownPotion["PortalCooldown"] = TAG_Int(0)
	thrownPotion["Fire"] = TAG_Short(0)
	thrownPotion["xTile"] = TAG_Short(-1)
	thrownPotion["zTile"] = TAG_Short(-1)
	thrownPotion["FallDistance"] = TAG_Float(0.0)
	
	rotation = TAG_List()
	rotation.append(TAG_Float(0))
	rotation.append(TAG_Float(0))
	thrownPotion["Rotation"] = rotation
	
	thrownPotion["Invulnerable"] = TAG_Byte(0)
	
	potion = TAG_Compound()
	potion["id"] = TAG_Short(373)
	potion["Damage"] = TAG_Short(potionId)
	potion["Count"] = TAG_Byte(1)
	
	tag = TAG_Compound()
	customPotionEffects = TAG_List()
	customPotionEffect = TAG_Compound()
	customPotionEffect["Amplifier"] = TAG_Byte(amp)
	customPotionEffect["Duration"] = TAG_Int(duration)
	customPotionEffect["Id"] = TAG_Byte(effect)
	customPotionEffects.append(customPotionEffect)
	tag["CustomPotionEffects"] = customPotionEffects
	potion["tag"] = tag

	thrownPotion["Potion"] = potion
	# Creates a potion with the choosen effect, type, and duration
	
	return thrownPotion

def createSnowball((x, y, z), (vx, vy, vz)):
	snowball = TAG_Compound()
	snowball["yTile"] = TAG_Short(-1)
	
	motion = TAG_List()
	motion.append(TAG_Double(vx))
	motion.append(TAG_Double(vy))
	motion.append(TAG_Double(vz))
	snowball["Motion"] = motion
	
	snowball["OnGround"] = TAG_Byte(0)
	snowball["inGround"] = TAG_Byte(0)
	snowball["shake"] = TAG_Byte(0)
	snowball["Dimension"] = TAG_Int(0)
	snowball["inTile"] = TAG_Byte(0)
	snowball["Air"] = TAG_Short(300)
	snowball["id"] = TAG_String(u'Snowball')
	
	pos = TAG_List()
	pos.append(TAG_Double(x))
	pos.append(TAG_Double(y))
	pos.append(TAG_Double(z))
	snowball["Pos"] = pos
	
	snowball["PortalCooldown"] = TAG_Int(0)
	snowball["Fire"] = TAG_Short(0)
	snowball["xTile"] = TAG_Short(-1)
	snowball["zTile"] = TAG_Short(-1)
	snowball["FallDistance"] = TAG_Float(0.0)
	
	rotation = TAG_List()
	rotation.append(TAG_Float(0))
	rotation.append(TAG_Float(0))
	snowball["Rotation"] = rotation
	
	snowball["Invulnerable"] = TAG_Byte(0)
	# Creates a snowball with the needed data
	
	return snowball

def createArrow((x, y, z), (vx, vy, vz)):
	arrow = TAG_Compound()
	arrow["yTile"] = TAG_Short(-1)
	arrow["pickup"] = TAG_Byte(2)
	
	motion = TAG_List()
	motion.append(TAG_Double(vx))
	motion.append(TAG_Double(vy))
	motion.append(TAG_Double(vz))
	arrow["Motion"] = motion
	
	arrow["OnGround"] = TAG_Byte(0)
	arrow["inGround"] = TAG_Byte(0)
	arrow["shake"] = TAG_Byte(0)
	arrow["damage"] = TAG_Double(2.0)
	arrow["Dimension"] = TAG_Int(0)
	arrow["inTile"] = TAG_Byte(0)
	arrow["Air"] = TAG_Short(300)
	arrow["id"] = TAG_String(u'Arrow')
	
	pos = TAG_List()
	pos.append(TAG_Double(x))
	pos.append(TAG_Double(y))
	pos.append(TAG_Double(z))
	arrow["Pos"] = pos
	
	arrow["PortalCooldown"] = TAG_Int(0)
	arrow["Fire"] = TAG_Short(0)
	arrow["xTile"] = TAG_Short(-1)
	arrow["zTile"] = TAG_Short(-1)
	arrow["FallDistance"] = TAG_Float(0.0)
	arrow["inData"] = TAG_Byte(0)
	
	rotation = TAG_List()
	rotation.append(TAG_Float(0))
	rotation.append(TAG_Float(0))
	arrow["Rotation"] = rotation
	
	arrow["Invulnerable"] = TAG_Byte(0)
	# Creates a Arrow with the needed data
	
	return arrow
	
def createTNT((x, y, z), (vx, vy, vz), fuse):
	primedTnt = TAG_Compound()
	
	motion = TAG_List()
	motion.append(TAG_Double(vx))
	motion.append(TAG_Double(vy))
	motion.append(TAG_Double(vz))
	primedTnt["Motion"] = motion
	
	primedTnt["OnGround"] = TAG_Byte(1)
	primedTnt["Fuse"] = TAG_Byte(fuse)
	primedTnt["Dimension"] = TAG_Int(0)
	primedTnt["Air"] = TAG_Short(300)
	primedTnt["id"] = TAG_String(u'PrimedTnt')
	
	pos = TAG_List()
	pos.append(TAG_Double(x))
	pos.append(TAG_Double(y))
	pos.append(TAG_Double(z))
	primedTnt["Pos"] = pos
	
	primedTnt["PortalCooldown"] = TAG_Int(0)
	primedTnt["Fire"] = TAG_Short(-1)
	primedTnt["FallDistance"] = TAG_Float(0.0)
	
	rotation = TAG_List()
	rotation.append(TAG_Float(0.0))
	rotation.append(TAG_Float(0.0))
	primedTnt["Rotation"] = rotation
	
	primedTnt["Invulnerable"] = TAG_Byte(0)
	# Creates a Primed-Tnt Tag Compound with certain data

	return primedTnt
