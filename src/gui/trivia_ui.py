import src.globals as gb
from src.gui.trivia_button import TriviaButton
from src.utils.constants import *
from src.utils.resources import *

class TriviaUi:
    def __init__(self, screen) -> None:
        self.button1 = TriviaButton(screen.width/2 - 64*1.5 - 100, screen.height/2 - 21*1.5 + 120, num=1)
        self.button2 = TriviaButton(screen.width/2 - 64*1.5 + 100, screen.height/2 - 21*1.5 + 120, num=2)
        self.button3 = TriviaButton(screen.width/2 - 64*1.5 + 100, screen.height/2 - 21*1.5 + 200, num=3)
        self.button4 = TriviaButton(screen.width/2 - 64*1.5 - 100, screen.height/2 - 21*1.5 + 200, num=4)

    def draw(self, screen):
        #Desenha a tela de trivia com a pergunta e os quatro botões com as respostas
        screen.surface.blit(assets['book'], (screen.width/2 - 146 * 1.5, screen.height/2 - 180 * 1.5))  
        trivia_text = [fonts['16'].render(line, True, BLACK) for line in gb.trivia.title]
        for num, line in enumerate(trivia_text): screen.surface.blit(line, (screen.width/2 - 150, screen.height/2 - 21*2 - 100 + 20*num))  
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        self.button4.draw(screen)
