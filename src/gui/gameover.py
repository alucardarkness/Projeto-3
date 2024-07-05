import src.globals as gb
from src.gui.button import Button
from pygame import draw, Rect
from src.constants import *

class Gameover:
    def __init__(self) -> None:
        self.new_game_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2, text='New Game', event='new game')
        self.exit_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2 + 100, text='  Exit', event='close')

    def draw(self):
        gb.screen.surface.blit(gb.asset['hub'], (0, 0))
        score_text = gb.font.render(f"Total Score: {gb.level * gb.player.points / gb.cron} ", True, BLACK)
        gb.screen.surface.blit(score_text, (gb.screen.width/2 - 100, gb.screen.height/2 - 21*2 - 100))  
        self.new_game_button.draw()
        self.exit_button.draw()