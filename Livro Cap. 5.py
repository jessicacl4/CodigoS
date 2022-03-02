"""5.1 Modifique o programa para exibir os números de 1 a 100.

x = 1
while x<=100:
    print(x)
    x+=1
______________________________________________________________________________________________________

 5.2 Modifique o programa para exibir os números de 50 a 100. 

 x = 50
while x<=100:
    print(x)
    x+=1
______________________________________________________________________________________________________

5.3 Faça um programa para escrever a contagem regressiva do lança­mento de um foguete. 
O programa deve imprimir 10, 9, 8, ... , 1, O e Fogo! na tela. 

x = 10
while x>=0:
    print(x)
    x-=1
print("\nFogo!!!")
______________________________________________________________________________________________________

5.4 Modifique o programa anterior para imprimir de 1 até o número  digitado pelo usuário, mas, dessa vez, 
apenas os números ímpares.

fim = int(input("Informe o último número da sequência ímpar: "))
x = 1
while x <= fim: 
    if x%2 != 0:
        print(x)
    x+=1

-----//-----

fim = int(input("Informe o último número da sequência ímpar: "))
x = 1
while x <= fim: 
    print(x)
    x+=2
______________________________________________________________________________________________________

Reescreva o programa anterior para escrever os 10 primeiros múlti­plos de 3. 

x=0
cont = 1

while cont <= 10: 
    x+=3
    print(x)
    cont+=1

-----//-----

x=3
cont = 1

while cont <= 10: 
    if x%3 == 0:
        print(x)
        cont+=1
    x+=1
______________________________________________________________________________________________________


5.6 Altere o programa anterior para exibir os resultados no mesmo form­ato de uma tabuada: 2xl = 2, 2x2 = 4, ...


print("Tabuada de 3\n")
x=3
cont = 1

while cont <= 10: 
    if x%3 == 0:
        print(f"3 x {cont} = {x}\n")
        cont+=1
    x+=1

______________________________________________________________________________________________________

5.7 Modifique o programa anterior de forma que o usuário também 
digite o início e o fim da tabuada, em vez de começar com 1 e 10.

n = int(input("Tabuada de :\n"))
cont = int(input("Começar de:\n"))
cont_fim = int(input("Terminar em :\n"))

x = n

while cont <= cont_fim: 
    if x%n == 0:
        print(f"\n{n} x {cont} = {n * cont}\n")
        cont+=1
    x+=n
______________________________________________________________________________________________________

 5.8 Escreva um programa que leia dois números. 
 Imprima o resultado da multiplicação do primeiro pelo segundo. 
 Utilize apenas os operadores de soma e subtração para calcular o resultado. 
 Lembre-se de que podemos entender a multi­plicação de dois números como somas sucessivas de um deles. 
 Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4. 

num1 = int(input("Informe o primeiro numero:"))
num2 = int(input("Informe o segundo numero:"))

i = 1
soma = 0

while i <= num2:
    soma+=num1
    i+=1

print(f"\n{num1} x {num2} = {soma}\n")

______________________________________________________________________________________________________

5.9 Escreva um programa que leia dois números. 
Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
Utilize apenas os operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de 
vezes que podemos retirar o divisor do dividendo. 
Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20. 


num1 = int(input("Informe o primeiro numero:"))
num2 = int(input("Informe o segundo numero:"))

x = num1
cont = 0

while x > 0:
    x = x - num2 
    cont+=1         #O quociente representa qtas vzs eu consigo subtrair o divisor do dividendo
print(f"\n {num1} / {num2} = {cont}")

______________________________________________________________________________________________________

5.10 Modifique o programa anterior para que aceite respostas com letras 
maiúsculas e minúsculas em todas as questões. 

pontos= 0 
questão= 1 
while questão<= 3: 
    resposta= input(f"Resposta da questão {questão}: ") 
    if questão== 1 and (resposta== "b" or resposta=="B"): 
        pontos= pontos+ 1 
    if questão== 2 and (resposta== "a" or resposta=="A"): 
        pontos= pontos+ 1 
    if questão== 3 and (resposta== "d" or resposta=="D"): 
        pontos= pontos+ 1 
    questão= questão+ 1 
print(f"O aluno fez {pontos} ponto(s)") 

______________________________________________________________________________________________________

5.11 Escreva um programa que pergunte o depósito inicial e a taxa de 
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
Escreva o total ganho com juros no período. 

 deposito = float(input(" Informe o valor do depósito inicial:"))
taxa = float(input(" Qual a taxa de juros (%)?:"))

saldo = deposito
i = 0

while i<24:
    saldo = saldo + (saldo * taxa/100)
    i+=1
    print(f"Saldo mês {i}: {saldo:.2f}")
    
print(f"\nGanho total: R${(saldo - deposito):.2f}")

______________________________________________________________________________________________________

5.12 Altere o programa anterior de forma a perguntar também o valor  depositado mensalmente. 
Esse valor será depositado no início de cada mês, e você  deve considerá-lo para o cálculo de juros do mês seguinte.

deposito = float(input("Informe o valor do depósito inicial:"))
taxa = float(input("Qual a taxa de juros (%)?:"))
deposito_mes = float(input("Informe o valor a depoisitar mensalmente: "))

saldo = deposito
i = 0

while i<24:
    saldo = saldo + (saldo * taxa/100) + deposito_mes
    i+=1
    print(f"Saldo mês {i}: {saldo:.2f}")
    
print(f"\nGanho total: R${(saldo - deposito):.2f}")

______________________________________________________________________________________________________

5.13 Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
Pergunte também o valor mensal que será pago. 
Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago. 
divida = float(input("Divida: "))
taxa_juro = float(input("Juro: "))
pag_mensal = float(input("Pagamento Mensal: "))

juro_mensal = divida * taxa_juro/100
divida_ini = divida

if juro_mensal > pag_mensal:
    print("A dívida nunca poderá ser paga")
else:
    cont = 0
    total_juro = 0
    while divida > pag_mensal: # como no laço estou subtraindo pag_mensal o teste tem que ser até ele e eu indico a sobra da divida à parte
        juro_mensal = divida * taxa_juro/100
        divida = divida + juro_mensal - pag_mensal
        cont+=1
        total_juro+=juro_mensal

total_pago = divida_ini + total_juro

print(f"A qtd de meses para saldar a dívida é {cont}")
print(f"Total juros: R${total_juro:.2f}")
print(f"Total pago. R${total_pago:.2f}")

______________________________________________________________________________________________________

 5.14 Escreva um programa que leia números inteiros do teclado. 
 O pro­grama deve ler os números até que o usuário digite O (zero). 
 No final da execução, exiba a quantidade de números digitados, 
 assim como a soma e a média aritmética. 

cont=0
soma=0
media=0

while True:
    num = int(input("Digite um número inteiro: "))
    if num == 0:
        break
    soma+=num
    cont+=1
media = soma/cont
print(f"A quantidade de números digitados é: {cont}")
print(f"A Soma dos números digitados é: {soma}")
print(f"A Média dos números digitados é: {media}")

______________________________________________________________________________________________________

5.15 Escreva um programa para controlar uma pequena máquina registra­dora. 
Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. 
Utilize a tabela de códigos a seguir para obter o preço de cada produto: 
--------------------
  Código    Preço
    1       0,50
    2       1,00
    3       4,00 
--------------------
  Código    Preço 
    5       7,00 
    9       8,00 
--------------------
Seu programa deve exibir o total das compras depois que o usuário digitar O. 
Qualquer outro código deve gerar a mensagem de erro "Código inválido''. 

tabela = print("Tabela de Preços\n1 - 0,50\n2 - 1,00\n3 - 4,00\n5 - 7,00\n9 - 8,00\n")
codigo =[1, 2, 3, 5, 9]
preco =[0.50, 1.00, 4.00, 7.00, 8.00]
soma = 0

while True:
    num = int(input("Informe o código da compra: "))
    i = 0
    if num in codigo:
        while i < len(preco):
            if num == codigo[i]:
                soma+=preco[i]
            i+=1
    elif num == 0:
       break
    else:
        print(f"Código inválido!")

print(f"O total das suas compras deu: R${soma:.2f}")

______________________________________________________________________________________________________

5.16 - Execute o Programa 5.1 para os seguintes valores: 501,745,384, 2, 7 e 1. 

#Programa 5.1 - Fiz o código do meu jeito

Vejamos como exemplo um programa que leia um valor e que imprima a quan­tidade de cédulas necessárias para pagar esse mesmo valor.
Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1. 


valor = int(input("Informe o valor a pagar: "))

cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont1 = 0

while True:
    if valor >= 50:
        valor -= 50
        cont50+=1

    elif valor >= 20:
        valor -= 20
        cont20+=1

    elif valor >= 10:
        valor -= 10
        cont10+=1

    elif valor >= 5:
        valor -= 5
        cont5+=1
    
    elif valor >= 1:
        valor -= 1
        cont1+=1
    
    else:
        break

cedulas = cont50 + cont20 + cont10 + cont5 + cont1


print(f"Para saldar a dívida serão necessárias {cedulas} cédulas: \n{cont50} notas de R$50\n{cont20} notas de R$20\n{cont10} notas de R$10 \n{cont5} notas de R$5\n{cont1} notas de R$1")

______________________________________________________________________________________________________

5.17 - O que acontece se digitarmos O (zero) no valor a pagar? 
5.18 - Modifique o programa para também trabalhar com notas de R$100. 

cedulas = [100,50,20,10,5,1]

i=0
cont_cedulas = 0

valor = int(input("Informe o valor a pagar: "))
    
while i < len(cedulas):
    if valor >= cedulas[i]:
        valor -= cedulas[i]
        cont_cedulas+=1
    else:
        i+=1
print(f"Sera(o) necessária(s) {cont_cedulas} cedulas para quitar o valor informado!")

_____________________________________________________________________________________


5.19 - Modifique o programa para aceitar valores decimais, ou seja, tam­bém contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50. 
5.20 - O que acontece se digitarmos 0,001 no programa anterior? Caso ele não funcione, altere-o de forma a corrigir o problema. 

cedulas = [100.00, 50.00, 20.00, 10.00, 5.00, 1.00, 0.50, 0.10, 0.05, 0.02, 0.01]

i=0
cont_cedulas = 0

valor = float(input("Informe o valor a pagar: "))

if valor < 0.01:
        print("Informe valor de no mínimo R$0.01 centavos!")
        
while i < len(cedulas):
    if valor >= cedulas[i]:
        valor -= cedulas[i]
        cont_cedulas+=1
    else:
        i+=1
print(f"Sera(o) necessária(s) {cont_cedulas} cedulas para quitar o valor informado!")

____________________________________________________________________________________


 5.21 Reescreva o Programa 5.1 de forma a continuar executando até que o 
valor digitado seja O. Utilize repetições aninhadas. 


____________________________________________________________________________________

5.22 Escreva um programa que exiba uma lista de opções (menu): adição, 
subtração, divisão, multiplicação e sair. 
Imprima a tabuada da operação escolhida. 
Repita até que a opção saída seja escolhida. 

ope = int(input("Menu de Operações\n(1) Soma\n(2) Subtração\n(3) Multiplicação\n(4) Divisão \n(5) Sair \nInforme a operação a realizar: \n"))

while True:
    if ope > 5 or ope < 1:
        print("Escolha uma opção da lista")
    elif ope == 5:
        break
    else:
        tab = int(input("Tabuada de: "))
        i = 0
        while i <=10:
            if ope == 1:
                soma = tab + i
                print(f"\n{tab} + {i} = {soma}")
            elif ope == 2:
                menos = tab - i
                print(f"\n{tab} - {i} = {menos}")
            elif ope == 3:
                multip = tab * i
                print(f"\n{tab} * {i} = {multip}")
            else:
                div = tab / (i+1)
                print(f"\n{tab} / {i+1} = {div:.2f}")
        i+=1

____________________________________________________________________________________


5.23 Escreva um programa que leia um número e verifique se é ou não um número primo. 
Para fazer essa verificação, calcule o resto da divisão do número 
por 2 e depois por todos os números ímpares até o número lido. 
Se o resto de uma dessas divisões for igual a zero, o número não é primo. 
Observe que O e 1 não são primos e que 2 é o único número primo que é par. 

num = int(input("Informe um número:"))

if num < 0:
    print("Número inválido. Informe apenas números positivos")

if num == 0 or num == 1:
    print("Caso especial")

if num == 2:
    print("O número é primo!")

elif num%2 == 0:
    print("O número não é primo. O único número par primo é 2")

else:
    i = 3
    while i < num:
        if num%i == 0:
            break
        i+=2
    if i == num:
        print(f"O número {num} é primo")
    else:
        print(f"O número {num} não é primo pois é divisível por {i}")

____________________________________________________________________________________



____________________________________________________________________________________
5.25 Escreva um programa que calcule a raiz quadrada de um número. 
Utilize o método de Newton para obter um resultado aproximado. 
Sendo n o  número a obter a raiz quadrada, considere a base 6=2. 
Calcule p usando a fórmula p=(b+(n/6))/2. 
Agora, calcule o quadrado de p. 
A cada passo, faça b=p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o 
quadrado de p for menor que 0,0001. 

5.26 Escreva um programa que calcule o resto da divisão inteira entre dois números. 
Utilize apenas as operações de soma e subtração para calcular o resultado. 

5.27 Escreva um programa que verifique se um número é palíndromo. 
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. 
Exemplos: 454, 10501 



5.24 Modifique o programa anterior de forma a ler um número n. 
Imprima os n primeiros números primos. 

"""

num = int(input("Digite um número: "))
if num < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if num >= 1:
        print("2")
        cont = 1
        j = 3
        while cont < num:
            i = 3
            while(i < j):
                if j % i == 0:
                    break
                i += 2
            if i == j:
                print(i)
                cont+= 1
            j+=2
