import os


BASE_DIR = os.getcwd()

ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

CHARACTER_ASSETS = os.path.join(ASSETS_DIR, 'character')
CHARACTER = os.path.join(CHARACTER_ASSETS, 'Pink_Monster', 'Pink_Monster.png')

LANDSCAPE = os.path.join(ASSETS_DIR, 'landscape')
STONE_ASSET = os.path.join(LANDSCAPE, 'stone.png')

ITEMS = os.path.join(ASSETS_DIR, 'items')
TOOLS = os.path.join(ITEMS, 'tools')
SHOVEL_TOOL = os.path.join(TOOLS, 'shovel.png')

MAP_OBJECTS = os.path.join(ASSETS_DIR, 'map_objects')
HOUSE_ASSET = os.path.join(MAP_OBJECTS, 'house.png')
