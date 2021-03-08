import os


# LOOP COM WHILE USANDO TRUE
state=True

while state == True:
    # LIMPAR TELA print("\n" * os.get_terminal_size().lines)
    print("Bem vindos a Calculadora em Python")
    print("Escolha uma das opções abaixo:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    escolha = int(input())

    if escolha == 1:
        state=True
        print("Somar")
    if escolha == 2:
        state=True
        print("Subtrair")
    if escolha == 3:
        state=True
        print("Multiplicar")
    if escolha == 4:
        state=True
        print("Dividir")
    if escolha == 0:
        state=False
        print("Sair")

print("Saindo Loop")

# LOOP COM WHILE USANDO ESPRESSÃO

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou jéssica? ')


# LOOP COM WHILE USANDO BREAK
state=True
while state == True:
    # LIMPAR TELA print("\n" * os.get_terminal_size().lines)
    print("Bem vindos a Calculadora em Python")
    print("Escolha uma das opções abaixo:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    escolha = int(input())

    if escolha == 1:
        state=True
        print("Somar")
    if escolha == 2:
        state=True
        print("Subtrair")
    if escolha == 3:
        state=True
        print("Multiplicar")
    if escolha == 4:
        state=True
        print("Dividir")
    if escolha == 0:
        break
        print("Sair")

print("Saindo Loop")