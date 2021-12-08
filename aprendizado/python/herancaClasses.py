class Carro:
    portas = 2

    def __init__(self, nome):
        self.nome = nome


class Ferrari(Carro):
    def __init__(self, modelo):
        super().__init__('Ferrari')
        self.modelo = modelo


a = Ferrari('F50')

print('Nome: ', a.nome)
print('Modelo: ', a.modelo)
print('Portas: ', a.portas)
