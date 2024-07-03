from pygame import draw, Rect
from src.utils.screen import Screen
white = (255, 255, 255)  

class RenderMaze:
    def __init__(self, maze:list) -> None:
        self.maze = maze
        self.length = len(maze)

    def draw(self, screen: Screen, pos_x: int, pos_y: int):
        screen.surface.fill(white)  
        for x in range(self.length):
            for y in range(self.length):
                if self.maze[x][y] == '#':
                    draw.rect(screen.surface, (0, 125, 255), 
                              Rect(((x * 16 - pos_x) * screen.resolution + screen.width/2), 
                                   ((y * 16 - pos_y) * screen.resolution + screen.width/2), 
                                   16 * screen.resolution, 
                                   16 * screen.resolution))      
