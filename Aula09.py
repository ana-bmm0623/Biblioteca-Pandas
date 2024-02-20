#Tuplas, Dicionários e Sets

'''
- Tuplas 

- São listas imutáveis em Python;

- Ao contrário das listas, que permitem alterações, você não pode adicionar, remover ou alterar itens em uma tupla depois de criá-la;

- Exemplos de tuplas

- As tuplas são frequentemente utilizadas para estruturar dados imutáveis, como dias da semana, coordenadas geográficas e informações de contato de uma pessoa.

'''
dias_da_semana = ("segunda", "terça", "quarta")
print(dias_da_semana)
print(type(dias_da_semana))
'''
- Dicionários

- São estruturas de dados em Python que armazenam elementos como pares chave-valor;

- Cada chave é associada a um valor;

- Exemplos práticos

- Os dicionários podem ser utilizados para armazenar informações sobre pessoas, produtos ou qualquer outro tipo de objeto.
'''
pessoa = {"nome": "Rogério", "idade": 35}
print(pessoa["nome"])
print(pessoa.keys())
print(pessoa.items())
print(type(pessoa))
pessoa["peso"] = 85
print(pessoa)
print(pessoa.values())
'''
- Sets

- São estruturas de dados em Python que representam conjuntos matemáticos;

- Eles contêm elementos únicos e não mantêm nenhuma ordem específica;

- Exemplos práticos de uso

- Os sets são frequentemente utilizados para remover duplicatas de uma lista ou para fazer operações matemáticas, como união ou interseção.
'''
conjunto = {"branco", "laranja", "marrom"}