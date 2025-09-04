def funcao(variavel):
    vlocal = 'azul'
    global vlocal1
    vlocal1 = 'azul'

funcao()

print(vlocal1)