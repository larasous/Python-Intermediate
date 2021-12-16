"""
Métodos de classe - classmethod:
- Retorna um objeto da classe
"""

class Pessoa:
    
    ano_atual = 2021
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): # cls se refere a classe
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
p1 = Pessoa.por_ano_nascimento('Luiz', 2003)  # criando uma pessoa pelo ano de nascimento
print(p1.nome, p1.idade)
p1.get_ano_nascimento()