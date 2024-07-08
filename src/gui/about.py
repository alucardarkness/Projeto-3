from src.utils.resources import *
from src.gui.back_button import BackButton
from src.utils.constants import *

class About:
    def __init__(self) -> None:
        self.back_button = BackButton(180, 115, event='close')

    def draw(self, screen):
        #Renderiza a tela estatica das informacoes sobre o jogo
        screen.surface.blit(assets['hub'], (0, 0))
        self.back_button.draw(screen)
        count = 0
        title = fonts['32'].render('Labirintos da Unicamp', True, BLACK)
        screen.surface.blit(title, (screen.width/2 - 150, screen.height/2 - 230))  
        for line in ABOUT.split('\n'):
            count += 1
            score_text = fonts['16'].render(line, True, BLACK)
            screen.surface.blit(score_text, (screen.width/2 - 175, screen.height/2 - 200 + 20 * count))  
            
        title = fonts['32'].render('Labirintos da Unicamp', True, BLACK)
        screen.surface.blit(title, (screen.width/2 - 150, screen.height/2 - 230))  
        screen.surface.blit(assets['frame'], (screen.width/2 -36 - 75, screen.height/2 + 175))
        screen.surface.blit(assets['frame'], (screen.width/2 -36 + 75, screen.height/2 + 175))
        screen.surface.blit(assets['frame'], (screen.width/2 -36, screen.height/2 + 175))
        screen.surface.blit(assets['frame'], (screen.width/2 -36, screen.height/2 + 100))
        screen.surface.blit(assets['frame'], (screen.width/2 -36 - 85, screen.height/2 + 90))
        A = fonts['32'].render('A', True, WHITE)
        D = fonts['32'].render('D', True, WHITE)
        W = fonts['32'].render('W', True, WHITE)
        S = fonts['32'].render('S', True, WHITE)
        Q = fonts['32'].render('Q', True, WHITE)
        screen.surface.blit(A, (screen.width/2 -10 - 75, screen.height/2 + 198))  
        screen.surface.blit(D, (screen.width/2 -10 + 75, screen.height/2 + 198))  
        screen.surface.blit(S, (screen.width/2 -10, screen.height/2 + 198))  
        screen.surface.blit(W, (screen.width/2 -10, screen.height/2 + 123))  
        screen.surface.blit(Q, (screen.width/2 -10 - 85, screen.height/2 + 113))  
