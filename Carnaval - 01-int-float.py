"""Exercício 1:

Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;

Dica! Para calcular o log10, utilize a função log10 do módulo math conforme exemplo abaixo
>>> from math import log10
>>> log10(100)
2.0


from math import log10

print("Menu de Operações\n")

A = int(input("Informe o primeiro número:"))
B = int(input("Informe o primeiro número:"))

soma = A + B
menos = B - A
mult = A * B
div = A / B
resto = A % B
log = log10(A)
exp = A ** B

print("\n\nTabela de Resultados \n")

print(f"{A:5} + {B} = {soma}\n")
print(f"{B:5} - {A} = {menos}\n")
print(f"{A:5} * {B} = {mult}\n")
print(f"{A:5} / {B} = {div:.2}\n")
print(f"{A:5} % {B} = {resto}\n")
print(f"   log10({A}) = {log:.2}\n")
print(f"{A:5} ** {B} = {exp}")

Exercício 2:

Faça um programa que receba a base e altura de um triângulo e imprima a área dele.

Dica!
A área de um triângulo é dada pela seguinte fórmula abaixo
area=(base x altura)/2

print("Àrea do Triângulo")

base = float(input("Informe a base do triângulo: "))
alt = float(input("Informe a altura do triângulo: "))

area = (base * alt)/2

print(f"A área do triângulo é: {area:.2f}!")




Exercício 3:

No exercício acima você calculou a área de um triângulo a partir da sua base e altura. 
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. 
Os resultados devem ser idênticos.


Dica!
A área de um triângulo também é dada pela seguintes fórmulas abaixo
s=(s1+s2+s3)/2
area=√(s.(s-s1).(s-s2).(s-s3))

from cmath import sqrt


print("Àrea do Triângulo - Fórmula de Heron")

s1 = float(input("Informe o lado 1 do triângulo: "))
s2 = float(input("Informe o lado 2 do triângulo: "))
s3 = float(input("Informe o lado 3 do triângulo: "))

s=(s1+s2+s3)/2

area= sqrt((s*(s-s1)*(s-s2)*(s-s3)))

print(f"A área do triângulo é: {area:.2f}!")


Exercício 4:

Faça um programa que receba do usuário seu peso em kg e altura em metros 
e imprima o Índice de Massa Corporal (IMC) do usuário.

Dica!
O IMC é calculado de acordo com a fórmula abaixo
IMC=peso/〖altura〗^2 


print("Cálculo do IMC")

peso = float(input("Informe o seu peso (kg): "))
alt = float(input("Informe a sua altura (m)): "))

IMC=peso/(alt**2 )

print(f"O seu IMC é: {IMC:.2f}!")





Exercício 5:

Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. 
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.

num = int(input("Informe um número de 4 digitos: "))

u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10

soma = u + d + c + m

print(f"O número informacdo é {num}.\n{m} + {c} + {d} + {u} = {soma}")
"""

