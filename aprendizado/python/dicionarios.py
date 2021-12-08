dicionario = {'nome': 'Lucas', 'idade': 23, 'interesses': []}
print(dicionario)

print('\nAcrescentando valor ao dicionário >>>')

dicionario['interesses'].append('Desenvolvimento')
dicionario['interesses'].append('Livros')
dicionario['interesses'].append('Rock')
print(dicionario)

print('\nRemovendo ultimo valor da lista do dicionário >>>')
dicionario['interesses'].pop()
print(dicionario)

print('\nAlterando valor do indice nome >>>')
dicionario['nome'] = 'Lucas de Oliveira'
print(dicionario)
