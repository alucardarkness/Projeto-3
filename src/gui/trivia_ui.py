import src.globals as gb
from src.gui.trivia_button import TriviaButton
from pygame import draw, Rect
from src.constants import *

class TriviaUi:
    def __init__(self) -> None:
        self.button1 = TriviaButton(gb.screen.width/2 - 64*1.5 - 100, gb.screen.height/2 - 21*1.5 + 120, num=1)
        self.button2 = TriviaButton(gb.screen.width/2 - 64*1.5 + 100, gb.screen.height/2 - 21*1.5 + 120, num=2)
        self.button3 = TriviaButton(gb.screen.width/2 - 64*1.5 + 100, gb.screen.height/2 - 21*1.5 + 200, num=3)
        self.button4 = TriviaButton(gb.screen.width/2 - 64*1.5 - 100, gb.screen.height/2 - 21*1.5 + 200, num=4)

    def draw(self):
        gb.screen.surface.blit(gb.asset['book'], (gb.screen.width/2 - 146 * 1.5, gb.screen.height/2 - 180 * 1.5))  
        trivia_text = [gb.font16.render(line, True, BLACK) for line in gb.trivia.title]
        for num, line in enumerate(trivia_text): gb.screen.surface.blit(line, (gb.screen.width/2 - 150, gb.screen.height/2 - 21*2 - 100 + 20*num))  
        self.button1.draw()
        self.button2.draw()
        self.button3.draw()
        self.button4.draw()
