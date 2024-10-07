import pygame
import sys
import random
import math
import time

pygame.init()

# Define the number of characters
NUM_SQUARES = 8
NUM_CIRCLES = 8
NUM_SQUARES_HAT = 1
NUM_CIRCLES_HAT = 1
NUM_ANGRY_CIRCLES = 1
NUM_SCARED_C = 0
NUM_SCARED_S = 0
NUM_HATGUY = 0
NUM_MILDANGRY_C =0
NUM_MILDANGRY_S =0
NUM_REDANGRY_C =0
NUM_REDANGRY_S =0
NUM_REDANGRY_BAT=0
NUM_REDANGRY_GUN=0
NUM_DEAD=0




SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

MENU = 0
PLAYING = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

play_button_image = pygame.image.load("images/Begin_button.png")
play_button_image = pygame.transform.scale(play_button_image, (200, 100))
play_button_rect = play_button_image.get_rect()
play_button_rect.center = (SCREEN_WIDTH // 2 -150, SCREEN_HEIGHT - 330)

# Load and scale the quit button image
quit_button_image = pygame.image.load("images/Quit_button.png")  # Ensure you have a 'Quit_button.png' image file
quit_button_image = pygame.transform.scale(quit_button_image, (230, 120))  # Scale it to the desired size
quit_button_rect = quit_button_image.get_rect()
quit_button_rect.center = (SCREEN_WIDTH // 2 + 140, SCREEN_HEIGHT - 320)  # Position it below the play button


tv_image = pygame.image.load("images/tv.png")

HOVER_SCALE_FACTOR = 1.06

# Load character images
CHAR_SCALE = 2  # Adjust this value to change the character size
ANGRY_CIRCLE_SCALE = 2.5
HTM_SCALE = 2
SCARED_CIRCLE_SCALE = 3
MILDANGRY_CIRCLE_SCALE = 3
MILDANGRY_SQUARE_SCALE = 3
DEAD_SCALE=2
GUN_SCALE=3
square_image = pygame.transform.scale(pygame.image.load("images/square.png"), (45 * CHAR_SCALE, 75 * CHAR_SCALE))
circle_image = pygame.transform.scale(pygame.image.load("images/circle.png"), (45 * CHAR_SCALE, 75 * CHAR_SCALE))
circleHat_image = pygame.transform.scale(pygame.image.load("images/circleHat.png"), (45 * CHAR_SCALE, 75 * CHAR_SCALE))
squareHat_image = pygame.transform.scale(pygame.image.load("images/squareHat.png"), (45 * CHAR_SCALE, 75 * CHAR_SCALE))
hatguy_image = pygame.transform.scale(pygame.image.load("images/hatman.png"), (45 * HTM_SCALE, 75 * HTM_SCALE))

dead_image=pygame.transform.scale(pygame.image.load("images/dead.png"), (75 * DEAD_SCALE, 90 * DEAD_SCALE))

redangrybatimages=[
    pygame.transform.scale(pygame.image.load("images/redangrybat1.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat1.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat1.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat1.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat1.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat1.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
 pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat2.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat3.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat3.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/redangrybat3.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat3.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat3.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat3.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat3.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat4.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/redangrybat4.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat4.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat4.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redangrybat4.png"), (45 * SCARED_CIRCLE_SCALE, 60 * SCARED_CIRCLE_SCALE)),
]
redangrygunimages=[
    pygame.transform.scale(pygame.image.load("images/redAngrySquareGun1.png"), (70* GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun1.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun1.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun1.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun1.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun1.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
 pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
    pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun2.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun3.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun3.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
    pygame.transform.scale(pygame.image.load("images/redAngrySquareGun3.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun3.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun3.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun3.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun3.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun4.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
    pygame.transform.scale(pygame.image.load("images/redAngrySquareGun4.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun4.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun4.png"), (70 * GUN_SCALE, 70 * GUN_SCALE)),
   pygame.transform.scale(pygame.image.load("images/redAngrySquareGun4.png"), (70 * GUN_SCALE, 70 * SCARED_CIRCLE_SCALE)),
]
RedAngrycircleimages = [
   pygame.transform.scale(pygame.image.load("images/body_red1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
 pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/body_red3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_red3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   
]

RedAngrysquareimages = [
   pygame.transform.scale(pygame.image.load("images/body_redsquare1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
 pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/body_redsquare3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/body_redsquare3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   
]

MildAngrycircleimages = [
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
 pygame.transform.scale(pygame.image.load("images/mild_angry_circle3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/mild_angry_circle4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/mild_angry_circle5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_circle5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   
]

MildAngrysquareimages = [
    pygame.transform.scale(pygame.image.load("images/mild_angry_square1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square1.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square2.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
 pygame.transform.scale(pygame.image.load("images/mild_angry_square3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square3.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/mild_angry_square4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square4.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/mild_angry_square5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/mild_angry_square5.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
]

circleScared_images = [
   pygame.transform.scale(pygame.image.load("images/circleScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
 pygame.transform.scale(pygame.image.load("images/circleScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/circleScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/circleScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/circleScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),

]

squareScared_image = [
   pygame.transform.scale(pygame.image.load("images/squareScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared1.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared2.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared3.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared4.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
   pygame.transform.scale(pygame.image.load("images/squareScared5.png"), (35 * SCARED_CIRCLE_SCALE, 50 * SCARED_CIRCLE_SCALE)),
]

angry_circle_images = [
   pygame.transform.scale(pygame.image.load("images/01.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/01.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/01.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/02.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/02.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/02.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/10.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),    
    pygame.transform.scale(pygame.image.load("images/10.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/10.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/11.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),    
    pygame.transform.scale(pygame.image.load("images/11.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/11.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/12.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/12.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/12.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/20.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/20.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/20.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/21.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/21.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/21.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/22.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/22.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/22.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/31.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/31.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/31.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/32.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/32.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/32.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/40.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/40.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/40.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/41.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/41.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/41.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/42.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/42.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/42.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/50.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/50.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/50.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/51.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/51.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/51.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/52.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/52.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/52.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/60.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/60.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/60.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/61.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/61.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/61.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/62.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/62.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    pygame.transform.scale(pygame.image.load("images/62.png"), (45 * ANGRY_CIRCLE_SCALE, 60 * ANGRY_CIRCLE_SCALE)),
    
]


def is_in_image(movable_rect, char_rect):
    intersection_rect = movable_rect.clip(char_rect)
    return intersection_rect.width > 0 and intersection_rect.height > 0


def analyze_captured_image(captured_image, square_characters, circle_characters, angry_circle_characters, squareHat_characters, circleHat_characters,Mild_angry_circle_characters,Mild_angry_square_characters,squareScared_characters ,circleScared_characters,Red_angry_circle_characters,Red_angry_square_characters,redangrybat_characters,redangrygun_characters,dead_characters ,tv_rect):
    capture_sound=pygame.mixer.Sound('Audio/capture_sound.wav')
    
    has_Red_angry_circle = any(is_in_image(captured_image, RedAngrycircle_rect) for _, RedAngrycircle_rect, _, _, _ in Red_angry_circle_characters)
    has_Red_angry_square = any(is_in_image(captured_image, RedAngrysquare_rect) for _, RedAngrysquare_rect, _, _, _ in Red_angry_square_characters)
    hasredangrybat=any(is_in_image(captured_image, redangrybat_rect) for _, redangrybat_rect, _, _, _ in redangrybat_characters)
    hasredangrygun=any(is_in_image(captured_image, redangrygun_rect) for _, redangrygun_rect, _, _, _ in redangrygun_characters)
    # Check if any character with a hat is in the captured image
    has_dead=any(is_in_image(captured_image, dead_rect) for _, dead_rect, _, _ in dead_characters)
   
    has_hat = any(is_in_image(captured_image, hat_rect) for _, hat_rect, _, _ in squareHat_characters) or any(is_in_image(captured_image, hat_rect) for _, hat_rect, _, _ in circleHat_characters)
    if has_dead:
        return "## Hatred Everywhere"
    if hasredangrybat and hasredangrygun:
        capture_sound.play()
        return "## War begins"
    has_circle = any(is_in_image(captured_image, circle_rect) for _, circle_rect, _, _ in circle_characters)
    # if has_Red_angry_circle and has_Red_angry_square:

    
    only_angry_circle = all(is_in_image(captured_image, angry_circle_rect) for _, angry_circle_rect, _, _, _ in angry_circle_characters)
    
    
    has_angry_circle = any(is_in_image(captured_image, angry_circle_rect) for _, angry_circle_rect, _, _, _ in angry_circle_characters)
 
    has_square = any(is_in_image(captured_image, square_rect) for _, square_rect, _, _ in square_characters)

    

    has_scared_circle = any(is_in_image(captured_image, circleScared_rect) for _, circleScared_rect, _, _, _ in circleScared_characters)
    # has_circle = any(is_in_image(captured_image, circle_rect) for _, circle_rect, _, _ in circle_characters)
    
    
    has_mild_angry_circle = any(is_in_image(captured_image, MildAngrycircle_rect) for _, MildAngrycircle_rect, _, _, _ in Mild_angry_circle_characters)
    has_mild_angry_square = any(is_in_image(captured_image, MildAngrysquare_rect) for _, MildAngrysquare_rect, _, _, _ in Mild_angry_square_characters)
  

   
    
    has_scared_square = any(is_in_image(captured_image, squareScared_rect) for _, squareScared_rect, _, _, _ in squareScared_characters)

    if has_Red_angry_circle and has_Red_angry_square:
        capture_sound.play()

        return "## Anger is Widespread"

    if has_mild_angry_square and has_mild_angry_circle:
        x=random.random()
        if x>=0.5:
            capture_sound.play()
            return "## Squares hate Circles"
        else: 
            capture_sound.play()
            return "## Circles hate Squares"
        
    if has_scared_square and has_circle:
        capture_sound.play()
        return "## Circles snub squares"    
        
    if not has_hat:
        if has_mild_angry_circle and has_square:
            capture_sound.play()
            return "## Angry Circle scares Square"

    if has_scared_circle and has_square:
        capture_sound.play()
        return "  ## Squares snub circle"
    
    total_hats = NUM_SQUARES_HAT + NUM_CIRCLES_HAT
    if not has_hat:
        if has_angry_circle and has_circle:
            capture_sound.play()
            return "## Angry Square scares Circles"
    if total_hats > 11:
        if has_hat:
            capture_sound.play()
            return "  ## Hats aren't cool anymore"
    elif has_hat:
        capture_sound.play()
        return "  ## Hats are cool"
    
    if only_angry_circle and not has_circle:
        capture_sound.play()
        return "## Looks like someone is angry"
    
    # Check for TV screen in the captured image
    if captured_image.colliderect(tv_rect):
        capture_sound.play()
        return "  ## Screen on Screen"
    
    has_square = any(is_in_image(captured_image, square_rect) for _, square_rect, _, _ in square_characters)
    if has_square and not has_circle:
        capture_sound.play()
        return "  ## Just normal squares"
    elif has_circle and not has_square:
        capture_sound.play()
        return "  ## Just normal circles"
    # elif has_square and has_circle:
    #     return "  ## Just normal peeps"

    return "  ## Nothing interesting"



def load_special_character_images(scale):
    special_character_1 = pygame.transform.scale(pygame.image.load("images/specialcharachter1.png"), (80* scale, 100* scale))
    special_character_2 = pygame.transform.scale(pygame.image.load("images/specialcharachter2.png"), (70* scale, 100 * scale))
    special_character_3 = pygame.transform.scale(pygame.image.load("images/specialcharachter3.png"), (120 * scale, 60 * scale))
    return special_character_1, special_character_2, special_character_3

# Function to handle the special character sequence
def special_character_sequence(screen, screen_width, screen_height, special_character_scale=2):
    special_character_1, special_character_2, special_character_3 = load_special_character_images(special_character_scale)

    # Initialize character rects and positions
    special_char_1_rect = special_character_1.get_rect()
    special_char_1_rect.midleft = (0, screen_height * 3 // 4)  # Adjust to 3/4 height from the top
    special_char_2_rect = special_character_2.get_rect()
    special_char_2_rect.midright = (screen_width, screen_height * 3 // 4)  # Adjust to 3/4 height from the top
    special_char_3_rect = special_character_3.get_rect()
    special_char_3_rect.center = (screen_width // 2, screen_height * 3 // 4)  # Adjust to 3/4 height from the top

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
                

        # Move special_char_1 to the right and special_char_2 to the left
        special_char_1_rect.move_ip(2.3, 0)
        special_char_2_rect.move_ip(-2.3, 0)

        # Check if special_char_1 has reached the center of the screen
        if special_char_1_rect.right >= screen_width / 2-10:
            done = True
            capture_sound=pygame.mixer.Sound('Audio/gunshot.wav')
            capture_sound.play()
            screen.blit(special_character_3, special_char_3_rect)  # Immediately draw special_char_3
        # Draw the special characters (only if not done)
        if not done:
            screen.blit(special_character_1, special_char_1_rect)
            screen.blit(special_character_2, special_char_2_rect)
        

        pygame.display.update()  # Update the display instead of flipping
        clock.tick(60)

    # After the sequence is done, leave special_char_3 on the screen for 7 seconds
    start_time = time.time()
    while time.time() - start_time < 7:
        screen.blit(special_character_3, special_char_3_rect)
        pygame.display.update()


def draw_play_button():
    if play_button_rect.collidepoint(pygame.mouse.get_pos()):
        button_width = int(play_button_image.get_width() * HOVER_SCALE_FACTOR)
        button_height = int(play_button_image.get_height() * HOVER_SCALE_FACTOR)
        button_image_scaled = pygame.transform.scale(play_button_image, (button_width, button_height))
        button_rect_scaled = button_image_scaled.get_rect(center=play_button_rect.center)
        screen.blit(button_image_scaled, button_rect_scaled)
    else:
        screen.blit(play_button_image, play_button_rect)

def draw_quit_button():
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        button_width = int(quit_button_image.get_width() * HOVER_SCALE_FACTOR)
        button_height = int(quit_button_image.get_height() * HOVER_SCALE_FACTOR)
        button_image_scaled = pygame.transform.scale(quit_button_image, (button_width, button_height))
        button_rect_scaled = button_image_scaled.get_rect(center=quit_button_rect.center)
        screen.blit(button_image_scaled, button_rect_scaled)
    else:
        screen.blit(quit_button_image, quit_button_rect)

def draw_title():
    font = pygame.font.Font(None, 48)
    text = font.render("Game Capture Spread", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(text, text_rect)


def display_intro_text():
    intro_text = "Whoever controls the media, Controls the mind."
    font = pygame.font.Font(None, 36)
    total_width, _ = font.size(intro_text)
    space_between = 5
    x = 600
    y = SCREEN_HEIGHT // 2 - font.get_height() // 2

    for char in intro_text:
        char_surface = font.render(char, True, GRAY)
        char_rect = char_surface.get_rect(topleft=(x, y))
        screen.blit(char_surface, char_rect)
        pygame.display.update()
        pygame.time.wait(100)
        x += char_rect.width + space_between 
    
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade_surface.fill(BLACK)
    
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(60)

def gameplay_screen():
    
    global NUM_CIRCLES
    global NUM_CIRCLES_HAT
    global NUM_ANGRY_CIRCLES
    global NUM_HATGUY
    global NUM_SQUARES
    global NUM_SQUARES_HAT
    global NUM_SCARED_C
    global NUM_SCARED_S
    global NUM_MILDANGRY_S
    global NUM_MILDANGRY_C
    global NUM_REDANGRY_C
    global NUM_REDANGRY_S
    global NUM_REDANGRY_BAT
    global NUM_REDANGRY_GUN
    global NUM_DEAD
    
    
    square_characters = []
    circle_characters = []
    circleHat_characters = []
    circleScared_characters = []
    squareHat_characters = []
    squareScared_characters = []
    angry_circle_characters = []
    Mild_angry_circle_characters = []
    Mild_angry_square_characters = []
    Red_angry_circle_characters=[]
    Red_angry_square_characters=[]
    redangrybat_characters=[]
    redangrygun_characters=[]
    dead_characters=[]

    # Initialize Scared circle characters

    for _ in range(NUM_DEAD):
        dead_char = dead_image.copy()
        dead_rect = dead_char.get_rect()
        dead_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = 0
        
        dead_characters.append((dead_char, dead_rect, move_angle, move_speed))

    for _ in range(NUM_SCARED_C):
        circleScared_char = circleScared_images[0].copy()
        circleScared_rect = circleScared_char.get_rect()
        circleScared_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index = 0
        circleScared_characters.append((circleScared_char, circleScared_rect, move_angle, move_speed,frame_index))

    for _ in range(NUM_SCARED_S):
        squareScared_char = squareScared_image[0].copy()
        squareScared_rect = squareScared_char.get_rect()
        squareScared_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index = 0
        squareScared_characters.append((squareScared_char, squareScared_rect, move_angle, move_speed,frame_index))    
    
    for _ in range(NUM_MILDANGRY_C):
        MildAngrycircle_char = MildAngrycircleimages[0].copy()
        MildAngrycircle_rect = MildAngrycircle_char.get_rect()
        MildAngrycircle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index=0
        Mild_angry_circle_characters.append((MildAngrycircle_char, MildAngrycircle_rect, move_angle, move_speed,frame_index))

    for _ in range(NUM_MILDANGRY_S):
        MildAngrysquare_char = MildAngrysquareimages[0].copy()
        MildAngrysquare_rect = MildAngrysquare_char.get_rect()
        MildAngrysquare_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index=0
        Mild_angry_square_characters.append((MildAngrysquare_char, MildAngrysquare_rect, move_angle, move_speed,frame_index))

    for _ in range(NUM_REDANGRY_C):
        RedAngrycircle_char = RedAngrycircleimages[0].copy()
        RedAngrycircle_rect = RedAngrycircle_char.get_rect()
        RedAngrycircle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index=0
        Red_angry_circle_characters.append((RedAngrycircle_char, RedAngrycircle_rect, move_angle, move_speed,frame_index)) 

    for _ in range(NUM_REDANGRY_S):
        RedAngrysquare_char = RedAngrysquareimages[0].copy()
        RedAngrysquare_rect = RedAngrysquare_char.get_rect()
        RedAngrysquare_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index=0
        Red_angry_square_characters.append((RedAngrysquare_char, RedAngrysquare_rect, move_angle, move_speed,frame_index))
    for _ in range(NUM_REDANGRY_BAT):
        redangrybat_char = redangrybatimages[0].copy()
        redangrybat_rect = redangrybat_char.get_rect()
        redangrybat_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index=0
        redangrybat_characters.append((redangrybat_char, redangrybat_rect, move_angle, move_speed,frame_index))
    # Initialize square characters
    for _ in range(NUM_REDANGRY_GUN):
        redangrygun_char = redangrygunimages[0].copy()
        redangrygun_rect = redangrygun_char.get_rect()
        redangrygun_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index=0
        redangrygun_characters.append((redangrygun_char, redangrygun_rect, move_angle, move_speed,frame_index))
    # Initialize square characters
    for _ in range(NUM_SQUARES):
        square_char = square_image.copy()
        square_rect = square_char.get_rect()
        square_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        square_characters.append((square_char, square_rect, move_angle, move_speed))

    # Initialize circle characters
    for _ in range(NUM_CIRCLES):
        circle_char = circle_image.copy()
        circle_rect = circle_char.get_rect()
        circle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        circle_characters.append((circle_char, circle_rect, move_angle, move_speed))

    # Initialize squareHat characters
    for _ in range(NUM_SQUARES_HAT):
        squareHat_char = squareHat_image.copy()
        squareHat_rect = squareHat_char.get_rect()
        squareHat_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        squareHat_characters.append((squareHat_char, squareHat_rect, move_angle, move_speed))
        
    # Initialize circleHat characters
    for _ in range(NUM_CIRCLES_HAT):
        circleHat_char = circleHat_image.copy()
        circleHat_rect = circleHat_char.get_rect()
        circleHat_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        circleHat_characters.append((circleHat_char, circleHat_rect, move_angle, move_speed))
        
    # Initialize angry circle characters
    for _ in range(NUM_ANGRY_CIRCLES):
        angry_circle_char = angry_circle_images[0].copy()
        angry_circle_rect = angry_circle_char.get_rect()
        angry_circle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
        move_angle = random.uniform(0, 2 * math.pi)
        move_speed = random.randint(3, 5)
        frame_index = 0
        angry_circle_characters.append((angry_circle_char, angry_circle_rect, move_angle, move_speed, frame_index))


    movable_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 95, 300, 190)
    captured_image = None
    last_capture_time = 0
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()
    last_direction_change = pygame.time.get_ticks()

    headline_font = pygame.font.Font(None, 24)
    headline_text = ""
   # Define the TV screen rectangle
    tv_rect = tv_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Capture the area within the movable rectangle
                current_time = pygame.time.get_ticks()
                if current_time - last_capture_time >= 4000:
                    captured_image = screen.subsurface(movable_rect).copy()
                    last_capture_time = current_time

                    # Analyze the captured image and get the headline text
                    headline_text = analyze_captured_image(movable_rect, square_characters, circle_characters, angry_circle_characters, squareHat_characters, circleHat_characters,Mild_angry_circle_characters,Mild_angry_square_characters,squareScared_characters,circleScared_characters,Red_angry_circle_characters,Red_angry_square_characters,redangrybat_characters,redangrygun_characters,dead_characters, tv_rect)
                    if headline_text == "  ## Hats are cool":
                        capture_sound=pygame.mixer.Sound('Audio/hatsAreCool.wav')
                        capture_sound.play()
                        NUM_CIRCLES_HAT  = NUM_CIRCLES_HAT + 1
                        NUM_SQUARES_HAT = NUM_SQUARES_HAT +1
                        NUM_CIRCLES -=1
                        NUM_SQUARES -=1
                        
                        for _ in range(1):
                            if circle_characters:
                                circle_characters.pop(0)
                                
                            if square_characters:
                                square_characters.pop(0)
                                
                        circleHat_char = circleHat_image.copy()
                        circleHat_rect = circleHat_char.get_rect()
                        circleHat_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                        move_angle = random.uniform(0, 2 * math.pi)
                        move_speed = random.randint(3, 5)
                        circleHat_characters.append((circleHat_char, circleHat_rect, move_angle, move_speed))
                          
                        squareHat_char = squareHat_image.copy()
                        squareHat_rect = squareHat_char.get_rect()
                        squareHat_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                        move_angle = random.uniform(0, 2 * math.pi)
                        move_speed = random.randint(3, 5)
                        squareHat_characters.append((squareHat_char, squareHat_rect, move_angle, move_speed))
                          
                    elif headline_text == "  ## Hats aren't cool anymore":
                        capture_sound=pygame.mixer.Sound('Audio/breakingnews.wav')
                        capture_sound.play()
                        NUM_CIRCLES += NUM_CIRCLES_HAT/2 + NUM_SQUARES_HAT/2
                        NUM_SQUARES += NUM_CIRCLES_HAT/2 + NUM_SQUARES_HAT/2
                        
                        # Remove circleHat characters
                        for _ in range (NUM_CIRCLES_HAT):
                            if circleHat_characters:
                                circleHat_characters.pop(0)
                        for _ in range (NUM_SQUARES_HAT):
                            if square_characters:
                                squareHat_characters.pop(0)
                                
                        # Add circle characters
                        for _ in range(NUM_CIRCLES_HAT):
                            circle_char = circle_image.copy()
                            circle_rect = circle_char.get_rect()
                            circle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            circle_characters.append((circle_char, circle_rect, move_angle, move_speed))
                        
                        for _ in range(NUM_SQUARES_HAT):
                            square_char = square_image.copy()
                            square_rect = square_char.get_rect()
                            square_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            square_characters.append((square_char, square_rect, move_angle, move_speed))
                        
                        NUM_CIRCLES_HAT = 0
                        NUM_SQUARES_HAT = 0
                    
                   

                    elif headline_text == "## Angry Square scares Circles" :
                        capture_sound=pygame.mixer.Sound('Audio/squareSnubCircle.wav')
                        capture_sound.play()
                        NUM_CIRCLES -=2
                    
                        NUM_SCARED_C +=2
                        
                        for _ in range(2):
                            if circle_characters:
                                circle_characters.pop(0)
                        
                        # Add Mild Angry and scared circle characters
                        for _ in range(2):
                            circleScared_char = circleScared_images[0].copy()
                            circleScared_rect = circleScared_char.get_rect()
                            circleScared_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            circleScared_characters.append((circleScared_char, circleScared_rect, move_angle, move_speed,frame_index))
                        
                        # for _ in range(1):
                        # MildAngrycircle_char = MildAngrycircleimages[0].copy()
                        # MildAngrycircle_rect = MildAngrycircle_char.get_rect()
                        # MildAngrycircle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                        # move_angle = random.uniform(0, 2 * math.pi)
                        # move_speed = random.randint(3, 5)
                        # Mild_angry_circle_characters.append((MildAngrycircle_char, MildAngrycircle_rect, move_angle, move_speed,frame_index))


                    elif headline_text == "  ## Squares snub circle" :
                        capture_sound=pygame.mixer.Sound('Audio/squareSnubCircle.wav')
                        capture_sound.play()
                        NUM_CIRCLES -=2
                        NUM_MILDANGRY_C +=2
                        
                        
                        for _ in range(2):
                            if circle_characters:
                                circle_characters.pop(0)
                        
                        # Add Mild Angry and scared circle characters
                        # for _ in range(2):
                        #     circleScared_char = circleScared_images[0].copy()
                        #     circleScared_rect = circleScared_char.get_rect()
                        #     circleScared_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                        #     move_angle = random.uniform(0, 2 * math.pi)
                        #     move_speed = random.randint(3, 5)
                        #     circleScared_characters.append((circleScared_char, circleScared_rect, move_angle, move_speed,frame_index))
                        
                        # for _ in range(1):
                        for _ in range(2):
                            MildAngrycircle_char = MildAngrycircleimages[0].copy()
                            MildAngrycircle_rect = MildAngrycircle_char.get_rect()
                            MildAngrycircle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            frame_index = 0
                            Mild_angry_circle_characters.append((MildAngrycircle_char, MildAngrycircle_rect, move_angle, move_speed,frame_index))

                            
                    elif headline_text =="## Angry Circle scares Square":
                        capture_sound=pygame.mixer.Sound('Audio/circleSnubSquare.wav')
                        capture_sound.play()
                        NUM_SQUARES -=2
                        # NUM_MILDANGRY_C +=1
                        NUM_SCARED_S +=2
                        
                        for _ in range(2):
                            if square_characters:
                                square_characters.pop(0)
                        
                        # Add Mild Angry and scared circle characters
                        for _ in range(2):
                            squareScared_char = squareScared_image[0].copy()
                            squareScared_rect = squareScared_char.get_rect()
                            squareScared_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            squareScared_characters.append((squareScared_char, squareScared_rect, move_angle, move_speed,frame_index))
                        
                    elif headline_text == "## Circles snub squares" :
                        capture_sound=pygame.mixer.Sound('Audio/circleSnubSquare.wav')
                        capture_sound.play()
                        NUM_SQUARES -=2
                        # NUM_MILDANGRY_C +=1
                        NUM_MILDANGRY_S +=2
                        
                        for _ in range(2):
                            if square_characters:
                                square_characters.pop(0)
                        
                        # Add Mild Angry and scared circle characters
                        
                        for _ in range(2):
                            MildAngrysquare_char = MildAngrysquareimages[0].copy()
                            MildAngrysquare_rect = MildAngrysquare_char.get_rect()
                            MildAngrysquare_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            frame_index = 0
                            Mild_angry_square_characters.append((MildAngrysquare_char, MildAngrysquare_rect, move_angle, move_speed,frame_index))

                    elif headline_text == "## Squares hate Circles" :
                        # NUM_MILDANGRY_C +=1
                        capture_sound=pygame.mixer.Sound('Audio/squaresHateCircle.wav')
                        capture_sound.play()
                        if (len(Red_angry_circle_characters)  + len(Red_angry_square_characters)) < 2:
                            NUM_REDANGRY_C +=2
                            NUM_SQUARES -=1
                            
                            for _ in range(1):
                                if square_characters:
                                    square_characters.pop(0)
                            
                            # Add Mild Angry and scared circle characters
                            
                            for _ in range(2):
                                RedAngrycircle_char = RedAngrycircleimages[0].copy()
                                RedAngrycircle_rect = RedAngrycircle_char.get_rect()
                                RedAngrycircle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                                move_angle = random.uniform(0, 2 * math.pi)
                                move_speed = random.randint(3, 5)
                                frame_index = 0
                                Red_angry_circle_characters.append((RedAngrycircle_char, RedAngrycircle_rect, move_angle, move_speed,frame_index))

                        else:
                            print(12) 
                            for _ in range(len(circle_characters)):
                                if circle_characters:
                                    circle_characters.pop(0)  
                            for _ in range(len(square_characters)):
                                if square_characters:
                                    square_characters.pop(0)  
                            for _ in range(len(circleHat_characters)):
                                if circleHat_characters:
                                    circleHat_characters.pop(0)  
                            for _ in range(len(squareHat_characters)):
                                if squareHat_characters:
                                    squareHat_characters.pop(0)  
                            for _ in range(len(circleScared_characters)):
                                if circleScared_characters:
                                    circleScared_characters.pop(0)  
                            for _ in range(len(squareScared_characters)):
                                if squareScared_characters:
                                    squareScared_characters.pop(0)  

                            for _ in range(len(angry_circle_characters)):
                                if angry_circle_characters:
                                    angry_circle_characters.pop(0) 
                            for _ in range(len(Mild_angry_circle_characters)):
                                if Mild_angry_circle_characters:
                                    Mild_angry_circle_characters.pop(0) 
                            for _ in range(len(Mild_angry_square_characters)):
                                if Mild_angry_square_characters:
                                    Mild_angry_square_characters.pop(0) 

                            for _ in range(12):
                                RedAngrycircle_char = RedAngrycircleimages[0].copy()
                                RedAngrycircle_rect = RedAngrycircle_char.get_rect()
                                RedAngrycircle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                                move_angle = random.uniform(0, 2 * math.pi)
                                move_speed = random.randint(3, 5)
                                frame_index = 0
                                Red_angry_circle_characters.append((RedAngrycircle_char, RedAngrycircle_rect, move_angle, move_speed,frame_index))
                            for _ in range(12):
                                RedAngrysquare_char = RedAngrysquareimages[0].copy()
                                RedAngrysquare_rect = RedAngrysquare_char.get_rect()
                                RedAngrysquare_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                                move_angle = random.uniform(0, 2 * math.pi)
                                move_speed = random.randint(3, 5)
                                frame_index = 0
                                Red_angry_square_characters.append((RedAngrysquare_char, RedAngrysquare_rect, move_angle, move_speed,frame_index))


                    


                    

                    elif headline_text == "## Circles hate Squares" :
                        capture_sound=pygame.mixer.Sound('Audio/CirclesHateSquares.wav')
                        capture_sound.play()
                        if (len(Red_angry_circle_characters)  + len(Red_angry_square_characters)) < 2:
                            NUM_CIRCLES -=1
                            # NUM_MILDANGRY_C +=1
                            NUM_REDANGRY_S +=2
                            
                            for _ in range(1):
                                if circle_characters:
                                    circle_characters.pop(0)
                            
                            # Add Mild Angry and scared circle characters
                            
                            for _ in range(2):
                                RedAngrysquare_char = RedAngrysquareimages[0].copy()
                                RedAngrysquare_rect = RedAngrysquare_char.get_rect()
                                RedAngrysquare_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                                move_angle = random.uniform(0, 2 * math.pi)
                                move_speed = random.randint(3, 5)
                                frame_index = 0
                                Red_angry_square_characters.append((RedAngrysquare_char, RedAngrysquare_rect, move_angle, move_speed,frame_index))
                        else: 
                            print(12)
                            for _ in range(len(circle_characters)):
                                if circle_characters:
                                    circle_characters.pop(0)  
                            for _ in range(len(square_characters)):
                                if square_characters:
                                    square_characters.pop(0)  
                            for _ in range(len(circleHat_characters)):
                                if circleHat_characters:
                                    circleHat_characters.pop(0)  
                            for _ in range(len(squareHat_characters)):
                                if squareHat_characters:
                                    squareHat_characters.pop(0)  
                            for _ in range(len(circleScared_characters)):
                                if circleScared_characters:
                                    circleScared_characters.pop(0)  
                            for _ in range(len(squareScared_characters)):
                                if squareScared_characters:
                                    squareScared_characters.pop(0)  

                            for _ in range(len(angry_circle_characters)):
                                if angry_circle_characters:
                                    angry_circle_characters.pop(0) 
                            for _ in range(len(Mild_angry_circle_characters)):
                                if Mild_angry_circle_characters:
                                    Mild_angry_circle_characters.pop(0) 
                            for _ in range(len(Mild_angry_square_characters)):
                                if Mild_angry_square_characters:
                                    Mild_angry_square_characters.pop(0)  
                            
                            for _ in range(12):
                                RedAngrycircle_char = RedAngrycircleimages[0].copy()
                                RedAngrycircle_rect = RedAngrycircle_char.get_rect()
                                RedAngrycircle_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                                move_angle = random.uniform(0, 2 * math.pi)
                                move_speed = random.randint(3, 5)
                                frame_index = 0
                                Red_angry_circle_characters.append((RedAngrycircle_char, RedAngrycircle_rect, move_angle, move_speed,frame_index))
                            for _ in range(12):
                                RedAngrysquare_char = RedAngrysquareimages[0].copy()
                                RedAngrysquare_rect = RedAngrysquare_char.get_rect()
                                RedAngrysquare_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                                move_angle = random.uniform(0, 2 * math.pi)
                                move_speed = random.randint(3, 5)
                                frame_index = 0
                                Red_angry_square_characters.append((RedAngrysquare_char, RedAngrysquare_rect, move_angle, move_speed,frame_index))

                    elif headline_text=="## Anger is Widespread":
                        capture_sound=pygame.mixer.Sound('Audio/AngerisWidespread.wav')
                        capture_sound.play()
                        special_character_sequence(screen, 1920, 1080)
                        
                        for _ in range(2):
                            redangrybat_char = redangrybatimages[0].copy()
                            redangrybat_rect = redangrybat_char.get_rect()
                            redangrybat_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            frame_index = 0
                            redangrybat_characters.append((redangrybat_char, redangrybat_rect, move_angle, move_speed,frame_index))

                        for _ in range(2):
                            redangrygun_char = redangrygunimages[0].copy()
                            redangrygun_rect = redangrygun_char.get_rect()
                            redangrygun_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            frame_index = 0
                            redangrygun_characters.append((redangrygun_char, redangrygun_rect, move_angle, move_speed,frame_index))

                    elif headline_text== "## War begins":
                        capture_sound=pygame.mixer.Sound('Audio/WarBegins.wav')
                        capture_sound.play()
                        NUM_REDANGRY_BAT +=2
                        NUM_REDANGRY_GUN +=2
                        NUM_REDANGRY_S -=3
                        NUM_REDANGRY_C -=3
                        NUM_DEAD +=2
                        
                        for _ in range(3):
                            if Red_angry_circle_characters:
                                Red_angry_circle_characters.pop(0)
                            if Red_angry_square_characters:
                                Red_angry_square_characters.pop(0)
                        # Add Mild Angry and scared circle characters
                        
                        for _ in range(2):
                            redangrybat_char = redangrybatimages[0].copy()
                            redangrybat_rect = redangrybat_char.get_rect()
                            redangrybat_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            frame_index = 0
                            redangrybat_characters.append((redangrybat_char, redangrybat_rect, move_angle, move_speed,frame_index))

                        for _ in range(2):
                            redangrygun_char = redangrygunimages[0].copy()
                            redangrygun_rect = redangrygun_char.get_rect()
                            redangrygun_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = random.randint(3, 5)
                            frame_index = 0
                            redangrygun_characters.append((redangrygun_char, redangrygun_rect, move_angle, move_speed,frame_index))

                        for _ in range(2):
                            dead_char = dead_image.copy()
                            dead_rect = dead_char.get_rect()
                            dead_rect.center = (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100))
                            move_angle = random.uniform(0, 2 * math.pi)
                            move_speed = 0
                            
                            dead_characters.append((dead_char, dead_rect, move_angle, move_speed))

                        
                       

                    elif headline_text == "## Hatred Everywhere" :
                        print(111)
                        capture_sound=pygame.mixer.Sound('Audio/HatredEverywhere.wav')
                        capture_sound.play()

                        for alpha in range(255, -1, -5):  # Gradually decrease opacity
                            image=pygame.image.load("images/ClosingPage.png")

                            screen.fill((0,0,0))
                            screen.blit(image,(0,0))  # Fill screen with black
                            s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create surface the size of the screen
                            s.set_alpha(alpha)  # Set transparency level
                            screen.blit(s, (0,0))  # Apply the transparent overlay
                            pygame.display.update()  # Update the display
                            pygame.time.delay(50)  # Short delay between fades

                        # Typing text effect
                        messages = [
                            "Retributive justice, exemplified by the adage 'An eye for an eye,' ultimately leads to universal detriment,",
                            "                     as it incapacitates the collective sight of a society.",
                            "   The media serves a pivotal role in disseminating information, yet it necessitates critical consumption",
                            "     by the public due to the potential dissemination of unfounded claims which can be equally damaging." ,
                            " This reflects a broader scenario where there is a common perception that media outlets are significantly ",
                            "influenced by a major political party,  leading to reporting that is skewed to reflect the party's agenda.",
                            "In the context of a digital game, a movable rectangle representing the media highlights user control over",
                            "     media representation, contrasting with the perceived governmental control over media in India.",
                            "   The independence of the media, as a fundamental pillar of democracy, must be safeguarded to ensure",
                            "                 unbiased and equitable functioning within the democratic framework."
                        ]
                        font = pygame.font.Font(None, 36)  # Use a default font and size 36
                        text_y = SCREEN_HEIGHT // 2 -200  # Start y position for text
                        for message in messages:
                            text_x = 300  # Start x position for text
                            for letter in message:
                                text = font.render(letter, True, (255, 255, 255))  # Render the letter in white
                                screen.blit(text, (text_x, text_y))  # Draw the letter on the screen
                                pygame.display.update()  # Update the display to show the letter
                                pygame.time.delay(50)  # Delay to create a typing effect
                                text_x += text.get_width()  # Move x position for the next letter
                            text_y += 50  # Move y position for the next line

                        # End the game
                        pygame.quit()
                        sys.exit()

        current_time = pygame.time.get_ticks()
        if current_time - last_direction_change >= 800:
            for i, (square_char, square_rect, _, _) in enumerate(square_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                square_characters[i] = (square_char, square_rect, move_angle, move_speed)

            for i, (circle_char, circle_rect, _, _) in enumerate(circle_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                circle_characters[i] = (circle_char, circle_rect, move_angle, move_speed)
                
            for i, (circleHat_char, circleHat_rect, _, _) in enumerate(circleHat_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                circleHat_characters[i] = (circleHat_char, circleHat_rect, move_angle, move_speed)

            for i, (squareHat_char, squareHat_rect, _, _) in enumerate(squareHat_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                squareHat_characters[i] = (squareHat_char, squareHat_rect, move_angle, move_speed)
                
            for i, (angry_circle_char, angry_circle_rect, _, _, _) in enumerate(angry_circle_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                angry_circle_characters[i] = (angry_circle_char, angry_circle_rect, move_angle, move_speed, 0)

            for i, (circleScared_char, circleScared_rect, _, _, _) in enumerate(circleScared_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                circleScared_characters[i] = (circleScared_char, circleScared_rect, move_angle, move_speed, 0)

            for i, (squareScared_char, squareScared_rect, _, _, _) in enumerate(squareScared_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                squareScared_characters[i] = (squareScared_char, squareScared_rect, move_angle, move_speed, 0)

            for i, (MildAngrycircle_char, MildAngrycircle_rect, _, _, _) in enumerate(Mild_angry_circle_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                Mild_angry_circle_characters[i] = (MildAngrycircle_char, MildAngrycircle_rect, move_angle, move_speed, 0)    

            for i, (MildAngrysquare_char, MildAngrysquare_rect, _, _, _) in enumerate(Mild_angry_square_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                Mild_angry_square_characters[i] = (MildAngrysquare_char, MildAngrysquare_rect, move_angle, move_speed, 0) 

            for i, (RedAngrycircle_char, RedAngrycircle_rect, _, _, _) in enumerate(Red_angry_circle_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                Red_angry_circle_characters[i] = (RedAngrycircle_char, RedAngrycircle_rect, move_angle, move_speed, 0)    

            for i, (RedAngrysquare_char, RedAngrysquare_rect, _, _, _) in enumerate(Red_angry_square_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                Red_angry_square_characters[i] = (RedAngrysquare_char, RedAngrysquare_rect, move_angle, move_speed, 0) 
            for i, (redangrybat_char, redangrybat_rect, _, _, _) in enumerate(redangrybat_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                redangrybat_characters[i] = (redangrybat_char, redangrybat_rect, move_angle, move_speed, 0) 

            for i, (redangrygun_char, redangrygun_rect, _, _, _) in enumerate(redangrygun_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = random.randint(3, 7)
                redangrygun_characters[i] = (redangrygun_char, redangrygun_rect, move_angle, move_speed, 0) 

            for i, (dead_char, dead_rect, _, _) in enumerate(dead_characters):
                move_angle = random.uniform(0, 2 * math.pi)
                move_speed = 0
                dead_characters[i] = (dead_char, dead_rect, move_angle, move_speed) 

            last_direction_change = current_time

        movable_rect.center = pygame.mouse.get_pos()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        movable_rect.centerx = max(movable_rect.width // 2, min(mouse_x, SCREEN_WIDTH - movable_rect.width // 2))
        movable_rect.centery = max(movable_rect.height // 2, min(mouse_y, SCREEN_HEIGHT - movable_rect.height // 2))

        screen.fill(GRAY)
        
        # Draw square characters behind the TV image
        for square_char, square_rect, move_angle, move_speed in square_characters:
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            square_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if square_rect.left < -100:
                square_rect.right = SCREEN_WIDTH
            if square_rect.right > SCREEN_WIDTH+ 100:
                square_rect.left = 0
            if square_rect.top < -100:
                square_rect.bottom = SCREEN_HEIGHT
            if square_rect.bottom > SCREEN_HEIGHT+ 100:
                square_rect.top = 0

            screen.blit(square_char, square_rect)

        # Draw circle characters behind the TV image
        for circle_char, circle_rect, move_angle, move_speed in circle_characters:
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            circle_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if circle_rect.left < -100:
                circle_rect.right = SCREEN_WIDTH
            if circle_rect.right > SCREEN_WIDTH+ 100:
                circle_rect.left = 0
            if circle_rect.top < -100:
                circle_rect.bottom = SCREEN_HEIGHT
            if circle_rect.bottom > SCREEN_HEIGHT+ 100:
                circle_rect.top = 0

            screen.blit(circle_char, circle_rect)
            
        # Draw circleHat characters behind the TV image
        for circleHat_char, circleHat_rect, move_angle, move_speed in circleHat_characters:
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            circleHat_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if circleHat_rect.left < -100:
                circleHat_rect.right = SCREEN_WIDTH
            if circleHat_rect.right > SCREEN_WIDTH + 100:
                circleHat_rect.left = 0
            if circleHat_rect.top < -100:
                circleHat_rect.bottom = SCREEN_HEIGHT
            if circleHat_rect.bottom > SCREEN_HEIGHT+ 100:
                circleHat_rect.top = 0

            screen.blit(circleHat_char, circleHat_rect)
            
        # Draw squareHat characters behind the TV image
        for squareHat_char, squareHat_rect, move_angle, move_speed in squareHat_characters:
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            squareHat_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if squareHat_rect.left < -100:
                squareHat_rect.right = SCREEN_WIDTH 
            if squareHat_rect.right > SCREEN_WIDTH +100:
                squareHat_rect.left = 0
            if squareHat_rect.top < -100:
                squareHat_rect.bottom = SCREEN_HEIGHT
            if squareHat_rect.bottom > SCREEN_HEIGHT+100:
                squareHat_rect.top = 0

            screen.blit(squareHat_char, squareHat_rect)


        for dead_char, dead_rect, move_angle, move_speed in dead_characters:
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            dead_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if dead_rect.left < -100:
                dead_rect.right = SCREEN_WIDTH 
            if dead_rect.right > SCREEN_WIDTH +100:
                dead_rect.left = 0
            if dead_rect.top < -100:
                dead_rect.bottom = SCREEN_HEIGHT
            if dead_rect.bottom > SCREEN_HEIGHT+100:
                dead_rect.top = 0

            screen.blit(dead_char, dead_rect)
            
        for i, (angry_circle_char, angry_circle_rect, move_angle, move_speed, frame_index) in enumerate(angry_circle_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            angry_circle_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if angry_circle_rect.left < -100:
                angry_circle_rect.right = SCREEN_WIDTH
            if angry_circle_rect.right > SCREEN_WIDTH+100:
                angry_circle_rect.left = 0
            if angry_circle_rect.top < -100:
                angry_circle_rect.bottom = SCREEN_HEIGHT
            if angry_circle_rect.bottom > SCREEN_HEIGHT+100:
                angry_circle_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(angry_circle_images)
            angry_circle_char = angry_circle_images[frame_index]

            angry_circle_characters[i] = (angry_circle_char, angry_circle_rect, move_angle, move_speed, frame_index)

            screen.blit(angry_circle_char, angry_circle_rect)


        for i, (circleScared_char, circleScared_rect, move_angle, move_speed, frame_index) in enumerate(circleScared_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            circleScared_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if circleScared_rect.left < -100:
                circleScared_rect.right = SCREEN_WIDTH
            if circleScared_rect.right > SCREEN_WIDTH+100:
                circleScared_rect.left = 0
            if circleScared_rect.top < -100:
                circleScared_rect.bottom = SCREEN_HEIGHT
            if circleScared_rect.bottom > SCREEN_HEIGHT+100:
                circleScared_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(circleScared_images)
            circleScared_char = circleScared_images[frame_index]

            circleScared_characters[i] = (circleScared_char, circleScared_rect, move_angle, move_speed, frame_index)

            screen.blit(circleScared_char, circleScared_rect)  

        for i, (squareScared_char, squareScared_rect, move_angle, move_speed, frame_index) in enumerate(squareScared_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            squareScared_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if squareScared_rect.left < -100:
                squareScared_rect.right = SCREEN_WIDTH
            if squareScared_rect.right > SCREEN_WIDTH+100:
                squareScared_rect.left = 0
            if squareScared_rect.top < -100:
                squareScared_rect.bottom = SCREEN_HEIGHT
            if squareScared_rect.bottom > SCREEN_HEIGHT+100:
                squareScared_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(squareScared_image)
            squareScared_char = squareScared_image[frame_index]

            squareScared_characters[i] = (squareScared_char, squareScared_rect, move_angle, move_speed, frame_index)

            screen.blit(squareScared_char, squareScared_rect)


        for i, (MildAngrycircle_char, MildAngrycircle_rect, move_angle, move_speed, frame_index) in enumerate(Mild_angry_circle_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            MildAngrycircle_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if MildAngrycircle_rect.left < -100:
                MildAngrycircle_rect.right = SCREEN_WIDTH
            if MildAngrycircle_rect.right > SCREEN_WIDTH+100:
                MildAngrycircle_rect.left = 0
            if MildAngrycircle_rect.top < -100:
                MildAngrycircle_rect.bottom = SCREEN_HEIGHT
            if MildAngrycircle_rect.bottom > SCREEN_HEIGHT+100:
                MildAngrycircle_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(MildAngrycircleimages)
            MildAngrycircle_char = MildAngrycircleimages[frame_index]

            Mild_angry_circle_characters[i] = (MildAngrycircle_char, MildAngrycircle_rect, move_angle, move_speed, frame_index)

            screen.blit(MildAngrycircle_char, MildAngrycircle_rect) 

        for i, (MildAngrysquare_char, MildAngrysquare_rect, move_angle, move_speed, frame_index) in enumerate(Mild_angry_square_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            MildAngrysquare_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if MildAngrysquare_rect.left < -100:
                MildAngrysquare_rect.right = SCREEN_WIDTH
            if MildAngrysquare_rect.right > SCREEN_WIDTH+100:
                MildAngrysquare_rect.left = 0
            if MildAngrysquare_rect.top < -100:
                MildAngrysquare_rect.bottom = SCREEN_HEIGHT
            if MildAngrysquare_rect.bottom > SCREEN_HEIGHT+100:
                MildAngrysquare_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(MildAngrysquareimages)
            MildAngrysquare_char = MildAngrysquareimages[frame_index]

            Mild_angry_square_characters[i] = (MildAngrysquare_char, MildAngrysquare_rect, move_angle, move_speed, frame_index)

            screen.blit(MildAngrysquare_char, MildAngrysquare_rect)     

        # Draw the TV image at a fixed position
        for i, (RedAngrycircle_char, RedAngrycircle_rect, move_angle, move_speed, frame_index) in enumerate(Red_angry_circle_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            RedAngrycircle_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if RedAngrycircle_rect.left < -100:
                RedAngrycircle_rect.right = SCREEN_WIDTH
            if RedAngrycircle_rect.right > SCREEN_WIDTH+100:
                RedAngrycircle_rect.left = 0
            if RedAngrycircle_rect.top < -100:
                RedAngrycircle_rect.bottom = SCREEN_HEIGHT
            if RedAngrycircle_rect.bottom > SCREEN_HEIGHT+100:
                RedAngrycircle_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(RedAngrycircleimages)
            RedAngrycircle_char = RedAngrycircleimages[frame_index]

            Red_angry_circle_characters[i] = (RedAngrycircle_char, RedAngrycircle_rect, move_angle, move_speed, frame_index)

            screen.blit(RedAngrycircle_char, RedAngrycircle_rect) 

        for i, (RedAngrysquare_char, RedAngrysquare_rect, move_angle, move_speed, frame_index) in enumerate(Red_angry_square_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            RedAngrysquare_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if RedAngrysquare_rect.left < -100:
                RedAngrysquare_rect.right = SCREEN_WIDTH
            if RedAngrysquare_rect.right > SCREEN_WIDTH+100:
                RedAngrysquare_rect.left = 0
            if RedAngrysquare_rect.top < -100:
                RedAngrysquare_rect.bottom = SCREEN_HEIGHT
            if RedAngrysquare_rect.bottom > SCREEN_HEIGHT+100:
                RedAngrysquare_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(RedAngrysquareimages)
            RedAngrysquare_char = RedAngrysquareimages[frame_index]

            Red_angry_square_characters[i] = (RedAngrysquare_char, RedAngrysquare_rect, move_angle, move_speed, frame_index)

            screen.blit(RedAngrysquare_char, RedAngrysquare_rect) 

        for i, (redangrybat_char, redangrybat_rect, move_angle, move_speed, frame_index) in enumerate(redangrybat_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            redangrybat_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if redangrybat_rect.left < -100:
                redangrybat_rect.right = SCREEN_WIDTH
            if redangrybat_rect.right > SCREEN_WIDTH+100:
                redangrybat_rect.left = 0
            if redangrybat_rect.top < -100:
                redangrybat_rect.bottom = SCREEN_HEIGHT
            if redangrybat_rect.bottom > SCREEN_HEIGHT+100:
                redangrybat_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(redangrybatimages)
            redangrybat_char = redangrybatimages[frame_index]

            redangrybat_characters[i] = (redangrybat_char, redangrybat_rect, move_angle, move_speed, frame_index)

            screen.blit(redangrybat_char, redangrybat_rect) 

        for i, (redangrygun_char, redangrygun_rect, move_angle, move_speed, frame_index) in enumerate(redangrygun_characters):
            move_x = move_speed * math.cos(move_angle)
            move_y = move_speed * math.sin(move_angle)
            redangrygun_rect.move_ip(move_x, move_y)

            # Wrap around the screen edges
            if redangrygun_rect.left < -100:
                redangrygun_rect.right = SCREEN_WIDTH
            if redangrygun_rect.right > SCREEN_WIDTH+100:
                redangrygun_rect.left = 0
            if redangrygun_rect.top < -100:
                redangrygun_rect.bottom = SCREEN_HEIGHT
            if redangrygun_rect.bottom > SCREEN_HEIGHT+100:
                redangrygun_rect.top = 0

            # Update the animation frame
            frame_index = (frame_index + 1) % len(redangrygunimages)
            redangrygun_char = redangrygunimages[frame_index]

            redangrygun_characters[i] = (redangrygun_char, redangrygun_rect, move_angle, move_speed, frame_index)

            screen.blit(redangrygun_char, redangrygun_rect) 

         
            
        screen.blit(tv_image, tv_rect)

        # Draw the captured image in the center of the screen
        if captured_image:
            scaled_image = pygame.transform.scale(captured_image, (int(captured_image.get_width() * 0.8), int(captured_image.get_height() * 0.73)))  # Scale down the image by 20%
            screen.blit(scaled_image, (SCREEN_WIDTH // 2 - scaled_image.get_width() // 2, SCREEN_HEIGHT // 2 - scaled_image.get_height() // 2 -45))  # Draw the scaled image 50 pixels above the center

        pygame.draw.rect(screen, BLACK, movable_rect, width=2)
        
       # Render headline text in black color
        headline_surface = headline_font.render(headline_text, True, (0, 0, 0))  # Black color styling

# Get the rectangle for the headline text
        headline_rect = headline_surface.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 523))

# Create a rectangle surface to act as the red frame around the text
        headline_frame_rect = pygame.Rect(headline_rect.left - 5, headline_rect.top - 5, headline_rect.width + 10, headline_rect.height + 10)
        pygame.draw.rect(screen, (255, 0, 0), headline_frame_rect)  # Draw the red frame

# Blit the black text onto the screen
        screen.blit(headline_surface, headline_rect)


        
        pygame.display.update()
        clock.tick(60)


def main():
    game_state = MENU

    background_image = pygame.image.load("images/start_back.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == MENU:

                    if play_button_rect.collidepoint(event.pos):
                        capture_sound=pygame.mixer.Sound('Audio/click.wav')
                        typewriter_so = pygame.mixer.Sound('Audio/typewriter.wav')
                        capture_sound.play()
                        typewriter_so.play()
                        screen.fill(BLACK)
                        display_intro_text()
                        
                        game_state = PLAYING
                        gameplay_screen()  # Call the gameplay_screen function here
                    elif quit_button_rect.collidepoint(event.pos):
                        
                        pygame.quit()
                        sys.exit()

        screen.blit(background_image, (0, 0)) 

        if game_state == MENU:
            draw_play_button()
            draw_quit_button()
            screen.blit(quit_button_image, quit_button_rect)
        pygame.display.update()

      

if __name__ == "__main__":
    main()