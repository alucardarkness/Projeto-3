import src.globals as gb
from src.gui.button import Button
from pygame import draw, Rect
from src.constants import *
from src.gui.game_ui import GameUi
from src.gui.hub import Hub
from src.gui.pause import Pause
from src.gui.scoreboard import Scoreboard
from src.gui.trivia_ui import TriviaUi
from src.gui.gameover import Gameover
from src.gui.about import About

class Interface:
    def __init__(self) -> None:
        self.hub = Hub()
        self.pause = Pause()
        self.game_ui = GameUi()
        self.scoreboard = Scoreboard()
        self.trivia_ui = TriviaUi()
        self.gameover = Gameover()
        self.about = About()
        
    def draw(self):
        match gb.state:
            case "hub": self.hub.draw()
            case "game": 
                self.game_ui.draw()
                if gb.on_trivia:
                    self.trivia_ui.draw()
                elif gb.is_paused:
                    self.pause.draw()
            case "scoreboard":
                self.scoreboard.draw()
            case "gameover":
                self.gameover.draw()
            case "about":
                self.about.draw()