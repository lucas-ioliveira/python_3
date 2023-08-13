#Função def - parte 2 - return
'''
Geralmente não se ultiliza print() em funções.
'''

#Ex:
'''def divisao(n1, n2):
    return n1 / n2 #Retorna os valores e não execulta nada abaixo dele.

divide = divisao(8, 2)
print(divide)
'''
#Ex2:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(n1, n2)

if divide:
    print(divide)
else:
    print('Conta inválida.')
