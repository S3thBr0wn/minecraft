from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc

def main():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.postToChat("you have reached the end of the level")
	mc.setBlocks(x+1, y+16.5, z+0, x-3, y+17.5, z+0, 43)
	mc.setBlocks(x+1, y+9, z+0, x+1, y+0, z+0, 45)
	mc.setBlocks(x+1, y+18, z+0, x-3, y+18, z+0, 43)
	mc.setBlocks(x+1, y+20, z+0, x-0, y+20, z+0, 43)
	mc.setBlocks(x+1, y+19, z+0, x-1, y+19, z+0, 43)
	mc.setBlocks(x+1, y+18, z+0, x-2, y+18, z+0, 43)
	mc.setBlocks(x+1, y+17, z+0, x-4, y+17, z+0, 43)
	mc.setBlocks(x+1, y+17, z+0, x-3, y+17, z+0, 49)
	mc.setBlocks(x+1, y+16, z+0, x-2, y+16, z+0, 43)
	mc.setBlocks(x+1, y+15, z+0, x-1, y+15, z+0, 43)
	mc.setBlocks(x+1, y+14, z+0, x-0, y+14, z+0, 43)
	mc.setBlocks(x+1, y+19, z+0, x-0, y+19, z+0, 49)
	mc.setBlocks(x+1, y+18, z+0, x-1, y+18, z+0, 49)
	mc.setBlocks(x+1, y+17, z+0, x-2, y+17, z+0, 49)
	mc.setBlocks(x+1, y+16, z+0, x-1, y+16, z+0, 49)
	mc.setBlocks(x+1, y+15, z+0, x-0, y+15, z+0, 49)
	mc.setBlocks(x+1, y+20, z+0, x+1, y+10, z+0, 103)
	mc.setBlocks(x+1, y+19, z+0, x+1, y+9, z+0, 42)
	mc.setBlocks(x+1, y+18, z+0, x+1, y+8, z+0, 42)
	mc.setBlocks(x+1, y+17, z+0, x+1, y+7, z+0, 42)
	mc.setBlocks(x+1, y+16, z+0, x+1, y+6, z+0, 42)
	mc.setBlocks(x+1, y+15, z+0, x+1, y+5, z+0, 42)
	mc.setBlocks(x+1, y+14, z+0, x+1, y+4, z+0, 42)
	mc.setBlocks(x+1, y+13, z+0, x+1, y+3, z+0, 42)
	mc.setBlocks(x+1, y+12, z+0, x+1, y+2, z+0, 42)
	mc.setBlocks(x+1, y+11, z+0, x+1, y+1, z+0, 42)
	mc.setBlocks(x+1, y+10, z+0, x+1, y+1, z+0, 42)
	mc.setBlocks(x+1, y+9, z+0, x+1, y+1, z+0, 42)
	mc.setBlocks(x+1, y+8, z+0, x+1, y+1, z+0, 42)
	mc.setBlocks(x+1, y+7, z+0, x+1, y+1, z+0, 42)
main()

	

"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
