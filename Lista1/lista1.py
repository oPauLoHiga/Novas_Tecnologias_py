# 1.	Ler dois números inteiros, executar e mostrar o resultado das seguintes operações:
# adição, subtração, multiplicação e divisão.

# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite outro numero: "))
# soma = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2
# print(soma,sub, mul, div)

# 2.	Escreva um programa que receba uma string como entrada e retorne a string invertida.
# Exemplo: "Olá" → "álO".

# ABC = input("Digite uma palavra: ")
# ABCinvertido = ABC[::-1]
# print("Palavra invertida: ",ABCinvertido)

# 3.	Crie um programa que conte o número de vogais (a, e, i, o, u) em uma string fornecida pelo usuário, ignorando maiúsculas e minúsculas.
# Exemplo: "Python" → 2 vogais.

# palavra = input("Digite uma palavra: ")
# vogais = ("a","e","i","o","u")
# contador = 0
# palavramin = palavra.lower()
# for letra in palavramin:
#     if letra in vogais:
#         contador += 1
# print("A palavra possui ",contador," Vogais")


# 4.	Faça um programa que receba três números do usuário e calcule a média aritmética deles.
# Exemplo: 4, 6, 8 → Média = (4 + 6 + 8) / 3 = 6.

# soma = 0
# cont = 0
# for cont in range(3):
#     num = int(input('Digite um valor: '))
#     soma += num
#     print(num)
#     cont += 1
# print("A soma das notas é: ",soma)
#
# medida = soma / cont
# print("A media dos numeros é igual a: ",medida)

# 5.	Escreva um programa que calcule o fatorial de um número inteiro positivo fornecido.
# Use uma constante para representar o valor inicial (1).
# Exemplo: Entrada = 5 → Resultado = 5 × 4 × 3 × 2 × 1 = 120.
# import math
# num = int(input("Digite um número: "))
# resultado = math.factorial(num)
# print(resultado)


# 6.	Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
# Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
# com a fórmula: LITROS_USADOS = DISTÂNCIA / 12. O programa deve apresentar os valores da velocidade média,
# tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

# consumo = 12
# tempo = input("Digite o tempo de viagem em horas, (EX: 2.5) : ")
# tempo = float(tempo.replace(",", "."))
#
# velocidade = input("Digite a velocidade media durante a viagem: ")
# velocidade = float(velocidade.replace(",", "."))
#
# distancia = tempo * velocidade
# combustivel_utilizado = distancia / consumo
#
# import os
# os.system("cls")
#
# print(f"\nVelocidade media da viagem: {velocidade}Km/h")
# print(f"\nTempo da viagem: {tempo}Hrs")
# print(f"\nA viagem teve uma distancia de: {distancia}Km")
# print(f"\nNa viagem utilizou: {combustivel_utilizado}L\n")



