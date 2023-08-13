'''
while (enquanto) em python
utilizado para realizar ações enquanto
uma condição for verdadeira.
Quando tiver a palavra 'continue' dentro da
função, será executado infinitamente.
Quando tiver a palavra 'break' dentro da função
será interrompido o loop
'''

# ex
'''
while True: # loop infinito.
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}!')
'''
'''
# ex

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1
print('Acabou')
'''