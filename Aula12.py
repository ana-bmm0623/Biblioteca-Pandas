# Exercícios

'''
1-) Crie uma classe "Livro" com os atributos título e autor. Crie instâncias e imprima suas informações 
'''
class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def imprimir(self):
        print(f"O livro {self.titulo} do autor {self.autor}")

livro1 = Livro("Os suicidas", "Raphael Montes")
livro1.imprimir()

'''
2-) Crie uma classe "ContaBancaria" com métodos para depósito, saque e verificação de saldo. Crie instâncias e teste os métodos.
'''

class ContaBancaria():
    def __init__(self, conta, agencia, saldo):
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo

    def deposito(self, valorDeposito):
        self.saldo = float(self.saldo) + valorDeposito
        print(f"Depósito realizado com sucesso. O saldo é R$ {self.saldo}.")

    def saque(self, valorASacar):
        if(valorASacar > self.saldo):
            print(f"Não é possível realizar essa operação. O valor que deseja sacar ultrapassa o saldo da conta.")
        else:  
            self.saldo = float(self.saldo) - valorASacar
            print(f"Saque realizado com sucesso. O saldo é R$ {self.saldo}.")

    def saldo(self):
        print(f"O saldo é R$ {self.saldo}.")

conta = ContaBancaria("1111", "11", "0")
conta.deposito(100.00)
conta.saldo
conta.saque(10.50)
conta.saque(120)