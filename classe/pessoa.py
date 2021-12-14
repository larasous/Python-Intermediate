"""
Atributos - variáveis da classe
Métodos - funções que pertencem a classe
Self se refere a instancia da classe
"""
from datetime import datetime


class Pessoa:
    
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))
    
    def __init__(self, nome, idade, falando=False, comendo=False):
        
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
    
    def falar(self, assunto):
        
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando')
            
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
    
    def parar_falar(self):
        
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False
    
    def comer(self, alimento):
        
        if self.falando:
            print(f'{self.nome} está falando e não pode comer')
            return
        
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
    
    def parar_comer(self):
        
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False
    
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade