class moto:
    def __init__(self, modelo, ano, cor, cilindrada):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cilindrada = cilindrada

m1 = moto('Moto01', '1980', 'verde', '25000')
m2 = moto('Moto02', '1820', 'preta', '9000')

print('Moto 01:', m1.modelo, m1.ano, m1.cor, m1.cilindrada)
print('Moto 02:', m2.modelo, m2.ano, m2.cor, m2.cilindrada)
