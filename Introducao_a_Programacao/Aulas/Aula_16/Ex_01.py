class pessoa:
    def __init__(self, nome, sexo, dt_nascimento, rg):
        self.nome = nome
        self.sexo = sexo
        self.dt_nascimento = dt_nascimento
        self.rg = rg

p1 = pessoa('Gabriel', 'Masculino', '01/05/2010', 'SP-21.541.200')
p2 = pessoa('Maria', 'Feminino', '01/01/2009', 'MG-25.251.253')

print('Pessoa 1:', p1.nome, p1.sexo, p1.dt_nascimento, p1.rg)
print('Pessoa 2:', p2.nome, p2.sexo, p2.dt_nascimento, p2.rg)
