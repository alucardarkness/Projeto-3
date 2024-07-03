from src.services.random_maze_gen import Maze
from src.game_entities.player import Player
from src.utils.screen import Screen

def init():
    global maze
    global player
    global key_dict
    global entity_stack
    global screen
    
    maze = Maze(45)
    player = Player()
    screen = Screen(resolution=2)
    entity_stack = [player]
    key_dict = {'A':False, 'D':False, 'W':False, 'S':False, 'Q':False}
