from src.services.random_maze_gen import Maze
from src.services.render_maze import RenderMaze
from src.utils.screen import Screen
from src.game_entities.player import Player
import pygame  

pygame.init()  
pygame.display.set_caption('Projeto 3')  

# creating the display surface object   
# of specific dimension..e(X, Y).   
screen = Screen(resolution=2)
maze = Maze(45)
player = Player()
render_maze = RenderMaze(maze.maze)
# set the pygame window name   
key_dict = {'A':False, 'D':False, 'W':False, 'S':False}
# infinite loop   
while True:  
    for event in pygame.event.get():  
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):  
            # gets the key name  
            key_name = pygame.key.name(event.key)  
            # converts to uppercase the key name  
            key_name = key_name.upper()  
            if key_name not in key_dict:
                key_dict[key_name] = False
            # if any key is pressed  
            if event.type == pygame.KEYDOWN:  
                # prints on the console the key pressed  
                print(u'"{}" key pressed'.format(key_name))  
                key_dict[key_name] = True
 
            # if any key is released  
            elif event.type == pygame.KEYUP:  
                # prints on the console the released key  
                print(u'"{}" key released'.format(key_name))  
                key_dict[key_name] = False

        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  

        player.move(key_dict)
        # Draws the surface object to the screen.   

        render_maze.draw(screen, player.x, player.y)
        player.draw(screen)

        pygame.display.update()   