from pygame import draw
import src.globals as gb

class Bomb:
    def __init__(self, x:float, y:float, fuse_time:int = 120) -> None:
        self.x = x
        self.y = y
        self.fuse_time = fuse_time
    
    def hit(self):
        self.fuse_time = 0

    def update(self):
        self.fuse_time -= 1
        if self.fuse_time == 0:
            self.explodir(int(self.x), int(self.y))
        if self.fuse_time <= -35:
            gb.entity_stack.remove(self)
            
    def explodir(self, x, y):
        print('Explodiu', x, y)
        for i in range(x-1 if x > 1 else x, (x+2) if x+2 < gb.maze.length -1 else x+1):
            for j in range(y-1 if y > 1 else y, y+2 if y+2 < gb.maze.length-1 else y+1):
                if gb.maze.maze[i][j] == '#': gb.maze.maze[i][j] = '.'
        for entity in gb.entity_stack:
            if abs(entity.x - self.x) < 2.5 and abs(entity.y - self.y) < 2.5:
                entity.hit()
    def draw(self):
        if self.fuse_time > 0:
            if (self.fuse_time//20) % 2 == 0:
                gb.screen.surface.blit(gb.asset['bomb'], 
                                    ((((self.x - gb.player.x) * 16 - 8) * gb.screen.resolution + gb.screen.width/2), 
                                    (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))
                
            else:
                gb.screen.surface.blit(gb.asset['bomb_tick'], 
                                    ((((self.x - gb.player.x) * 16 - 8) * gb.screen.resolution + gb.screen.width/2), 
                                    (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))
        if self.fuse_time < 0:
            gb.screen.surface.blit(gb.asset['explosion'][abs(self.fuse_time)], 
                                    ((((self.x - gb.player.x) * 16 - 25) * gb.screen.resolution + gb.screen.width/2), 
                                    (((self.y - gb.player.y) * 16 - 25) * gb.screen.resolution + gb.screen.width/2)))