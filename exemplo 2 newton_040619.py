with open ('ma1a','r',encoding ='utf-8') as arquivo:
    lista = []
    for linha in arquivo.readlines():
        div = linha.split(',')
        dicionario = {'ra': div[0],
                      'nome': div[1],
                      'nota': div[6].replace('\n','')}
        lista.append(dicionario)

print(lista[10])
