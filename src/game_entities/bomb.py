from pygame import draw
import src.globals as gb

class Bomb:
    def __init__(self, x:float, y:float, fuse_time:int = 120) -> None:
        self.x = x
        self.y = y
        self.fuse_time = fuse_time
    
    def update(self):
        self.fuse_time -= 1
        if self.fuse_time == 0:
            self.explodir(int(self.x), int(self.y))
            
    def explodir(self, x, y):
        print('Explodiu', x, y)
        for i in range(x-1 if x > 1 else x, (x+2) if x+2 < gb.maze.length -1 else x+1):
            for j in range(y-1 if y > 1 else y, y+2 if y+2 < gb.maze.length-1 else y+1):
                gb.maze.maze[i][j] = '.'
        if abs(gb.player.x - self.x) < 2.5 and abs(gb.player.y - self.y) < 2.5:
            gb.player.hit()
    def draw(self):
        if self.fuse_time > 0:
            gb.screen.surface.blit(gb.asset['bomb'], 
                                ((((self.x - gb.player.x) * 16 - 8) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))