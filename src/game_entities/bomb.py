import src.globals as gb
from src.utils.resources import *

class Bomb:
    def __init__(self, x:float, y:float, fuse_time:int = 120) -> None:
        self.x = x
        self.y = y
        self.fuse_time = fuse_time
    
    def hit(self):
        #Se a bomba for atingida por outra, ela explode instantaneamente
        if self.fuse_time > 0: self.fuse_time = 0

    def update(self):
        #Decresce o fuse_time a cada game_tick. Quando chega no zero, explode. E depois de 35 game_ticks ela é removida
        if self.fuse_time == 0:
            self.explodir(int(self.x), int(self.y))
        if self.fuse_time <= -35:
            gb.entity_stack.remove(self)
        self.fuse_time -= 1
            
    def explodir(self, x, y):
        #Destroi todas as paredes adjacentes ao quadrante em que a bomba foi plantada
        for i in range(x-1 if x > 1 else x, (x+2) if x+2 < gb.maze.length -1 else x+1):
            for j in range(y-1 if y > 1 else y, y+2 if y+2 < gb.maze.length-1 else y+1):
                if gb.maze.maze[i][j] == '#': gb.maze.maze[i][j] = '.'
        
        #Atinge todas as entidades em volta da bomba
        for entity in gb.entity_stack:
            if abs(entity.x - self.x) < 2 and abs(entity.y - self.y) < 2 and entity != self:
                entity.hit()
                
    def draw(self, screen):
        #Enquanto o fuse_time é positivo, a animacao alterna entre a normal e a bomb_tick (versão esbranquiçada)
        if self.fuse_time > 0:
            screen.surface.blit(assets['bomb'] if (self.fuse_time//20) % 2 == 0 else assets['bomb_tick'], 
                                    ((((self.x - gb.player.x) * 16 - 8) * screen.resolution + screen.width/2), 
                                    (((self.y - gb.player.y) * 16 - 8) * screen.resolution + screen.width/2)))
        #Depois de chegar no tick 0, ela ainda utiliza os ticks negativos para gerar a animacao da explosão
        if self.fuse_time <= 0:
            screen.surface.blit(assets['explosion'][abs(self.fuse_time)], 
                                    ((((self.x - gb.player.x) * 16 - 25) * screen.resolution + screen.width/2), 
                                    (((self.y - gb.player.y) * 16 - 25) * screen.resolution + screen.width/2)))