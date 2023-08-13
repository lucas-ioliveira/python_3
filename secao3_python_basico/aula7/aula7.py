# Introdução à formatação de Strings
# print(f'texto {a variável}')

nome = 'Lucas'
idade = 25
altura = 1.75
peso = 80
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')

# pode ser dessa maneira também
print('{} tem {} anos de idade e seu imc é: {}'.format(nome, idade, imc))

# pode ser dessa maneira também
print('{0} tem {1} anos de idade e seu imc é: {2}'.format(nome, idade, imc))

# pode ser dessa maneira também
print('{n} tem {i} anos de idade e seu imc é: {im}'.format(n=nome, i=idade, im=imc))