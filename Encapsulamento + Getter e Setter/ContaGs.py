class Conta:
    def __init__(self, titular,numero,saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = 0

    #Metodo Get
    def get_saldo(self):
        return self.saldo

    #Metodo Set
    def set_saldo(self, saldo):
        if saldo < 0:
            print ('Saldo não pode ser menor que 0')
        else:
            self.saldo = saldo

    def saque(self, valor):
        if self.saldo>=valor:
            self.saldo-=valor
            print('Saque realizado com sucesso')
        else:
            print('Saldo insuficiente')

    def deposita(self, valor):
        self.saldo+=valor

    def extrato(self):
        print('Cliente:', self.titular,'Saldo atual:', self.saldo)

