from pygame import draw, Rect
import src.globals as gb

white = (255, 255, 255)  

def draw_maze():
    gb.screen.surface.fill(white)  
    int_x = int(gb.player.x)
    int_y = int(gb.player.y)
    for x in range((int_x - 15) if int_x > 15 else 0, (int_x + 15) if int_x + 15 < gb.maze.length else gb.maze.length):
        for y in range((int_y - 15) if int_y > 15 else 0, (int_y + 15) if int_y + 15 < gb.maze.length else gb.maze.length):
            match gb.maze.maze[x][y]:
                case "#": 
                    gb.screen.surface.blit(gb.asset['wall'], 
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
