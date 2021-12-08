class Carro:
    print('Carregando classe...')

    nome = 'Ferrari'

    # o 'self' equivale ao 'this' do javascript
    def __init__(self):
        self.motor_running = False

    def ignition(self):
        self.motor_running = True
        print('vrumm.....')

    print('Fim definição nome.')
    # dentro da classe aceita funções e loops
    if int(len(nome) % 2) == 0:
        portas = 2
    else:
        portas = 3


carrinho = Carro()

print('Nome: ', carrinho.nome)
print('Portas: ', carrinho.portas)
print('O carro está andando? ', carrinho.motor_running)

carrinho.ignition()
print('E agora, está andando? ', carrinho.motor_running)
