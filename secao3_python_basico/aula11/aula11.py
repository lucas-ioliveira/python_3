
'''
Aula sobre len() -Conta a Quantidade de caracteres de uma string.
retorno da função len é int
'''
'''
# exemplo

usuario = input('Digite seu usuário: ')
qtd_caractere = len(usuario)

print(usuario, qtd_caractere, type(qtd_caractere))
'''
'''
# exemplo 2

usuario = input('Digite seu usuário: ')
qtd_caractere = len(usuario)

if qtd_caractere < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema')
'''
# exemplo 3
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados é: {len(string1) + len(string2)}')