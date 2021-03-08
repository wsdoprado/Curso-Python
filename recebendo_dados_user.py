
# Entrada de Dados
print("Qual o seu nome?")
nome = input() #String
print("Qual sua idade?")
idade = input() #String

# Saída de Dados1
#print(f"O seu nome é: {nome}")
# Saída de Dados2
#print(f"O seu nome é: " + nome)
# Saída de Dados3
print(f"O seu nome é: %s " % nome)

print(nome + " você tem: " + idade + " anos.")

print("Entre com um numero:" )
numero1 = input()

print("Entre com um numero:" )
numero2 = input()

soma = int(numero1) + int(numero2)

print("A soma é: %i " % soma)

if soma < 20:
    print("A soma %i é menor que 20" % soma)
elif  soma > 20 and soma <= 100:
    print("A soma %i é maior que 20 e menor igual a 100" % soma)
else:
    print("A soma %i é maior que 100" % soma)