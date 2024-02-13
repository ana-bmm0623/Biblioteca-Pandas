#Exercícios de Condições e Loops

'''
2-) Escreva um programa em Python que solicite ao usuário que adivinhe um número entre 1 e 50. O programa deve informar ao usuário se o número é maior ou menor e continuar solicitando novas tentativas até que o número seja descoberto.
'''
import random 
numero_aleatorio = random.randrange(1,51)
numero = int(input("Digite um número entre 1 e 50: "))
while (numero != numero_aleatorio):
    if(numero > numero_aleatorio):
        print("Tente novamente. Dica: digite um número menor!")
        numero = int(input("Digite um número entre 1 e 50: "))

    elif (numero < numero_aleatorio):
        print("Tente novamente. Dica: digite um número maior!")
        numero = int(input("Digite um número entre 1 e 50: "))

print("Parabéns! O número secreto é: ", numero_aleatorio)