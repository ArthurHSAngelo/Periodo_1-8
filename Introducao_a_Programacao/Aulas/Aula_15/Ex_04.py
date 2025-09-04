def funcao():
    global nome
    nome = input('Digite um nome: ')

def funcao_secundaria():
    print(nome)

funcao()

funcao_secundaria()
