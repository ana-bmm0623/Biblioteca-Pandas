#Strings

# Definição

'''
- Uma string é uma sequência de caracteres, que pode incluir letras, números, espaços e símbolos;
'''

# Características

'''
- Imutáveis;
- Ordenadas;
- Indexáveis.
'''

# Criação de Strings

# Utilizando aspas simples ou duplas
'''
- São iguais em Python e delimitam o início e o final de uma string.
'''

# Utilizando 3 aspas
'''
- Para strings que ocupam mais de uma linha;
'''

# Concatenação de Strings

'''
- Utilizar o operador + para juntar duas strings.
'''

# Acesso a Caracteres via índice

# índice

'''
- Cada caractere de uma string tem um índice associado, que começa em 0.
'''

# Acesso

'''
- Podemos acessar um caractere específico de uma string usando o índice entre colchetes ([]);
'''

# Por exemplo

'''
- Para acessar o terceiro caractere de uma string: 
'''

frase = "Python é incrível"
terceiro_caractere = frase[2]
print(terceiro_caractere)

# Operações Básicas com Strings

# Repetição de strings

'''
- Repetir uma string uma quantidade determinada de vezes com o operador *;
'''

# Concatenação de Strings

'''
- Unir duas ou mais strings usando o operador +;
'''

# Slicing de Strings

'''
- Criar uma nova string a partir de fragmentos de outra string já existente;
'''

primeiro_nome = "Rogério"
sobrenome = "Nogueira"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)
print(frase * 4)

# Prática de slicing

# Básico

'''
- Podemos selecionar uma parte de uma string definindo os índices de início e fim
'''

frase_1 = "Pizza é vida!"
trecho = frase_1[0:5]
print(trecho)

# Intervalos e Passos

'''
- Podemos definir o intervalo e o passo de slicing.
'''
trecho = frase_1[0:5:2]

# Exemplo

'''
- O slicing é utilizado em diversas situações, desde manipulação de dados até jogos de tabuleiro;
'''

# Métodos de Strings

# find()

'''
- Localiza o primeiro índice da substring em uma string;
'''

print(frase.find("incr"))
print(frase[9:])

# upper() e lower()

'''
- Converter uma string para letras maiúsculas e minúsculas
''' 

print(frase.lower())
print(frase.upper())

# replace()

'''
- Substitui caracteres
'''

print(frase.replace(" ", "-"))