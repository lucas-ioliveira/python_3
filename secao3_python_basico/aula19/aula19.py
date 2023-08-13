'''
Split, join, enumerate em python
* Split - Dividir uma string
* Join - Juntar uma lista
* Enumerate - Enumerar elementos da lista
'''
# Split
'''Estou passando para a nova variável que me dará um retorno
com cada palavra em uma lista'''
string = "O Brasil é o pais do futebol, o Brasil é penta."
lista = string.split(' ')
print(lista)

print('-=' * 20)

# Join
'''
A string2 é composta 1° pela "," em seguida a função join e passa
o parâmetro que quero fazer a junção
'''
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)
print(string)
print(lista)
print(string2)

print('-=' * 20)

# Enumerate
lista = ['Lucas', 'Kerollyn', 'Antonio']
for indice, nome in enumerate(lista):
    print(indice,nome)
    

