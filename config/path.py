import os


BASE_DIR = os.getcwd()

# STATICS
STATIC_DIR = os.path.join(BASE_DIR, 'static')
SPRITES_DIR = os.path.join(STATIC_DIR, 'sprites')
MENU_SPRITES_DIR = os.path.join(SPRITES_DIR, 'menu')
GAME_SPRITES_DIR = os.path.join(SPRITES_DIR, 'game')
GAME_BORDER_SPRITES = os.path.join(GAME_SPRITES_DIR, 'border')
