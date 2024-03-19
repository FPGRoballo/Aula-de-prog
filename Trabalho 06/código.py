#Variáveis para números
numero_1 = 84
print("Número 1:", numero_1)
numero_2 = 79
print("Número 2:", numero_2)
numero_3 = 50
print("Número 3:", numero_3)
numero_4 = 65
print("Número 4:", numero_4)

#Variável para frase
frase = "Olá, professor! Este aqui é o meu trabalho."

#Variável para palavra
palavra = "Exercício"

print("Frase:", frase)
print("Palavra:", palavra)

números = (numero_1, numero_2, numero_3, numero_4)
soma = sum(números)
média = soma / len("números")
print ("A média dos números é:" , média)

quadrado = pow(numero_3,2)
print ("50 Elevado ao Quadrado é:", quadrado)
dobro = numero_2 * 2
print ("O dobro de 79 é:", dobro)

quantidade = len(palavra)
print ("A palavra tem {} letras" .format(quantidade))

def check_space(frase):
    count = 0
    for i in range(0, len(frase)):
        if frase[i] == " ":
            count += 1
    return count
print ("O número de espaços em branco é:", check_space(frase))

if numero_1>numero_2:
    print("O primeiro número é maior que o segundo")
if numero_1<numero_2:
    print("O primeiro número é menor que o segundo")

lista = [84, 79, 50, 65]
print("O maior número da lista é:", max(lista))
