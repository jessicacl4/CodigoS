"""Lista de exercícios
Tema: laço de repetição

Exercício 1:

Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos 
pelo usuário e imprime-a na tela. O usuário digitará 0 como um valor para indicar que nenhum outro 
valor será fornecido. 
 Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.


# Solução 1


soma = 0
i = 0

while True:
    valor = float(input("Insira um valor para cálcula da média (0 - sair): "))
    if(valor == 0):
        break
    else:
        soma+=valor
    i+=1

media = soma / i

print(f"A média dos valores inseridos é: {media}")

____________///________________

Solução 2


def calc_media(lst:list) -> float:
    return(sum(lst)/len(lst))

valor = []

while True:
    entr = float(input("Insira um valor para cálcula da média (0 - sair): "))
    if(entr == 0):
        break
    valor.append(entr)

media = calc_media(valor)

print(f"A média dos valores inseridos é: {media}")
______________________________________________________

Exercício 2:

Escreva um programa que exiba uma tabela de conversão de temperatura para graus Celsius 
e graus Fahrenheit. 
A tabela deve incluir linhas para todas as temperaturas entre 0 e 100 graus Celsius 
que são múltiplos de 10 graus Celsius. Dê um título apropriado para cada coluna.


def conv_celcius_fahrenheit(celcius:float) -> float:
    fahrenheit =  celcius * 1.8 + 32
    return (fahrenheit)

i = 0
celcius = []
fahr = []

for _ in range(11):
    celcius.append(i)
    conv = conv_celcius_fahrenheit(i)
    fahr.append(conv)
    i+=10

print(" Temp. ºC     Temp. F     ")
i = 0
for _ in range(11):
    print(f"|   {celcius[i]}        | {fahr[i]}      |")
    i+=1
_____________________________________________________________________________

Exercício 3:

Um determinado zoológico cobra a entrada com base na idade do visitante. 
Os visitantes com 2 anos de idade ou menos não pagam para entrar. 
Crianças entre 3 e 12 anos custa R$14,00. 
Idosos com 65 anos ou mais custam R$18,00. 
A entrada para todos os outros visitantes é de R$23,00. 
Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, 
com uma idade inserida em cada linha. 
O usuário digitará uma linha em branco para indicar que não há mais visitantes no grupo. 
Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada. 
O custo deve ser exibido usando duas casas decimais.


num_visit = int(input("Bem vindo querido visitante! \nInforme o número de pessoas:"))

i=1
idade_visit = []
for _ in range(num_visit):
    idade = int(input(f"Informe a idade do visitante{[i]}: "))
    if (idade == ""):
        break
    idade_visit.append(idade)
    i+=1

j=0
valor = 0
for _ in range(num_visit):
    if idade_visit[j] <= 2:
        valor+=0
    elif idade_visit[j] > 2 and idade_visit[j]<=13:
        valor += 14
    elif idade_visit[j] >= 65:
        valor += 18
    else :
        valor += 23
    j+=1

print(f"Caro visitante o valor a pagar na entrada é de R${valor:.2f}")

______________________________________________________________________

Exercício 4 (desafio):

Uma aproximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita):

pi≈3+4/2x3x4-4/4x5x6+4/6x7x8-4/8x9x10+4/10x11x12-4/12x13x14+⋯

Escreva um programa que calcule o número pi com 15 aproximações. 
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. 
A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!

def calc_pi()->float:
    i=2
    pi = 3
    j = 2
    print(f"Pi1: {pi}")
    for _ in range(7):
        pi1 =  (4/(i*(i+1)*(i+2)))
        print(f"Pi{j}: {pi1}")
        pi2 =  -(4/((i+2)*(i+3)*(i+4)))
        print(f"Pi{j+1}: {pi2}")
        pi += (pi1 + pi2)
        i+=4
        j+=2
    return(pi)

print(f"Pi com 15 aproximações: {calc_pi()}")

______________________________________________________________________

Exercício 5:

Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. 
A sua nota fica sendo a média dos votos restantes. 

Você deve fazer um programa que receba o nome do ginasta 
e as notas dos sete jurados alcançadas pelo atleta em sua apresentação
e depois informe a sua média, conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informadas ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04


d = dict()
num = int(input("Informe o número de atletas: "))

w = 1
for _ in range(num):
    nome = input(f"Informe o nome do {w}º atleta: ")
    d[nome] = []
    j = 1
    print("Informe as notas dos 7 juris: \n")
    for _ in range(7):
        nota = float(input(f"Nota {j}: "))
        d[nome].append(nota)
        j+=1
  
    d[nome].remove(max(d[nome]))
    d[nome].remove(min(d[nome]))

    print(f"Atleta: {nome}")
    soma = 0
    i = 0
    for _ in range(len(d[nome])):
        soma += d[nome][i]
        print(f"Nota {i+1}: {d[nome][i]}")
        i+=1
    media = soma/len(d[nome])

    print(f"\nResultado Final")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {max(d[nome])}")
    print(f"Pior nota: {min(d[nome])}")
    print(f"Média: {media}")

    w+=1

______________________________________________________________________
Exercício 6:

Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
faça um programa que calcule o valor de H com N termos.

def calc_H(N: int)->float:
    i=2
    H=1
    print(H)
    for _ in range(N-1):
        H += 1/i
        print(H)
    return(H)

N = int(input("Informe o valor de N: "))

print(f"O valor de H é: {calc_H(N)}")

"""

