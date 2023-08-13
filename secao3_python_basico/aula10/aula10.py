'''
Aula sobre operadores lógicos
and
or
not
in
not in
'''

# (Verdadeiro e verdadeiro = verdadeiro) as duas expressões tem que ser verdadeira
'''comparacao1 and comaparacao2'''

# (verdadeiro ou verdadeiro = verdadeiro) uma expressão tem que ser verdadeira
'''comp1 or comp2'''

# not inverte a expressão
'''
a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

# exemplo

nome = 'Lucas'
if 'u' in nome: # in é como se fosse 'estar em'
    print('Existe a letra U no seu nome.')

# exemplo
nome = 'Lucas'
if 'asas' not in nome: # not in é "se não estiver"
    print('Executei.')
else:
    print('Existe o texto')
'''
# Exemplo Login
# cadastrado no bd
usuario_bd = 'lucas'
senha_bd = '1234'

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválida')



