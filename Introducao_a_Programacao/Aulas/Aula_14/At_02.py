def exibe(info):
    for x in info:
        print(info[x])

dic = {'nome': input('Qual o nome: '),
       'cidade': input('Qual a cidade: ')}

exibe(dic)
