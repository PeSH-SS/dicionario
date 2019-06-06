al1 = {'nome':'Isabela','nota':'7'}
al2 = {'nome':'Ricardo','nota':'10'}
al3 = {'nome':'Fernanda','nota':'9'}
al4 = {'nome':'João Paulo','nota':'7'}
al5 = {'nome':'Guilherme','nota':'8'}
al6 = {'nome':'Lorenza','nota':'9'}
al7 = {'nome':'Zeynep','nota':'8'}

lista = [al1, al2, al3, al4, al5, al6, al7]

maior_nota = 0
pessoas = []
for elemento in lista:
    
    if elemento ['nota'].isnumeric():
        nota = int(elemento['nota'])
    else:
        nota = 0

    if nota > maior_nota:
        maior_nota = nota
        pessoa = elemento

print(pessoa)
