dados = (('Lucas', 'Ubiratã', 23), ('João', 'Campo Mourão', 30))

# utilizando o for para printar os dados
for nome, cidade, idade in dados:
    print(nome, cidade, idade)
    print('\n')

# printando só alguns elementos
for nome, *_ in dados:
    print(nome + ' | Resto: ', *_)
    print('\n')

# utilizando função


def getUsuario(dados):

    for linha in dados:
        nome, cidade, idade = linha
        print(nome, cidade, idade)


if __name__ == '__main__':
    getUsuario(dados)
