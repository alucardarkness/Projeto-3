from src.game_entities.bomb import Bomb
from pygame import time
from math import sqrt
import src.globals as gb
from src.utils.resources import assets

class Player:
    def __init__(self, x:float = 1.5, y:float = 1.5, speed:float = 0.05, hp:int = 4, points:int = 0, time:int = 60, name:str = "Anomimous") -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.item = "bomb"
        self.hp = hp
        self.points = points
        self.time = time
        self.last_death = (int(self.x), int(self.y))
        self.name = name
        self.total_points = 0

    def respawn(self, x:float = 1.5, y:float = 1.5, speed:float = 0.05, hp:int = 4, points:int = 0, time:int = 60):
        #Reinicia todos 
        self.x = x
        self.y = y
        self.speed = speed
        self.item = "bomb"
        self.hp = hp
        self.points = points
        self.time = time
        self.vector2 = [0, 0] 
        self.last_death = (int(self.x), int(self.y))

    def update(self):
        #Verifica se a tecla Q foi apertada e verifica se o jogador chegou no final do labirinto com a quantidade minima de pontos. 
        #Caso o level seja o 5, ao invés de ir para a proxima fase, ele encerra o jogo.
        if gb.key_dict['Q']: self.use_item()
        if gb.maze.maze[int(self.x)][int(self.y)] == 'S' and self.points >= gb.level * 10:
            self.total_points += self.points
            if gb.level < 5:
                gb.event = 'phase_complete'
            else:
                gb.event = 'game_over'
        if self.hp > 5: self.hp = 5
        self.move()
        
    def use_item(self):
        #Se tiver uma bomba, adiciona na pilha de entidades uma bomba ativa nas cordenadas do player
        if self.item == "bomb": 
            gb.entity_stack.append(Bomb(self.x, self.y))
            self.item = None
            
    def hit(self):
        #Quando o player é atingido, seu hp diminui por 1, sua posicao reseta para o inicio e caso sua vida chegue a zero, dispara o evento de gameover
        self.hp -= 1
        self.last_death = (int(self.x), int(self.y))
        self.x = 1.5
        self.y = 1.5
        if self.hp <= 0:
            gb.event = 'gameover'
        
    def move(self):
        #Movimenta para 8 direcoes possiveis, combinando as teclas para andar na diagonal e cancelando teclas opostas
        self.vector2 = [0, 0]
        if gb.key_dict['D']: self.vector2[0] += 1
        if gb.key_dict['A']: self.vector2[0] -= 1
        if gb.key_dict['W']: self.vector2[1] -= 1
        if gb.key_dict['S']: self.vector2[1] += 1
            
        #Ao invés de verificar quando houver a colisão, ele verifica se o movimento na direção desejada irá entrar em um quadrante de parede.
        #Caso seja o caso, ele não realiza o movimento. Para que o movimento na diagonal reflita a distancia percorrida similar ao caminhar reto
        #Foi multiplicado a velodicade em linha reta por raiz de 2, mantendo assim a mesma velocidade no plano para todas as dimensoes.
        match self.vector2:
            case [1,0]: 
                if gb.maze.maze[int(self.x+0.2 + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed * sqrt(2) 
            case [-1,0]: 
                if gb.maze.maze[int(self.x-0.2 - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed * sqrt(2) 
            case [0,1]: 
                if gb.maze.maze[int(self.x)][int(self.y+0.2 + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed * sqrt(2) 
            case [0,-1]: 
                if gb.maze.maze[int(self.x)][int(self.y-0.2 - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed * sqrt(2) 
            case [1,1]: 
                if gb.maze.maze[int(self.x+0.2 + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed 
                if gb.maze.maze[int(self.x)][int(self.y+0.2 + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed
            case [1,-1]: 
                if gb.maze.maze[int(self.x+0.2 + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed
                if gb.maze.maze[int(self.x)][int(self.y-0.2 - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed
            case [-1,1]: 
                if gb.maze.maze[int(self.x-0.2 - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed
                if gb.maze.maze[int(self.x)][int(self.y+0.2 + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed
            case [-1,-1]: 
                if gb.maze.maze[int(self.x-0.2 - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed
                if gb.maze.maze[int(self.x)][int(self.y-0.2 - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed
            
    def draw(self, screen):
        #Escolhe o sprite de acordo com a direção na qual ele está andando e o frame da animação de acordo com o game_tick no momento e a velocidade do player
        current_sprite = (int(self.speed * time.get_ticks()) % 20) // 5
        match self.vector2:
            case [0, 0]: screen.surface.blit(assets['player_front'][0], (screen.width/2 - 4 * screen.resolution, screen.height/2 - 8 * screen.resolution))
            case [0, 1]: screen.surface.blit(assets['player_front'][current_sprite], (screen.width/2 - 4 * screen.resolution, screen.height/2 - 8 * screen.resolution))
            case [0, -1] | [1, -1] | [-1, -1]: screen.surface.blit(assets['player_back'][current_sprite], (screen.width/2 - 4 * screen.resolution, screen.height/2 - 8 * screen.resolution))
            case [1, 0] | [1, 1]: screen.surface.blit(assets['player_right'][current_sprite], (screen.width/2 - 4 * screen.resolution, screen.height/2 - 8 * screen.resolution))
            case [-1, 0] | [-1, 1]: screen.surface.blit(assets['player_left'][current_sprite], (screen.width/2 - 4 * screen.resolution, screen.height/2 - 8 * screen.resolution))