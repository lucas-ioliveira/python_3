'''
Joguinho de advinhação simples
para testar as funções.
'''

secreto = 'perfume'
digitados = []
chances = 3

while True:
    print('A palavra secreta tem 7 letras, dica: usamos após o banho.')
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letras = input('Digite uma letra: ')

    if len(letras) > 1:
        print('aaah, isso não vale, digite apenas uma letra.')
        continue

    digitados.append(letras)

    if letras in secreto:
        print(f'uhuuul, a letra {letras} existe na palavra secreta.')
    else:
        print(f'affzz, a letra {letras} não existe na palavra secreta.')
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! a palavra  era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letras not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()

