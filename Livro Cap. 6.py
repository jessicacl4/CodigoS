
"""Calcule a media 
lista = [2,4,6]

x = 0
soma = 0

while x<len(lista):
    soma+= lista[x]
    x+=1

media = soma / len(lista)


print(media)

"""

"""Calcule a media com notas digitadas

lista = [0,0,0,0,0]

i = 0

while i<len(lista):
    lista[i] = int(input(f"Informe o item {i} da lista:"))
    i+=1
print(lista)
Adição de elementos à lista

L = []

while True:
    n = int(input("Informe um número (0 sai):"))
    if n == 0:
        break
    L.append(n)

print (L)

i = 0
while i < len (L):
    print(L[i])
    i+=1
 
_____________________________________________________________________________________________
"""


""" 6.1 Modifique o Programa 6.2 para ler 7 notas em vez de 5.

# Programa 6.2 - Cálculo da Média com notas digitadas 
notas= [0, 0, 0, 0, 0, 0, 0]
soma = 0 
i = 1 
while i <= len(notas): 
    notas[i-1] = float(input(f"Nota {i}:"))
    soma += notas[i-1] 
    i+= 1 

i = 1

while i <= len(notas):
    print(f"Nota {i}: {notas[i-1]:6.2f}") 
    i+= 1 
print(f"Média: {soma / i:5.2f}") 


_____________________________________________________________________________________________

6.2 Faça um programa que leia duas listas e que gere uma terceira com os 
elementos das duas primeiras. 


lista1 = []
lista2 = []

print("\nLista 1\n")
while True:
    num1 = int(input("Informe um valor para adicionar à lista 1 (0 para sair): "))
    if num1 == 0:
        break
    lista1.append(num1)

print("\nLista 2\n")
while True:
    num2 = int(input("Informe um valor para adicionar à lista 2 (0 - sair): "))
    if num2 == 0:
        break
    lista2.append(num2)

lista3 = lista1[:] #é igual aos elementos da lista2
lista3.extend(lista2)
print(lista3)

"""

"""
6.3 Faça um programa que percorra duas listas e gere uma terceira sem 
elementos repetidos. 
"""

lista1 = []
lista2 = []

print("\nLista 1\n")
while True:
    num1 = int(input("Informe um valor para adicionar à lista 1 (0 para sair): "))
    if num1 == 0:
        break
    lista1.append(num1)

print("\nLista 2\n")
while True:
    num2 = int(input("Informe um valor para adicionar à lista 2 (0 - sair): "))
    if num2 == 0:
        break
    lista2.append(num2)


lista3 = lista1[:]

i = 0
while i < len(lista1):
    j = 0
    while j < len(lista2):
        if lista3[i] == lista2[j]:
            lista2.remove(lista2[j])
        j+=1
    i+=1

lista3.extend(lista2)
print("\nLista 3")
i = 0
while i < len(lista3):
    print(f"Lista3[{i}] = {lista3[i]}")
    i+=1