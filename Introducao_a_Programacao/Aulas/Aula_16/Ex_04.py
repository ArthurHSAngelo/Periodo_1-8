class moto:
    def __init__(self, modelo, ano, cor, cilindrada):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cilindrada = cilindrada
    
    def ligar_motor(self):
        print('Ligando o motor da moto ' + self.modelo)
    
    def desligar_motor(self):
        print('Desligando o motor da moto ' + self.modelo)

m1 = moto('Moto01', '1980', 'verde', '25000')
m2 = moto('Moto02', '1820', 'preta', '9000')

m1.ligar_motor()
m1.desligar_motor()
print('-' * 20)
m2.ligar_motor()
m2.desligar_motor()
