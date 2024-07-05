import src.services.render_maze as render_maze
from src.gui.interface import Interface
import pygame  
import src.globals as gb 
import csv
from src.constants import *
from datetime import date
import pickle
from src.services.random_maze_gen import Maze
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
                #print(u'"{}" key pressed'.format(key_name))  
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
            gb.cron += 1
            if gb.player.time == 0:
                gb.event = 'gameover'
                gb.player.hit()
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  
    
    def set_phase():
        gb.maze = Maze(gb.level)
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
                # Saving the objects:
                with open(SAVE_FILE, 'wb') as f:  # Python 3: open(..., 'wb')
                    pickle.dump([gb.maze, gb.player, gb.entity_stack, gb.level, gb.cron], f)
                    f.close()
            case "load_game":
                # Getting back the objects:
                with open(SAVE_FILE, 'rb') as f:  # Python 3: open(..., 'rb')
                    gb.maze, gb.player, gb.entity_stack, gb.level, gb.cron = pickle.load(f)
                    f.close()
                gb.state = 'game'
            case "restart":
                gb.is_paused = False
                set_phase()
            case "exit":
                pygame.quit()  
                quit()
            case "ranking":
                gb.state = 'scoreboard'
            case "info": 
                gb.state = 'about'
            case "new_game":
                gb.state = 'game'
                gb.level = 1
                set_phase()
            case "phase_complete":
                gb.level += 1
                set_phase()

            case "gameover":
                gb.state = "gameover"
                with open(SCORE_FILE, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['aluno', int(100 *gb.level * gb.player.points / gb.cron)])
                    csvfile.close()
                    
                maze = None
                with open(f"storage/mazes/maze_{gb.level}") as f:
                    content = f.read().splitlines()
                    maze = [[c for c in line] for line in content[1:]]
                    if maze[gb.player.last_death[0]][gb.player.last_death[1]] not in ('E', 'S', '#'): 
                        maze[gb.player.last_death[0]][gb.player.last_death[1]] = 'A'
                with open(f"storage/mazes/maze_{gb.level}", 'w') as w:
                    w.write(str(date.today()) + '\n' + '\n'.join([''.join(line) for line in maze]))
                    w.close()
        gb.event = None
    match gb.state:
        case "game":
            for entity in gb.entity_stack:
                if not gb.is_paused and not gb.on_trivia:
                    entity.update()
            render_maze.draw_maze()
            for entity in gb.entity_stack:
                # Draws the surface object to the screen.   
                entity.draw()
            render_maze.draw_maze_pos()
    interface.draw()
    pygame.display.update()   
    clock.tick(60)