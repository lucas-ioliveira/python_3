'''
Listas [] em Python
apped, insert, pop, del,
clear, extend, +, min, max
range
Uma lista pode conter vários valores e
vários tipos.
'''

# ex
'''
listas = ['a', 'b', 'c', 'd', 'e', 10.5]
# para acessar um indice:
print(listas[5])

# para modificar um indice:
listas[5] = '20.8'
print(listas[5])

# fatiamento:
print(listas[1:4])
'''
# ex 2

l1 = [1,2,3]
l2 = [4,5,6]
print(l1)
print(l2)

# extender listas
l1.extend(l2)

# adicionar indice ao final da lista
l2.append('b')

# adicionar indice a lista onde eu quiser.
l2.insert(0,'banana')

# deletar indice do final da lista
l2.pop()

# deletar qualquer indice
l3 = [1,2,3,4,5,6,7,8,9]
del(l3[3:5])
print(l3)

# apresentar valor max. e min.
print(max(l3) )
print(min(l3) )
