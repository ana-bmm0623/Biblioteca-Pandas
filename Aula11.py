# Orientações a Objetos

class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def saudacao(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

class Professor(Pessoa):
    def __init__(self, nome, idade, sexo, titulo):
        super().__init__(nome, idade, sexo)
        self.titulo = titulo
    def info(self):
        print(f"O titulo é {self.titulo}")

pessoa1 = Pessoa("Rogério", "40", "Masculino")
pessoa2 =  Pessoa("Ana", "18", "Feminino")
pessoa3 = Pessoa("Artur", "15", "Masculino")

pessoa1.saudacao()
pessoa2.saudacao()
pessoa3.saudacao()

prof_1 = Professor("Manoel", "65", "Masculino", "Doutor")
print(prof_1.nome)
prof_1.info()