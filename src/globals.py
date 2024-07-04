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
    global asset

    maze = Maze(45)
    player = Player()
    screen = Screen(resolution=5)
    entity_stack = [player]
    maze.get_maze_entities()
    key_dict = {'A':False, 'D':False, 'W':False, 'S':False, 'Q':False}
    font = pygame.font.Font("fonts/font.ttf", 32)
    level = 1
    asset = {
        "wall": pygame.transform.scale_by(pygame.image.load("assets/textures/wall.png"), screen.resolution),
        "floor": pygame.transform.scale_by(pygame.image.load("assets/textures/path.png"), screen.resolution),
        "spawn": pygame.transform.scale_by(pygame.image.load("assets/textures/spawn.png"), screen.resolution),
        "exit": pygame.transform.scale_by(pygame.image.load("assets/textures/exit.png"), screen.resolution),
        "heart": pygame.transform.scale_by(pygame.image.load("assets/textures/heart.png"), screen.resolution),
        "clock": pygame.transform.scale_by(pygame.image.load("assets/textures/clock.png"), screen.resolution),
        "coin": pygame.transform.scale_by(pygame.image.load("assets/textures/coin.png"), screen.resolution),
        "bomb": pygame.transform.scale_by(pygame.image.load("assets/textures/bomb.png"), screen.resolution),
        "enemy": pygame.transform.scale_by(pygame.image.load("assets/textures/enemy.png"), screen.resolution),
        "player": pygame.transform.scale_by(pygame.image.load("assets/textures/player.png"), screen.resolution),
        
    }