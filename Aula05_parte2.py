#Exercícios de Condições e Loops

'''
2-) Leia dois números e efetue a adição. Caso o valor somado seja maior que 20,este deverá ser apresentado somando-se a ele mais 8; caso o valor seja menor ou igual a 20, este deverá ser apresentado subtraindo-se;
'''
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

soma = a + b

if(soma > 20):
    soma += 8
    print(soma)
elif(soma <= 20):
    soma -= 5
    print(soma)