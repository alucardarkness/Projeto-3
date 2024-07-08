import src.globals as gb
from src.utils.constants import *
from src.game_entities.heart import Heart
from src.game_entities.clock import Clock
from src.game_entities.coin import Coin
from src.game_entities.stable_bomb import StableBomb
from random import randint

class Trivia:
    def __init__(self, enemy, is_ally:bool=False) -> None:
        self.enemy = enemy
        self.id = self.enemy.question
        content = '' #Carrega o arquivo de trivia de acordo com o id
        with open(f"storage/trivias/trivia_{self.id}.txt") as f:
            content = f.read().splitlines()
            f.close()
        self.title = content[0].split(';')
        self.answers = content[1].split(';')
        self.correct = int(content[2])
        self.is_ally = is_ally
    
    def submit(self, answer):
        #Quando um dos 4 botões for apertado, ele verifica se a resposta é a correta
        gb.on_trivia = False            
        if answer == self.correct:
            if self.is_ally: #Se for uma trivia de aliado, ele deixa um item aleatorio no lugar
                item_list = [Heart(self.enemy.x, self.enemy.y), Clock(self.enemy.x, self.enemy.y), StableBomb(self.enemy.x, self.enemy.y)]
                gb.entity_stack.append(item_list[randint(0, 2)])
            gb.player.points += 5 #Dá 5 pontos para o jogador
            self.enemy.hit() #Destroi o inimigo/aliado que chamou a trivia
        else:
            #Se a resposta estive errada
            if not self.is_ally: 
                gb.player.hit() #Se for inimigo, da dano ao player
            else:
                self.enemy.hit() #Se for aliado, apenas se destroi
