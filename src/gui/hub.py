import src.globals as gb
from src.gui.button import Button
from pygame import draw, Rect
from src.utils.constants import *

class Hub:
    def __init__(self) -> None:
        self.new_game_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2 - 200, text='New Game', event='new_game')
        self.load_game_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2 - 100, text='Load Game', event='load_game')
        self.ranking_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2, text=' Ranking', event='ranking')
        self.info_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2 + 100, text='  About', event='info')
        self.exit_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2 + 200, text='  Exit', event='exit')

    def draw(self):
        gb.screen.surface.blit(gb.asset['hub'], (0, 0))
        self.new_game_button.draw()
        self.load_game_button.draw()
        self.ranking_button.draw()
        self.info_button.draw()
        self.exit_button.draw()