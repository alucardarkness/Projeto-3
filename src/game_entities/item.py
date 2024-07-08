import src.globals as gb
from pygame import time
from src.utils.constants import *
from src.utils.resources import assets

class Item:
    #Classe genérica da qual todos os item herdam, mudando apenas o metodo effect para cada um
    def __init__(self, x:float, y:float, asset_id:str) -> None:
        self.x = x
        self.y = y
        self.asset_id = asset_id
        self.height = assets[asset_id].get_height()
        self.width = assets[asset_id].get_width()


    def effect(self):
        return
    
    def hit(self):
        gb.entity_stack.remove(self)

    def update(self):
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            self.effect()
            self.hit()

    def draw(self, screen):
        current_sprite = (time.get_ticks() // 750) % 2
        screen.surface.blit(assets[self.asset_id], 
                                ((((self.x - gb.player.x) * 16) * screen.resolution - self.width/2 + screen.width/2), 
                                 (((self.y - gb.player.y) * 16 -1 + 2 * current_sprite) * screen.resolution - self.height/2 + screen.height/2)))