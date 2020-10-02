import os

current_path = os.path.dirname(__file__) # Game File Location
asset_path = os.path.join(current_path, 'Assets') # Asset Folder Path

image_path = os.path.join(asset_path, "Images") # Image Folder Path
sound_path = os.path.join(asset_path, "Sounds") # Sound Folder Path
font_path = os.path.join(asset_path, "Fonts") # Font Folder Path

# Game Config

BUILD_VERSION = "0.47.12-public" # Build Version

PROGRAM_NAME = "Space Invaders" # Game Game
AUTHOR = "Kevin Apetrei" # Game Author

# Title Template = f"{config.PROGRAM_NAME} | {config.BUILD_VERSION} | By {config.AUTHOR}"

NUMBER_OF_ENEMIES = 6 # Number of Enemies

GAME_WINDOW_SIZE = (800, 600) # Game Window Size

ICON = os.path.join(image_path, 'icon.png') # Icon File
BACKGROUND = os.path.join(image_path, 'background.png') # Background Image

PLAYER_IMG = os.path.join(image_path, 'player.png') # Player Image
ENEMY_IMG = os.path.join(image_path, 'enemy.png') # Enemy Image

BULLET_IMG = os.path.join(image_path, 'bullet.png') # Bullet Image

BEBAS_REGULAR_FONT = os.path.join(font_path, "Bebas-Regular.ttf") # Bebas Regular Font File

BACKGROUND_MUSIC = os.path.join(sound_path, "background_music.wav") # Background Music File
EXPLOSION_EFFECT = os.path.join(sound_path, "explosion_effect.wav") # Explosion Effect File
LASER_EFFECT = os.path.join(sound_path, "laser_effect.wav") # Laser Effect File
