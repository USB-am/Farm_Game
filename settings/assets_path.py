import os


BASE_DIR = os.getcwd()

ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

LANDSCAPE = os.path.join(ASSETS_DIR, 'landscape')
STONE_ASSET = os.path.join(LANDSCAPE, 'stone.png')

ITEMS = os.path.join(ASSETS_DIR, 'items')
TOOLS = os.path.join(ITEMS, 'tools')
SHOVEL_TOOL = os.path.join(TOOLS, 'shovel.png')
