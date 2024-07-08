import src.globals as gb
from src.gui.button import Button
from src.utils.constants import *
from src.utils.resources import *

class Gameover:
    def __init__(self, screen) -> None:
        self.new_game_button = Button(screen.width/2 - 64*2, screen.height/2 - 21*2, text='New Game', event='new_game')
        self.exit_button = Button(screen.width/2 - 64*2, screen.height/2 - 21*2 + 100, text='  Exit', event='close')

    def get_total_score(self):
        return int(100 *gb.level * gb.player.total_points / gb.cron)
    
    def draw(self, screen):
        #Desenha a tela de fim de jogo mostrando o total_score
        screen.surface.blit(assets['hub'], (0, 0))
        score_text = fonts['32'].render(f"Total Score: {self.get_total_score()} ", True, BLACK)
        screen.surface.blit(score_text, (screen.width/2 - 100, screen.height/2 - 21*2 - 100))  
        self.new_game_button.draw(screen)
        self.exit_button.draw(screen)