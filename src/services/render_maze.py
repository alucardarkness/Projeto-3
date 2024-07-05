import src.globals as gb
from src.utils.constants import *
from random import randint
def draw_maze():
    gb.screen.surface.fill(WHITE)  
    int_x = int(gb.player.x)
    int_y = int(gb.player.y)
    for x in range((int_x - 15) if int_x > 15 else 0, (int_x + 15) if int_x + 15 < gb.maze.length else gb.maze.length):
        for y in range((int_y - 15) if int_y > 15 else 0, (int_y + 15) if int_y + 15 < gb.maze.length else gb.maze.length):
            match gb.maze.maze[x][y]:
                case "#": 
                    if y+1 < gb.maze.length and gb.maze.maze[x][y+1] == '#':
                        gb.screen.surface.blit(gb.asset['wall'], 
                                            (((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                                ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2)))
                    else:
                        gb.screen.surface.blit(gb.asset['wall_side'], 
                                            (((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                                ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2)))    
                case ".": 
                    gb.screen.surface.blit(gb.asset['floor'], 
                                           (((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                            ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2)))
                case "E":
                    gb.screen.surface.blit(gb.asset['spawn'], 
                                           (((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                            ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2)))
                case "S":
                    gb.screen.surface.blit(gb.asset['exit'], 
                                           (((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                            ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2)))

def draw_maze_pos():
    int_x = int(gb.player.x)
    int_y = int(gb.player.y)
    for x in range((int_x - 15) if int_x > 15 else 0, (int_x + 15) if int_x + 15 < gb.maze.length else gb.maze.length):
        for y in range((int_y - 15) if int_y > 15 else 0, (int_y + 15) if int_y + 15 < gb.maze.length else gb.maze.length):
            if gb.maze.maze[x][y] == '#':
                if y+1 < gb.maze.length and gb.maze.maze[x][y+1] == '#':
                    gb.screen.surface.blit(gb.asset['wall'], 
                                        (((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                        ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2)))
                else:
                    gb.screen.surface.blit(gb.asset['wall_top'], 
                                        (((x - gb.player.x) * 16 * gb.screen.resolution + gb.screen.width/2), 
                                        ((y - gb.player.y) * 16 * gb.screen.resolution + gb.screen.width/2)))                        