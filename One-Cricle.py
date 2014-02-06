from pymclevel import MCSchematic
from pymclevel.nbt import *
from pymclevel.box import Vector
from pymclevel.materials import alphaMaterials
import time

debug = True
logFile = []

block_map = {
    0:"minecraft:air",1:"minecraft:stone",2:"minecraft:grass",3:"minecraft:dirt",4:"minecraft:cobblestone",5:"minecraft:planks",6:"minecraft:sapling",
    7:"minecraft:bedrock",8:"minecraft:flowing_water",9:"minecraft:water",10:"minecraft:flowing_lava",11:"minecraft:lava",12:"minecraft:sand",13:"minecraft:gravel",
    14:"minecraft:gold_ore",15:"minecraft:iron_ore",16:"minecraft:coal_ore",17:"minecraft:log",18:"minecraft:leaves",19:"minecraft:sponge",20:"minecraft:glass",
    21:"minecraft:lapis_ore",22:"minecraft:lapis_block",23:"minecraft:dispenser",24:"minecraft:sandstone",25:"minecraft:noteblock",26:"minecraft:bed",
    27:"minecraft:golden_rail",28:"minecraft:detector_rail",29:"minecraft:sticky_piston",30:"minecraft:web",31:"minecraft:tallgrass",32:"minecraft:deadbush",
    33:"minecraft:piston",34:"minecraft:piston_head",35:"minecraft:wool",36:"minecraft:piston_extension",37:"minecraft:yellow_flower",38:"minecraft:red_flower",
    39:"minecraft:brown_mushroom",40:"minecraft:red_mushroom",41:"minecraft:gold_block",42:"minecraft:iron_block",43:"minecraft:double_stone_slab",
    44:"minecraft:stone_slab",45:"minecraft:brick_block",46:"minecraft:tnt",47:"minecraft:bookshelf",48:"minecraft:mossy_cobblestone",49:"minecraft:obsidian",
    50:"minecraft:torch",51:"minecraft:fire",52:"minecraft:mob_spawner",53:"minecraft:oak_stairs",54:"minecraft:chest",55:"minecraft:redstone_wire",
    56:"minecraft:diamond_ore",57:"minecraft:diamond_block",58:"minecraft:crafting_table",59:"minecraft:wheat",60:"minecraft:farmland",61:"minecraft:furnace",
    62:"minecraft:lit_furnace",63:"minecraft:standing_sign",64:"minecraft:wooden_door",65:"minecraft:ladder",66:"minecraft:rail",67:"minecraft:stone_stairs",
    68:"minecraft:wall_sign",69:"minecraft:lever",70:"minecraft:stone_pressure_plate",71:"minecraft:iron_door",72:"minecraft:wooden_pressure_plate",
    73:"minecraft:redstone_ore",74:"minecraft:lit_redstone_ore",75:"minecraft:unlit_redstone_torch",76:"minecraft:redstone_torch",77:"minecraft:stone_button",
    78:"minecraft:snow_layer",79:"minecraft:ice",80:"minecraft:snow",81:"minecraft:cactus",82:"minecraft:clay",83:"minecraft:reeds",84:"minecraft:jukebox",
    85:"minecraft:fence",86:"minecraft:pumpkin",87:"minecraft:netherrack",88:"minecraft:soul_sand",89:"minecraft:glowstone",90:"minecraft:portal",
    91:"minecraft:lit_pumpkin",92:"minecraft:cake",93:"minecraft:unpowered_repeater",94:"minecraft:powered_repeater",
    95:"minecraft:stained_glass",96:"minecraft:trapdoor",97:"minecraft:monster_egg",98:"minecraft:stonebrick",
    99:"minecraft:brown_mushroom_block",100:"minecraft:red_mushroom_block",101:"minecraft:iron_bars",102:"minecraft:glass_pane",103:"minecraft:melon_block",
    104:"minecraft:pumpkin_stem",105:"minecraft:melon_stem",106:"minecraft:vine",107:"minecraft:fence_gate",108:"minecraft:brick_stairs",109:"minecraft:stone_brick_stairs",
    110:"minecraft:mycelium",111:"minecraft:waterlily",112:"minecraft:nether_brick",113:"minecraft:nether_brick_fence",114:"minecraft:nether_brick_stairs",
    115:"minecraft:nether_wart",116:"minecraft:enchanting_table",117:"minecraft:brewing_stand",118:"minecraft:cauldron",119:"minecraft:end_portal",
    120:"minecraft:end_portal_frame",121:"minecraft:end_stone",122:"minecraft:dragon_egg",123:"minecraft:redstone_lamp",124:"minecraft:lit_redstone_lamp",
    125:"minecraft:double_wooden_slab",126:"minecraft:wooden_slab",127:"minecraft:cocoa",128:"minecraft:sandstone_stairs",129:"minecraft:emerald_ore",
    130:"minecraft:ender_chest",131:"minecraft:tripwire_hook",132:"minecraft:tripwire",133:"minecraft:emerald_block",134:"minecraft:spruce_stairs",
    135:"minecraft:birch_stairs",136:"minecraft:jungle_stairs",137:"minecraft:command_block",138:"minecraft:beacon",139:"minecraft:cobblestone_wall",
    140:"minecraft:flower_pot",141:"minecraft:carrots",142:"minecraft:potatoes",143:"minecraft:wooden_button",144:"minecraft:skull",145:"minecraft:anvil",
    146:"minecraft:trapped_chest",147:"minecraft:light_weighted_pressure_plate",148:"minecraft:heavy_weighted_pressure_plate",149:"minecraft:unpowered_comparator",
    150:"minecraft:powered_comparator",151:"minecraft:daylight_detector",152:"minecraft:redstone_block",153:"minecraft:quartz_ore",154:"minecraft:hopper",
    155:"minecraft:quartz_block",156:"minecraft:quartz_stairs",157:"minecraft:activator_rail",158:"minecraft:dropper",159:"minecraft:stained_hardened_clay",
    170:"minecraft:hay_block",171:"minecraft:carpet",172:"minecraft:hardened_clay",173:"minecraft:coal_block",174:"minecraft:packed_ice",175:"minecraft:double_plant"
}

shapes = {
    "One Circle": 1,
    "Sphere": 3,
    }

inputs = (
    ("Shape Type:", tuple(sorted(shapes.keys()))),
    ("Block Type:", alphaMaterials.Stone),
    )
    
def createOneCircle():
    e = MCSchematic(shape=(8,2,7),filename='')
    e._Blocks = [[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,55,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]])
    return e
    
def createSphere():
    e = MCSchematic(shape=(8,30,7),filename='')
    e._Blocks = [[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,55,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,159,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,159,93,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,159,137,137,137,137,137,137],[0,55,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,0,137,137,137,137,137,137],[137,55,137,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137],[0,0,0,137,137,137,137,137]],[[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[55,0,55,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55],[0,0,0,55,55,55,55,55]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,13,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]])
    return e
    
def mapBlocks(blockid):
    bid = block_map[blockid]
    return str(bid)

def createCMDBlock(x, y, z, level, command):
    commandBlock = TAG_Compound()
    commandBlock["id"] = TAG_String("Control")
    commandBlock["x"] = TAG_Int(x)
    commandBlock["y"] = TAG_Int(y)
    commandBlock["z"] = TAG_Int(z)
    commandBlock["CustomName"] = TAG_String(u'@')
    commandBlock["TrackOutput"] = TAG_Byte(1)
    commandBlock["Command"] = TAG_String(command)
    chunk = level.getChunk(x/16, z/16)
    chunk.TileEntities.append(commandBlock)
    chunk.dirty = True
    if debug == True:
        app = str("X: " + str(x) + " Y: " + str(y) + " Z: " + str(z) + "\n")
        logFile.append(app)
        del app
    del commandBlock

def createOne(level, dest):
    vec = Vector(-1,0,-2)
    level.copyBlocksFrom(createOneCircle(),createOneCircle().bounds,vec + dest)

def createOneTiles(boxx, boxy, boxz, idBlock, dataBlock, level, offset):
    blockvar = ",DisplayTile:" + str(idBlock) + ",DisplayData:" + str(dataBlock) + ",DisplayOffset:" + str(offset)
    destination = buildCoords(boxx, boxy, boxz)
    createCMDBlock(boxx + 6, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,265f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,340f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,350f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,360f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,360f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,270f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,280f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,290f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,300f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,310f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,320f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,330f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,260f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,250f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,240f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,230f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,220f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,210f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,200f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,130f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,140f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,150f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,160f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,170f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,180f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,190f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,120f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,110f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,100f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,90f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,80f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,70f]" + blockvar + "}"))
    createCMDBlock(boxx + 1, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,60f]" + blockvar + "}"))
    createCMDBlock(boxx + 1, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,0f]" + blockvar + "}"))
    createCMDBlock(boxx + 1, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,10f]" + blockvar + "}"))
    createCMDBlock(boxx + 1, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,20f]" + blockvar + "}"))
    createCMDBlock(boxx - 1, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,30f]" + blockvar + "}"))
    createCMDBlock(boxx - 1, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,40f]" + blockvar + "}"))
    createCMDBlock(boxx - 1, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,50f]" + blockvar + "}"))
    createCMDBlock(boxx - 1, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[90f,5-f]" + blockvar + "}"))
    
    
def createAnObjectCalledSphere(level, dest):
    vec = Vector(-1,-28,-2)
    level.copyBlocksFrom(createSphere(),createSphere().bounds,vec + dest)
    
def buildCoords(selx, sely, selz):
    coord = str(selx) + " " + str(sely) + " " + str(selz)
    return coord
    
def createSphereTiles(boxx, boxy, boxz, idBlock, dataBlock, level, offset):
    blockvar = ",DisplayTile:" + str(idBlock) + ",DisplayData:" + str(dataBlock) + ",DisplayOffset:" + str(offset)
    destination = buildCoords(boxx, boxy, boxz)
    createCMDBlock(boxx + 6, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[175f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[175f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[175f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayName:1,Rotation:[175f,265f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[120f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[120f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 6, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[120f,175f]" + blockvar + "}"))
    #
    createCMDBlock(boxx + 5, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[120f,265f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[110f,85f]" + blockvar +"}"))
    createCMDBlock(boxx + 5, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayIile:1,Rotation:[110f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[110f,265f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[100f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[100f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 5, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[100f,175f]" + blockvar + "}"))
    #
    createCMDBlock(boxx + 4, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[100f,265f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-40f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Roatation:[-40f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-40f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-40f,265]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-30f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 4, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-30f,85f]" + blockvar + "}"))
    #
    createCMDBlock(boxx + 3, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-30f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-30f,265f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-20f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-20f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-20f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-20f,265]" + blockvar + "}"))
    createCMDBlock(boxx + 3, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-10f,-5f]" + blockvar + "}"))
    #
    createCMDBlock(boxx + 2, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-10f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-10f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[-10f,265f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[0f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[0f,85]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 3, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[0f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 2, boxy, boxz + 4, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[0f,265f]" + blockvar + "}"))
    #
    createCMDBlock(boxx + 1, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[20f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx + 1, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[20f,85f]" + blockvar + "}"))
    createCMDBlock(boxx + 1, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[20f,175f]" + blockvar + "}"))
    createCMDBlock(boxx + 1, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[20f,265f]" + blockvar + "}"))
    #
    createCMDBlock(boxx - 1, boxy, boxz - 2, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[30f,-5f]" + blockvar + "}"))
    createCMDBlock(boxx - 1, boxy, boxz - 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[30f,85f]" + blockvar + "}"))
    createCMDBlock(boxx - 1, boxy, boxz, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[30f,175f]" + blockvar + "}"))
    createCMDBlock(boxx - 1, boxy, boxz + 1, level, str("/summon MinecartRideable " + destination + " {CustomDisplayTile:1,Rotation:[30f,265f]" + blockvar + "}"))
    
    
    
    
def perform(level, box, options):
    xbox = box.maxx - box.minx
    ybox = box.maxy - box.miny
    zbox = box.maxz - box.minz
    form = options["Shape Type:"]
    blockid = options["Block Type:"].ID
    blockdata = options["Block Type:"].blockData
    
    if form == "One Circle":
        createOne(level, [box.minx,box.miny,box.minz])
        createOneTiles(box.minx, box.miny, box.minz, blockid, blockdata, level, 84)
    if form == "Sphere":
        createAnObjectCalledSphere(level, [box.minx,box.miny,box.minz])
        createSphereTiles(box.minx, box.miny, box.minz, blockid, blockdata, level, 84)
    if debug == True:
        with open("logging.txt", "w") as f:
            f.writelines(logFile)
    level.markDirtyBox = True

    

