from src.services.random_maze_gen import Maze
from src.game_entities.player import Player
from src.utils.screen import Screen
from src.game_entities.enemy import Enemy
import pygame
from src.constants import *
import csv

def init():
    global maze
    global player
    global key_dict
    global entity_stack
    global screen
    global font
    global font16
    global level
    global asset
    global is_paused
    global state
    global event
    global scoreboard
    global on_trivia
    global trivia
    global cron
    global difficulty
    
    difficulty = 1
    level = 0
    cron = 0
    maze = None
    on_trivia = None
    trivia = None
    with open(SCORE_FILE) as file:
        scoreboard = list(csv.reader(file, delimiter=','))[1:]
    is_paused = False
    state = "hub"

    player = Player()
    screen = Screen(resolution=5)
    entity_stack = None
    key_dict = {'A':False, 'D':False, 'W':False, 'S':False, 'Q':False}
    font = pygame.font.Font("fonts/font.ttf", 32)
    font16 = pygame.font.Font("fonts/font.ttf", 16)
    event = None
    asset = {
        "wall": pygame.transform.scale_by(pygame.image.load("assets/textures/wall.png"), screen.resolution),
        "floor": pygame.transform.scale_by(pygame.image.load("assets/textures/path.png"), screen.resolution),
        "spawn": pygame.transform.scale_by(pygame.image.load("assets/textures/spawn.png"), screen.resolution),
        "exit": pygame.transform.scale_by(pygame.image.load("assets/textures/exit.png"), screen.resolution),
        "heart": pygame.transform.scale_by(pygame.image.load("assets/textures/heart.png"), screen.resolution),
        "clock": pygame.transform.scale_by(pygame.image.load("assets/textures/clock.png"), screen.resolution),
        "coin": pygame.transform.scale_by(pygame.image.load("assets/textures/coin.png"), screen.resolution),
        "bomb": pygame.transform.scale_by(pygame.image.load("assets/textures/bomb.png"), screen.resolution),
        "bomb_tick": pygame.transform.scale_by(pygame.image.load("assets/textures/bomb_tick.png"), screen.resolution),
        "enemy": pygame.transform.scale_by(pygame.image.load("assets/textures/teacher1.png"), screen.resolution),
        "player": pygame.transform.scale_by(pygame.image.load("assets/textures/player.png"), screen.resolution),
        "ally": pygame.transform.scale_by(pygame.image.load("assets/textures/ally2.png"), screen.resolution),

        "hit_points": pygame.transform.scale_by(pygame.image.load("assets/textures/heart.png"), 4),
        "book": pygame.transform.scale_by(pygame.image.load("assets/textures/book.png"), 3),
        "button": pygame.transform.scale_by(pygame.image.load("assets/textures/button.png"), 4),
        "button_hover": pygame.transform.scale_by(pygame.image.load("assets/textures/button_hover.png"), 4),
        "hub": pygame.image.load("assets/textures/hub.png"),
        "back_button": pygame.transform.scale_by(pygame.image.load("assets/textures/back_button.png"), 3),
        "back_button_hover": pygame.transform.scale_by(pygame.image.load("assets/textures/back_button_hover.png"), 3),
        "trivia_button": pygame.transform.scale_by(pygame.image.load("assets/textures/button.png"), 3)
    }
    