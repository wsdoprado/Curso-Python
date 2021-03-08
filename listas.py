

lista1 = [100, 33, 1, 55, 99, 5, 7]

lista2 = ['W', 'i', 'l', 'l', 'i', 'a', 'm']

lista3 = []

lista4 = list(range(19))

lista5  = list('Tatiana Maria')


if 8 in lista4:
    print("Encontrei o número 8")
else:
    print("Não encontrei o número 8")

print(lista1)
print("Ordenando a Lista com o Sort")
lista1.sort()
print(lista1)

# Contar quantos elementos na lista
print(lista1.count(1))
print(lista5.count('a'))

print(lista1)
print("Adicionando elementos 100, 250, 1000, 66 na Lista com Append - Elemento único")
lista1.append([100, 250, 1000, 66])
print(lista1)

if [100, 250, 1000, 66] in lista1:
    print("Encontrei os elementos 100, 250, 1000, 66 na Lista")
else:
    print("Não encontrei o elemento na Lista")

#Adicionando Elementos com Extend
print("Adicionando elementos 44, 555, 666 na Lista com Extend - Elemento individual")
lista1.extend([44, 555, 666])
print(lista1)

#Adicionando elementos na lista com insert
lista1.insert(1, 'Chaaaama')
print(lista1)

# Juntando 2 listas
lista6 = lista1 + lista2
print(lista6)
# Juntando 2 listas
lista1.extend(lista2)
print(lista1)
# Juntando 2 listas
lista1 = lista1 + lista2
print(lista1)

# Invertendo a Lista com Reverse
print("Invertendo a Lista com Reverse")
lista1.reverse()
print(lista1)

#Copiando listas
lista7 = lista2.copy()
print(lista7)

#Tamanho das Listas
print(len(lista1))

#Remover Elementos da Lista com POP
print(lista5)
aux = lista5.pop() #POP retorna o elemento retirado
print(lista5)
lista5.append(aux)
print(lista5)

#LIMPAR LISTA
lista5.clear()
print(lista5)

#Transformando String em Lista com split - o mesmo usa espaços para separar
curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

#Transformando String em Lista com split - o mesmo usa , para separar
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#Transformando uma lista em String. colocando espaço entre elementos
curso2 = ['Programação', 'em', 'Python', 'Essencial']
print(curso2)
curso2 = ' '.join(curso2)
print(curso2)

print(curso2)