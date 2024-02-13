#Exercícios de Condições e Loops

'''
3-) Escreva um programa em Python que calcule o preço total de uma compra. O programa deve solicitar que o usuário digite o preço de cada item e calcular o total da compra, incluindo impostos.
'''

total_compra = 0.0
imposto = 0.1

while True:
    valor_item = input("Digite o valor do item ou s para sair: ")
    if valor_item == 's':
        break
    total_compra = total_compra + float(valor_item)

total_compra = total_compra * imposto + total_compra

print("O valor total é: ", total_compra)