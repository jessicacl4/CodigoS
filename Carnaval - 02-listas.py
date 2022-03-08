"""Exercício 1:

Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). 
Imprima na tela o elemento e sua respectiva posição na lista. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
>>> Elemento 1 na posição 0
>>> Elemento 3 na posição 1
>>> Elemento 6 na posição 2
>>> Elemento “H” na posição 3

lista = [1, "amor", [1,2,3], 10.52]

i = 0
while i < len(lista):
    print(f"Elemento {lista[i]} na posição {i}")
    i+=1
___________________________________________________________________

Exercício 2:

Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a lista na ordem inversa. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] a saída deve ser
>>> [[7,7,7], “H”, 6, 3, 1]

lista = [1, "amor", [1,2,3], 10.52]

i = len(lista)-1
while i >= 1:
    print(f"Elemento {lista[i]} na posição {i}")
    i-=1

___________________________________________________________________

Exercício 3:

Crie uma lista com 6 números inteiros. 
Imprima o maior, o menor e suas respectivas posições. 
Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.


lista = [0, 0, 0, 0, 0, 0]
i = 0
while i < len(lista):
    num = int(input(f"Informe o número da posição [{i}]:"))
    lista[i] = num
    i+=1


i = 0
maior = i
while i < len(lista):
    if lista[i] > maior:
        maior = lista[i]
    
    elif lista[i] == maior:
        j = 0
        while j < len(lista):
            if i < j:
                maior = lista[i]

            else:
                maior = lista[j]
                x = j
            j+=1
    i+=1


i = len(lista)-1
menor = lista[i]

while i >= 0:
    if lista[i] < menor:
        menor = lista[i]
    elif lista[i] == maior:
        j = 0
        while j < len(lista):
            if i < j:
                menor = lista[i]
            else:
                menor = lista[j]
            j+=1
    i-=1

print(f"Lista: {lista}")

print(f"O maior elemento é {maior} e está na posição ")
print(f"O menor elemento é {menor} e está na posição ")


---- // ----

lista = [0, 0, 0, 0, 0, 0]
i = 0
while i < len(lista):
    num = int(input(f"Informe o número da posição [{i}]:"))
    lista[i] = num
    i+=1

maior = max(lista)
pos_maior = lista.index(maior)


menor = min(lista)
pos_menor = lista.index(menor)


print(f"O maior elemento é {maior} e está na posição {pos_maior}")
print(f"O menor elemento é {menor} e está na posição {pos_menor}")

_________________________________________________________________________

Exercício 4:

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas 
e mostre a média calculada juntamente com todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 

Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho


lista = [0,0,0,0,0,0,0,0,0,0,0,0]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
i = 0
soma = 0
while i < len(lista):
    temp = int(input(f"Informe a temperatura do mês de {meses[i]}:"))
    lista[i] = temp
    soma+=lista[i]
    i+=1

media = soma/i

print(lista)
print(soma)
print(f"Temperatura média: {media}")

print(f"Meses com temperatura acima da média anual de {media:.1f}ºC:")

j = 0
while j < len(meses):
    if lista[j] > media:
        print(f"{j} - {meses[j]}")
    j+=1

_________________________________________________________________________

Exercício 5:

Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
adicione o elemento 7000 logo após o elemento 6000 na lista acima. 
O resultado final deverá ser:
>>> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


lista1 = [10,20,[300, 400, [5000, 6000], 500], 30, 40]

i = 0
while i < 3:
    if i == 2:
        lista2 = lista1[i]
        j = 0
        while j < len (lista2):
            if j == 2:
                lista3 = lista2[j]
                lista3.append(7000)
            j+=1

    i+=1

print(lista1)

______________________________________________________________________________________________

Faça um programa que remova strings vazias de uma lista de strings. 
Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]


lista = ["Olá", "", "meu", "nome", "", "é", "facilitador", ""]

i = 0
while i < len(lista):
    if lista[i] == "":
        del lista[i]
    i+=1

print(lista)

______________________________________________________________________________________________

Exercício 7:

Dada a lista de strings [“1”, “7”, “99”, “15”] 
construa um programa que converte todos os elementos desta lista para inteiro.
Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, 
converta todos os elementos para int.

lista = ["1", "7", "99", "15"] 

i = 0
lista_int = []
lista_str = []

while i < len(lista):
    lista_int.append(int(lista[i]))
    i+=1

i = 0
while i < len(lista_int):
    lista_str.append(str(lista_int[i]))
    i+=1

print(f"Lista de inteiros: {lista_int}")
print(f"Lista de strings: {lista_str}")

"""







