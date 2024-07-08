import src.globals as gb
from src.utils.resources import *
from src.utils.constants import *

class GameUi:
    def __init__(self) -> None:
        pass
    
    def draw(self, screen):
        #Desenha todos os componentes de interface do jogo durante a gameplay
        for i in range(gb.player.hp):
            screen.surface.blit(assets['heart'], (40 * i , 10))
        level_text = fonts['32'].render(f"level {gb.level}", True, BLACK)
        clock_text = fonts['32'].render(str(gb.player.time).rjust(10) if gb.player.time > 0 else 'game_over!', True, BLACK)
        score_text = fonts['32'].render(f"Score: {gb.player.points}/{gb.level*10}" , True, BLACK)
        item_text = fonts['16'].render(f"Press [Q]", True, BLACK)
        screen.surface.blit(level_text, (screen.width - 100, 10))  
        screen.surface.blit(clock_text, (screen.width/2 - 100, 10))  
        screen.surface.blit(score_text, (10, 50))  
        screen.surface.blit(assets['frame'], (screen.width - 100, 50))
        screen.surface.blit(item_text, (screen.width - 95, 130))  

        if gb.player.item: 
            screen.surface.blit(assets['bomb'], (screen.width - 90, 60))