# Listas

# O que são as listas em Python?
'''
- As listas são coleções de itens que podem ser de diferentes tipos;
- Cada item é separado por uma vírgula e as listas são criadas usando colchetes;
'''

# Para que servem as listas?

'''
- As listas são utilizadas para armazenar coleções de dados que podem ser modificados durante a execução do programa;
'''

# Como criar uma lista?
'''
- Podemos criar uma lista utilizando colchetes ([]) e separando cada item da lista com uma vírgula;
- Por exemplo, lista_frutas = ["maçã", "banana", "laranja", "abacaxi", "uva"]
'''

nome = "Rogério"
print(nome)

lista_nomes = ["Rogério", "Luana", "Luanara",1, 2]
print(lista_nomes)

# Acessando elementos por índice

'''
- Os elementos da lista são acessados através de índices, que começam em 0;
- Por exemplo, lista_frutas[2] retorna "laranja".
'''

#Slicing de listas

'''
- É possível acessar um subconjunto da lista utilizando o slicing, que é feito utilizando a notação : [início:fim];
- Por exemplo, lista_frutas[1:3] retorna ["banana", "laranja"];
'''

# Exercício 

'''
Crie uma lista de 5 frutas e imprima a terceira fruta da lista.
'''

lista_frutas = ["amora", "banana", "caqui", "damasco", "embaúba"]
print(lista_frutas[2])

# Removendo elementos 

'''
- Podemos remover elementos de uma lista utilizando a função remove(), que remove o primeiro item da lista que corresponda ao valor passado como parâmetro;
- Ou utilizando a operação de del, que remove o item pelo índice.
'''

# Adicionando elementos 
'''
- Podemos adicionar elementos em uma lista utilizando a função append(), que adiciona um item ao final da lista;
- Ou seja, utilizando a operação de concatenação "+".
'''

lista_frutas.append("figo")
print(lista_frutas)

lista_frutas.remove("caqui")
print(lista_frutas)

# Tamanho da lista
print(len(lista_frutas))

# Deixar em ordem 
print(sorted(lista_frutas))

#Inverter a ordem
lista_frutas.reverse
print(lista_frutas)