# This filter creates Traz-Landers Redstone Controlled Spawner Layout
# This was created by Podshot
# If you modify this filter, please give credit to Podshot
# Have an idea? Can you improve this code? Fork the Github!
# Link: https://github.com/Podshot/MCEdit-Filters
import time # for timing
from numpy import *
from pymclevel import alphaMaterials
from pymclevel.schematic import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_Float
from pymclevel import TAG_String
from pymclevel.nbt import TAG_Byte_Array
from pymclevel.box import Vector
from math import sqrt
import random

# Some imports are not used, but you can never have too many imports :D
displayName = "Red-Spawner"

VERSION = "1.2.0"
UPDATE_URL = ""

inputs = (
        ("Extend amount", (0,0,10)),
        ("Made by Podshot", "label"),
        ("Change the sponge that is generated", "label"),
        ("To a spawner that spawns a spawner minecart between", "label"),
        ("The sponge and the dispenser", "label"),
        ("Make sure to add a lava bucket to the dispenser before use!", "label"),
        ("", "label"),
        ("It will generate the layout towards the west, put the selection box", "label"),
        ("were the inupt is. Make sure the selection box is 1x1x1!", "label"),
        ("Version: 1.2","label"),
)

def repeated():
    e = MCSchematic(shape=(3,3,3),filename='')
    e._Blocks = [[[0,0,0],[0,20,0],[0,0,0]],[[0,19,0],[20,0,20],[1,23,1]],[[0,0,0],[0,0,0],[55,93,55]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,2,0]],[[0,0,0],[0,0,0],[0,9,0]]])
    return e
    
def createSchematic():
    e = MCSchematic(shape=(9,6,3),filename='')
    e._Blocks = [[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,20,0],[0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,19,0],[0,0,0,0,0,0,20,0,20],[1,0,1,0,0,1,1,23,1]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[93,1,93,1,75,55,55,93,55]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,76,1,55,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,1,55,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,55,0,0,0,0,0,0,0]]]
    e.root_tag['Data'] = TAG_Byte_Array([[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,2,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[1,0,9,0,1,0,0,9,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,5,0,14,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,15,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,15,0,0,0,0,0,0,0]]])
    return e
        
    
def perform(level, box, options):
    platform(level, box, options)
    level.markDirtyBox(box)

def repeat(level, dest, count):
    # Sets the variable "re" to one digit higher than what the user defined (more on why later)
    re = count + 1
    cur = 1
    # Sets the current "cycle" to 1
    x = 9
    # Start amount of blocks to move the vector away from the selection box
    while cur != re:
        # Calls a "while" statement
        # As long as the variable "cur" does not equal the variable "re" it runs the code underneath
        # This is why I set "re" to be one higher than the user defined amount, because the "while" will end when
        # It equals the defined amount, so one higher will generate what the user wanted
        vec = Vector(x,-1,-2)
        # Sets the vector variable
        level.copyBlocksFrom(rep,rep.bounds,vec + dest)
        # Copys the blocks
        x = x + 3
        # Sets the variable x to 3 digits higher than is was previous
        cur = cur + 1
        # Sets the variable "cur" one digit higher
        

        
red = createSchematic()
rep = repeated()
def place(level,dest):
    vec = Vector(0,-1,-2)
    level.copyBlocksFrom(red,red.bounds,vec + dest)

def platform(level, box, options):
    method = "Red-Spawner"
    print '%s: Started: %s' % (method, time.ctime())
    times = options["Extend amount"]
    place(level,[box.minx,box.miny,box.minz])
    # Calls the place block function (Defined at line 70)
    if times != 0:
        # Checks to see if the extend amount is not zero
        repeat(level, [box.minx,box.miny,box.minz], times)
        # Calls the repeat function
    print '%s: Ended: %s' % (method, time.ctime())
