from src.services.random_maze_gen import Maze
from src.game_entities.player import Player
from src.utils.screen import Screen
from src.game_entities.enemy import Enemy
import pygame

def init():
    global maze
    global player
    global key_dict
    global entity_stack
    global screen
    global font
    global level
    global timer

    maze = Maze(45)
    player = Player()
    screen = Screen(resolution=2)
    entity_stack = [player, Enemy(5.5, 5.5, 'Hello World?')]
    key_dict = {'A':False, 'D':False, 'W':False, 'S':False, 'Q':False}
    font = pygame.font.Font("fonts/font.ttf", 32)
    timer = 60
    level = 1