"""
Exercícios de Tuplas

Diferenças para Listas:

1 - Tuplas são representadas por parenteses ()

2 - Tuplas são imutáveis - não tem com alterar seus dados. Qualquer nova operação gera uma nova tupla

OBS: Tuplas são definidas por virgulas e não por parenteses

"""

tupla1 = (1, 2, 3, 4, 5, 6)
tupla2 = 1, 2, 3, 4, 5, 6
tupla3 = (1)
tupla4 =  (1,)
tupla5 = 1,
print("Printando a Tupla1: ")
print(tupla1)
print(type(tupla1))
print("")
print("Printando a Tupla2: ")
print(tupla2)
print(type(tupla2))
print("")
print("Printando a Tupla3: ")
print(tupla3)
print(type(tupla3))
print("")
print("Printando a Tupla4: ")
print(tupla4)
print(type(tupla4))
print("")
print("Printando a Tupla5: ")
print(tupla5)
print(type(tupla5))

print("")
print("Gerando uma Tupla com Range: ")
tupla = tuple(range(11))
print(tupla)

print("")
print("Desempacotamento de Tuplas: ")
tuplacidade = ('Pouso Alegre', 'MG')
cidade, estado = tuplacidade
print(cidade)
print(estado)

print("")
print("Operações em Tuplas: ")
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

print("")
print("Concatenação de Tuplas: ")
print(sum(tupla))