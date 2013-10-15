from pymclevel.nbt import *

displayName = "Id to Block Name"

def num2str(string):
    popped4 = ''
    print 'String: %s' % (string)
    popped = string.pop(4)
    print 'Pop #1: %s' % (string)
    popped2 = string.pop(4)
    print 'Pop #2: %s' % (string)
    popped3 = string.pop(4)
    print 'Pop #3: %s' % (string)
    try:
        popped4 = string.pop(4)
    except IndexError:
        popped4 = ''
        pass
    if popped == '0':
        string.append('minecraft:air')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '1':
        string.append('minecraft:stone')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '2':
        string.append('minecraft:grass')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '3':
        string.append('minecraft:dirt')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '4':
        string.append('minecraft:cobblestone')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '5':
        string.append('minecraft:planks')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '6':
        string.append('minecraft:sapling')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '7':
        string.append('minecraft:bedrock')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '8':
        string.append('minecraft:flowing_water')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '9':
        string.append('minecraft:water')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '10':
        string.append('minecraft:flowing_lava')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '11':
        string.append('minecraft:lava')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '12':
        string.append('minecraft:sand')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '13':
        string.append('minecraft:gravel')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '14':
        string.append('minecraft:gold_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '15':
        string.append('minecraft:iron_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '16':
        string.append('minecraft:coal_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '17':
        string.append('minecraft:log')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '18':
        string.append('minecraft:leaves')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '19':
        string.append('minecraft:sponge')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '20':
        string.append('minecraft:glass')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '21':
        string.append('minecraft:lapis_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '22':
        string.append('minecraft:lapis_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '23':
        string.append('minecraft:dispenser')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '24':
        string.append('minecraft:sandstone')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '25':
        string.append('minecraft:noteblock')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '26':
        string.append('minecraft:bed')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '27':
        string.append('minecraft:golden_rail')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '28':
        string.append('minecraft:dectector_rail')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '29':
        string.append('minecraft:sticky_piston')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '30':
        string.append('minecraft:web')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '31':
        string.append('minecraft:tallgrass')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '32':
        string.append('minecraft:deadbush')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '33':
        string.append('minecraft:piston')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '34':
        string.append('minecraft:piston_head')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '35':
        string.append('minecraft:wool')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '36':
        string.append('minecraft:piston_extension')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '37':
        string.append('minecraft:yellow_flower')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '38':
        string.append('minecraft:red_flower')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '39':
        string.append('minecraft:brown_mushroom')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '40':
        string.append('minecraft:red_mushroom')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '41':
        string.append('minecraft:gold_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '42':
        string.append('minecraft:iron_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '43':
        string.append('minecraft:double_stone_slab')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '44':
        string.append('minecraft:stone_slab')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '45':
        string.append('minecraft:brick_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '46':
        string.append('minecraft:tnt')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '47':
        string.append('minecraft:bookshelf')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '48':
        string.append('minecraft:mossy_cobblestone')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '49':
        string.append('minecraft:obsidian')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '50':
        string.append('minecraft:torch')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '51':
        string.append('minecraft:fire')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '52':
        string.append('minecraft:mob_spawner')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '53':
        string.append('minecraft:oak_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '54':
        string.append('minecraft:chest')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '55':
        string.append('minecraft:redstone_wire')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '56':
        string.append('minecraft:diamond_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '57':
        string.append('minecraft:diamond_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '58':
        string.append('minecraft:crafting_table')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '59':
        string.append('minecraft:wheat')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '60':
        string.append('minecraft:farmland')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '61':
        string.append('minecraft:furnace')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '62':
        string.append('minecraft:lit_furnace')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '63':
        string.append('minecraft:standing_sign')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '64':
        string.append('minecraft:wooden_door')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '65':
        string.append('minecraft:ladder')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '66':
        string.append('minecraft:rail')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '67':
        string.append('minecraft:stone_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '68':
        string.append('minecraft:wall_sign')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '69':
        string.append('minecraft:lever')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '70':
        string.append('minecraft:stone_pressure_plate')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '71':
        string.append('minecraft:iron_door')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '72':
        string.append('minecraft:wooden_pressuer_plate')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '73':
        string.append('minecraft:redstone_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '74':
        string.append('minecraft:lit_redstone_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '75':
        string.append('minecraft:unlit_redstone_torch')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '76':
        string.append('minecraft:redstone_torch')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '77':
        string.append('minecraft:stone_button')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '78':
        string.append('minecraft:snow_layer')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '79':
        string.append('minecraft:ice')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '80':
        string.append('minecraft:snow')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '81':
        string.append('minecraft:cactus')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '82':
        string.append('minecraft:clay')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '83':
        string.append('minecraft:reeds')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '84':
        string.append('minecraft:jukebox')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '85':
        string.append('minecraft:fence')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '86':
        string.append('minecraft:pumpkin')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '87':
        string.append('minecraft:netherrack')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '88':
        string.append('minecraft:soul_sand')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '89':
        string.append('minecraft:glowstone')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '90':
        string.append('minecraft:portal')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '91':
        string.append('minecraft:lit_pumpkin')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '92':
        string.append('minecraft:cake')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '93':
        string.append('minecraft:unpowered_repeater')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '94':
        string.append('minecraft:powered_repeater')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '95':
        string.append('minecraft:chest_locked_aprilfools_super_old_legacy_we_should_not_even_have_this')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '96':
        string.append('minecraft:trapdoor')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '97':
        string.append('minecraft:monster_egg')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '98':
        string.append('minecraft:stonebrick')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '99':
        string.append('minecraft:brown_mushroom_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '100':
        string.append('minecraft:red_mushroom_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '101':
        string.append('minecraft:iron_bars')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '102':
        string.append('minecraft:glass_pane')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '103':
        string.append('minecraft:melon_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '104':
        string.append('minecraft:pumpkin_stem')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '105':
        string.append('minecraft:melon_stem')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '106':
        string.append('minecraft:vine')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '107':
        string.append('minecraft:fence_gate')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '108':
        string.append('minecraft:brick_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '109':
        string.append('minecraft:stone_brick_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '110':
        string.append('minecraft:mycelium')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '111':
        string.append('minecraft:waterlily')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '112':
        string.append('minecraft:nether_brick')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '113':
        string.append('minecraft:nether_brick_fence')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '114':
        string.append('minecraft:nether_brick_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '115':
        string.append('nether_wart')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '116':
        string.append('minecraft:enchanting_table')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '117':
        string.append('minecraft:brewing_stand')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '118':
        string.append('minecraft:cauldron')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '119':
        string.append('minecraft:end_portal')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '120':
        string.append('minecraft:end_portal_frame')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '121':
        string.append('minecraft:end_stone')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '122':
        string.append('minecraft:dragon_egg')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '123':
        string.append('minecraft:redstone_lamp')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '124':
        string.append('minecraft:lit_redstone_lamp')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '125':
        string.append('minecraft:double_wooden_slab')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '126':
        string.append('minecraft:wooden_slab')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '127':
        string.append('minecraft:cocoa')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '128':
        string.append('minecraft:sandstone_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '129':
        string.append('minecraft:emerald_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '130':
        string.append('minecraft:ender_chest')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '131':
        string.append('minecraft:tripwire_hook')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '132':
        string.append('minecraft:tripwire')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '133':
        string.append('minecraft:emerald_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '134':
        string.append('minecraft:spruce_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '135':
        string.append('minecraft:birch_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '136':
        string.append('minecraft:jungle_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '137':
        string.append('minecraft:command_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '138':
        string.append('minecraft:beacon')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '139':
        string.append('minecraft:cobblestone_wall')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '140':
        string.append('minecraft:flower_pot')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '141':
        string.append('minecraft:carrots')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '142':
        string.append('minecraft:potatoes')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '143':
        string.append('minecraft:wooden_button')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '144':
        string.append('minecraft:skull')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '145':
        string.append('minecraft:anvil')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '146':
        string.append('minecraft:trapped_chest')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '147':
        string.append('minecraft:light_weighted_pressure_plate')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '148':
        string.append('minecraft:heavy_weighted_pressure_plate')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '149':
        string.append('minecraft:unpowered_comarator')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '150':
        string.append('minecraft:powered_comparator')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '151':
        string.append('minecraft:daylight_detector')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '152':
        string.append('minecraft:redstone_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '153':
        string.append('minecraft:quartz_ore')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '154':
        string.append('minecraft:hopper')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '155':
        string.append('minecraft:quartz_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '156':
        string.append('minecraft:quartz_stairs')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '157':
        string.append('minecraft:activator_rail')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '158':
        string.append('minecraft:dropper')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '159':
        string.append('minecraft:stained_hardened_clay')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '170':
        string.append('minecraft:hay_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '171':
        string.append('minecraft:carpet')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '172':
        string.append('minecraft:hardened_clay')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '173':
        string.append('minecraft:coal_block')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '174':
        string.append('minecraft:packed_ice')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    if popped == '175':
        string.append('minecraft:double_plant')
        string.append(popped2)
        string.append(popped3)
        string.append(popped4)
    return string

def perform(level, box, options):

    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            if t["id"].value == "Control":
                x = t["x"].value
                y = t["y"].value
                z = t["z"].value

                if (x,y,z) in box:
                    command = t["Command"].value
                    if command.startswith("/setblock") or command.startswith("/testforblock") or command.startswith("setblock") or command.startswith("testforblock"):
                        command = command.split()
                        new_command = num2str(command)
                        new_command = ' '.join(new_command)
                        t["Command"] = TAG_String(new_command)
                        chunk.dirty = True

                    
                    
