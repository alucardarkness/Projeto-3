import src.globals as gb
from src.gui.button import Button
from pygame import draw, Rect
from src.utils.constants import *

class Trivia:
    def __init__(self, enemy, is_passivel:bool=False) -> None:
        self.enemy = enemy
        self.id = self.enemy.question
        self.title = self.get_title(self.id)
        self.answers = self.get_answers(self.id)
        self.correct = self.get_correct(self.id)
        self.is_passivel = is_passivel
    def get_title(self, trivia_id):
        match trivia_id:
            case 0: return ["Hello World?"]
            case 1: return ["Integrais tambem sao conhecidas por:"]
            case 2: return ["Qual o tipo de data structure", "denotado por {}?"]
            case 3: return ["Qual a cor do cavalo branco", "de napoleao?"]
            case 4: return ["Qual o nome do minotauro que", "enfrentou Teseus?"]
            case 5: return ["Qual foi o tema do projeto 2?"]
            case 6: return ["Qual das series a seguir possui", "o maior numero de episodios?"]

            
    
    def get_answers(self, trivia_id):
        match trivia_id:
            case 0:
                return ("True True", "True False", "False True", "False False")
            case 1:
                return ("Antiderivada", "Soma infinitesimal", "Funcao da area", "Aproximacao linear")
            case 2:
                return ("Tupla", "Soma lista", "Dicionario", "String")
            case 3:
                return ("Vermelho", "Ele nao tinha cavalo", "Branco", "Preto")
            case 4:
                return ("Asterios", "Asmodeus", "Asmodeus", "Aaracokra")
            case 5:
                return ("Cheetos", "Domino", "Recursao", "Cores")
            case 6:
                return ("Power rangers", "One piece", "Doctor who", "Vila sesamo")
    def get_correct(self, trivia_id):
        match trivia_id:
            case 0: return 1
            case 1: return 1
            case 2: return 3
            case 3: return 3
            case 4: return 1
            case 5: return 2
            case 6: return 4
    
    def submit(self, answer):
        gb.on_trivia = False
        if answer == self.correct:
            self.enemy.hit()
            gb.player.points += 5
        else:
            if not self.is_passivel: 
                gb.player.hit()
            else:
                self.enemy.hit()
