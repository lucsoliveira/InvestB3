def funcao(a, b, c='dC', *args, **kwargs):
    # o c='dC' possui um valor default para c
    # o *args é uma tupla com valores posicionais
    # o kwargs é um dicionários com valores atribuidos
    print(a, b, c, args, kwargs)


funcao('A', 'B', 'C', 'D', 'E', z='Z', w='W')

# um exemplo disso no Django


def filter(**lookups):
    for k, v in lookups.items():
        print(k.split('__'), v)


filter(name__startswith='Hen', age__lt=30, city_endswith='rói')
