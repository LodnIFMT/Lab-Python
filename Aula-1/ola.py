print('Ola mundo\n')

nome = 'Lucas'
idade = 20
altura = 1.75

print(f'Ola {nome}')
print(F'Você tem {idade} anos')
print(f'Altura: {altura}\n')

def ola(nome):
    print(f'Ola {nome} Seja Bem Vindo')

ola('Sarah')
ola(nome)
ola(input('Digite Seu Nome: '))