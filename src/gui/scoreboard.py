import src.globals as gb
from src.gui.back_button import BackButton
from src.utils.constants import *
from src.utils.resources import *

class Scoreboard:
    def __init__(self) -> None:
        self.back_button = BackButton(180, 115, event='close')

    def draw(self, screen):
        #Renderiza a tela de score, mostrando o placar pela ordem de quem tem mais ponto
        screen.surface.blit(assets['hub'], (0, 0))
        self.back_button.draw(screen)
        gb.scoreboard.sort(key=lambda x: (-int(x[1]), x[0]))
        count = 0
        for player, score in gb.scoreboard:
            count += 1
            score_text = fonts['16'].render(f"{str(count).rjust(2)}. {player.ljust(40)} {score.rjust(10)}", True, BLACK)
            screen.surface.blit(score_text, (screen.width/2 - 150, screen.height/2 - 200 + 20 * count))  
            if count == 20: break