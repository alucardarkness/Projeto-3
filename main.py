from src.gui.interface import Interface
import pygame  
import src.globals as gb 
import csv
from src.utils.constants import *
from datetime import date
import pickle
from src.services.maze import Maze
from src.screen import Screen
import src.utils.resources as rs 
from random import randint

#Inicia o pygame, as variaveis globais e as fontes e assets
pygame.init()  
gb.init()
rs.init()

#Instancia a tela e a Interface
screen = Screen(resolution=4)
interface = Interface(screen)

#Configura um Clock que dispara a cada 1000 milisegundos (1s)
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption('Projeto 3')  


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
        #Configura uma nova fase para o jogo
        gb.maze = Maze(gb.level)
        gb.entity_stack = [gb.player]
        gb.maze.set_maze_allies()
        gb.maze.set_maze_items()
        gb.maze.set_maze_enemies()
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
                    scoreboard = list(csv.reader(file, delimiter=','))
                    
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
                    
                #Grava no arquivo de aliados uma nova estátua guardando o lugar onde o player morreu e ultima pergunta que foi respondida ou não. 
                with open(STATUES_FILE) as r, open(STATUES_FILE, 'a', newline='') as w:
                    reader = list(csv.reader(r))
                    writer = csv.writer(w)
                    writer.writerow([int(reader[-1][0] if len(reader) > 0 else 0)+1, gb.player.name, *gb.player.last_death, gb.level, gb.trivia.id if gb.trivia else randint(1,6)])
                    
                    
        #reseta o event
        gb.event = None
        
    #Controla a maquina de estados do jogo
    if gb.state == "game" and not gb.is_paused and not gb.on_trivia:
        #Quando está no jogo, não pausado e não está em uma trivia, a cada game_tick ele atualiza todas as entidades presentes no mapa
        for entity in gb.entity_stack:
            entity.update()
                
        #Desenha as partes inferiores do labirinto
        gb.maze.draw(screen)
        #Desenha todas as entidades presentes na pilha
        for entity in gb.entity_stack:
            entity.draw(screen)
        #Desenha as partes superiores do labirinto
        gb.maze.draw_pos(screen)
        
        #Desenhar as coisas nessa ordem gera um efeito de perspectiva e profundidade, dando a impressão de que o player pode ficar atrás de uma parede do labirinto

    #desenha a interface
    interface.draw(screen)
    pygame.display.update()   
    clock.tick(60)