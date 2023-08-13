'''
Aula sobre operadores relacionais
== (Igualdade) >(Maior) >=(Maior ou igual) <(Menor) <=(Menor ou igual) !=(Diferente)
Sempre retorna um valor booleano
'''

#  Exemplo
'''
num_1 = 2
num_2 = 2
expressao = (num_1 == num_2)
print(expressao)

#  Exemplo 2

num_1 = 2
num_2 = 2
expressao = (num_1 > num_2)
print(expressao)

#  Exemplo 3

num_1 = 2
num_2 = 2
expressao = (num_1 >= num_2)
print(expressao)

#  Exemplo 4

num_1 = 2
num_2 = 2
expressao = (num_1 < num_2)
print(expressao)

#  Exemplo 5

num_1 = 2
num_2 = 2
expressao = (num_1 <= num_2)
print(expressao)

#  Exemplo 6

num_1 = 2
num_2 = 2
expressao = (num_1 != num_2)
print(expressao)

#  Exemplo 7
nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')
#  idade para obter o emprestimo
idade_limite = 18
idade = int(idade)

if idade >= idade_limite:
    print(f'{nome} pode obter o empréstimo')
else:
    print(f'{nome} Não pode obter o empréstimo')
'''
#  Exemplo 7
nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')
#  idade para obter o emprestimo
idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade
idade = int(idade)

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode obter o empréstimo')
else:
    print(f'{nome} Não pode obter o empréstimo')



