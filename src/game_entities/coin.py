import src.globals as gb
from src.game_entities.item import Item
from src.utils.resources import assets

class Coin(Item):
    def __init__(self, x:int, y:int) -> None:
        super().__init__(x, y, 'coin')

    def effect(self):
        gb.player.points += 1