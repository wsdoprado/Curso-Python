"""
Estrutura de Repetição em Python
"""

nome = "William Stephan do Prado"
nome1 = "Tatiana"
lista = [1, 2, 3, 4, 5, 6]

# LOOP em cima de String
for letra in nome:
    print(letra)

#  LOOP em cima de Lista
for letra1 in lista:
    print(letra1)
# LOOP em cima de Range
for aux in range(1, 10):
    print(aux)

# LOOP em cima de uma LISTA/String printando apenas o conteudo
for _, letra in enumerate(nome):
    print(letra)

# LOOP em cima de uma LISTA/String printando apenas o conteudo e índice
for indice, letra in enumerate(nome):
    print(indice,letra)

count = int(input('Qunatas vezes o Loop vai rodar?'))

for n in range(1, count+1):
    print("Imprimindo: %i " % n)

# Concatenação de String
print(nome1)
nome1 += ' Maria Guedes'
print(nome1)