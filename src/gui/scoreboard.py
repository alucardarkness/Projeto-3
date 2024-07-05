import src.globals as gb
from src.gui.back_button import BackButton
from pygame import draw, Rect
from src.utils.constants import *

class Scoreboard:
    def __init__(self) -> None:
        self.back_button = BackButton(180, 115, event='close')

    def draw(self):
        gb.screen.surface.blit(gb.asset['hub'], (0, 0))
        self.back_button.draw()
        gb.scoreboard.sort(key=lambda x: (-int(x[1]), x[0]))
        count = 0
        for player, score in gb.scoreboard:
            count += 1
            score_text = gb.font16.render(f"{count}. {player.ljust(40)} {score.rjust(10)}", True, BLACK)
            gb.screen.surface.blit(score_text, (gb.screen.width/2 - 150, gb.screen.height/2 - 200 + 20 * count))  
            if count == 20: break