#Classe Main não possui atributos
class Main:
    pass
print('Testando o código')

#Aqui estamos usando uma linha de código para a importação da classe
#FROM é utilizado para sabermos qual arquivo/módulo sera utilizado
#IMPORT é utilizado para sabermos qual classe iremos importar
from ClassCliente import Cliente
from Conta import Conta

#Declarando um novo objeto C1
#Passamos para o objeto a Classe que sera instanciada (CLIENTE)
#Passamos os atributos criados no metodo construtor da classe CLIENTE
c1 = Cliente('João','519999525225')

#Declarando um novo objeto CONTA
#Passamos para o objeto a Classe que sera instanciada (CONTA)
#Passamos os atributos criados no metodo construtor da classe CONTA
conta = Conta(c1.nome,6565,0)

#Primeiro iremos imprimir o a referencia do nosso objeto
print(c1)
#Na sequencia iremos imprimir os dados que armazenamos nela
print(c1.nome,' e ',c1.telefone)
#Aqui iremos imprimir os dados armazenados na Classe Conta
print(conta.titular, 'Numero',conta.numero, 'Saldo', conta.saldo)



