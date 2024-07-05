import src.globals as gb
from src.gui.button import Button
from pygame import draw, Rect
from src.constants import *
from src.gui.game_ui import GameUi
from src.gui.hub import Hub
from src.gui.pause import Pause
from src.gui.scoreboard import Scoreboard

class Interface:
    def __init__(self) -> None:
        self.hub = Hub()
        self.pause = Pause()
        self.game_ui = GameUi()
        self.scoreboard = Scoreboard()
    def draw(self):
        match gb.state:
            case "hub": self.hub.draw()
            case "game": 
                self.game_ui.draw()
                if gb.is_paused:
                    self.pause.draw()
            case "scoreboard":
                self.scoreboard.draw()
                