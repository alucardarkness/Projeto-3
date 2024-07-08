from src.utils.resources import *
from src.gui.button import Button
from src.utils.constants import *
from pygame import time
import src.globals as gb

class Hub:
    def __init__(self, screen) -> None:
        self.new_game_button = Button(screen.width/2 - 64*2 - 50, screen.height/2 - 21*2 - 200, text='New Game', event='new_game')
        self.load_game_button = Button(screen.width/2 - 64*2 + 50, screen.height/2 - 21*2 - 100, text='Load Game', event='load_game')
        self.ranking_button = Button(screen.width/2 - 64*2 - 50, screen.height/2 - 21*2, text=' Ranking', event='ranking')
        self.info_button = Button(screen.width/2 - 64*2 + 50, screen.height/2 - 21*2 + 100, text='  About', event='info')
        self.exit_button = Button(screen.width/2 - 64*2 - 50, screen.height/2 - 21*2 + 200, text='  Exit', event='exit')

    def draw(self, screen):
        #Desenha os 5 botões da tela inicial
        screen.surface.blit(assets['hub'], (0, 0))
        self.new_game_button.draw(screen)
        self.load_game_button.draw(screen)
        self.ranking_button.draw(screen)
        self.info_button.draw(screen)
        self.exit_button.draw(screen)
        
        current_sprite_item = (time.get_ticks() // 750) % 2
        current_sprite_player = (int(0.04 * time.get_ticks()) % 20) // 5
        screen.surface.blit(assets['player_right'][current_sprite_player], (screen.width/2 - 64*2 + 235, screen.height/2 - 21*2 - 180))
        screen.surface.blit(assets['enemy_right'][current_sprite_player], (screen.width/2 - 64*2 - 20, screen.height/2 - 21*2 - 90))
        screen.surface.blit(assets['bomb'], (screen.width/2 - 64*2 + 235, screen.height/2 -2 + 4 * current_sprite_item - 21*2 + 20))
        screen.surface.blit(assets['heart'], (screen.width/2 - 64*2 - 20, screen.height/2 -2 + 4 * current_sprite_item - 21*2 + 130))
        screen.surface.blit(assets['coin'], (screen.width/2 - 64*2 + 235, screen.height/2 -2 + 4 * current_sprite_item - 21*2 + 220))