from random import shuffle, randint
import src.globals as gb
from src.utils.resources import assets
from src.game_entities.heart import Heart
from src.game_entities.clock import Clock
from src.game_entities.coin import Coin
from src.game_entities.stable_bomb import StableBomb
from src.game_entities.enemy import Enemy
from src.game_entities.ally import Ally
from datetime import date
from src.utils.constants import *
from src.utils.resources import *
import csv

class Maze:
    def __init__(self, level:int, size: int = 10):
        if size > 30: size = 30
        if size < 5: size = 5
        if level > 5: level = 5
        if level < 1: level = 1
        self.level = level
        self.length = level * 16 + 1
        self.maze = [['#' for _ in range(self.length)] for _ in range(self.length)] #Instancia a matriz maze apenas com #

        #Abre o arquivo do labirinto do level e salva ele em content
        content = None
        with open(f"storage/mazes/maze_{level}") as f:
            content = f.read().splitlines()
            f.close()
            
        #Se a data do labirinto não foi hoje, ele gera um novo labirinto e sobrescreve o antigo
        if content[0] < str(date.today()): 
            self.make_path(self.maze, 1, 1, self.length)
            self.place_itens()
            self.maze[1][1], self.maze[self.length - 2][self.length - 2] = 'E', 'S'
            with open(f"storage/mazes/maze_{level}", 'w') as w:
                w.write(str(date.today()) + '\n' + '\n'.join([''.join(line) for line in self.maze]))
                w.close()
        else:
            #Caso contrario, ele apenas carrega o arquivo sendo o labirinto
            self.maze = [[c for c in line] for line in content[1:]]
            
    def make_path(self, maze, x, y, l):
        #Funcao recursiva responsável por gerar o labirinto. 
        #"É como se fosse uma minhoca cavando tuneis aleatorios até preencher todo o espaço"
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
        #Sorteia os possiveis itens que terão em cada espaço do labirinto, podendo ser também um professor ou apenas caminho.
        #Adiciona um character no labirinto marcando um "spawn" desse item
        item_list = ["H", "T", "C", "C", "B"] + ['M'] * 2 * gb.difficulty + ['.'] * 30 * gb.difficulty
        for i in range(1, self.length, 2):
            for j in range(1, self.length, 2):
                if self.maze[i][j] == '.':
                    random_item = item_list[randint(0, len(item_list)-1)]
                    self.maze[i][j] = random_item


    def set_maze_items(self): 
        #Converte os "spawners" em items
        for i in range(1, self.length-1, 2):
            for j in range(1, self.length-1, 2):
                match self.maze[i][j]:
                    case "H": 
                        gb.entity_stack.append(Heart(i+0.5, j+0.5))
                        self.maze[i][j] = '.'
                    case "T": 
                        gb.entity_stack.append(Clock(i+0.5, j+0.5))
                        self.maze[i][j] = '.'
                    case "C": 
                        gb.entity_stack.append(Coin(i+0.5, j+0.5))
                        self.maze[i][j] = '.'
                    case "B": 
                        gb.entity_stack.append(StableBomb(i+0.5, j+0.5))
                        self.maze[i][j] = '.'

    def set_maze_enemies(self): 
        #Converte os "spawners" em inimigos
        for i in range(1, self.length-1, 2):
            for j in range(1, self.length-1, 2):
                if self.maze[i][j] == "M": 
                    gb.entity_stack.append(Enemy(i+0.5, j+0.5))
                    self.maze[i][j] = '.'

    def set_maze_allies(self): 
        allies_counter = 3
        with open(STATUES_FILE) as file: 
            alies_list = list(csv.reader(file, delimiter=','))
        #Converte os "spawners" em entidades
        for ally_id, player_name, x, y, level, trivia_id in alies_list:
            if int(level) == gb.level:
                x, y = int(x), int(y)
                if self.maze[x][y] == '.': 
                    gb.entity_stack.append(Ally(x+0.5, y+0.5, int(ally_id), int(trivia_id))) 
                    allies_counter -= 1
        #Se não foi adicionado ao mapa ao menos 3 aliados, ele completa randomicamente até atingir o minimo
        while allies_counter > 0:
            x, y = randint(1, self.length-2), randint(1, self.length-2)
            if self.maze[x][y] == '.':
                gb.entity_stack.append(Ally(x+0.5, y+0.5, -1, randint(1,6))) 
                allies_counter -= 1

    def draw(self, screen):
        screen.surface.fill(WHITE)  
        int_x = int(gb.player.x)
        int_y = int(gb.player.y)
        #Renderiza apenas os tiles proximos ao player
        for x in range((int_x - 15) if int_x > 15 else 0, (int_x + 15) if int_x + 15 < self.length else self.length):
            for y in range((int_y - 15) if int_y > 15 else 0, (int_y + 15) if int_y + 15 < self.length else self.length):
                asset = None
                #Escolhe o asset que será desenhado de acordo com a letra no labirinto
                match self.maze[x][y]:
                    case "#": 
                        if not (y+1 < self.length and self.maze[x][y+1] == '#'): 
                            asset = assets['wall_side'][((x+y)*(x-y))%7]
                    case ".": asset = assets['floor']
                    case "E": asset = assets['spawn']
                    case "S": asset = assets['exit']

                if asset: screen.surface.blit(asset, 
                            (((x - gb.player.x) * 16 * screen.resolution + screen.width/2), 
                            ((y - gb.player.y) * 16 * screen.resolution + screen.height/2)))

    def draw_pos(self, screen):
        int_x = int(gb.player.x)
        int_y = int(gb.player.y)
        #Renderiza apenas os tiles proximos ao player
        for x in range((int_x - 15) if int_x > 15 else 0, (int_x + 15) if int_x + 15 < self.length else self.length):
            for y in range((int_y - 15) if int_y > 15 else 0, (int_y + 15) if int_y + 15 < self.length else self.length):
                if self.maze[x][y] == '#':
                    screen.surface.blit((assets['wall_t'] if x+1 < self.length and self.maze[x+1][y] == '#' else assets['wall']) if y+1 < self.length and self.maze[x][y+1] == '#' else assets['wall_top'], 
                        (((x - gb.player.x) * 16 * screen.resolution + screen.width/2), 
                        ((y - gb.player.y) * 16 * screen.resolution + screen.height/2)))


    def __str__(self) -> str:
        return '\n'.join([''.join(line) for line in self.maze])