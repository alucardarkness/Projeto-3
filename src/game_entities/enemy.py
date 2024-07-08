import src.globals as gb
from src.utils.resources import assets
from src.services.maze_path_tracker import PathTracker
from src.utils.constants import *
from src.services.trivia import Trivia
from random import randint
from pygame import time

class Enemy():
    def __init__(self, x:float, y:float, speed:float=0.02) -> None:
        self.x = x
        self.y = y
        self.question = randint(1, 6)
        self.default_speed = speed
        self.speed = speed
        self.path = PathTracker(int(self.x), int(self.y)).path #Atribui um caminho a ser percorrido pelo Professor
        self.next_x = self.x
        self.next_y = self.y
        self.vector2 = [0, 0]

    def hit(self):
        gb.entity_stack.remove(self)

    def update(self):
        #Verifica se a linha entre ele e o jogador não possui paredes
        def is_path_free(x, y, player_x, player_y):
            for i in range(min(x, player_x), max(x, player_x)+1):
                for j in range(min(y, player_y), max(y, player_y)+1):
                    if gb.maze.maze[i][j] == '#':
                        return False
            return True
        
        #Se ele percorreu todos os passos do trajeto, ele gera um novo trajeto aleatorio
        if len(self.path) == 0:
            self.path = PathTracker(int(self.x), int(self.y)).path
            
        #Se ele chegou no ponto do caminho, ele pega da lista de caminhos o proximo ponto.
        if self.next_x == round(self.x, 1) and self.next_y == round(self.y, 1):
            x, y = self.path.pop(0)
            self.next_x = x+0.5
            self.next_y = y+0.5
            
        #Se move em direcao ao proximo ponto do caminho
        self.vector2 = [0, 0]
        if self.next_x != round(self.x, 1): self.vector2[0] = 1 if self.next_x > self.x else -1
        if self.next_y != round(self.y, 1): self.vector2[1] = 1 if self.next_y > self.y else -1
        self.x += self.vector2[0] * self.speed
        self.y += self.vector2[1] * self.speed
        
        #Quando chega perto do player, dispara a Trivia
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.on_trivia = True
            gb.trivia = Trivia(self)

        #Quando ele está em uma linha direta com o player, sem paredes, e olhando para a direcao do player. E o player não está na entrada do labirinto,
        #ele define como proximo ponto a posicao atual do player e multiplica a velocidade por 4.
        if (((int(self.x) == int(gb.player.x) and self.y - gb.player.y < 10 and self.y - gb.player.y > 0 and self.vector2 == [0, -1]) or
            (int(self.x) == int(gb.player.x) and gb.player.y - self.y < 10 and gb.player.y - self.y > 0 and self.vector2 == [0, 1]) or
            (int(self.y) == int(gb.player.y) and self.x - gb.player.x < 10 and self.x - gb.player.x > 0 and self.vector2 == [-1, 0]) or
            (int(self.y) == int(gb.player.y) and gb.player.x - self.x < 10 and gb.player.x - self.x > 0 and self.vector2 == [1, 0]))
            and is_path_free(int(self.x), int(self.y), int(gb.player.x), int(gb.player.y))
            and gb.maze.maze[int(gb.player.x)][int(gb.player.y)] != 'E'):
            self.speed = self.default_speed * 4
            self.path = [(int(gb.player.x), int(gb.player.y))]
        else:
            self.speed = self.default_speed
            
    def draw(self, screen):
        #Escolhe o sprite de acordo com a direção na qual ele está andando e o frame da animação de acordo com o game_tick no momento e a velocidade atual do inimigo
        current_sprite = (int(self.speed * time.get_ticks()) % 20) // 5
        match self.vector2:
            case [0, 0]: screen.surface.blit(assets['enemy_front'][0], 
                                ((((self.x - gb.player.x) * 16 - 4) * screen.resolution + screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * screen.resolution + screen.width/2)))
            case [0, 1]: screen.surface.blit(assets['enemy_front'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * screen.resolution + screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * screen.resolution + screen.width/2)))
            case [0, -1] | [1, -1] | [-1, -1]: screen.surface.blit(assets['enemy_back'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * screen.resolution + screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * screen.resolution + screen.width/2)))
            case [1, 0] | [1, 1]: screen.surface.blit(assets['enemy_right'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * screen.resolution + screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * screen.resolution + screen.width/2)))
            case [-1, 0] | [-1, 1]: screen.surface.blit(assets['enemy_left'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * screen.resolution + screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * screen.resolution + screen.width/2)))