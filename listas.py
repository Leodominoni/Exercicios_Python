#> LISTAS
#Criação de lista

notas = [7.9, 9.7, 8.2]
lista = []
lista = list()
lista = [26, 'Malibu', 3.14159, False]
lista_de_lista = [10, [1,2,3]]

# Indexação e Slices (fatiamento)

lista = [10, 'Malibu', 3.14159, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) #-1 é o último

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:4]) #posicao 0 até a 3 o index 4 nao vai aparecer
print(lista[3:])#posicao 3 ate o final
print(lista[2:6:2]) #pula em dois em dois

#iteração com FOR
for elemento in lista:
    print(elemento)

#utilizando os indices

print(len(lista)) #len é para saber a quantidade de elementos dentro da lista

for i in range(len(lista)):
    print(lista[i])
#metodo de listas
lista = [1, 3,14,8,2]
print (lista)
lista.append(5)
print('depois do append: ',lista) 

#insert escolhe a posição do elemento
lista.insert(2, 50)
print ('depois do insert:', lista)

#extend - juntar duas listas
lista2 = [1,2,3]
lista.extend(lista2)
print('depois do extend:', lista)

#pop - remove elemento especifico ou o ultimo
lista.pop()
print('depois do pop: ', lista)
lista.pop(0)
print('depois do pop: ', lista)

#remove - diz qual elemento vc quer retirar
lista.remove(5)
print('depois de tirar o elemento desejado: ',lista)

#count - contar quantos itens tem na lista
print('conta a qtde de vezes que aparece: ', lista.count(2))

#index 
print('indice do elemento 12: ', lista.index(12))

#sort - ordenar sua lista
lista.sort()
print('Ordena a lista: ', lista.sort)
lista.sort(reserve=True)
print('Ordena a lista: ', lista.sort)

#FUNÇÃO
#len - conta os elementos
print(len(lista))
#sum - soma todos os elementos
print(sum(lista))
#max - retorna o maior elemento
print(max(lista))
#min - retorna o menor elemento
print(min(lista))




