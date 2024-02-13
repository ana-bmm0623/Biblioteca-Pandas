#Exercícios de Condições e Loops

'''
1-) Para doar sangue é necessário:

- Ter entre 16 e 69 anos;
- Pesar mais de 50 kg;
- Estar descansado(ter dormido pelo menos 6 horas nas últimas 24 horas).

Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 horas para uma pessoa e diga se pode doar sangue ou não.
'''
nome = input("Digite o nome do paciente:")
idade = int(input("Digite a idade do paciente " + nome + ": "))
peso = float(input("Digite o peso do paciente " + nome + ": "))
quant_horas_dormidas = int(input("Digite a quantidade de horas que o paciente " + nome + "dormiu: "))

if(idade > 16) and (idade < 69) and (peso > 50.0) and (quant_horas_dormidas >= 6):
    print("O paciente " + nome + " pode doar sangue. ")
else:
    print("O paciente " + nome + " não pode doar sangue. ")
