#Funções

'''
- Funções são blocos de código que permitem agrupar um conjunto de instruções que podem ser chamadas quando necessário;
'''

# Tipos de funções

'''
- Funções Nativas

* Funções presentes na linguagem Python que permitem ao programador executar operações lógicas, matemáticas de texto e etc;

- Funções de Biblioteca

* Funções pré-desenvolvidas disponíveis em bibliotecas Python para uso em diversos cenários de programação;

- Funções Personalizadas

* Funções criadas pelo programador, com base nas necessidades específicas do projeto.

'''

# Parâmetros e Argumentos de Funções

'''
- Parâmetros

* Funções presentes na linguagem Python que permitem ao programador executar operações lógicas, matemáticas, de texto e etc;

- Argumentos

* Funções pré-desenvolvidas disponíveis em bibliotecas Python para uso em diversos cenários de programação

'''

# Escopo de variáveis

'''
- Escopo Local

* Dentro de uma função, as variáveis e parâmetros são locais e só podem ser acessados dentro desta função;

- Escopo Global

* As variáveis declaradas no escopo global podem ser acessadas de qualquer lugar do código;
'''

def soma(a,b ):
    resultado = a + b
    return resultado

print(soma(4, 10))

soma_lados = soma(20,49)
print(soma_lados)

def soma_multiplica(valor1, valor2, operacao):
    if operacao == "somar":
        resultado = valor1 + valor2
    if operacao == "multiplicar":
        resultado = valor1 * valor2
    return resultado

valor_1 = float(input("Informe o valor 1: "))
valor_2 = float(input("Informe o valor 2: "))
opcao = input("Qual é a operação: ")
resultado = soma_multiplica(valor_1, valor_2, opcao)
print(resultado)