from random import shuffle, randint
import src.globals as gb
from src.game_entities.heart import Heart
from src.game_entities.clock import Clock
from src.game_entities.coin import Coin
from src.game_entities.stable_bomb import StableBomb
from src.game_entities.enemy import Enemy
from src.game_entities.ally import Ally

from datetime import date
from src.utils.constants import *

class Maze:
    def __init__(self, level:int, size: int = 10):
        if size > 30: size = 30
        if size < 5: size = 5
        if level > 5: level = 5
        if level < 1: level = 1
        self.level = level
        self.length = level * 16 + 1
        self.maze = [['#' for _ in range(self.length)] for _ in range(self.length)]

        content = None
        with open(f"storage/mazes/maze_{level}") as f:
            content = f.read().splitlines()
            f.close()
        if content[0] < str(date.today()): 
            self.make_path(self.maze, 1, 1, self.length)
            self.place_itens()
            self.maze[1][1], self.maze[self.length - 2][self.length - 2] = 'E', 'S'
            with open(f"storage/mazes/maze_{level}", 'w') as w:
                w.write(str(date.today()) + '\n' + '\n'.join([''.join(line) for line in self.maze]))
                w.close()
        else:
            self.maze = [[c for c in line] for line in content[1:]]
            
    def make_path(self, maze, x, y, l):
        maze[y][x] = '.'
        ord = [0,1,2,3]
        shuffle(ord)
        for dir in ord:
            match dir:
                case 0:
                    if y + 2 < l and maze[y+2][x] == '#':
                        maze[y+1][x] = '.'
                        self.make_path(maze, x, y+2, l)
                case 1:
                    if x + 2 < l and maze[y][x+2] == '#':
                        maze[y][x+1] = '.'
                        self.make_path(maze, x+2, y, l)
                case 2:
                    if y - 2 > 0 and maze[y-2][x] == '#':
                        maze[y-1][x] = '.'
                        self.make_path(maze, x, y-2, l)
                case 3:
                    if x - 2 > 0 and maze[y][x-2] == '#':
                        maze[y][x-1] = '.'
                        self.make_path(maze, x-2, y, l)
    
    def place_itens(self):
        statues_count = 3
        item_list = ["H", "T", "C", "C", "B", "A"] + ['M'] * 2 * gb.difficulty + ['.'] * 30 * gb.difficulty
        for i in range(1, self.length, 2):
            for j in range(1, self.length, 2):
                if self.maze[i][j] == '.':
                    random_item = item_list[randint(0, len(item_list)-1)]
                    if random_item == 'A':
                        statues_count -= 1
                        if statues_count < 0: random_item = '.'
                    self.maze[i][j] = random_item


    def set_maze_entities(self): 
        statues_count = 3
        for i in range(1, self.length-1):
            for j in range(1, self.length-1):
                match self.maze[i][j]:
                    case "H": 
                        gb.entity_stack.append(Heart(i, j))
                        self.maze[i][j] = '.'
                    case "T": 
                        gb.entity_stack.append(Clock(i, j))
                        self.maze[i][j] = '.'
                    case "C": 
                        gb.entity_stack.append(Coin(i, j))
                        self.maze[i][j] = '.'
                    case "B": 
                        gb.entity_stack.append(StableBomb(i, j))
                        self.maze[i][j] = '.'
                    case "M": 
                        gb.entity_stack.append(Enemy(i, j, randint(1, 6)))
                        self.maze[i][j] = '.'
                    case "A": 
                        statues_count -= 1
                        if statues_count >= 0:
                            gb.entity_stack.append(Ally(i, j, randint(1, 6)))
                        self.maze[i][j] = '.'
    def __str__(self) -> str:
        return '\n'.join([''.join(line) for line in self.maze])