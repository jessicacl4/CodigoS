"""# Programa 4.1 -Lê dois valores e imprime qual é o maior

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número:"))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print(f"Os números {num1} e {num2} são iguais")

__________________________________________________________________________________________

4.2 Escreva um programa que pergunte a velocidade do carro de um usuário. 
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

vel = float(input("Qual a velocidade do seu carro?"))

if vel > 80:
    multa = 5 * (vel - 80) 
    print(f" Multa a pagar: R${multa:.2f}")
else:
    print(f" Você é um bom condutor")
__________________________________________________________________________________________
4.3 Escreva um programa que leia três números e que imprima o maior e o menor. 
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if (num1 > num2) and (num1 > num3):
    print(f"O maior número é: {num1}")
    if (num2 > num3):
        print(f"O menor número é: {num3}")
    else:
        print(f"O menor número é: {num2}")
elif (num2 > num1) and (num2 > num3):
    print(f"O maior número é: {num2}")
    if (num1 > num3):
        print(f"O menor número é: {num3}")
    else:
        print(f"O menor número é: {num1}")
else:
    print(f"O maior número é: {num3}")
    if (num2 > num1):
        print(f"O menor número é: {num1}")
    else:
        print(f"O menor número é: {num2}")    
            
----- /// -----
   
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

maior = num1

if (num2 > num1) and (num2 > num3):
     maior = num2
elif (num3 > num1) and (num3 > num2):
     maior = num3

menor = num1
if (num2 < num1) and (num2 < num3):
     menor = num2
elif (num3 < num1) and (num3 < num2):
     menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

----- /// -----

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

print(f"\nO maior número é {max(num1,num2,num3)}")
print(f"O menor número é {min(num1,num2,num3)}")

__________________________________________________________________________________________

4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
para os inferiores ou iguais, de 15%.


salario = float(input("Informe o seu salário:"))

if salario > 1250.00:
    aumento = salario * 0.10 
else:
    aumento = salario * 0.15 

salario += aumento
print(f" O aumento é de R${aumento:.2f} e o seu salário passa a ser R${salario:.2f} ")

__________________________________________________________________________________________

4.6 Escreva um programa que pergunte a distância que um passageiro 
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km 
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.


dist = float(input("Informe a distância a percorrer:"))

if dist <= 200:
    passagem = dist * 0.50 
else:
    passagem = dist * 0.45 

print(f" A distância a percorrer é de {dist} Km e o preço da passagem é R${passagem:.2f} ")

__________________________________________________________________________________________

4.8 Escreva um programa que leia dois números e que pergunte qual 
operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), 
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. 



lista = ["Soma","Subtração", "Multiplicação", "Divisão"]
ope = int(input("Menu de Operações\n(1) Soma\n(2) Subtração\n(3) Multiplicação\n(4) Divisão \nInforme a operação a realizar: \n"))
num1 = int(input("Informe o primeiro número:"))
num2 = int(input("Informe o segundo número:"))

if ope == 1:
    conta = num1 + num2
elif ope == 2:
    conta = num1 - num2
elif ope == 3:
    conta = num1 * num2
elif ope == 4:
    conta = num1 / num2
else:
    print("Você não escolheu nenhuma das opções informadas!")

print(f" A operação escolhida é {lista[ope-1]} e o resultado é {conta:.2f} ")
__________________________________________________________________________________________

4.9 Escreva um programa para aprovar o empréstimo bancário para com­pra de uma casa. 
O programa deve perguntar o valor da casa a comprar, o salário e  a quantidade de anos a pagar. 
O valor da prestação mensal não pode ser superior a 30% do salário. 
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. 



casa = float(input("Informe o valor da casa:\n"))
salario = float(input("Informe o seu salário:\n"))
anos = int(input("Em quantos anos você deseja pagar a casa?\n"))

prestacao = casa / (anos*12)

limite = (salario - (salario * 0.30))

if prestacao <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo reprovado!")
__________________________________________________________________________________________

4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. 
Calcule o preço a pagar de acordo com a tabela a seguir.

+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+

kWh = int(input("Informe a qtd de kWh consumida: "))

tipo_inst = input("R - residências, \n I - indústrias \n C - Comércios \n Informe o tipo de instalação:")

preco_consumo = 0.55

if tipo_inst == "R":
    if kWh <= 500:
        preco_consumo = 0.40
    else:
        preço_consumo = 0.65

elif tipo_inst == "C":
    if kWh > 1000:
        preco_consumo = 0.60
else:
    if kWh > 5000:
        preco_consumo = 0.60

print(f"O preço a pagar é: {preco_consumo}")


"""