class pessoa:
    def __init__(self, nome, sexo, dt_nascimento, rg):
        self.nome = nome
        self.sexo = sexo
        self.dt_nascimento = dt_nascimento
        self.rg = rg
    
    def saudacao(self):
        print('Olá, bom dia ' + self.nome)
    
    def despedida(self):
        print('Adeus! ' + self.nome)

p1 = pessoa('Gabriel', 'Masculino', '01/05/2010', 'SP-21.541.200')
p2 = pessoa('Maria', 'Feminino', '01/01/2009', 'MG-25.251.253')

p1.saudacao()
p1.despedida()
print('-' * 20)
p2.saudacao()
p2.despedida()
