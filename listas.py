

lista1 = [100, 33, 1, 55, 99, 5, 7]

lista2 = ['W', 'i', 'l', 'l', 'i', 'a', 'm']

lista3 = []

lista4 = list(range(19))

lista5  = list('Tatiana Maria')


print("EXERCICIOS EM PYTHON - WILLIAM PRADO")

print("")
print("->> Busca em Listas com IN")
if 8 in lista4:
    print("Encontrei o número 8")
else:
    print("Não encontrei o número 8")

print("")
print(lista1)
print("->> Ordenando a Lista com o Sort")
lista1.sort()
print(lista1)

print("")
print("->> Contar quantos elementos na lista com .count")
print(lista1.count(1))
print(lista5.count('a'))

print("")
print(lista1)
print("->> Adicionando elementos 100, 250, 1000, 66 na Lista com Append - Elemento único")
lista1.append([100, 250, 1000, 66])
print(lista1)

if [100, 250, 1000, 66] in lista1:
    print("Encontrei os elementos 100, 250, 1000, 66 na Lista")
else:
    print("Não encontrei o elemento na Lista")


print("")
print("->> Adicionando elementos 44, 555, 666 na Lista com Extend - Elemento individual")
lista1.extend([44, 555, 666])
print(lista1)

print("")
print("->> Adicionando elementos na lista com insert")
lista1.insert(1, 'Chaaaama')
print(lista1)

print("")
print("->> Juntando 2 listas")
lista6 = lista1 + lista2
print(lista6)

print("")
print("->> Juntando 2 listas")
lista1.extend(lista2)
print(lista1)

print("")
print("->> Juntando 2 listas")
lista1 = lista1 + lista2
print(lista1)

print("")
print("Invertendo a Lista com Reverse")
lista1.reverse()
print(lista1)

print("")
print("Copiando listas com .copy")
lista7 = lista2.copy()
print(lista7)

print("")
print("->> Tamanho das Listas com LEN")
print(len(lista1))

print("")
print("->>Remover Elementos da Lista com POP | #POP retorna o elemento retirado")
print(lista5)
aux = lista5.pop()
print(lista5)
lista5.append(aux)
print(lista5)

print("")
print("->> LIMPAR LISTA com .clear")
lista5.clear()
print(lista5)

print("")
print("->> Transformando String em Lista com split - o mesmo usa espaços para separar")
curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

print("")
print("->> Transformando String em Lista com split - o mesmo usa , para separar")
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

print("")
print("->> Transformando uma lista em String e colocando espaço entre elementos")
curso2 = ['Programação', 'em', 'Python', 'Essencial']
print(curso2)
curso2 = ' '.join(curso2)
print(curso2)

print("")
print("->> Adicionando variaveris em lista")
numeros =  [1, 2, 3, 4, 5, 1]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 1

numeros = [num1, num2, num3, num4, num5, num6]
print(numeros)

print("")
print("->> Acesso a dados com índice")
cores = ['azul', 'amarelo', 'verde', 'preto']
print(cores[0]) #Azul
print(cores[1]) #Amarelo
print(cores[2]) #Verde
print(cores[3]) #Preto

print("")
print("->> Acesso a dados com índice invertido")
print(cores[-1]) #Preto
print(cores[-2]) #Verde
print(cores[-3]) #Amarelo
print(cores[-4]) #Azul

print("")
print("->> Exemplo FOR em Listas")
for cor in cores:
    print(cor)
indice = 0

print("")
print("->>Exemplo WHILE em Listas")
while indice < len(cores):
    print(cores[indice])
    indice+=1

print("")
print("->> Gerando indices com enumerate")
for indice, cor in enumerate(cores):
    print(indice, cor)

print("")
print("Buscando indice em uma lista - Retorna do primeiro elemento encontrado")
print(numeros.index(1))
print("Buscando indice em uma lista - Retorna do primeiro elemento encontrado")
print(numeros.index(5))
print("Buscando indice em uma lista com range de inicio- Retorna do primeiro elemento encontrado")
print(numeros.index(1, 0, 6))

print("")
print("Tipo de Dados numeros")
print(type(numeros))

print("")
print("Tipo de Dados numeros após conversão para tuple")
tuple = tuple(numeros)
print(type(tuple))


print("")
print("Copiando Listas com copy e sem copy")
lista = [1, 2, 3, 4, 5, 6]
listacopia = lista.copy()
print(lista)
print(listacopia)
listacopia.append(7)
print(lista)
print(listacopia)

print("Copias de Listas sem o .copy")
lista = [1, 2, 3, 4, 5, 6]
listacopia = lista
print(lista)
print(listacopia)
listacopia.append(7)
print(listacopia)
print(lista)