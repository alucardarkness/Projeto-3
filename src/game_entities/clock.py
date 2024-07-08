import src.globals as gb
from src.game_entities.item import Item
from src.utils.resources import *

class Clock(Item):
    def __init__(self, x:int, y:int) -> None:
        super().__init__(x, y, 'clock')

    def effect(self):
        gb.player.time += 10
