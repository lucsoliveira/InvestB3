nome = 'Lucas Oliveira'

# verifica se são vogais
# caso seja, coloca em maiuscula a vogal

for c in nome:
    if c in 'aeiou':  # aqui a tupla pode ser usada também, o 'in' funcinar como o 'OR'
        print(c.upper())
    elif c == 'a':
        print('@')
    else:
        print(c)
