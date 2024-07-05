import src.services.render_maze as render_maze
from src.gui.interface import Interface
import pygame  
import src.globals as gb 


pygame.init()  
gb.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption('Projeto 3')  

interface = Interface()

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
                print(u'"{}" key pressed'.format(key_name))  
                gb.key_dict[key_name] = True
                if key_name == 'ESCAPE' and gb.state == 'game':
                    gb.is_paused = not gb.is_paused
 
            # if any key is released  
            elif event.type == pygame.KEYUP:  
                # prints on the console the released key  
                #print(u'"{}" key released'.format(key_name))  
                gb.key_dict[key_name] = False
        if event.type == pygame.USEREVENT and gb.state == "game" and not gb.is_paused: 
            gb.player.time -= 1
            if gb.player.time == 0:
                gb.event = 'gameover'
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  
    
    def set_phase():
        gb.maze = gb.maze_list[gb.level-1]
        gb.entity_stack = [gb.player]
        gb.maze.set_maze_entities()
        gb.player.respawn()

    if gb.event:
        print(gb.event)
        match gb.event:
            case "escape": 
                gb.is_paused = False
            case "close": 
                gb.is_paused = False
                gb.state = 'hub'
            case "restart":
                gb.is_paused = False
                set_phase()
            case "exit":
                pygame.quit()  
                quit()
            case "ranking":
                gb.state = 'scoreboard'
            case "new_game":
                gb.state = 'game'
                gb.level = 1
                set_phase()
            case "phase_complete":
                if gb.level < 5:
                    gb.level += 1
                    set_phase()
                else:
                    print("win game")
        gb.event = None
    match gb.state:
        case "hub":
            pass
        case "scoreboard":
            pass
        case "game":
            render_maze.draw_maze()
            for entity in gb.entity_stack:
                if not gb.is_paused:
                    entity.update()
                # Draws the surface object to the screen.   
                entity.draw()
    interface.draw()
    pygame.display.update()   
    clock.tick(60)