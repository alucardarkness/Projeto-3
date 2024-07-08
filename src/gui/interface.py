import src.globals as gb
from src.gui.game_ui import GameUi
from src.gui.hub import Hub
from src.gui.pause import Pause
from src.gui.scoreboard import Scoreboard
from src.gui.trivia_ui import TriviaUi
from src.gui.gameover import Gameover
from src.gui.about import About

class Interface:
    def __init__(self, screen) -> None:
        self.hub = Hub(screen)
        self.pause = Pause(screen)
        self.game_ui = GameUi()
        self.scoreboard = Scoreboard()
        self.trivia_ui = TriviaUi(screen)
        self.gameover = Gameover(screen)
        self.about = About()
        
    def draw(self, screen):
        #Controla qual/quais telas devem ser renderizadas no momento de acordo com o state do jogo.
        match gb.state:
            case "hub": self.hub.draw(screen)
            case "game": 
                self.game_ui.draw(screen)
                #Durante o jogo, tanto a trivia, quanto o pause sobrescrevem o mapa
                if gb.on_trivia:
                    self.trivia_ui.draw(screen)
                elif gb.is_paused:
                    self.pause.draw(screen)
            case "scoreboard":
                self.scoreboard.draw(screen)
            case "gameover":
                self.gameover.draw(screen)
            case "about":
                self.about.draw(screen)