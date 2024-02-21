# Exercícios
import math
'''
1-) Crie uma classe "Círculo" que calcule sua área e circunferência. Use herança para criar a subclasse chamada "Cilindro" que calcula seu volume.
'''
class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        area = math.pi * self.raio **2
        return area
    
    def calcularCircunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        return circunferencia

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        self.altura = altura
        super().__init__(raio)

    def calcularVolume(self):
        volume = self.calcularArea() * self.altura
        return volume
    
cilindro1 = Cilindro(2, 10)
print(cilindro1.calcularVolume())
print(cilindro1.calcularArea())
print(cilindro1.calcularCircunferencia())

'''
2-) Crie um sistema de gerenciamento de biblioteca. Crie classes para Livro, Autor e Usuário. Permita empréstimo, devolução e busca de livros;
'''
class Autor():
    def __init__(self, nome):
        self.nome = nome

class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def emprestarLivro(self):
        if not self.emprestado:
            self.emprestado = True
            print(f"Empréstimo do livro '{self.titulo}' realizado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    def devolverLivro(self):
        if self.emprestado:
            self.emprestado = False
            print(f"Devolução do livro '{self.titulo}' realizada com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já foi devolvido.")

    def buscarLivro(self):
        pass

autor_1 = Autor("Wes Nascimento")
livro_1 = Livro("Python Básico", autor_1)

livro_1.emprestarLivro()
print(autor_1.nome)
print(livro_1.titulo)
livro_1.emprestarLivro()


class Usuario():
    def __init__(self, login):
        self.login = login

autor_1 = Autor("Wes Nascimento")
livro_1 = Livro("Python Básico", autor_1)

livro_1.emprestarLivro()
print(autor_1.nome)
print(livro_1.titulo)
livro_1.emprestarLivro()