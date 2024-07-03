from pygame import draw, Rect
import src.globals as gb

white = (255, 255, 255)  

def draw_maze():
    gb.screen.surface.fill(white)  
    int_x = int(gb.player.x)
    int_y = int(gb.player.y)
    for x in range((int_x - 15) if int_x > 15 else 0, (int_x + 15) if int_x + 15 < gb.maze.length else gb.maze.length):
        for y in range((int_y - 15) if int_y > 15 else 0, (int_y + 15) if int_y + 15 < gb.maze.length else gb.maze.length):
            if gb.maze.maze[x][y] == '#':
                draw.rect(gb.screen.surface, (0, 125, 255), 
                            Rect(((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                16 * gb.screen.resolution, 
                                16 * gb.screen.resolution))      
