#Arquivo de variáveis globais. Podem ser acessadas de qualquer lugar do código, e controlam grande parte do jogo
from src.services.maze import Maze
from src.services.trivia import Trivia
from src.game_entities.player import Player
from src.utils.constants import *
import csv
import os

def init():
    global maze, player, key_dict, entity_stack, screen, level, is_paused, state, event, scoreboard, on_trivia, trivia, cron, difficulty    
    
    level = 0
    cron = 0
    difficulty = 1
    maze = None
    is_paused = False
    on_trivia = False
    trivia = None
    entity_stack = []
    event = None
    state = "hub"
    key_dict = {'A':False, 'D':False, 'W':False, 'S':False, 'Q':False}
    player = Player(name=os.getlogin())
    with open(SCORE_FILE) as file: scoreboard = list(csv.reader(file, delimiter=','))
