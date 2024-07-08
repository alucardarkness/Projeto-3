import src.globals as gb
from src.utils.resources import assets
from src.game_entities.item import Item

class StableBomb(Item):
    def __init__(self, x:int, y:int) -> None:
        super().__init__(x, y, 'bomb')

    def effect(self):
        gb.player.item = "bomb"