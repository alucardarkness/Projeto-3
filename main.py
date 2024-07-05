import src.services.render_maze as render_maze
from src.gui.interface import Interface
import pygame  
import src.globals as gb 
import csv
from src.utils.constants import *
from datetime import date
import pickle
from src.services.random_maze_gen import Maze
pygame.init()  
gb.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption('Projeto 3')  

interface = Interface()

while True:  
    #Interpreta todos os eventos do pygame que ocorreram naquele loop
    for event in pygame.event.get():  
        
        #Captura as teclas apertadas e soltadas
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):  
            key_name = pygame.key.name(event.key)  
            key_name = key_name.upper()  
            if key_name not in gb.key_dict:
                gb.key_dict[key_name] = False
            if event.type == pygame.KEYDOWN:  
                gb.key_dict[key_name] = True
                if key_name == 'ESCAPE' and gb.state == 'game':
                    gb.is_paused = not gb.is_paused
            elif event.type == pygame.KEYUP:  
                gb.key_dict[key_name] = False
                
        #Quando estiver dentro de um jogo e não estiver pausado, configura um timer que dispara derrota quando o jogador perder
        if event.type == pygame.USEREVENT and gb.state == "game" and not gb.is_paused: 
            gb.player.time -= 1
            gb.cron += 1
            if gb.player.time < 0:
                gb.on_trivia = False
                gb.event = 'gameover'
                gb.player.hit()
                
        if event.type == pygame.QUIT:  
            pygame.quit()  
            quit()  
    
    def set_phase():
        gb.maze = Maze(gb.level)
        gb.entity_stack = [gb.player]
        gb.maze.set_maze_entities()
        gb.player.respawn()

    if gb.event:
        print(gb.event)
        match gb.event:
            case "escape": gb.is_paused = False                 #Esc
            case "info": gb.state = 'about'                     #Botão para ir para o about
            case "exit":                                        #Botão sair
                pygame.quit()  
                quit()

            #vai para a tela de ranking e carrega o arquivo de scoreboard
            case "ranking": 
                gb.state = 'scoreboard'             #Botão para ir para o ranking
                with open(SCORE_FILE) as file:
                    gb.scoreboard = list(csv.reader(file, delimiter=','))[1:]
                    
            #Começa um novo jogo
            case "new_game":
                gb.state = 'game'
                gb.level = 1
                gb.player.points = 0
                set_phase()
            
            #Reinicia a fase
            case "restart":
                gb.is_paused = False
                set_phase()

            #Sai da fase e salva ela
            case "close": 
                gb.is_paused = False
                if gb.state == "game":
                    #Grava as variaveis de fase em um arquivo pkl
                    with open(SAVE_FILE, 'wb') as f: 
                        pickle.dump([gb.maze, gb.player, gb.entity_stack, gb.level, gb.cron], f)
                        f.close()
                gb.state = 'hub'

            #Carrega a fase a partir de um arquivo pkl
            case "load_game":
                with open(SAVE_FILE, 'rb') as f: 
                    gb.maze, gb.player, gb.entity_stack, gb.level, gb.cron = pickle.load(f)
                    f.close()
                gb.state = 'game'
                
            #dispara o evento quando o jogador chega na saida
            case "phase_complete":
                gb.level += 1
                set_phase()

            #dispara quando o jogador perder ou chegar no final da quinta fase
            case "gameover":
                gb.state = "gameover"
                #grava o score do jogador no arquivo de scores
                with open(SCORE_FILE, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([gb.player.name, int(100 *gb.level * gb.player.points / gb.cron)])
                    csvfile.close()
                    
                #abre o labirinto em que o jogador perdeu, adiciona a estatua na posição e salva o labirinto
                maze = None
                with open(f"storage/mazes/maze_{gb.level}", 'r') as f:
                    content = f.read().splitlines()
                    maze = [[c for c in line] for line in content[1:]]
                    
                with open(f"storage/mazes/maze_{gb.level}", 'w') as w:
                    if maze[gb.player.last_death[0]][gb.player.last_death[1]] not in ('E', 'S', '#'): 
                        maze[gb.player.last_death[0]][gb.player.last_death[1]] = 'A'
                    w.write(str(date.today()) + '\n' + '\n'.join([''.join(line) for line in maze]))
                    w.close()
                    
        #reseta o event
        gb.event = None
        
    #Controla a maquina de estados do jogo
    match gb.state:
        case "game":
            for entity in gb.entity_stack:
                if not gb.is_paused and not gb.on_trivia:
                    entity.update()
            render_maze.draw_maze()
            for entity in gb.entity_stack:
                entity.draw()
            render_maze.draw_maze_pos()
    interface.draw()
    pygame.display.update()   
    clock.tick(60)