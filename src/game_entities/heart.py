import src.globals as gb
from src.utils.resources import assets
from src.game_entities.item import Item

class Heart(Item):
    def __init__(self, x:int, y:int) -> None:
        super().__init__(x, y, 'heart')

    def effect(self):
        if gb.player.hp < 5: 
            gb.player.hp += 1 
