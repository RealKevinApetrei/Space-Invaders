import pygame
from pygame import mixer

import random
import math
import time

import warnings

import config


# Initalize PyGame and Everything else
pygame.init() # INIT PyGame
warnings.simplefilter("ignore") # Ignore Warnings (DEPRECATIONWARNING)

# Create Screen
screen = pygame.display.set_mode(config.GAME_WINDOW_SIZE) # (Width, Height)
RUNNING = True # Game running...

# Title and Icon
pygame.display.set_caption(f"{config.PROGRAM_NAME} | {config.BUILD_VERSION} | By {config.AUTHOR}") # Game Title

icon = pygame.image.load(config.ICON) # Icon
pygame.display.set_icon(icon) # Set Icon

# Background
background = pygame.image.load(config.BACKGROUND) # Load Background Image

# Background Music
mixer.music.load(config.BACKGROUND_MUSIC) # Load Background Music File
mixer.music.set_volume(0.05) # Set Volume
mixer.music.play(-1) # Play Background Music (WITH LOOP)

# Player
playerImg = pygame.image.load(config.PLAYER_IMG) # Set Player Image
playerX = 370 # Player X Position
playerY = 480 # Player Y Position

playerX_change = 0 # Player X Position Change

def player(x, y): # Update Player Position
    screen.blit(playerImg, (x, y)) # Draw Player (Image, Position(x, y))

# Bullet
bulletImg = pygame.image.load(config.BULLET_IMG) # Set Bullet Image
bulletX = 0 # Bullet X Position
bulletY = 480 # Bullet Y Position

"""
Ready - You can't see the bullet on the screen.
Fire - The bullet is currently moving.
"""
bullet_state = "ready"

bulletX_change = 0 # Bullet X Position Change
bulletY_change = 10 # Bullet Y Position Change

# SCORE
score_value = 0 # Score Value

font = pygame.font.Font(config.BEBAS_REGULAR_FONT, 50) # Text Font (font, size)
textX = 400 # Text X Position
textY = 10 # Text Y Position

# GAME OVER TEXT
over_font = pygame.font.Font(config.BEBAS_REGULAR_FONT, 64) # Game Over Font (font, size)

def game_over_text(): # Game Over
    over_text = over_font.render("GAME OVER", True, (255, 255, 255)) # Render Text (Text, Display(True/False), Color(RGB))
    screen.blit(over_text, (200, 250)) # Draw Score (score, X, Y)

def show_score(x, y): # Show Score
    score = font.render(str(score_value), True, (255, 255, 255)) # Render Text (Text, Display(True/False), Color(RGB))
    screen.blit(score, (textX, textY)) # Draw Score (score, X, Y)

def fire_bullet(x, y): # Fire Bullet
    global bullet_state # Global Bullet State
    
    bullet_state = "fire" # Change Bullet State
    screen.blit(bulletImg, (x + 16, y + 10)) # Draw Bullet

def isCollision(enemyX, enemyY, bulletX, bulletY): # Check Colission between Bullet and Enemy
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))) # Find Linear Distance between 2 'objects'
    if distance < 27: # If distance is less that 27px...
        return True # Collision is TRUE
    else:
        return False # Collision is FALSE

# Enemies
enemyImg = [] # Set Enemy Image (LIST)
enemyX = [] # Enemy X Position (LIST)
enemyY = [] # Enemy Y Position (LIST)
enemyX_change = [] # Enemy X Position Change (LIST)
enemyY_change = [] # Enemy Y Position Change (LIST)
enemyRow = [] # Enemy Row Position (LIST)

for _ in range(config.NUMBER_OF_ENEMIES): # For each enemy...
    enemyImg.append(pygame.image.load(config.ENEMY_IMG)) # Add Enemy Image
    enemyX.append(random.randint(0, 735)) # Add Enemy X Position (RANDOM)
    enemyY.append(random.randint(50, 150)) # Add Enemy Y Position (RANDOM)

    enemyX_change.append(2) # Add Enemy X Position Change
    enemyY_change.append(40) # Add Enemy Y Position Change
    
    enemyRow.append(0) # Add Enemy Row Position

def enemy(x, y, enemy): # Update Player Position
    screen.blit(enemyImg[enemy], (x, y)) # Draw Player (Image, Position(x, y))


# GAME LOOP
while RUNNING:
    # RGB - (RED, GREEN, BLUE)
    # screen.fill((0, 0, 0)) # Screen Colour
    screen.blit(background, (0, 0)) # Set Background Image

    for event in pygame.event.get(): # For each event...
        if event.type == pygame.QUIT: # Quit Button
            RUNNING = False # Stop Game
        
        if event.type == pygame.KEYDOWN: # If keystroke pressed...
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Left Arrow
                playerX_change = -5 # Move Left (-5)

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Right Arrow
                playerX_change = 5 # Move Right (+5)
            
            if event.key == pygame.K_SPACE: # Space Bar
                if bullet_state == "ready": # If Bullet is "ready"...
                    bullet_sound = mixer.Sound(config.LASER_EFFECT) # Laser Effect
                    mixer.Sound.set_volume(bullet_sound, 0.2) # Set Volume
                    mixer.Sound.play(bullet_sound) # Play Effect (NO LOOP)

                    bulletX = playerX # Set Starting X Position of Player X Position  v
                    fire_bullet(bulletX, bulletY) # Fire Bullet

        if event.type == pygame.KEYUP: # If keystroke released...
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d: # If keystroke RIGHT or LEFT...
                playerX_change = 0 # Stop Movement Left/Right

    
    # ENEMY MOVEMENT AND BOUNDARIES AND COLLISSION AND UPDATE ENEMIES
    for enemyVal in range(config.NUMBER_OF_ENEMIES): # For each enemy...
        if enemyY[enemyVal] > 440: # If Y Position (>440)
            for enemyVal2 in range(config.NUMBER_OF_ENEMIES): # For each enemy...
                enemyY[enemyVal2] = 2000 # Move enemy out of screen
            game_over_text() # Game Over Function
            break # Exit Loop

        enemyX[enemyVal] += enemyX_change[enemyVal] # Update Enemy X Position

        if enemyX[enemyVal] <= 0: # Left Boundary (x=0)
            enemyX_change[enemyVal] = 3 + (0.15 * enemyRow[enemyVal]) # Set Boundary (x=0)
            enemyRow[enemyVal] += 1 # Add Enemy Row Position (+1)
            enemyY[enemyVal] += enemyY_change[enemyVal] # Move Enemy Down 

        elif enemyX[enemyVal] >= 736: # Right Boundary (x=800-64)
            enemyX_change[enemyVal] = -3 + (-0.15 * enemyRow[enemyVal]) # Set Boundary (x=736)
            enemyRow[enemyVal] += 1 # Add Enemy Row Position (+1)
            enemyY[enemyVal] += enemyY_change[enemyVal] # Move Enemy Down 

        # COLLISION
        collision = isCollision(enemyX[enemyVal], 
                                enemyY[enemyVal], 
                                bulletX, 
                                bulletY) # Check Collission
    
        if collision: # If TRUE...
            explosion_effect = mixer.Sound(config.EXPLOSION_EFFECT) # Explosion Effect
            # mixer.Sound.set_volume(explosion_effect, 0.5) # Set Volume
            mixer.Sound.play(explosion_effect) # Play Effect (NO LOOP)

            bulletY = 480 # Reset Bullet Y Position
            bullet_state = "ready" # Reset Bullet State

            score_value += 1 # Add Bullet Score (+1)

            enemyX[enemyVal] = random.randint(0, 735) # NEW Enemy X Position (RANDOM)
            enemyY[enemyVal] = random.randint(50, 150) # NEW Enemy Y Position (RANDOM)

        enemy(enemyX[enemyVal], enemyY[enemyVal], enemyVal) # Draw Enemy

    # PLAYER MOVEMENT AND BOUNDARIES
    playerX += playerX_change # Update Player X Position

    if playerX <= 0: # Left Boundary (x=0)
        playerX = 0 # Set Boundary (x=0)
    elif playerX >= 736: # Right Boundary (x=800-64)
        playerX = 736 # Set Boundary (x=736)

    # BULLET MOVEMENT
    if bulletY <= 0: # If Y below or equal to 0...
        bulletY = 480 # Reset Bullet Y Position
        bullet_state = "ready" # Reset Bullet State

    if bullet_state == "fire": # If state is "fire"...
        fire_bullet(bulletX, bulletY) # Fire Bullet
        bulletY -= bulletY_change # Move Bullet Up

    # FINAL UPDATES
    player(playerX, playerY) # Draw Player
    show_score(textX, textY) # Show Score

    pygame.display.update() # Update Screen