import src.services.render_maze as render_maze
from src.gui.interface import Interface
import pygame  
import src.globals as gb 

interface = Interface()

pygame.init()  
gb.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption('Projeto 3')  

# creating the display surface object   
# of specific dimension..e(X, Y).   
# set the pygame window name   


# infinite loop   
while True:  
    for event in pygame.event.get():  
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):  
            # gets the key name  
            key_name = pygame.key.name(event.key)  
            # converts to uppercase the key name  
            key_name = key_name.upper()  
            if key_name not in gb.key_dict:
                gb.key_dict[key_name] = False
            # if any key is pressed  
            if event.type == pygame.KEYDOWN:  
                # prints on the console the key pressed  
                #print(u'"{}" key pressed'.format(key_name))  
                gb.key_dict[key_name] = True
 
            # if any key is released  
            elif event.type == pygame.KEYUP:  
                # prints on the console the released key  
                #print(u'"{}" key released'.format(key_name))  
                gb.key_dict[key_name] = False
        if event.type == pygame.USEREVENT: 
            gb.player.time -= 1
            print(gb.player.time)
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  
    
    render_maze.draw_maze()
    for entity in gb.entity_stack:
        entity.update()
        # Draws the surface object to the screen.   
        entity.draw()

    interface.draw()
    pygame.display.update()   
    clock.tick(60)