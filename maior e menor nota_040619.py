al1 = {'nome':'Isabela','nota':7.5}
al2 = {'nome':'Ricardo','nota':9.9}
al3 = {'nome':'Fernanda','nota':9.5}
al4 = {'nome':'João Paulo','nota':7}
al5 = {'nome':'Guilherme','nota':8}
al6 = {'nome':'Lorenza','nota':9.45}
al7 = {'nome':'Zeynep','nota':10}

lista = [al1, al2, al3, al4, al5, al6, al7]

maiornota = 0
for elemento in lista:
    if elemento['nota'] > maiornota:
        maiornota = elemento['nota']
       

menornota = 10
for elemento in lista:
    if elemento['nota'] < menornota:
        menornota = elemento['nota']

print('Maior nota:',maiornota)
print('Menor nota:',menornota)
    
