'''
Operador ternário em Python
'''
logged_user = True
msg = 'Usuário Logado.' if logged_user else 'Usuário precisa logar'
print(msg)
print('-=' * 30)

print('Exemplo 2')
idade = input('Qual sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
    print(msg)
