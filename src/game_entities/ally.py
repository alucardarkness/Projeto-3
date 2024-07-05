import src.globals as gb
from pygame import draw
from src.utils.constants import *
from src.services.trivia import Trivia
from src.game_entities.heart import Heart
from src.game_entities.clock import Clock
from src.game_entities.coin import Coin
from src.game_entities.stable_bomb import StableBomb
from random import randint
class Ally():
    def __init__(self, x:float, y:float, question:str, speed:float=0.02) -> None:
        self.x = x + 0.5
        self.y = y + 0.5
        self.question = question

    def hit(self):
        item_list = [Heart(self.x-0.5, self.y-0.5), Clock(self.x-0.5, self.y-0.5), Coin(self.x-0.5, self.y-0.5), StableBomb(self.x-0.5, self.y-0.5)]
        gb.entity_stack.append(item_list[randint(0, 3)])
        gb.entity_stack.remove(self)

    def update(self):
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.on_trivia = True
            gb.trivia = Trivia(self, True)

    def draw(self):
        gb.screen.surface.blit(gb.asset['ally'], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))